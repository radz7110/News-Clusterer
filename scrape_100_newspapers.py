#!/usr/bin/env python
"""
Scrape Headlines from 100+ Newspapers
Demonstrates how to use the expanded feed list with different configurations
"""

import sys
from topic_clusterer import (
    scrape_rss_feeds,
    embed_headlines,
    cluster_with_dbscan,
    label_clusters_with_llm,
    reduce_to_2d,
    plot_static_visualization,
    plot_interactive_map,
    save_results,
)
import json
from collections import defaultdict, Counter


def example_1_scrape_all_sources():
    """
    Example 1: Scrape from all available sources to get diverse coverage
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 1: Scrape from ALL Available Sources")
    print("=" * 70)

    articles = scrape_rss_feeds(num_articles=100, use_json_feeds=True)
    headlines = [article['title'] for article in articles]

    print(f"\nScraped {len(articles)} headlines")
    print(f"Sources: {len(set(a['source'] for a in articles))} different newspapers")

    # Show breakdown by category
    by_category = defaultdict(int)
    by_country = defaultdict(int)

    for article in articles:
        by_category[article.get('category', 'Unknown')] += 1
        by_country[article.get('country', 'Unknown')] += 1

    print("\nBy Category:")
    for category in sorted(by_category.keys()):
        print(f"  {category:25s}: {by_category[category]:3d} articles")

    print("\nBy Country:")
    for country in sorted(by_country.keys()):
        print(f"  {country:15s}: {by_country[country]:3d} articles")

    # Cluster and visualize
    embeddings = embed_headlines(headlines)
    labels, n_clusters = cluster_with_dbscan(embeddings, eps=0.6, min_samples=2)
    cluster_labels = label_clusters_with_llm(articles, labels)
    embeddings_2d = reduce_to_2d(embeddings)

    plot_static_visualization(embeddings_2d, labels, cluster_labels, "ex1_all_sources.png")
    try:
        plot_interactive_map(embeddings_2d, labels, articles, cluster_labels, "ex1_all_sources.html")
    except ImportError:
        pass

    save_results(articles, labels, cluster_labels, "ex1_all_sources.json")

    print("\n✓ Results saved:")
    print("  • ex1_all_sources.png")
    print("  • ex1_all_sources.html")
    print("  • ex1_all_sources.json")


def example_2_technology_focused():
    """
    Example 2: Scrape tech-focused sources only
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 2: Technology-Focused News")
    print("=" * 70)

    # First, scrape from all sources
    all_articles = scrape_rss_feeds(num_articles=200, use_json_feeds=True)

    # Filter to tech articles
    tech_keywords = ['tech', 'ai', 'software', 'data', 'cyber', 'app', 'startup', 'internet', 'computer', 'digital']
    tech_sources = {'The Verge', 'TechCrunch', 'Wired', 'Ars Technica', 'HackerNews', 'ZDNet', 'PC World', 'AnandTech'}

    tech_articles = [
        a for a in all_articles
        if a['source'] in tech_sources or any(kw in a['title'].lower() for kw in tech_keywords)
    ][:100]

    print(f"\nFiltered to {len(tech_articles)} tech articles")
    print(f"From {len(set(a['source'] for a in tech_articles))} tech sources")

    headlines = [article['title'] for article in tech_articles]
    embeddings = embed_headlines(headlines)
    labels, n_clusters = cluster_with_dbscan(embeddings, eps=0.5, min_samples=2)
    cluster_labels = label_clusters_with_llm(tech_articles, labels)
    embeddings_2d = reduce_to_2d(embeddings)

    plot_static_visualization(embeddings_2d, labels, cluster_labels, "ex2_tech_news.png")
    try:
        plot_interactive_map(embeddings_2d, labels, tech_articles, cluster_labels, "ex2_tech_news.html")
    except ImportError:
        pass

    save_results(tech_articles, labels, cluster_labels, "ex2_tech_news.json")

    print("\n✓ Results saved:")
    print("  • ex2_tech_news.png")
    print("  • ex2_tech_news.html")
    print("  • ex2_tech_news.json")


def example_3_international_comparison():
    """
    Example 3: Compare news from different countries
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 3: International News Comparison")
    print("=" * 70)

    articles = scrape_rss_feeds(num_articles=100, use_json_feeds=True)

    # Group by country
    by_country = defaultdict(list)
    for article in articles:
        country = article.get('country', 'Unknown')
        by_country[country].append(article)

    print(f"\nCollected news from {len(by_country)} countries")
    print("\nBreakdown:")

    for country in sorted(by_country.keys()):
        count = len(by_country[country])
        sources = set(a['source'] for a in by_country[country])
        print(f"  {country:20s}: {count:2d} articles from {len(sources)} sources")

    # Cluster globally
    headlines = [article['title'] for article in articles]
    embeddings = embed_headlines(headlines)
    labels, n_clusters = cluster_with_dbscan(embeddings, eps=0.6, min_samples=2)
    cluster_labels = label_clusters_with_llm(articles, labels)
    embeddings_2d = reduce_to_2d(embeddings)

    plot_static_visualization(embeddings_2d, labels, cluster_labels, "ex3_international.png")
    try:
        plot_interactive_map(embeddings_2d, labels, articles, cluster_labels, "ex3_international.html")
    except ImportError:
        pass

    save_results(articles, labels, cluster_labels, "ex3_international.json")

    print("\n✓ Results saved:")
    print("  • ex3_international.png")
    print("  • ex3_international.html")
    print("  • ex3_international.json")


def example_4_business_focus():
    """
    Example 4: Business and finance news
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 4: Business & Finance News")
    print("=" * 70)

    # Load and filter to business sources
    import json
    from pathlib import Path

    feeds_file = "feeds.json"
    if Path(feeds_file).exists():
        with open(feeds_file) as f:
            feeds_data = json.load(f)
            business_feeds = feeds_data['categories'].get('business_finance', [])

        print(f"Found {len(business_feeds)} business news sources")
        print(f"Sources: {', '.join([f['name'] for f in business_feeds[:5]])}...")

    articles = scrape_rss_feeds(num_articles=100, use_json_feeds=True)

    # Filter to business articles
    business_sources = {'Bloomberg', 'Financial Times', 'CNBC', 'MarketWatch', 'Yahoo Finance', 'Seeking Alpha'}
    business_articles = [a for a in articles if a['source'] in business_sources][:100]

    if not business_articles:
        print("Note: Not enough business articles from dedicated sources")
        print("Using all articles instead")
        business_articles = articles

    print(f"\nCollected {len(business_articles)} business articles")

    headlines = [article['title'] for article in business_articles]
    embeddings = embed_headlines(headlines)
    labels, n_clusters = cluster_with_dbscan(embeddings, eps=0.55, min_samples=2)
    cluster_labels = label_clusters_with_llm(business_articles, labels)
    embeddings_2d = reduce_to_2d(embeddings)

    plot_static_visualization(embeddings_2d, labels, cluster_labels, "ex4_business.png")
    try:
        plot_interactive_map(embeddings_2d, labels, business_articles, cluster_labels, "ex4_business.html")
    except ImportError:
        pass

    save_results(business_articles, labels, cluster_labels, "ex4_business.json")

    print("\n✓ Results saved:")
    print("  • ex4_business.png")
    print("  • ex4_business.html")
    print("  • ex4_business.json")


def example_5_multi_language():
    """
    Example 5: Multi-language international coverage
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 5: Multi-Language International News")
    print("=" * 70)

    articles = scrape_rss_feeds(num_articles=100, use_json_feeds=True)

    # Group by language (approximate)
    language_map = {
        'UK': 'English',
        'USA': 'English',
        'Canada': 'English',
        'Australia': 'English',
        'Germany': 'German',
        'France': 'French',
        'India': 'Hindi/English',
        'Hong Kong': 'Chinese/English',
        'China': 'Chinese',
        'International': 'English',
    }

    by_language = defaultdict(list)
    for article in articles:
        country = article.get('country', 'Unknown')
        lang = language_map.get(country, 'Other')
        by_language[lang].append(article)

    print(f"\nNews in {len(by_language)} languages:")
    for lang in sorted(by_language.keys()):
        count = len(by_language[lang])
        print(f"  {lang:20s}: {count:2d} articles")

    headlines = [article['title'] for article in articles]
    embeddings = embed_headlines(headlines)
    labels, n_clusters = cluster_with_dbscan(embeddings, eps=0.6, min_samples=2)
    cluster_labels = label_clusters_with_llm(articles, labels)
    embeddings_2d = reduce_to_2d(embeddings)

    plot_static_visualization(embeddings_2d, labels, cluster_labels, "ex5_multilingual.png")
    try:
        plot_interactive_map(embeddings_2d, labels, articles, cluster_labels, "ex5_multilingual.html")
    except ImportError:
        pass

    save_results(articles, labels, cluster_labels, "ex5_multilingual.json")

    print("\n✓ Results saved:")
    print("  • ex5_multilingual.png")
    print("  • ex5_multilingual.html")
    print("  • ex5_multilingual.json")


def show_menu():
    """Show interactive menu."""
    print("\n" + "=" * 70)
    print("Scrape Headlines from 100+ Newspapers - Examples")
    print("=" * 70)
    print("\n1. Scrape from ALL sources (100+ newspapers)")
    print("2. Technology-focused news")
    print("3. International comparison by country")
    print("4. Business & finance news")
    print("5. Multi-language international coverage")
    print("\nOr run directly:")
    print("  python scrape_100_newspapers.py 1")
    print("  python scrape_100_newspapers.py 2")
    print("  etc.")
    print("\n" + "=" * 70)

    choice = input("\nChoose example (1-5): ").strip()

    return choice


def main():
    """Main function."""
    examples = {
        "1": example_1_scrape_all_sources,
        "2": example_2_technology_focused,
        "3": example_3_international_comparison,
        "4": example_4_business_focus,
        "5": example_5_multi_language,
    }

    if len(sys.argv) > 1:
        choice = sys.argv[1]
    else:
        choice = show_menu()

    if choice in examples:
        try:
            examples[choice]()
        except KeyboardInterrupt:
            print("\n\nInterrupted by user")
        except Exception as e:
            print(f"\nError: {e}")
            import traceback
            traceback.print_exc()
    else:
        print(f"Invalid choice: {choice}")


if __name__ == "__main__":
    main()
