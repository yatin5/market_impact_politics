import requests

def fetch_financial_data(ticker: str):
    """Fetch financial data for a given stock ticker."""
    base_url = "https://www.alphavantage.co/query"
    api_key = "your_alpha_vantage_api_key"  # Replace with your actual API key
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": ticker,
        "apikey": api_key
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"[MarketData] Fetched data for {ticker}:")
        print(data)
        return data
    else:
        print(f"[MarketData] Failed to fetch data for {ticker}: {response.status_code}")
        return None