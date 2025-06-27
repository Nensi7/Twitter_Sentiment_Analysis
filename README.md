# Twitter_Sentiment_Analysis

# Twitter Sentiment Analysis 📈📊

A modular Python pipeline for **Twitter sentiment analysis**, combining data scraping with `snscrape`, sentiment scoring using **VADER** and **TextBlob**, and visualization-ready CSV outputs optimized for BI tools like Power BI and Streamlit. The pipeline also integrates a trimmed sample from the large Sentiment140 dataset to improve load times.

---

## 🚀 Features

- **Trimmed Sentiment140 Subset** – Sampled ~5,000 rows from the 1.6 million tweet dataset for faster development.
- **Monthly Tweet Scraping** – Collected ~1,000 English tweets per month in 2024 using `snscrape`, no Twitter API needed.
- **Dual Sentiment Scoring**:
  - **VADER** for social media text, handling informal language and punctuation.
  - **TextBlob** for longer review text.
- **Monthly Aggregation** – Outputs CSV with sentiment counts and percentages for each month.
- **BI-Ready Output** – Compatible with Power BI, Plotly, and Streamlit dashboards.
- **Performance Optimization** – Works with smaller datasets to streamline iteration and loading.

---

## 📚 References

- snscrape – Twitter scraping tool 
- TextBlob – Sentiment analysis for review text
- pandas – Data manipulation library
- Power BI, Streamlit, Plotly – Visualization tools

--- 

##  Next Steps ✅ 

- Add daily granularity for more detailed trends.
- Filter data by specific hashtags or keywords.
- Upgrade sentiment analysis using transformer models such as BERT.
- Build a live dashboard using Streamlit or Dash.
- Automate the pipeline with Docker or CI/CD tools.

---

## 📦 Installation

```bash
git clone <repo-url>
cd twitter_sentiment_analysis
pip install -r requirements.txt


