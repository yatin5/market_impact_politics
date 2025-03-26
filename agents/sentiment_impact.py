from crewai.tools.base_tool import tool
from configs.config import OPENAI_API_KEY
from openai import OpenAI

client = OpenAI(api_key=OPENAI_API_KEY)
from tools.market_data import fetch_financial_data

@tool("Analyze sentiment and market impact")
def analyze_sentiment(news: list):
    """Analyze sentiment and predict market impact using OpenAI API."""
    results = {}
    for headline in news:
        prompt = (
            f"Analyze the following news headline for sentiment and market impact:\n"
            f"Headline: {headline}\n"
            f"Provide a sentiment (Positive, Neutral, Negative) and a brief market impact analysis."
        )
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a financial news analyst."},
            {"role": "user", "content": prompt}
        ])
        analysis = response.choices[0].message.content.strip()
        results[headline] = analysis
        print(f"[SentimentImpact] Analysis for headline: {headline}\n{analysis}\n")
    return results

def analyze_financial_impact(news: list):
    """Analyze the financial impact of relevant news using stock data."""
    financial_impact = {}
    for headline in news:
        # Example: Analyze impact on a specific stock ticker (e.g., AAPL)
        ticker = "AAPL"  # Replace with dynamic mapping if needed
        stock_data = fetch_financial_data(ticker)
        if stock_data:
            financial_impact[headline] = {
                "ticker": ticker,
                "impact": "Positive" if "gain" in headline.lower() else "Neutral"
            }
    print("[SentimentImpact] Financial impact analysis results:")
    for headline, impact in financial_impact.items():
        print(f"- {headline}: {impact}")
    return financial_impact

from tools.news_store import NewsStore

class NewsAnalyzer:
    def __init__(self):
        pass

    def analyze_news(self, headlines):
        """Analyze the sentiment and relevance of news headlines using OpenAI API."""
        results = {}
        for headline in headlines:
            prompt = (
                f"Analyze the following news headline for sentiment and relevance to financial markets:\n"
                f"Headline: {headline}\n"
                f"Provide a sentiment (Positive, Neutral, Negative) and relevance score (0-10)."
            )
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a financial news analyst."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=100
            )
            analysis = response.choices[0].message.content.strip()
            results[headline] = analysis
            print(f"[NewsAnalyzer] Analysis for headline: {headline}\n{analysis}\n")
        return results

news_store_tool = NewsStore

sentiment_impact = analyze_sentiment

news_analyzer = NewsAnalyzer()