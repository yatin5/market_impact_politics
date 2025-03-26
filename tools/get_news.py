from langchain.tools import BaseTool

class GetNewsTool(BaseTool):
    name: str = "get_news"
    description: str = "Retrieves all saved news headlines from the shared store"

    def _run(self, **kwargs) -> str:
        print("[GetNewsTool] Fetching saved news")
        return "Latest saved news"

    def _arun(self, **kwargs):
        raise NotImplementedError("Async not supported")
