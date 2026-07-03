#!/usr/bin/env python
"""
Results Analysis Script
Analyze and explore clustering results in detail
"""

import json
import sys
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime


def load_results(filepath: str = "clustering_results.json") -> dict:
    """Load clustering results from JSON file."""
    if not Path(filepath).exists():
        print(f"Error: {filepath} not found")
        print("Run topic_clusterer.py first to generate results")
        sys.exit(1)

    with open(filepath) as f:
        return json.load(f)


def print_summary(results: dict):
    """Print high-level summary."""
    print("\n" + "=" * 60)
    print("CLUSTERING SUMMARY")
    print("=" * 60)

    metadata = results.get('metadata', {})
    print(f"Timestamp:    {metadata.get('timestamp', 'Unknown')}")
    print(f"Total articles: {metadata.get('total_articles', 0)}")
    print(f"Number of clusters: {metadata.get('num_clusters', 0)}")


def print_cluster_overview(results: dict):
    """Print overview of each cluster."""
    print("\n" + "=" * 60)
    print("CLUSTER OVERVIEW")
    print("=" * 60)

    clusters = results.get('clusters', {})

    # Sort by size
    sorted_clusters = sorted(
        clusters.items(),
        key=lambda x: x[1].get('size', 0),
        reverse=True
    )

    print(f"\n{'Cluster':15s} {'Label':30s} {'Size':>6s} {'Percent':>8s}")
    print("-" * 65)

    total_articles = sum(c.get('size', 0) for c in clusters.values())

    for cluster_id, cluster_info in sorted_clusters:
        label = cluster_info.get('label', f'Cluster {cluster_id}')
        size = cluster_info.get('size', 0)
        percent = (size / total_articles * 100) if total_articles > 0 else 0

        # Truncate label if too long
        label_display = label[:28] if len(label) > 28 else label

        print(f"{cluster_id:15s} {label_display:30s} {size:>6d} {percent:>7.1f}%")


def print_cluster_details(results: dict, cluster_id: str = None):
    """Print detailed information about a specific cluster."""
    clusters = results.get('clusters', {})

    if cluster_id is None:
        # Pick largest cluster
        cluster_id = max(clusters.keys(), key=lambda k: clusters[k].get('size', 0))

    if cluster_id not in clusters:
        print(f"Error: Cluster {cluster_id} not found")
        return

    cluster = clusters[cluster_id]

    print("\n" + "=" * 60)
    print(f"CLUSTER DETAILS: {cluster_id}")
    print("=" * 60)

    print(f"\nLabel: {cluster.get('label', 'Unknown')}")
    print(f"Size: {cluster.get('size', 0)} articles")

    print("\nTop Headlines:")
    articles = cluster.get('articles', [])[:5]
    for i, article in enumerate(articles, 1):
        title = article.get('title', 'Untitled')
        source = article.get('source', 'Unknown')
        print(f"\n{i}. {title}")
        print(f"   Source: {source}")

    if len(cluster.get('articles', [])) > 5:
        print(f"\n... and {len(cluster.get('articles', [])) - 5} more articles in this cluster")


def print_source_analysis(results: dict):
    """Analyze article distribution by source."""
    print("\n" + "=" * 60)
    print("SOURCE ANALYSIS")
    print("=" * 60)

    clusters = results.get('clusters', {})
    source_stats = defaultdict(lambda: {"count": 0, "clusters": Counter()})

    for cluster_id, cluster_info in clusters.items():
        for article in cluster_info.get('articles', []):
            source = article.get('source', 'Unknown')
            source_stats[source]["count"] += 1
            source_stats[source]["clusters"][cluster_id] += 1

    print(f"\n{'Source':30s} {'Articles':>10s} {'Top Clusters':35s}")
    print("-" * 80)

    for source in sorted(source_stats.keys(), key=lambda s: source_stats[s]["count"], reverse=True):
        stats = source_stats[source]
        article_count = stats["count"]

        # Get top 2 clusters for this source
        top_clusters = stats["clusters"].most_common(2)
        cluster_str = ", ".join([
            f"{cid}({cnt})" for cid, cnt in top_clusters
        ])

        source_display = source[:28] if len(source) > 28 else source
        print(f"{source_display:30s} {article_count:>10d} {cluster_str:35s}")


def print_keyword_analysis(results: dict):
    """Analyze common words in each cluster."""
    print("\n" + "=" * 60)
    print("KEYWORD ANALYSIS")
    print("=" * 60)

    clusters = results.get('clusters', {})

    for cluster_id in sorted(clusters.keys()):
        cluster = clusters[cluster_id]
        label = cluster.get('label', f'Cluster {cluster_id}')

        # Extract words from titles
        articles = cluster.get('articles', [])
        all_words = []

        for article in articles[:10]:  # Sample first 10
            title = article.get('title', '').lower()
            words = [w for w in title.split() if len(w) > 3]  # Filter short words
            all_words.extend(words)

        # Count word frequencies
        word_counts = Counter(all_words)
        top_words = word_counts.most_common(5)

        print(f"\n{label} ({len(articles)} articles):")
        if top_words:
            print(f"  Top words: {', '.join([w[0] for w in top_words])}")


def print_timeline_analysis(results: dict):
    """Analyze article publication timeline."""
    print("\n" + "=" * 60)
    print("TIMELINE ANALYSIS")
    print("=" * 60)

    clusters = results.get('clusters', {})

    # Parse dates
    dates = defaultdict(int)
    earliest = None
    latest = None

    for cluster in clusters.values():
        for article in cluster.get('articles', []):
            pub_date = article.get('published', '')
            if pub_date:
                # Extract just the date part
                date_only = pub_date.split('T')[0]
                dates[date_only] += 1

                if earliest is None or date_only < earliest:
                    earliest = date_only
                if latest is None or date_only > latest:
                    latest = date_only

    if dates:
        print(f"\nEarliest article: {earliest}")
        print(f"Latest article: {latest}")
        print(f"Date range: {len(dates)} different dates")

        print("\nArticles by date:")
        for date in sorted(dates.keys()):
            count = dates[date]
            bar = "█" * (count // 2)  # Simple bar chart
            print(f"  {date} │ {bar} {count}")


def interactive_explorer(results: dict):
    """Interactive CLI for exploring results."""
    print("\n" + "=" * 60)
    print("INTERACTIVE EXPLORER")
    print("=" * 60)

    clusters = results.get('clusters', {})

    while True:
        print("\nOptions:")
        print("  1 - View cluster details")
        print("  2 - Search headlines")
        print("  3 - Export cluster")
        print("  4 - Back to main menu")

        choice = input("\nChoice (1-4): ").strip()

        if choice == "1":
            print("\nAvailable clusters:")
            for cid in sorted(clusters.keys()):
                label = clusters[cid].get('label', f'Cluster {cid}')
                size = clusters[cid].get('size', 0)
                print(f"  {cid:3s}: {label} ({size} articles)")

            cluster_id = input("\nCluster ID: ").strip()
            if cluster_id in clusters:
                print_cluster_details(results, cluster_id)

        elif choice == "2":
            keyword = input("Search term: ").strip().lower()
            print(f"\nHeadlines containing '{keyword}':")

            found = 0
            for cluster_id, cluster in clusters.items():
                label = cluster.get('label', f'Cluster {cluster_id}')
                for article in cluster.get('articles', []):
                    if keyword in article.get('title', '').lower():
                        print(f"\n[{label}]")
                        print(f"  {article['title']}")
                        print(f"  Source: {article.get('source', 'Unknown')}")
                        found += 1

            print(f"\nFound {found} matches")

        elif choice == "3":
            cluster_id = input("Cluster ID to export: ").strip()
            if cluster_id in clusters:
                filename = f"cluster_{cluster_id}_export.json"
                export_data = {
                    "cluster_id": cluster_id,
                    "label": clusters[cluster_id].get('label'),
                    "articles": clusters[cluster_id].get('articles', [])
                }
                with open(filename, 'w') as f:
                    json.dump(export_data, f, indent=2)
                print(f"Exported to {filename}")

        elif choice == "4":
            break


def main():
    """Main analysis function."""
    import argparse

    parser = argparse.ArgumentParser(description="Analyze topic clustering results")
    parser.add_argument('--file', default='clustering_results.json', help='Results JSON file')
    parser.add_argument('--cluster', help='Show details for specific cluster')
    parser.add_argument('--interactive', action='store_true', help='Interactive explorer mode')
    parser.add_argument('--export', help='Export cluster to JSON')

    args = parser.parse_args()

    # Load results
    results = load_results(args.file)

    # Run requested analysis
    if args.interactive:
        interactive_explorer(results)
    else:
        print_summary(results)
        print_cluster_overview(results)
        print_source_analysis(results)
        print_keyword_analysis(results)
        print_timeline_analysis(results)

        if args.cluster:
            print_cluster_details(results, args.cluster)

    print("\n" + "=" * 60)
    print("Analysis complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
