from src.config.config import TAVILY_API_KEY
from langchain_tavily import TavilySearch
from src.utils.logger import get_logger


logger = get_logger(__name__)   

def tavily_search_tool(query: str) -> str:
    """
    Search web via tavily api to get up to date travel information, attractions, activities, tips
    and local insights for the given query. 
    """
    search = TavilySearch(
        tavily_api_key= TAVILY_API_KEY,
        max_results=3,
        topic="travel"
    )
    return search.invoke({
        "query": query
    })

logger.info("TAVILY TOOL ALL SET")