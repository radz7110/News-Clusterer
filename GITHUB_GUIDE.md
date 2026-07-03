# 👋 Welcome to Topic Clusterer

**You found a project to cluster news headlines from 100+ newspapers using AI!**

This guide explains what this project does and how to use it on GitHub.

## 🎯 What Is This?

Topic Clusterer automatically:
1. 📡 Scrapes headlines from 100+ newspapers (BBC, Reuters, Bloomberg, etc.)
2. 🧠 Generates semantic embeddings using Claude AI
3. 🎯 Groups similar articles into topic clusters automatically
4. 🏷️ Labels each cluster with an AI-generated topic name
5. 📊 Creates interactive 2D visualizations

**Example:** Scrape 100 headlines → Get 12 topic clusters like "Technology News", "Climate Policy", "Sports Updates"

## 🚀 Quick Start (Copy & Paste)

### 1. Clone This Repository
```bash
git clone https://github.com/YOUR-USERNAME/topic-clusterer.git
cd topic-clusterer
```

### 2. Set Up (5 minutes)
```bash
# Create environment
python -m venv venv
venv\Scripts\activate  # Windows
# or: source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### 3. Add Your API Key
Get free key from [console.anthropic.com](https://console.anthropic.com/)

```bash
cp .env.example .env
# Edit .env and paste your API key
```

### 4. Run It!
```bash
python topic_clusterer.py
```

### 5. View Results
- Open `topic_clusters.html` in your browser (best view!)
- Or open `topic_clusters.png` to see the plot
- Or load `clustering_results.json` in code

**That's it!** ✅

## 📊 What You Get

| Output | What It Shows |
|--------|---------------|
| **topic_clusters.html** | Interactive 2D map with hover info |
| **topic_clusters.png** | Static plot (shareable image) |
| **clustering_results.json** | Raw data (all articles organized by cluster) |

## 🎯 Example Outputs

### Interactive HTML Map
- Hover over points to see full headlines
- Click legend to show/hide clusters
- Zoom and pan to explore
- Different colors = different topics

### Static PNG Plot
- Clean scatter plot showing all clusters
- Color-coded by topic
- High resolution (300 DPI)

### JSON Data
```json
{
  "clusters": {
    "0": {
      "label": "Technology News",
      "size": 15,
      "articles": [
        {
          "title": "New AI Model Breaks Records...",
          "source": "HackerNews",
          "link": "https://..."
        },
        ...
      ]
    }
  }
}
```

## 🎮 Try Different Examples

### Run the Demo Menu
```bash
python scrape_100_newspapers.py
```

Choose from:
1. **All sources** - Scrape from 100+ newspapers
2. **Tech only** - Just technology news
3. **International** - Compare news by country
4. **Business** - Finance and stocks
5. **Multi-language** - Global coverage

## 🛠️ Common Tasks

### Add Your Own Newspaper
```bash
python manage_feeds.py --add "My News" "https://feed.url/rss" "Technology" "USA"
```

### Analyze Results Interactively
```bash
python analyze_results.py -i
# Menu to search, export, analyze clusters
```

### Validate Your Setup
```bash
python test_setup.py
# Checks dependencies and API key
```

### Change Clustering Settings
Edit `config.json`:
```json
{
  "clustering": {
    "eps": 0.6,  // Lower = more clusters
    "min_samples": 2
  }
}
```

## 📁 Project Files Explained

| File | What It Does |
|------|--------------|
| **topic_clusterer.py** | Main pipeline (run this!) |
| **scrape_100_newspapers.py** | 5 example scenarios |
| **manage_feeds.py** | Add/test newspaper feeds |
| **analyze_results.py** | Explore clustering results |
| **test_setup.py** | Verify your setup |
| **feeds.json** | 70+ newspaper RSS feeds |
| **config.json** | Tunable parameters |
| **requirements.txt** | Python dependencies |

## ❓ FAQ

**Q: How much does it cost?**  
A: About $0.05 per run (Claude API calls). RSS feeds are free.

**Q: Do I need an API key?**  
A: Yes, get a free one from [console.anthropic.com](https://console.anthropic.com/)

**Q: Can I add more newspapers?**  
A: Yes! `feeds.json` has 70+ already. Add more with `manage_feeds.py`

**Q: Why are some clusters small?**  
A: Articles are diverse. Adjust `eps` in config.json for more/fewer clusters.

**Q: Can I modify the code?**  
A: Absolutely! MIT license - do whatever you want.

**Q: Does it work offline?**  
A: No, needs internet for RSS scraping and Claude API. But clustering works offline once you have data.

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| `API key not found` | Create `.env` file with your key |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| `Connection timeout` | Check internet, some feeds may be down |
| `No clusters found` | Increase `eps` to 0.7-0.8 in config |
| `Too much noise` | Decrease `eps` to 0.4-0.5 in config |

## 📚 Full Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - Get started in 5 minutes
- **[NEWSPAPERS.md](NEWSPAPERS.md)** - All 100+ newspaper sources
- **[README.md](README.md)** - Complete technical docs
- **[PROJECT_INDEX.md](PROJECT_INDEX.md)** - Full project overview

## 💡 Use Cases

- 📰 **Journalists** - Find trending topics
- 🔬 **Researchers** - Study news coverage patterns
- 💰 **Traders** - Monitor finance news
- 📊 **Data Scientists** - Clustering benchmark
- 👨‍🎓 **Students** - Learn NLP and embeddings
- 🤖 **AI Enthusiasts** - Explore Claude API

## 🔧 Advanced Usage

### Python API
```python
from topic_clusterer import scrape_rss_feeds, embed_headlines, cluster_with_dbscan

# Scrape
articles = scrape_rss_feeds(num_articles=100)

# Embed
embeddings = embed_headlines([a['title'] for a in articles])

# Cluster
labels, n_clusters = cluster_with_dbscan(embeddings)
```

### Filter by Category
```python
# Tech only
tech = [a for a in articles if a['category'] == 'Technology']

# International (non-USA)
intl = [a for a in articles if a['country'] != 'USA']
```

### Custom Feeds
Edit `feeds.json` directly or use:
```bash
python manage_feeds.py --add "My Feed" "url" "Category" "Country"
```

## 🎓 Learn More

- **DBSCAN Clustering**: https://scikit-learn.org/stable/modules/clustering.html#dbscan
- **Claude API**: https://console.anthropic.com/docs
- **Plotly Visualization**: https://plotly.com/python/
- **RSS Feeds**: https://www.feedspot.com

## 🤝 Contributing

Found a bug? Want to add a feature? You can:
- Open an Issue (describe the problem)
- Fork and submit a Pull Request
- Suggest improvements

MIT License - use freely!

## 🚀 Next Steps

1. Clone the repo
2. Set up (5 minutes)
3. Add API key
4. Run `python topic_clusterer.py`
5. Open the HTML file
6. Explore the clusters!

---

**Questions?** Check [README.md](README.md) for full docs or open an Issue.

**Ready to get started?** Follow the "Quick Start" section above! 🎉
