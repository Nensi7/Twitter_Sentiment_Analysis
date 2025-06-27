import pandas as pd
from datetime import datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load a small sample from Sentiment140 (first 50,000 rows, adjust path if needed)
df = pd.read_csv(
    "training.1600000.processed.noemoticon.csv",
    names=["polarity","id","date","query","user","text"],
    encoding="ISO-8859-1",
    parse_dates=["date"],
    nrows=50000
)

analyzer = SentimentIntensityAnalyzer()

records = []
for _, row in df.iterrows():
    d = row["date"].date()
    txt = row["text"]
    scores = analyzer.polarity_scores(txt)
    comp = scores["compound"]
    lbl = "positive" if comp >= 0.05 else "negative" if comp <= -0.05 else "neutral"
    records.append({
        "date": d,
        "hash": hash(txt),
        "text": txt,
        "compound": comp,
        "sentiment": lbl
    })
    if len(records) >= 5000:
        break

pd.DataFrame(records).to_csv("sample_1000_tweets_sentiment.csv", index=False)
print("Generated sample_1000_tweets_sentiment.csv with 1000 rows.")
