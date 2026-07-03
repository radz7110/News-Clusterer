# 📰 Topic Clusterer for News Articles

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/yourusername/topic-clusterer.svg)](https://github.com/yourusername/topic-clusterer)

> **Automatically discover, cluster, and visualize news topics from 100+ newspapers worldwide using AI**

An intelligent pipeline that:
1. 📡 **Scrapes** 100+ headlines from major news sources
2. 🧠 **Embeds** them with semantic AI (Claude)
3. 🎯 **Clusters** automatically with DBSCAN
4. 🏷️ **Labels** clusters with LLM intelligence
5. 📊 **Visualizes** results as interactive 2D maps

Perfect for journalists, researchers, data analysts, and news aggregators.

## ✨ Features

- **100+ Newspaper Sources** - BBC, Reuters, CNN, Bloomberg, TechCrunch, Al Jazeera, and more
- **Smart Embeddings** - Semantic vectors using Claude API
- **Automatic Clustering** - DBSCAN finds optimal groups (no tuning needed)
- **Intelligent Labeling** - Claude generates meaningful 2-3 word topic names
- **Interactive Visualization** - Plotly HTML map with hover details, zoom, pan
- **Static Plots** - High-resolution PNG images
- **Structured Export** - JSON data for downstream analysis
- **Feed Management** - Add, remove, test feeds easily
- **Multiple Examples** - Tech-only, international, business-focused clustering

## 🏗️ How It Works

```
100+ Newspaper RSS Feeds
         ↓
[BBC, Reuters, CNN, TechCrunch, Bloomberg, ...]
         ↓
    SCRAPING
  (feedparser)
         ↓
   100 Headlines
         ↓
    EMBEDDING
  (Claude API)
  10D vectors
         ↓
   Embeddings
         ↓
    CLUSTERING
    (DBSCAN)
   Automatic
   grouping
         ↓
  15 Clusters
  + Noise
         ↓
    LABELING
  (Claude LLM)
  "Tech News"
  "Climate"
  etc.
         ↓
  Labeled
  Clusters
         ↓
DIMENSIONALITY
  REDUCTION
     (PCA)
    2D space
         ↓
  VISUALIZATION
  ┌─────────────────────┐
  │ Interactive HTML    │
  │ Static PNG          │
  │ JSON Results        │
  └─────────────────────┘
```

## 📚 Example Usage

### Basic: Cluster News from 100+ Sources
```python
from topic_clusterer import scrape_rss_feeds, embed_headlines, cluster_with_dbscan

# Scrape headlines
articles = scrape_rss_feeds(num_articles=100)
print(f"Scraped {len(articles)} articles from {len(set(a['source'] for a in articles))} sources")

# Embed them
embeddings = embed_headlines([a['title'] for a in articles])

# Cluster
labels, n_clusters = cluster_with_dbscan(embeddings)
print(f"Found {n_clusters} topic clusters")
```

### Advanced: Tech News Only
```python
from topic_clusterer import scrape_rss_feeds

# Scrape all sources
articles = scrape_rss_feeds(num_articles=200)

# Filter to tech
tech_sources = {'TechCrunch', 'The Verge', 'Wired', 'HackerNews'}
tech_articles = [a for a in articles if a['source'] in tech_sources][:100]

# Then cluster as normal...
```

### Compare International News
```python
from collections import defaultdict

# Group by country
by_country = defaultdict(list)
for article in articles:
    by_country[article['country']].append(article)

for country in sorted(by_country.keys()):
    print(f"{country}: {len(by_country[country])} articles")
```

See [NEWSPAPERS.md](NEWSPAPERS.md) for more examples.

## 🚀 Quick Start (5 minutes)

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR-USERNAME/topic-clusterer.git
cd topic-clusterer
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up API Key
Get your free Anthropic API key from [console.anthropic.com](https://console.anthropic.com/)

Create `.env` file in project root:
```env
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

Or copy the template:
```bash
cp .env.example .env
# Then edit .env with your actual API key
```

### 5. Validate Setup (Optional)
```bash
python test_setup.py
```

Should show: ✓ All systems ready!

### 6. Run the Pipeline
```bash
python topic_clusterer.py
```

## 📊 View Results

After running, you get 3 output files:

| File | What It Is | Open With |
|------|-----------|-----------|
| `topic_clusters.html` | **Interactive 2D map** | Web browser (recommended!) |
| `topic_clusters.png` | High-res scatter plot | Image viewer |
| `clustering_results.json` | All articles + metadata | Text editor / Python |

**Try the interactive map first!** It's the best way to explore clusters.

## 📁 Project Files

| File | Purpose |
|------|---------|
| **topic_clusterer.py** | Main pipeline - run this! |
| **manage_feeds.py** | Add/remove/test RSS feeds |
| **scrape_100_newspapers.py** | 5 example clustering scenarios |
| **analyze_results.py** | Explore results (statistics, search, export) |
| **test_setup.py** | Verify your setup works |
| **feeds.json** | 70+ newspaper RSS feeds (categorized) |
| **config.json** | Tunable parameters |
| **requirements.txt** | Python dependencies |
| **.env.example** | Template for API key |

## 🎯 Common Tasks

### Run the Full Pipeline
```bash
python topic_clusterer.py
```
Scrapes 100 headlines → embeds → clusters → labels → visualizes

### Try Different Examples
```bash
python scrape_100_newspapers.py
# Shows menu with 5 options:
# 1. All sources (100+ newspapers)
# 2. Tech-only clustering
# 3. International comparison
# 4. Business & finance
# 5. Multi-language news
```

### Manage News Sources
```bash
python manage_feeds.py -i
# Interactive menu to add/remove/test feeds
```

### Analyze Results
```bash
python analyze_results.py --interactive
# Explore clusters, search headlines, export data
```

### Validate Your Setup
```bash
python test_setup.py
# Checks dependencies, API key, RSS connectivity
```

## 📚 Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - 5-minute setup guide
- **[NEWSPAPERS.md](NEWSPAPERS.md)** - Use 100+ newspaper sources
- **[PROJECT_INDEX.md](PROJECT_INDEX.md)** - Complete project overview
- **[example_usage.py](example_usage.py)** - 5 clustering examples

## 💡 Use Cases

✅ **Journalists** - Find trending topics across sources  
✅ **Researchers** - Analyze news coverage by country/category  
✅ **Traders** - Track business/finance news  
✅ **Data Scientists** - Benchmark clustering/embeddings  
✅ **Students** - Learn NLP, clustering, embeddings  
✅ **News Aggregators** - Automated story detection  

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

## 🔧 Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Scraping** | feedparser | RSS feed parsing |
| **Embeddings** | Claude 3.5 Haiku API | Semantic vectors |
| **Clustering** | scikit-learn DBSCAN | Density-based grouping |
| **Labeling** | Claude 3.5 Haiku API | LLM labels |
| **Reduction** | PCA | 2D projection |
| **Static Viz** | Matplotlib + Seaborn | PNG plots |
| **Interactive Viz** | Plotly | HTML dashboard |

## ⚡ Performance & Costs

- **Runtime**: 3-5 minutes for 100 articles
- **API Cost**: ~$0.05 per run
- **RAM**: 2GB minimum, 4GB recommended
- **Python**: 3.8 or higher

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

## ❓ FAQ

### Q: How much does this cost?
**A:** Anthropic API: ~$0.05 per run (embeddings + labeling). RSS feeds: Free.

### Q: Can I add my own newspaper?
**A:** Yes! Edit `feeds.json` or use `python manage_feeds.py --add`

### Q: Why are some feeds empty?
**A:** Feeds update in real-time. If temporarily empty, try running again later.

### Q: Can I use a different clustering algorithm?
**A:** Yes! DBSCAN is default, but you can modify `topic_clusterer.py` to use KMeans, AgglomerativeClustering, etc.

### Q: How do I use the results in my own code?
**A:** Load the JSON output:
```python
import json
with open('clustering_results.json') as f:
    results = json.load(f)
    # Access results['clusters']
```

### Q: Can this work offline?
**A:** RSS scraping needs internet. Claude API calls need internet. Clustering/visualization work offline once you have data.

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| `ANTHROPIC_API_KEY not found` | Create `.env` file with your API key |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| `Connection timeout` | Check internet; some feeds may be down |
| `No clusters found` | Increase `eps` parameter (try 0.7-0.8) |
| `Too many noise points` | Decrease `eps` parameter (try 0.4-0.5) |
| `Authentication failed` | Generate new token at https://github.com/settings/tokens |

See [QUICKSTART.md](QUICKSTART.md) for detailed troubleshooting.

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
