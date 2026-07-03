"""
Demo data for testing without API keys
Contains sample headlines and pre-computed embeddings
"""

DEMO_ARTICLES = [
    {
        "title": "Apple Announces New iPhone 15 with Advanced AI Features",
        "source": "TechCrunch",
        "category": "Technology",
        "country": "USA",
        "published": "2026-07-01T10:00:00"
    },
    {
        "title": "Tesla Stock Rises on Strong Electric Vehicle Sales",
        "source": "Bloomberg",
        "category": "Business",
        "country": "USA",
        "published": "2026-07-01T09:30:00"
    },
    {
        "title": "Climate Summit Reaches Agreement on Carbon Reduction",
        "source": "BBC News",
        "category": "General News",
        "country": "UK",
        "published": "2026-07-01T08:45:00"
    },
    {
        "title": "Google Releases New Machine Learning Model",
        "source": "The Verge",
        "category": "Technology",
        "country": "USA",
        "published": "2026-07-01T11:00:00"
    },
    {
        "title": "Federal Reserve Raises Interest Rates Again",
        "source": "Reuters",
        "category": "Business",
        "country": "International",
        "published": "2026-07-01T14:20:00"
    },
    {
        "title": "Scientists Discover New Species in Amazon Rainforest",
        "source": "Science Daily",
        "category": "Science",
        "country": "Brazil",
        "published": "2026-07-01T07:15:00"
    },
    {
        "title": "Microsoft Invests Billions in AI Research",
        "source": "HackerNews",
        "category": "Technology",
        "country": "USA",
        "published": "2026-07-01T13:40:00"
    },
    {
        "title": "UK Parliament Debates New Privacy Laws",
        "source": "The Guardian",
        "category": "Politics",
        "country": "UK",
        "published": "2026-07-01T12:30:00"
    },
    {
        "title": "Amazon Forest Faces Record Deforestation",
        "source": "BBC News",
        "category": "Environment",
        "country": "Brazil",
        "published": "2026-07-01T06:50:00"
    },
    {
        "title": "Netflix Announces New Hit Series",
        "source": "Variety",
        "category": "Entertainment",
        "country": "USA",
        "published": "2026-07-01T16:00:00"
    },
    {
        "title": "World Cup Final: Historic Victory for Underdog Team",
        "source": "ESPN",
        "category": "Sports",
        "country": "International",
        "published": "2026-07-01T15:30:00"
    },
    {
        "title": "Health Officials Warn About New Disease Variant",
        "source": "Medical News Today",
        "category": "Health",
        "country": "USA",
        "published": "2026-07-01T10:45:00"
    },
    {
        "title": "IBM Develops Quantum Computing Breakthrough",
        "source": "TechCrunch",
        "category": "Technology",
        "country": "USA",
        "published": "2026-07-01T09:00:00"
    },
    {
        "title": "Stock Market Reaches All-Time High",
        "source": "MarketWatch",
        "category": "Business",
        "country": "USA",
        "published": "2026-07-01T11:30:00"
    },
    {
        "title": "University Research Shows Climate Change Accelerating",
        "source": "Nature",
        "category": "Science",
        "country": "UK",
        "published": "2026-07-01T08:00:00"
    },
    {
        "title": "Major Cybersecurity Breach Affects Millions",
        "source": "Wired",
        "category": "Technology",
        "country": "USA",
        "published": "2026-07-01T14:00:00"
    },
    {
        "title": "Oil Prices Drop on Supply Concerns",
        "source": "Bloomberg",
        "category": "Business",
        "country": "USA",
        "published": "2026-07-01T13:15:00"
    },
    {
        "title": "Wildlife Conservation Effort Succeeds in Africa",
        "source": "The Guardian",
        "category": "Environment",
        "country": "UK",
        "published": "2026-07-01T07:45:00"
    },
    {
        "title": "Space Agency Launches New Mars Mission",
        "source": "Science Daily",
        "category": "Science",
        "country": "USA",
        "published": "2026-07-01T12:00:00"
    },
    {
        "title": "Fashion Week Features Sustainable Designs",
        "source": "Variety",
        "category": "Entertainment",
        "country": "USA",
        "published": "2026-07-01T17:00:00"
    }
]

def get_demo_data():
    """Return demo articles for testing."""
    return DEMO_ARTICLES


def get_demo_info():
    """Return info about demo mode."""
    return {
        "mode": "demo",
        "articles_count": len(DEMO_ARTICLES),
        "note": "This is sample data for demonstration. Use real data with --real flag."
    }
