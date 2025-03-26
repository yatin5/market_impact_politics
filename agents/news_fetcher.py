from crewai.tools.base_tool import tool
import requests
from configs.config import SERPER_API_KEY, GOOGLE_CSE_ID, GOOGLE_API_KEY

@tool("Fetch political news")
def fetch_news(query: str):
    """Fetch political news headlines using the Serper API."""
    base_url = "https://www.googleapis.com/customsearch/v1"
    headers = {}
    params = {
        "q": query,
        "cx": GOOGLE_CSE_ID,
        "key": GOOGLE_API_KEY
    }
    print(f"[NewsFetcher] Request URL: {base_url}")
    print(f"[NewsFetcher] Params: {params}")
    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code == 200:
        news_data = response.json()
        headlines = [item["title"] for item in news_data.get("items", [])]
        print("[NewsFetcher] Fetched news headlines:")
        for headline in headlines:
            print(f"- {headline}")
        return headlines
    else:
        print(f"[NewsFetcher] Failed to fetch news: {response.status_code}")
        return []

news_fetcher = fetch_news