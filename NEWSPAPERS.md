# Scraping from 100+ Newspapers

Complete guide to using the expanded RSS feed list to scrape headlines from over 100 newspapers worldwide.

## 📰 Available Newspapers by Category

### 📡 Major General News (12 sources)
- BBC News, Reuters, CNN, The New York Times, The Washington Post, The Guardian, USA Today, Associated Press, NPR, PBS NewsHour, ABC News, NBC News

### 💼 Business & Finance (8 sources)
- Bloomberg, Financial Times, Wall Street Journal, CNBC, MarketWatch, Yahoo Finance, Seeking Alpha, Investopedia

### 🖥️ Technology (10 sources)
- HackerNews, The Verge, TechCrunch, Wired, Ars Technica, Slashdot, AnandTech, ZDNet, PC World, MacRumors

### 🔬 Science & Health (6 sources)
- Nature, Science Daily, Medical News Today, Healthline, WebMD, The Atlantic (Science section)

### 🏛️ Politics & Government (4 sources)
- Politico, The Hill, Axios, Vox

### ⚽ Sports (4 sources)
- ESPN, Sports Illustrated, The Athletic, Bleacher Report

### 🎬 Entertainment (4 sources)
- Variety, The Hollywood Reporter, Deadline, Vulture

### 🌍 International (9 sources)
- Der Spiegel (Germany), France24 (France), DW News (Germany), Al Jazeera (Qatar), Times of India, Hindustan Times, South China Morning Post (Hong Kong), Sydney Morning Herald (Australia), The Globe and Mail (Canada)

### 🏙️ Local US News (10 sources)
- LA Times, Chicago Tribune, Boston Globe, New York Post, Philadelphia Inquirer, Miami Herald, Houston Chronicle, Denver Post, Seattle Times, Minneapolis Star Tribune

### 🇬🇧 UK News (6 sources)
- The Telegraph, The Times, The Independent, The Mirror, Sky News, The Sun

**Total: 70+ sources, growing regularly**

## 🚀 Quick Start

### Option 1: Use Default 5 Sources (Fastest)
```bash
python topic_clusterer.py
```
Uses: BBC, Reuters, CNN, The Guardian, HackerNews

### Option 2: Use All 100+ Newspapers
```bash
python topic_clusterer.py
# Then choose to load from feeds.json
```

### Option 3: Use Example Scripts
```bash
# Interactive menu with 5 different examples
python scrape_100_newspapers.py

# Or run specific example
python scrape_100_newspapers.py 1  # All sources
python scrape_100_newspapers.py 2  # Tech only
python scrape_100_newspapers.py 3  # International
python scrape_100_newspapers.py 4  # Business
python scrape_100_newspapers.py 5  # Multi-language
```

## 📊 Example Output

### All Sources (100+ articles)
```
Scraping from 70 news sources...
Target: ~1 articles per feed = 100 total

✓ BBC News (1 articles) [General News]
✓ Reuters (1 articles) [General News]
✓ CNN (1 articles) [General News]
✓ The New York Times (1 articles) [General News]
...
✓ The Guardian (1 articles) [General News]

============================================================
Scraping Summary: 68/70 feeds successful
Articles collected: 100 (target: 100)
============================================================
```

## 🛠️ Manage Your Feeds

### Interactive Feed Manager
```bash
python manage_feeds.py -i
```

Menu options:
1. Show statistics
2. List all feeds
3. List feeds by category
4. Test all feeds
5. Test specific feed
6. Add a feed
7. Remove a feed
8. Exit

### View Statistics
```bash
python manage_feeds.py --stats
```

Output:
```
FEED STATISTICS
============================================================

Total Feeds: 70

By Category:
  major_us_news              12 ( 17.1%)
  business_finance            8 ( 11.4%)
  technology                 10 ( 14.3%)
  ...
```

### List Feeds by Category
```bash
python manage_feeds.py --list
python manage_feeds.py --category technology
python manage_feeds.py --category business_finance
```

### Test Feed Connectivity
```bash
python manage_feeds.py --test-all      # Test all feeds
python manage_feeds.py --test "https://feeds.bbci.co.uk/news/rss.xml"
```

### Add Custom Feed
```bash
python manage_feeds.py --add "Feed Name" "https://feed.url/rss" "Category" "Country"
```

## 📝 Customization Guide

### Create Custom Feed List

Create `custom_feeds.json`:
```json
{
  "description": "My custom feeds",
  "categories": {
    "tech_and_business": [
      {
        "name": "TechCrunch",
        "url": "http://feeds.techcrunch.com/techcrunch/",
        "country": "USA",
        "category": "Technology"
      },
      {
        "name": "Bloomberg",
        "url": "https://feeds.bloomberg.com/markets/news.rss",
        "country": "USA",
        "category": "Business"
      }
    ]
  }
}
```

Then use:
```python
from topic_clusterer import scrape_rss_feeds

articles = scrape_rss_feeds(num_articles=50)
# Will load from default feeds.json (70+ sources)
```

### Filter by Category

```python
import json
from topic_clusterer import scrape_rss_feeds

# Get all articles
articles = scrape_rss_feeds(num_articles=200)

# Filter to specific categories
tech_articles = [a for a in articles if a['category'] == 'Technology']
business_articles = [a for a in articles if a['category'] == 'Business']
international_articles = [a for a in articles if a['country'] != 'USA']
```

### Filter by Country

```python
# Get only UK news
uk_articles = [a for a in articles if a['country'] == 'UK']

# Get only international (non-USA)
international = [a for a in articles if a['country'] != 'USA']

# Get specific country
india_articles = [a for a in articles if a['country'] == 'India']
```

### Use Specific Sources

```python
# Use only technology sources
from topic_clusterer import scrape_rss_feeds

tech_sources = {'The Verge', 'TechCrunch', 'Wired', 'Ars Technica', 'HackerNews'}

articles = scrape_rss_feeds(num_articles=100)
filtered = [a for a in articles if a['source'] in tech_sources]
```

## 📈 Examples

### Example 1: Cluster News from 100+ Newspapers

```python
from topic_clusterer import (
    scrape_rss_feeds, embed_headlines, cluster_with_dbscan,
    label_clusters_with_llm, reduce_to_2d, plot_interactive_map
)

# Scrape from all 70+ sources
articles = scrape_rss_feeds(num_articles=150)
headlines = [a['title'] for a in articles]

# Embed and cluster
embeddings = embed_headlines(headlines)
labels, n_clusters = cluster_with_dbscan(embeddings)
cluster_labels = label_clusters_with_llm(articles, labels)

# Visualize
embeddings_2d = reduce_to_2d(embeddings)
plot_interactive_map(embeddings_2d, labels, articles, cluster_labels)

print(f"Clustered {len(articles)} articles from {len(set(a['source'] for a in articles))} sources")
```

### Example 2: Tech News Only

```python
from topic_clusterer import scrape_rss_feeds

# Get diverse sources
articles = scrape_rss_feeds(num_articles=200)

# Filter to tech
tech_articles = [a for a in articles if a['category'] == 'Technology'][:100]

# Then cluster as normal...
```

### Example 3: International Comparison

```python
from topic_clusterer import scrape_rss_feeds
from collections import defaultdict

articles = scrape_rss_feeds(num_articles=150)

# Group by country
by_country = defaultdict(list)
for article in articles:
    by_country[article['country']].append(article)

# Now you can analyze per-country trends
for country in sorted(by_country.keys()):
    print(f"{country}: {len(by_country[country])} articles")
```

## 🔧 Configuration

Edit `config.json` to customize:

```json
{
  "scraping": {
    "num_articles": 100,
    "timeout": 30
  },
  "clustering": {
    "eps": 0.6,
    "min_samples": 2
  }
}
```

## ⚠️ Troubleshooting

### Issue: "Some feeds failed to load"
**This is normal!** Some feeds may be:
- Temporarily unavailable
- Rate-limited
- Geo-blocked
- Moved or discontinued

The script continues with available feeds. Success rate typically 85-95%.

### Issue: "Only got 50 articles instead of 100"
**Solutions:**
1. Some feeds had no articles available
2. Increase timeout: `timeout: 60` in config.json
3. Run again later (feeds update frequently)
4. Add more feeds to `feeds.json`

### Issue: "Different results each run"
This is expected because:
- RSS feeds update constantly
- Different articles available each day
- Feed timeouts vary

This is actually good for testing robustness!

### Add More Feeds

```bash
python manage_feeds.py --add "My Feed" "https://example.com/rss" "Technology" "USA"
```

Or edit `feeds.json` directly:

```json
{
  "name": "My News Site",
  "url": "https://example.com/rss.xml",
  "country": "USA",
  "category": "Technology"
}
```

## 📚 Feed Sources

### Finding More RSS Feeds

- **Google News RSS**: Add `?output=rss` to Google News URLs
- **Medium Publications**: `medium.com/@username/feed`
- **Reddit**: `reddit.com/r/subreddit/.rss`
- **YouTube Channels**: Search "YouTube channel RSS"
- **Newsletter Archives**: Many newsletters have RSS feeds
- **Company News**: Look for "Press Releases RSS" on company sites

### RSS Feed Directory

- https://www.feedspot.com - 100,000+ feeds
- https://directory.fsf.org/wiki/Feeds - Free software feeds
- https://blogtrottr.com - Find any blog's RSS

## 🔗 Full Feed List Reference

See `feeds.json` for complete list with:
- Feed name
- RSS URL
- Category
- Country of origin

## 🎯 Next Steps

1. **Explore:** `python manage_feeds.py --stats`
2. **Test:** `python manage_feeds.py --test-all`
3. **Scrape:** `python scrape_100_newspapers.py 1`
4. **Customize:** Edit `feeds.json` or create custom list
5. **Cluster:** `python topic_clusterer.py`

---

**Pro tip:** Combine with `analyze_results.py` to explore results by source and category!
