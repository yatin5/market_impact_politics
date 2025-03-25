# market_impact_politics - North America Political News Market Impact Agent

This AI-powered project uses CrewAI to analyze political news from the US and Canada and predict its impact on stock markets, commodities, and currencies.

## 🔧 Setup

1. Create the conda environment:


conda create -n market_agent_env python=3.10 -y
conda activate market_agent_env

Install dependencies:
pip install -r requirements.txt


Create a .env file:
NEWS_API_KEY=your_news_api_key
OPENAI_API_KEY=your_openai_key
SHEPHERD_API_KEY=your_shepherd_key


python main.py

