#!/usr/bin/env python
"""
Feed Management Utility
Manage, explore, and customize your RSS feed list
"""

import json
import sys
from pathlib import Path
from collections import defaultdict
import feedparser


def load_feeds(filepath: str = "feeds.json") -> dict:
    """Load feeds from JSON file."""
    if not Path(filepath).exists():
        print(f"Error: {filepath} not found")
        sys.exit(1)

    with open(filepath) as f:
        return json.load(f)


def save_feeds(feeds_data: dict, filepath: str = "feeds.json"):
    """Save feeds to JSON file."""
    with open(filepath, 'w') as f:
        json.dump(feeds_data, f, indent=2)
    print(f"✓ Saved to {filepath}")


def show_statistics():
    """Show feed statistics."""
    feeds_data = load_feeds()

    print("\n" + "=" * 70)
    print("FEED STATISTICS")
    print("=" * 70)

    total_feeds = 0
    by_category = defaultdict(int)
    by_country = defaultdict(int)

    for category, feeds_list in feeds_data.get('categories', {}).items():
        count = len(feeds_list)
        total_feeds += count
        by_category[category] = count

        for feed in feeds_list:
            country = feed.get('country', 'Unknown')
            by_country[country] += 1

    print(f"\nTotal Feeds: {total_feeds}")

    print("\nBy Category:")
    for category in sorted(by_category.keys()):
        count = by_category[category]
        percent = (count / total_feeds) * 100
        bar = "█" * (count // 2)
        print(f"  {category:30s} {count:3d} ({percent:5.1f}%) {bar}")

    print("\nBy Country:")
    for country in sorted(by_country.keys()):
        count = by_country[country]
        percent = (count / total_feeds) * 100
        print(f"  {country:20s} {count:3d} ({percent:5.1f}%)")

    print(f"\n{'=' * 70}\n")


def list_feeds(category: str = None):
    """List all feeds or feeds in a specific category."""
    feeds_data = load_feeds()

    print("\n" + "=" * 70)

    if category:
        if category not in feeds_data.get('categories', {}):
            print(f"Category '{category}' not found")
            print(f"Available: {', '.join(feeds_data.get('categories', {}).keys())}")
            return

        feeds_list = feeds_data['categories'][category]
        print(f"{category.upper()} - {len(feeds_list)} Feeds")
        print("=" * 70)

        for feed in feeds_list:
            print(f"\n{feed['name']}")
            print(f"  URL:      {feed['url']}")
            print(f"  Country:  {feed.get('country', 'Unknown')}")
            print(f"  Category: {feed.get('category', 'Unknown')}")
    else:
        print("ALL FEEDS BY CATEGORY")
        print("=" * 70)

        for category_name, feeds_list in feeds_data.get('categories', {}).items():
            print(f"\n{category_name} ({len(feeds_list)} feeds)")
            for feed in feeds_list:
                print(f"  • {feed['name']}")

    print(f"\n{'=' * 70}\n")


def test_feed(url: str):
    """Test if a feed URL is working."""
    print(f"\nTesting: {url}")
    print("-" * 70)

    try:
        feed = feedparser.parse(url)

        if not feed.entries:
            print("✗ No articles found")
            return False

        print(f"✓ Feed is working")
        print(f"  Title: {feed.feed.get('title', 'Unknown')}")
        print(f"  Articles: {len(feed.entries)}")
        print(f"  Latest: {feed.entries[0].get('published', 'Unknown')}")
        return True

    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def test_all_feeds(sample_size: int = 3):
    """Test all feeds and show which are working."""
    feeds_data = load_feeds()

    print("\n" + "=" * 70)
    print(f"TESTING FEEDS (sampling {sample_size} from each category)")
    print("=" * 70)

    results = {"working": 0, "failed": 0, "total": 0}

    for category, feeds_list in feeds_data.get('categories', {}).items():
        print(f"\n{category}:")

        # Sample feeds
        sample = feeds_list[:sample_size]

        for feed in sample:
            name = feed['name']
            url = feed['url']
            results['total'] += 1

            try:
                parsed = feedparser.parse(url)
                if parsed.entries:
                    print(f"  ✓ {name}")
                    results['working'] += 1
                else:
                    print(f"  ✗ {name} (no articles)")
                    results['failed'] += 1
            except Exception as e:
                print(f"  ✗ {name} ({str(e)[:30]})")
                results['failed'] += 1

    print(f"\n{'=' * 70}")
    print(f"Results: {results['working']}/{results['total']} working")
    success_rate = (results['working'] / results['total'] * 100) if results['total'] > 0 else 0
    print(f"Success Rate: {success_rate:.1f}%")
    print(f"{'=' * 70}\n")


def add_feed(name: str, url: str, category: str, country: str = "Unknown"):
    """Add a new feed."""
    feeds_data = load_feeds()

    if category not in feeds_data['categories']:
        feeds_data['categories'][category] = []

    new_feed = {
        "name": name,
        "url": url,
        "country": country,
        "category": category
    }

    feeds_data['categories'][category].append(new_feed)

    save_feeds(feeds_data)
    print(f"✓ Added '{name}' to {category}")


def remove_feed(name: str):
    """Remove a feed by name."""
    feeds_data = load_feeds()

    found = False
    for category, feeds_list in feeds_data['categories'].items():
        for i, feed in enumerate(feeds_list):
            if feed['name'].lower() == name.lower():
                feeds_data['categories'][category].pop(i)
                save_feeds(feeds_data)
                print(f"✓ Removed '{name}' from {category}")
                found = True
                break

    if not found:
        print(f"✗ Feed '{name}' not found")


def create_custom_feeds(feeds_list: list, output_file: str = "custom_feeds.json"):
    """Create a custom feeds file with specific feeds."""
    custom_data = {
        "description": "Custom feed configuration",
        "last_updated": "2026-07-02",
        "categories": {
            "custom": feeds_list
        }
    }

    with open(output_file, 'w') as f:
        json.dump(custom_data, f, indent=2)

    print(f"✓ Created {output_file} with {len(feeds_list)} feeds")


def interactive_menu():
    """Interactive menu for managing feeds."""
    while True:
        print("\n" + "=" * 70)
        print("FEED MANAGEMENT MENU")
        print("=" * 70)
        print("\n1. Show statistics")
        print("2. List all feeds")
        print("3. List feeds by category")
        print("4. Test all feeds")
        print("5. Test specific feed")
        print("6. Add a feed")
        print("7. Remove a feed")
        print("8. Exit")

        choice = input("\nChoice (1-8): ").strip()

        if choice == "1":
            show_statistics()

        elif choice == "2":
            list_feeds()

        elif choice == "3":
            feeds_data = load_feeds()
            categories = list(feeds_data.get('categories', {}).keys())
            print(f"\nAvailable categories: {', '.join(categories)}")
            cat = input("Enter category name: ").strip()
            if cat:
                list_feeds(cat)

        elif choice == "4":
            sample = input("Sample size per category (default 3): ").strip() or "3"
            try:
                test_all_feeds(int(sample))
            except ValueError:
                print("Invalid number")

        elif choice == "5":
            url = input("Feed URL: ").strip()
            if url:
                test_feed(url)

        elif choice == "6":
            name = input("Feed name: ").strip()
            url = input("Feed URL: ").strip()
            category = input("Category: ").strip()
            country = input("Country (optional): ").strip() or "Unknown"
            if name and url and category:
                add_feed(name, url, category, country)

        elif choice == "7":
            name = input("Feed name to remove: ").strip()
            if name:
                confirm = input(f"Remove '{name}'? (yes/no): ").strip().lower()
                if confirm == "yes":
                    remove_feed(name)

        elif choice == "8":
            break

        else:
            print("Invalid choice")


def main():
    """Main function."""
    import argparse

    parser = argparse.ArgumentParser(description="Manage RSS feeds")
    parser.add_argument('--stats', action='store_true', help='Show statistics')
    parser.add_argument('--list', action='store_true', help='List all feeds')
    parser.add_argument('--category', help='List feeds in category')
    parser.add_argument('--test-all', action='store_true', help='Test all feeds')
    parser.add_argument('--test', help='Test specific feed URL')
    parser.add_argument('--add', nargs=4, metavar=('NAME', 'URL', 'CATEGORY', 'COUNTRY'),
                       help='Add new feed')
    parser.add_argument('--remove', help='Remove feed by name')
    parser.add_argument('--interactive', '-i', action='store_true', help='Interactive mode')

    args = parser.parse_args()

    if args.stats:
        show_statistics()
    elif args.list:
        list_feeds()
    elif args.category:
        list_feeds(args.category)
    elif args.test_all:
        test_all_feeds()
    elif args.test:
        test_feed(args.test)
    elif args.add:
        add_feed(args.add[0], args.add[1], args.add[2], args.add[3])
    elif args.remove:
        remove_feed(args.remove)
    elif args.interactive:
        interactive_menu()
    else:
        # Default: show interactive menu
        interactive_menu()


if __name__ == "__main__":
    main()
