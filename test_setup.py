#!/usr/bin/env python
"""
Setup validation script
Checks that all dependencies are installed and API keys are configured
Run this before running topic_clusterer.py
"""

import sys
import os
from pathlib import Path


def check_python_version():
    """Check Python version."""
    print("✓ Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"  Python {version.major}.{version.minor}.{version.micro} ✓")
        return True
    else:
        print(f"  ERROR: Python 3.8+ required, got {version.major}.{version.minor}")
        return False


def check_dependencies():
    """Check all required packages are installed."""
    print("\n✓ Checking dependencies...")
    required = [
        'numpy',
        'feedparser',
        'sklearn',
        'matplotlib',
        'seaborn',
        'requests',
        'anthropic',
    ]

    optional = [
        'plotly',
    ]

    missing_required = []
    missing_optional = []

    for package in required:
        try:
            __import__(package)
            print(f"  {package:20s} ✓")
        except ImportError:
            missing_required.append(package)
            print(f"  {package:20s} ✗ MISSING")

    for package in optional:
        try:
            __import__(package)
            print(f"  {package:20s} ✓ (optional)")
        except ImportError:
            missing_optional.append(package)
            print(f"  {package:20s} ✗ MISSING (optional)")

    if missing_required:
        print(f"\n  ERROR: Missing required packages: {', '.join(missing_required)}")
        print(f"  Install with: pip install -r requirements.txt")
        return False

    if missing_optional:
        print(f"\n  WARNING: Missing optional packages: {', '.join(missing_optional)}")
        print(f"  Some features may be unavailable")

    return True


def check_api_key():
    """Check Anthropic API key is configured."""
    print("\n✓ Checking API key...")

    # Check .env file
    env_file = Path('.env')
    if env_file.exists():
        print("  .env file found ✓")
        try:
            from dotenv import load_dotenv
            load_dotenv()
        except ImportError:
            print("  WARNING: python-dotenv not installed, using environment variables only")

    api_key = os.getenv('ANTHROPIC_API_KEY')

    if not api_key:
        print("  ERROR: ANTHROPIC_API_KEY not found")
        print("  Set it in .env file or environment variable")
        print("  Get key from: https://console.anthropic.com/")
        return False

    if api_key.startswith('sk-ant-'):
        masked_key = api_key[:10] + '...' + api_key[-4:]
        print(f"  API key configured ✓ ({masked_key})")
        return True
    else:
        print("  WARNING: API key format may be incorrect (should start with 'sk-ant-')")
        return True


def check_rss_connectivity():
    """Test connectivity to RSS feeds."""
    print("\n✓ Testing RSS feed connectivity...")

    try:
        import feedparser
    except ImportError:
        print("  SKIP: feedparser not installed")
        return True

    test_feeds = [
        ("BBC", "http://feeds.bbci.co.uk/news/rss.xml"),
        ("HackerNews", "https://feeds.ycombinator.com/frontpage"),
    ]

    working = 0
    for name, url in test_feeds:
        try:
            feed = feedparser.parse(url)
            if feed.entries:
                print(f"  {name:15s} ✓ ({len(feed.entries)} articles)")
                working += 1
            else:
                print(f"  {name:15s} ✗ (no articles)")
        except Exception as e:
            print(f"  {name:15s} ✗ ({str(e)[:30]})")

    if working == 0:
        print("  WARNING: Could not connect to any RSS feeds")
        print("  Check internet connection and firewall settings")
        return False

    return True


def check_disk_space():
    """Check available disk space."""
    print("\n✓ Checking disk space...")

    try:
        import shutil
        total, used, free = shutil.disk_usage('.')
        free_gb = free / (1024**3)

        if free_gb > 1:
            print(f"  Available: {free_gb:.1f} GB ✓")
            return True
        else:
            print(f"  WARNING: Only {free_gb:.1f} GB available")
            return True
    except Exception as e:
        print(f"  Could not check disk space: {e}")
        return True


def run_minimal_test():
    """Run a minimal test of the core functionality."""
    print("\n✓ Running minimal functionality test...")

    try:
        from anthropic import Anthropic

        client = Anthropic()

        # Test API connectivity with a simple prompt
        message = client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=50,
            messages=[{
                "role": "user",
                "content": "Say 'Topic Clusterer ready' in 3 words or less."
            }]
        )

        response = message.content[0].text
        print(f"  API test successful ✓")
        print(f"  Response: '{response.strip()}'")
        return True

    except Exception as e:
        print(f"  ERROR: API test failed: {str(e)[:100]}")
        return False


def main():
    """Run all checks."""
    print("=" * 60)
    print("Topic Clusterer - Setup Validation")
    print("=" * 60)

    checks = [
        ("Python version", check_python_version),
        ("Dependencies", check_dependencies),
        ("API key", check_api_key),
        ("RSS connectivity", check_rss_connectivity),
        ("Disk space", check_disk_space),
        ("API functionality", run_minimal_test),
    ]

    results = []
    for name, check_func in checks:
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"  ERROR in {name}: {e}")
            results.append((name, False))

    # Summary
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status:8s} {name}")

    print(f"\n{passed}/{total} checks passed")

    if passed == total:
        print("\n🎉 All systems ready! Run: python topic_clusterer.py")
        return 0
    elif passed >= total - 1:
        print("\n⚠️  Most systems ready. Check warnings above.")
        print("   You may still be able to run the pipeline.")
        return 0
    else:
        print("\n❌ Some systems need attention. See errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
