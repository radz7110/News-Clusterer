# Topic Clusterer for News Articles

A complete pipeline to scrape news headlines from RSS feeds, embed them using AI, cluster them with DBSCAN, label clusters intelligently with Claude, and visualize the results on an interactive 2D map.

## Features

- **RSS Feed Scraping**: Retrieves 100+ recent headlines from BBC, Reuters, CNN, The Guardian, and HackerNews
- **Smart Embeddings**: Generates semantic embeddings using Claude's language understanding
- **DBSCAN Clustering**: Groups similar articles into thematic clusters with automatic noise detection
- **LLM Labeling**: Uses Claude to generate meaningful, human-readable cluster names
- **Interactive Visualization**: Creates both static (PNG) and interactive (HTML) 2D visualizations
- **Structured Output**: Exports complete results as JSON for further analysis

## Architecture

```
Raw Headlines
    ↓
Embed (Claude API)
    ↓
DBSCAN Clustering
    ↓
LLM Labeling (Claude)
    ↓
PCA → 2D Reduction
    ↓
[Static Plot] + [Interactive Plot] + [JSON Results]
```

## Installation

### 1. Create Virtual Environment
```bash
python -m venv venv
source venv/Scripts/activate  # Windows
# or
source venv/bin/activate      # macOS/Linux
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up API Key
Create a `.env` file in the project root:
```
ANTHROPIC_API_KEY=your_api_key_here
```

Get your API key from https://console.anthropic.com/

## Usage

### Basic Run
```bash
python topic_clusterer.py
```

This will:
1. Scrape 100 headlines from RSS feeds
2. Generate embeddings
3. Perform DBSCAN clustering
4. Label clusters with Claude
5. Create visualizations
6. Export results

### Output Files

After running, you'll get:

- **topic_clusters.png** - Static visualization with Matplotlib/Seaborn
- **topic_clusters.html** - Interactive Plotly visualization (hover for details)
- **clustering_results.json** - Complete clustering results with articles grouped by cluster

## Configuration

Edit these parameters in the `main()` function:

```python
# Number of articles to scrape
articles = scrape_rss_feeds(num_articles=100)

# DBSCAN parameters
labels, n_clusters = cluster_with_dbscan(embeddings, eps=0.6, min_samples=2)
```

### DBSCAN Parameters

- **eps**: Distance threshold for clustering (0.4-0.8 typical)
  - Lower = more clusters, stricter grouping
  - Higher = fewer, larger clusters
  
- **min_samples**: Minimum points to form a cluster (1-5 typical)
  - Lower = more small clusters
  - Higher = more noise points

## Key Technologies

| Component | Technology |
|-----------|-----------|
| Scraping | feedparser (RSS feeds) |
| Embeddings | Claude API (semantic understanding) |
| Clustering | scikit-learn DBSCAN |
| Labeling | Claude API (LLM) |
| Visualization | Matplotlib, Seaborn, Plotly |
| Dimensionality Reduction | PCA |

## How It Works

### 1. RSS Scraping
- Fetches headlines from 5 major news sources
- Extracts title, description, source, and publication date

### 2. Embedding Generation
- Sends headlines to Claude in batches
- Claude generates 10-dimensional semantic vectors
- Vectors capture semantic meaning of headlines

### 3. DBSCAN Clustering
- Calculates cosine distance between embeddings
- Groups articles by semantic similarity
- Automatically identifies noise (miscellaneous articles)

### 4. Cluster Labeling
- Sends 10 sample articles from each cluster to Claude
- Claude generates concise 2-3 word topic labels
- Labels reflect the cluster's semantic theme

### 5. Dimensionality Reduction
- Uses PCA to reduce embeddings to 2D
- Preserves main variance for visualization
- Enables interactive 2D exploration

### 6. Visualization
- **Static**: Matplotlib scatter plot with color-coded clusters
- **Interactive**: Plotly HTML with hover details and zoom

## Example Output

### JSON Results Structure
```json
{
  "metadata": {
    "timestamp": "2026-07-02T10:30:00",
    "total_articles": 100,
    "num_clusters": 8
  },
  "clusters": {
    "0": {
      "label": "Technology Innovation",
      "size": 15,
      "articles": [
        {
          "title": "New AI Model Breaks Records...",
          "source": "HackerNews",
          "published": "2026-07-02T09:00:00",
          "link": "https://..."
        }
      ]
    }
  }
}
```

## Troubleshooting

### Issue: API Key Not Found
**Solution**: Ensure `.env` file exists in project root with `ANTHROPIC_API_KEY=...`

### Issue: RSS Feeds Timeout
**Solution**: Some feeds may be temporarily unavailable. The script continues with available feeds.

### Issue: Few Clusters Found
**Solution**: Increase `eps` parameter in DBSCAN (e.g., 0.7, 0.8)

### Issue: Too Many Noise Points
**Solution**: Decrease `eps` or `min_samples` parameters

### Issue: Plotly Not Installed
**Solution**: Run `pip install plotly` for interactive visualization

## Advanced Customization

### Add Custom RSS Feeds
Edit the `feeds` list in `scrape_rss_feeds()`:
```python
feeds = [
    "your_feed_url_1",
    "your_feed_url_2",
    # ...
]
```

### Change Clustering Algorithm
Replace DBSCAN with alternatives:
```python
from sklearn.cluster import KMeans, AgglomerativeClustering

# KMeans example
clustering = KMeans(n_clusters=5)
labels = clustering.fit_predict(embeddings_scaled)
```

### Customize Visualization Colors
Change the color palette:
```python
# In plot functions
colors = sns.color_palette("coolwarm", len(unique_labels))
# or: "husl", "Set2", "Paired", etc.
```

## Performance Notes

- **Scraping**: ~10-30 seconds (depends on feed availability)
- **Embedding**: ~1-2 minutes (API calls for embeddings)
- **Clustering**: <1 second
- **Labeling**: ~30-60 seconds (API calls per cluster)
- **Visualization**: <5 seconds
- **Total**: ~3-5 minutes per run

## API Costs

- Embedding generation: ~0.01-0.03 USD per run
- Cluster labeling: ~0.02-0.05 USD per run
- **Total per run**: ~$0.05 estimate

## Future Enhancements

- [ ] Support for more RSS feed sources
- [ ] Incremental clustering (add new articles to existing clusters)
- [ ] Temporal analysis (trending topics over time)
- [ ] Sentiment analysis per cluster
- [ ] Multi-language support
- [ ] Custom embedding models (OpenAI, Hugging Face)
- [ ] Hierarchical clustering visualization
- [ ] Topic evolution tracking

## License

MIT

## Author

Created with Claude Code

---

**Questions?** Check the inline code comments or open an issue!
