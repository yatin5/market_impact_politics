# Mocking the Agent class for development purposes
class Agent:
    def __init__(self, role, goal, backstory, tools, verbose):
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.tools = tools
        self.verbose = verbose

    def filter_relevant_news(self, news):
        """Simulate filtering news for relevance."""
        specific_keywords = [
            "legislation", "policy change", "trade negotiation", "election",
            "leadership transition", "geopolitical event", "U.S.", "Canada"
        ]
        relevant_news = [
            headline for headline in news
            if any(keyword.lower() in headline.lower() for keyword in specific_keywords)
        ]
        print("[Relevance Filter] Relevant news headlines:")
        for headline in relevant_news:
            print(f"- {headline}")
        return relevant_news

from tools.news_store import save_news_tool, get_news_tool
from crewai.tools.base_tool import tool

@tool("Filter relevant news")
def filter_relevant_news(news: list):
    """Filter news headlines for relevance to financial markets."""
    specific_keywords = [
        "legislation", "policy change", "trade negotiation", "election",
        "leadership transition", "geopolitical event", "U.S.", "Canada"
    ]
    relevant_news = [
        headline for headline in news
        if any(keyword.lower() in headline.lower() for keyword in specific_keywords)
    ]
    print("[RelevanceFilter] Relevant news headlines:")
    for headline in relevant_news:
        print(f"- {headline}")
    return relevant_news

class RelevanceFilter:
    def filter_relevant_news(self, news):
        """Filter news headlines for relevance to financial markets."""
        specific_keywords = [
            "legislation", "policy change", "trade negotiation", "election",
            "leadership transition", "geopolitical event", "U.S.", "Canada"
        ]
        relevant_news = [
            headline for headline in news
            if any(keyword.lower() in headline.lower() for keyword in specific_keywords)
        ]
        print("[RelevanceFilter] Relevant news headlines:")
        for headline in relevant_news:
            print(f"- {headline}")
        return relevant_news

relevance_filter = RelevanceFilter()