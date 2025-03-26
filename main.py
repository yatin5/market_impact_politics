# Mocking the crewai package for development purposes
class Crew:
    def __init__(self, agents, tasks, verbose):
        self.agents = agents
        self.tasks = tasks
        self.verbose = verbose

    def kickoff(self):
        return "Mocked Crew kickoff completed."

class Task:
    def __init__(self, description, expected_output, agent):
        self.description = description
        self.expected_output = expected_output
        self.agent = agent

from agents.news_fetcher import news_fetcher
from agents.relevance_filter import relevance_filter
from agents.sentiment_impact import sentiment_impact
from agents.report_generator import report_generator
from configs import config
from tools.news_store import NewsStore
from agents.news_fetcher import fetch_news
from agents.relevance_filter import filter_relevant_news
from agents.sentiment_impact import analyze_sentiment, analyze_financial_impact
from agents.report_generator import generate_report


def main():

    shared_news_store = NewsStore()
    
    crew = Crew(
        agents=[
            news_fetcher,
            relevance_filter,
            sentiment_impact,
            report_generator,
        ],
        tasks=[
            Task(
                description="Fetch today's most relevent political news impacting North American markets",
                expected_output="A curated list of political news headlines with URLs.",
                agent=news_fetcher
            ),
            Task(
                description="Filter the news list to identify items relevent to market movement or investor sentiment.",
                expected_output="A filtered list of highly relevant articles with brief summaries",
                agent=relevance_filter
            ),
            Task(
                description="Analyze the sentiment and predict potential impact on financial markets (stocks, currency, commodities).",
                expected_output="Sentiment and impact assessment per aritcle.",
                agent=sentiment_impact
            ),
            Task(
                description="Generate a concise market impact report summarizing the key findings and trends.",
                expected_output="Final market report in a structured format.",
                agent=report_generator
            ),
        ],
        verbose=True,
    )

    # Fetch news using the NewsFetcher agent
    query = "North American politics"
    news_headlines = fetch_news.run(query)

    # Filter relevant news using the RelevanceFilter agent
    if news_headlines:
        relevant_news = filter_relevant_news.run(news_headlines)

        # Analyze sentiment using the SentimentImpact agent
        if relevant_news:
            sentiment_analysis = analyze_sentiment.run(relevant_news)

            # Analyze financial impact
            financial_impact = analyze_financial_impact(relevant_news)

            # Combine sentiment and financial impact into the final report
            final_report = generate_report.run({
                "sentiment_analysis": sentiment_analysis,
                "financial_impact": financial_impact
            })

            # Display the final report
            print("\nFinal Report:\n", final_report)
        else:
            print("No relevant news found.")
    else:
        print("No news headlines fetched.")

if __name__ == "__main__":
    main()

