# monthly_sentiment_snscrape.py

import snscrape.modules.twitter as sntwitter
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import datetime

analyzer = SentimentIntensityAnalyzer()
results = []

for month in range(1, 13):
    since = f"2024-{month:02d}-01"
    # set until for next month; December rolls to January 2025
    until = f"2024-{month+1:02d}-01" if month < 12 else "2025-01-01"
    query = f"#python lang:en since:{since} until:{until}"
    print(f"Scraping tweets from: {since} to {until}...")

    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= 1000:  # limit per month
            break
        tweets.append(tweet.content)

    pos = neu = neg = 0
    for txt in tweets:
        score = analyzer.polarity_scores(txt)["compound"]
        if score >= 0.05:
            pos += 1
        elif score <= -0.05:
            neg += 1
        else:
            neu += 1

    total = len(tweets)
    results.append({
        "month": since[:7],
        "total": total,
        "positive": pos,
        "neutral": neu,
        "negative": neg,
        "pct_positive": round(pos/total*100, 1) if total else 0,
        "pct_neutral": round(neu/total*100, 1) if total else 0,
        "pct_negative": round(neg/total*100, 1) if total else 0
    })

df = pd.DataFrame(results)
df.to_csv("sentiment_2024_by_month.csv", index=False)
print("✅ Generated sentiment_2024_by_month.csv")
