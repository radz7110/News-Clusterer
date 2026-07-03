"""
Example usage of the Topic Clusterer with custom parameters
Demonstrates different configurations and use cases
"""

from topic_clusterer import (
    scrape_rss_feeds,
    embed_headlines,
    cluster_with_dbscan,
    label_clusters_with_llm,
    reduce_to_2d,
    plot_static_visualization,
    plot_interactive_map,
    save_results
)
import json


def example_1_basic_usage():
    """
    Basic usage: Run the complete pipeline with default settings
    """
    print("\n" + "=" * 60)
    print("Example 1: Basic Usage")
    print("=" * 60)

    # Step 1: Scrape
    articles = scrape_rss_feeds(num_articles=50)
    headlines = [article['title'] for article in articles]

    # Step 2: Embed
    embeddings = embed_headlines(headlines)

    # Step 3: Cluster
    labels, n_clusters = cluster_with_dbscan(embeddings, eps=0.5, min_samples=2)

    # Step 4: Label
    cluster_labels = label_clusters_with_llm(articles, labels)

    # Step 5: Visualize
    embeddings_2d = reduce_to_2d(embeddings)
    plot_static_visualization(embeddings_2d, labels, cluster_labels, "example1_clusters.png")

    # Step 6: Save
    save_results(articles, labels, cluster_labels, "example1_results.json")

    print("✓ Example 1 complete")


def example_2_fine_grained_clustering():
    """
    Stricter clustering: Produce more, smaller clusters
    Good for detailed topic differentiation
    """
    print("\n" + "=" * 60)
    print("Example 2: Fine-Grained Clustering (More Clusters)")
    print("=" * 60)

    articles = scrape_rss_feeds(num_articles=100)
    headlines = [article['title'] for article in articles]
    embeddings = embed_headlines(headlines)

    # Lower eps = stricter clustering = more clusters
    labels, n_clusters = cluster_with_dbscan(embeddings, eps=0.4, min_samples=2)
    print(f"Generated {n_clusters} fine-grained clusters")

    cluster_labels = label_clusters_with_llm(articles, labels)
    embeddings_2d = reduce_to_2d(embeddings)
    plot_static_visualization(embeddings_2d, labels, cluster_labels, "example2_fine_clusters.png")
    save_results(articles, labels, cluster_labels, "example2_results.json")

    print("✓ Example 2 complete")


def example_3_broad_clustering():
    """
    Broader clustering: Produce fewer, larger clusters
    Good for high-level topic overview
    """
    print("\n" + "=" * 60)
    print("Example 3: Broad Clustering (Fewer Clusters)")
    print("=" * 60)

    articles = scrape_rss_feeds(num_articles=100)
    headlines = [article['title'] for article in articles]
    embeddings = embed_headlines(headlines)

    # Higher eps = looser clustering = fewer clusters
    labels, n_clusters = cluster_with_dbscan(embeddings, eps=0.8, min_samples=1)
    print(f"Generated {n_clusters} broad clusters")

    cluster_labels = label_clusters_with_llm(articles, labels)
    embeddings_2d = reduce_to_2d(embeddings)
    plot_static_visualization(embeddings_2d, labels, cluster_labels, "example3_broad_clusters.png")
    save_results(articles, labels, cluster_labels, "example3_results.json")

    print("✓ Example 3 complete")


def example_4_batch_processing():
    """
    Demonstrate batch processing and result analysis
    """
    print("\n" + "=" * 60)
    print("Example 4: Batch Processing & Analysis")
    print("=" * 60)

    articles = scrape_rss_feeds(num_articles=100)
    headlines = [article['title'] for article in articles]
    embeddings = embed_headlines(headlines)
    labels, n_clusters = cluster_with_dbscan(embeddings, eps=0.6, min_samples=2)
    cluster_labels = label_clusters_with_llm(articles, labels)

    # Analyze clusters
    from collections import Counter
    cluster_sizes = Counter(labels)

    print("\nCluster Analysis:")
    print(f"Total clusters: {n_clusters}")
    print(f"Noise points: {cluster_sizes.get(-1, 0)}")
    print(f"\nCluster sizes:")
    for cluster_id in sorted([k for k in cluster_sizes.keys() if k != -1]):
        size = cluster_sizes[cluster_id]
        label = cluster_labels.get(cluster_id, "Unknown")
        percentage = (size / len(articles)) * 100
        print(f"  {label:30s}: {size:3d} articles ({percentage:5.1f}%)")

    embeddings_2d = reduce_to_2d(embeddings)
    plot_static_visualization(embeddings_2d, labels, cluster_labels, "example4_analysis.png")
    save_results(articles, labels, cluster_labels, "example4_results.json")

    print("\n✓ Example 4 complete")


def example_5_specific_sources():
    """
    Demonstrate how to work with results from specific news sources
    """
    print("\n" + "=" * 60)
    print("Example 5: Source-Specific Analysis")
    print("=" * 60)

    articles = scrape_rss_feeds(num_articles=100)
    headlines = [article['title'] for article in articles]
    embeddings = embed_headlines(headlines)
    labels, n_clusters = cluster_with_dbscan(embeddings, eps=0.6, min_samples=2)
    cluster_labels = label_clusters_with_llm(articles, labels)

    # Analyze by source
    from collections import defaultdict
    articles_by_source = defaultdict(list)
    for i, article in enumerate(articles):
        articles_by_source[article['source']].append({
            'title': article['title'],
            'cluster': labels[i],
            'cluster_name': cluster_labels.get(labels[i], 'Unknown')
        })

    print("\nArticles by Source:")
    for source, source_articles in sorted(articles_by_source.items()):
        print(f"\n{source} ({len(source_articles)} articles):")
        # Show top 3 clusters for this source
        source_clusters = Counter(a['cluster'] for a in source_articles)
        for cluster_id, count in source_clusters.most_common(3):
            cluster_name = cluster_labels.get(cluster_id, f"Cluster {cluster_id}")
            print(f"  - {cluster_name}: {count} articles")

    embeddings_2d = reduce_to_2d(embeddings)
    plot_static_visualization(embeddings_2d, labels, cluster_labels, "example5_sources.png")
    save_results(articles, labels, cluster_labels, "example5_results.json")

    print("\n✓ Example 5 complete")


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("Topic Clusterer - Example Usage Demonstrations")
    print("=" * 60)
    print("\nChoose an example to run:")
    print("1. Basic usage (default settings)")
    print("2. Fine-grained clustering (more clusters)")
    print("3. Broad clustering (fewer clusters)")
    print("4. Batch processing & analysis")
    print("5. Source-specific analysis")
    print("\nRun directly: python example_usage.py")
    print("Then choose from the menu above")
    print("\nOr edit the main() section to run specific examples")

    # Uncomment to run examples programmatically:
    # example_1_basic_usage()
    # example_2_fine_grained_clustering()
    # example_3_broad_clustering()
    # example_4_batch_processing()
    # example_5_specific_sources()
