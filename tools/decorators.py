# tools/decorators.py

from langchain.tools import tool as langchain_tool

def tool(func):
    """Decorator to wrap a function as a LangChain-compatible tool."""
    return langchain_tool(func)
