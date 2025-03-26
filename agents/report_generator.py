# Mocking the Agent class for development purposes
class Agent:
    def __init__(self, role, goal, backstory, tools, verbose):
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.tools = tools
        self.verbose = verbose

    def generate_report(self, sentiment_analysis):
        """Simulate generating a market impact report."""
        report = "Market Impact Report:\n"
        for headline, sentiment in sentiment_analysis.items():
            report += f"- {headline}: {sentiment}\n"
        print("[Report Generator] Generated report:")
        print(report)
        return report

from tools.news_store import save_news, get_news  # tools, not classes
from crewai.tools.base_tool import tool

@tool("Generate market impact report")
def generate_report(sentiment_analysis: dict):
    """Generate a comprehensive market impact report."""
    report = "Market Impact Report:\n"
    for headline, analysis in sentiment_analysis.items():
        report += f"- {headline}:\n  {analysis}\n\n"
    print("[ReportGenerator] Generated report:")
    print(report)
    return report

class ReportGenerator:
    def generate_report(self, sentiment_analysis):
        """Generate a comprehensive market impact report."""
        report = "Market Impact Report:\n"
        for headline, analysis in sentiment_analysis.items():
            report += f"- {headline}:\n  {analysis}\n\n"
        print("[ReportGenerator] Generated report:")
        print(report)
        return report

report_generator = ReportGenerator()
