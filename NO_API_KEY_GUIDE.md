# Running Without an API Key

You can use News Headline Clusterer without paying for any API keys. Here are your options:

## Option 1: Demo Mode (Easiest)

**No setup needed. Just run:**

```bash
python topic_clusterer.py --demo
```

**What you get:**
- 20 sample news headlines
- Full clustering pipeline
- Simple keyword-based labels (no API calls)
- See exactly how it works
- ~5 seconds to run

**Perfect for:**
- Trying the project immediately
- Understanding how clustering works
- Sharing a quick demo
- Testing on new machine

---

## Option 2: Real Data + Free Local Embeddings (Recommended)

**Uses free, locally-running embeddings. No API key needed.**

```bash
python topic_clusterer.py --real
```

Or just run without arguments and choose "2" when prompted:
```bash
python topic_clusterer.py
# Select: 2 (Real data)
```

**What happens:**
1. Scrapes 100 real headlines from RSS feeds (free)
2. Generates embeddings locally using Sentence Transformers (free, open-source)
3. Clusters with DBSCAN (free, scikit-learn)
4. Labels using keyword analysis (free)
5. Creates visualizations (free)

**Embeddings Used:**
- **Sentence Transformers** (`all-MiniLM-L6-v2`)
  - Free, open-source
  - Runs entirely locally
  - 384-dimensional vectors
  - High quality
  - ~400MB download (one time)

**What you get:**
- Real news from 100+ newspapers
- High-quality semantic embeddings
- Professional clustering results
- Interactive visualization
- ~2-3 minutes to run

**Requirements:**
- Internet connection (to scrape RSS feeds only)
- ~400MB disk space (model downloads on first run)
- No API keys needed
- No registration needed

**Alternative Embeddings (if you want different models):**
- Universal Sentence Encoder (free, Google)
- Other Sentence Transformers models (free, open-source)
- BERT-based models (free, open-source)

Contact us if you want different embedding options!

**Perfect for:**
- Production use without costs
- Processing real news
- Serious analysis
- Learning embeddings

---

## Comparison

| Feature | Demo | Real + Local |
|---------|------|--------------|
| Setup time | 0 seconds | 5 minutes |
| Data | Sample (20 articles) | Real (100+ articles) |
| Embeddings | N/A (keywords) | Free local (384D) |
| Quality | Low (keywords) | High (semantic) |
| Cost | $0 | $0 |
| Internet needed | No | Yes (for RSS) |
| API key needed | No | No |
| Runtime | ~5 seconds | ~2-3 minutes |

---

## How to Upgrade

If you want even better results, you can optionally add an API key:

### Option 3: Real Data + Claude Embeddings (Best Quality, Paid)

1. Get API key from https://console.anthropic.com/
2. Add to `.env` file:
   ```env
   ANTHROPIC_API_KEY=sk-ant-your-key-here
   ```
3. Run normally:
   ```bash
   python topic_clusterer.py
   # Choose: 2 (Real data)
   # Will auto-detect API key and use Claude embeddings
   ```

**Cost:** ~$0.05 per run  
**Quality:** Excellent (Claude embeddings + LLM labels)

---

## Recommended Path

1. **First time:** Use `--demo` to see it work instantly
2. **Serious use:** Use `--real` for real data (no costs)
3. **Best quality:** Add API key for Claude embeddings (small cost)

---

## Troubleshooting

### "No module named 'sentence_transformers'"

Install it:
```bash
pip install sentence-transformers
```

### Demo mode doesn't exist on older version

Update to latest:
```bash
git pull origin main
pip install -r requirements.txt
```

### Real mode is slow first time

The embedding model downloads (~400MB). This only happens once.

### Want to switch between demo and real?

Just run again with different flag:
```bash
python topic_clusterer.py --demo    # Demo mode
python topic_clusterer.py --real    # Real mode
python topic_clusterer.py           # Ask me (interactive)
```

---

## Summary

- **Demo:** `python topic_clusterer.py --demo`
- **Real (free):** `python topic_clusterer.py --real`
- **Interactive:** `python topic_clusterer.py`

**No API key required for either option!** 🎉
