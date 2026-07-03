# News Headline Clusterer

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/yourusername/news-headline-clusterer.svg)](https://github.com/yourusername/news-headline-clusterer)

Automatically discover, cluster, and visualize news headlines from 100+ newspapers worldwide using AI embeddings.

Works completely free with no API keys required. Choose from demo mode or real data with free local embeddings.

An intelligent pipeline that:
1. Scrapes headlines from major news sources (or uses demo data)
2. Embeds with free local AI (Sentence Transformers)
3. Clusters automatically with DBSCAN
4. Labels clusters (keyword-based or LLM-enhanced)
5. Visualizes results as interactive 2D maps

Perfect for journalists, researchers, data analysts, and news aggregators.

## Features

- **Zero Cost to Start** - Demo mode works instantly with no setup
- **100+ Newspaper Sources** - BBC, Reuters, CNN, Bloomberg, TechCrunch, Al Jazeera, and more
- **Free Local Embeddings** - Sentence Transformers (384D vectors, runs locally)
- **Automatic Clustering** - DBSCAN finds optimal groups (no tuning needed)
- **Smart Labeling** - Keyword-based (free) or Claude LLM (optional, paid)
- **Interactive Visualization** - Plotly HTML map with hover details, zoom, pan
- **Static Plots** - High-resolution PNG scatter plots
- **Structured Export** - Complete JSON data for analysis
- **Feed Management** - Add, remove, test newspaper sources
- **Multiple Running Modes** - Demo, real data, or interactive choice
- **No API Keys Required** - Works completely free

## How It Works

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

## Example Usage

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

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR-USERNAME/news-headline-clusterer.git
cd news-headline-clusterer
```

### 2. Install Dependencies
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# or: source venv/bin/activate  # macOS/Linux

pip install -r requirements.txt
```

### 3. Run (Choose Your Mode)

**Demo Mode (10 seconds, no setup)**
```bash
python topic_clusterer.py --demo
```
Sample headlines, instant clustering. Perfect for quick test.

**Real Data (2-3 minutes, free embeddings)**
```bash
python topic_clusterer.py --real
```
Real headlines from 100+ newspapers. Free local embeddings, no API key needed.

**Interactive (You choose)**
```bash
python topic_clusterer.py
# Select 1 for demo or 2 for real data
```

**With Enhanced Labels (Optional, Paid)**
```bash
# Create .env file:
ANTHROPIC_API_KEY=sk-ant-your-key-here

python topic_clusterer.py --real
# Uses Claude for better labels (~$0.05 per run)
```

See [NO_API_KEY_GUIDE.md](NO_API_KEY_GUIDE.md) for detailed comparison of all modes.

## View Results

After running, you get 3 output files:

| File | What It Is | Open With |
|------|-----------|-----------|
| `topic_clusters.html` | **Interactive 2D map** | Web browser (recommended!) |
| `topic_clusters.png` | High-res scatter plot | Image viewer |
| `clustering_results.json` | All articles + metadata | Text editor / Python |

**Try the interactive map first!** It's the best way to explore clusters.

## Project Files

### Core Scripts
| File | Purpose |
|------|---------|
| **topic_clusterer.py** | Main pipeline - run this! |
| **demo_data.py** | Sample headlines for demo mode |
| **manage_feeds.py** | Add/remove/test RSS feeds |
| **scrape_100_newspapers.py** | 5 example clustering scenarios |
| **analyze_results.py** | Explore results (statistics, search, export) |
| **test_setup.py** | Verify your setup works |

### Configuration
| File | Purpose |
|------|---------|
| **feeds.json** | 70+ newspaper RSS feeds (categorized) |
| **config.json** | Tunable parameters |
| **requirements.txt** | Python dependencies |
| **.env.example** | Template for API key |

### Documentation
| File | Purpose |
|------|---------|
| **NO_API_KEY_GUIDE.md** | How to run without API keys (demo/free modes) |
| **QUICKSTART.md** | 5-minute setup guide |
| **NEWSPAPERS.md** | 100+ newspaper sources guide |
| **GITHUB_GUIDE.md** | Quick intro for GitHub visitors |

## Common Tasks

### Quick Demo (Instant)
```bash
python topic_clusterer.py --demo
```
Try it immediately with sample data. No setup needed.

### Real Data (Free)
```bash
python topic_clusterer.py --real
```
Full pipeline on real news. Free embeddings, no API key needed.

### Try Different Scenarios
```bash
python scrape_100_newspapers.py
```
5 example configurations:
- All sources (100+ newspapers)
- Tech-only clustering
- International comparison
- Business & finance
- Multi-language news

### Manage News Sources
```bash
python manage_feeds.py -i
```
Interactive menu to add/remove/test feeds.

### Analyze Results
```bash
python analyze_results.py --interactive
```
Explore clusters, search headlines, export data.

### Validate Setup
```bash
python test_setup.py
```
Check dependencies, API key, RSS connectivity.

## Documentation

- **[NO_API_KEY_GUIDE.md](NO_API_KEY_GUIDE.md)** - Run without API keys (demo or free embeddings)
- **[QUICKSTART.md](QUICKSTART.md)** - 5-minute setup guide
- **[NEWSPAPERS.md](NEWSPAPERS.md)** - Use 100+ newspaper sources
- **[PROJECT_INDEX.md](PROJECT_INDEX.md)** - Complete project overview
- **[example_usage.py](example_usage.py)** - 5 clustering examples

## Use Cases

- **Journalists** - Find trending topics across sources  
- **Researchers** - Analyze news coverage by country/category  
- **Traders** - Track business/finance news  
- **Data Scientists** - Benchmark clustering/embeddings  
- **Students** - Learn NLP, clustering, embeddings  
- **News Aggregators** - Automated story detection  

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

## Technology Stack

| Layer | Technology | Cost | Notes |
|-------|-----------|------|-------|
| **Scraping** | feedparser | Free | RSS parsing |
| **Embeddings** | Sentence Transformers (default) | Free | Local, 384D vectors |
| **Embeddings** | Claude API (optional) | $0.01-0.03 | Better quality labels |
| **Clustering** | scikit-learn DBSCAN | Free | Density-based grouping |
| **Labeling** | Keyword analysis (free) or Claude (paid) | Free/$0.02 | Auto or LLM |
| **Reduction** | PCA | Free | 2D projection |
| **Visualization** | Matplotlib + Seaborn | Free | PNG plots |
| **Visualization** | Plotly | Free | Interactive HTML |

## Performance & Costs

| Mode | Runtime | Cost | Requirements |
|------|---------|------|--------------|
| Demo | ~10 seconds | Free | None |
| Real (Free) | 2-3 minutes | Free | Internet for RSS |
| Real (With Claude) | 3-5 minutes | ~$0.05 | API key |

**System Requirements:**
- Python 3.8+
- 2GB RAM (4GB recommended)
- ~400MB disk space (model downloads once)

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

## FAQ

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

## Troubleshooting

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

**Default (Free Mode):**
- Embeddings: Free (Sentence Transformers, local)
- Labeling: Free (keyword-based)
- Total: $0

**With Claude API (Optional):**
- Embeddings: Free (still uses Sentence Transformers)
- Labeling: ~$0.02-0.05 per run (Claude labels)
- **Total per run**: ~$0.05 estimate

Most users never need to pay.

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

---

**Questions?** Check the documentation or open an issue on GitHub.
