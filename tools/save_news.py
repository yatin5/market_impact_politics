from langchain.tools import BaseTool

class SaveNewsTool(BaseTool):
    name: str = "save_news"
    description: str = "Saves a news headline to a shared store"

    def _run(self, news: str, **kwargs) -> str:
        print(f"[SaveNewsTool] Saving news: {news}")
        return f"Saved news: {news}"

    def _arun(self, news: str, **kwargs):
        raise NotImplementedError("Async not supported")
