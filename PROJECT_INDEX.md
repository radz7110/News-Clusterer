# Topic Clusterer Project Index

A complete implementation of a news article topic clustering system with RSS scraping, AI embeddings, DBSCAN clustering, LLM labeling, and interactive visualization.

## 📁 Project Structure

### Core Pipeline
- **`topic_clusterer.py`** (14 KB)
  - Main pipeline implementation
  - All 6 stages: scrape → embed → cluster → label → reduce → visualize
  - Scrapes 100+ headlines from major news sources
  - Uses Claude for embeddings and cluster labeling
  - Outputs: PNG plot, interactive HTML, JSON results

### Examples & Utilities
- **`example_usage.py`** (7 KB)
  - 5 example configurations demonstrating different use cases
  - Fine-grained clustering (more clusters)
  - Broad clustering (fewer clusters)
  - Batch processing and analysis
  - Source-specific analysis
  - Educational examples with detailed comments

- **`analyze_results.py`** (10 KB)
  - Post-processing analysis tool
  - Cluster summaries and statistics
  - Source distribution analysis
  - Keyword frequency analysis
  - Timeline analysis
  - Interactive explorer mode
  - Export individual clusters

- **`test_setup.py`** (7 KB)
  - Setup validation script
  - Checks Python version, dependencies, API key
  - Tests RSS feed connectivity
  - Verifies API functionality
  - Pre-flight checklist before running pipeline

### Configuration & Setup
- **`config.json`** (1.4 KB)
  - All tunable parameters in one place
  - Clustering settings (DBSCAN eps, min_samples)
  - Visualization options (colors, sizes, formats)
  - Output file paths
  - Model selections
  - Easy to customize without editing Python

- **`.env.example`** (0.3 KB)
  - Template for environment variables
  - Shows where to put ANTHROPIC_API_KEY
  - Copy to `.env` and fill in your key

- **`requirements.txt`** (158 bytes)
  - Python package dependencies
  - Core: anthropic, feedparser, scikit-learn
  - Visualization: matplotlib, seaborn, plotly
  - Install with: `pip install -r requirements.txt`

### Documentation
- **`QUICKSTART.md`** (5 KB)
  - 5-minute setup guide
  - Step-by-step installation
  - How to view results
  - Quick configuration tips
  - Troubleshooting common issues
  - **Start here!**

- **`README.md`** (6 KB)
  - Comprehensive documentation
  - Feature overview
  - Architecture diagram
  - Installation instructions
  - Complete usage guide
  - Parameter explanations
  - Troubleshooting section
  - Advanced customization
  - Performance notes and costs

- **`PROJECT_INDEX.md`** (this file)
  - Project structure overview
  - File descriptions
  - Quick reference guide

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set up API key
# Copy .env.example to .env and add your Anthropic API key

# 3. Validate setup (optional but recommended)
python test_setup.py

# 4. Run the pipeline
python topic_clusterer.py

# 5. View results
# - topic_clusters.html (interactive - recommended!)
# - topic_clusters.png (static plot)
# - clustering_results.json (data export)
```

## 📊 Data Flow

```
100 Headlines from RSS
        ↓
Anthropic API: Generate 10D Embeddings
        ↓
DBSCAN: Cluster Similar Articles
        ↓
Anthropic API: Label Each Cluster
        ↓
PCA: Reduce to 2D
        ↓
Visualization
├─ Static Plot (PNG)
├─ Interactive Plot (HTML)
└─ Data Export (JSON)
```

## 🎯 Key Features

### 1. RSS Scraping
- 5 major news sources: BBC, Reuters, CNN, The Guardian, HackerNews
- Configurable feeds in config.json
- Error handling for unavailable sources
- Extracts: title, description, source, publication date, link

### 2. Smart Embeddings
- Uses Claude API for semantic understanding
- 10-dimensional vectors capture article meaning
- Batch processing for efficiency
- Cached for reproducibility

### 3. DBSCAN Clustering
- Fully automated - no need to specify number of clusters
- Identifies noise points (articles that don't fit cleanly)
- Customizable density parameters (eps, min_samples)
- Cosine distance for semantic similarity

### 4. Intelligent Labeling
- Claude generates 2-3 word topic labels
- Based on actual article content
- Concise and human-readable
- 10 sample articles per cluster for context

### 5. Interactive Visualization
- **HTML Map**: Hover for headlines, zoom/pan, toggle clusters
- **PNG Plot**: High-resolution static image
- Color-coded by topic
- Noise points marked differently
- Plotly-powered for interactivity

### 6. Structured Export
- Complete JSON with all articles grouped by cluster
- Per-cluster statistics and metadata
- Timestamp and configuration info
- Ready for downstream analysis

## ⚙️ Configuration Guide

### Clustering Sensitivity

```python
# Stricter clustering (more, smaller clusters)
eps=0.4, min_samples=2

# Balanced (default)
eps=0.6, min_samples=2

# Looser clustering (fewer, larger clusters)
eps=0.8, min_samples=1
```

### Number of Articles

```python
# Quick test (1 minute)
num_articles=30

# Standard run (3-5 minutes)
num_articles=100

# Deep analysis (10+ minutes)
num_articles=200+
```

### Visualization Colors

Change in `topic_clusterer.py`:
```python
colors = sns.color_palette("husl", len(unique_labels))
# Options: "husl", "Set2", "coolwarm", "Paired", "tab10", etc.
```

## 📈 Output Examples

### Clustering Results JSON
```json
{
  "metadata": {
    "timestamp": "2026-07-02T10:30:00",
    "total_articles": 100,
    "num_clusters": 8
  },
  "clusters": {
    "0": {
      "label": "Technology Updates",
      "size": 15,
      "articles": [
        {
          "title": "New AI Breakthrough...",
          "source": "HackerNews",
          "published": "2026-07-02T09:00:00",
          "link": "https://..."
        }
      ]
    }
  }
}
```

### Analysis Output
```
CLUSTERING SUMMARY
====================================
Timestamp: 2026-07-02T10:30:00
Total articles: 100
Number of clusters: 8

CLUSTER OVERVIEW
====================================
Cluster  Label                    Size  Percent
0        Technology Updates         15     15.0%
1        Climate & Environment      12     12.0%
2        Politics & Government       8      8.0%
3        Business News              10     10.0%
```

## 🔧 Customization Examples

### Use Only Specific News Sources
```python
feeds = [
    "http://feeds.bbci.co.uk/news/rss.xml",
    "https://feeds.reuters.com/reuters/topNews",
]
```

### Adjust Cluster Labels Quality
```python
# More thorough labeling (slower, better quality)
max_articles_per_cluster: 15

# Faster labeling (fewer samples)
max_articles_per_cluster: 5
```

### Change Visualization Template
```python
# Static plot styling
plt.style.use('seaborn-v0_8-darkgrid')  # or other styles

# Interactive plot theme
fig.update_layout(template='plotly_dark')  # or 'plotly_white'
```

## 🧪 Testing & Validation

### Pre-Flight Check
```bash
python test_setup.py
```
Validates:
- Python version 3.8+
- All dependencies installed
- API key configured
- RSS feed connectivity
- API functionality

### Quick Test Run
```bash
# Edit topic_clusterer.py, change:
articles = scrape_rss_feeds(num_articles=20)
# Then run normally
python topic_clusterer.py
```

### Analyze Existing Results
```bash
python analyze_results.py

# Interactive exploration
python analyze_results.py --interactive

# Show specific cluster
python analyze_results.py --cluster 0

# Search headlines
python analyze_results.py --file clustering_results.json
# Then choose option 2 (search)
```

## 📊 Performance Characteristics

| Stage | Time | Cost |
|-------|------|------|
| Scraping (100 articles) | 10-30s | Free |
| Embedding | 1-2 min | $0.01-0.03 |
| Clustering | <1s | Free |
| Labeling (8 clusters) | 30-60s | $0.02-0.05 |
| Visualization | <5s | Free |
| **Total** | **3-5 min** | **~$0.05** |

## 🔐 Security & Privacy

- API key stored locally in `.env` (ignored by git)
- No data sent to external services except Anthropic
- Results stored locally only
- All processing happens client-side
- Add `.env` to `.gitignore` for safe sharing

## 📚 Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| LLM | Claude 3.5 Haiku | Embeddings + Labeling |
| Web Scraping | feedparser | RSS parsing |
| Clustering | scikit-learn DBSCAN | Density-based grouping |
| Embedding Reduction | PCA | 2D visualization |
| Static Visualization | Matplotlib/Seaborn | PNG output |
| Interactive Viz | Plotly | HTML exploration |
| Data Processing | NumPy/pandas | Array operations |

## 🎓 Learning Resources

Each file has educational value:

1. **topic_clusterer.py** - See complete ML pipeline
2. **example_usage.py** - Learn different configurations
3. **analyze_results.py** - Explore result analysis patterns
4. **test_setup.py** - System validation best practices

## 🐛 Troubleshooting Reference

| Issue | Solution |
|-------|----------|
| API key not found | Copy `.env.example` to `.env`, add your key |
| RSS feeds timeout | Some sources may be down, script continues with others |
| Few clusters | Increase `eps` parameter (e.g., 0.7 or 0.8) |
| Too many noise points | Decrease `eps` (e.g., 0.4 or 0.5) |
| Plotly not installed | `pip install plotly` |
| Memory error | Reduce `num_articles` parameter |
| Slow performance | Check internet connection and API rate limits |

## 📈 Next Steps

1. **Get Started**: Follow QUICKSTART.md
2. **Understand**: Read README.md for detailed docs
3. **Experiment**: Try example_usage.py scenarios
4. **Analyze**: Use analyze_results.py to explore output
5. **Customize**: Edit config.json and parameters
6. **Extend**: Add custom RSS feeds or modify clustering logic

## 🔗 External Resources

- **Anthropic API**: https://console.anthropic.com/
- **DBSCAN Documentation**: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html
- **Feedparser Docs**: https://feedparser.readthedocs.io/
- **Plotly Reference**: https://plotly.com/python/

---

**Ready to run?** Start with: `python QUICKSTART.md` then `python topic_clusterer.py`

**Questions?** Check the relevant documentation file above.

**Found a bug?** Review test_setup.py output and check your API key configuration.
