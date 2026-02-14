from src.config.config import SERPER_API_KEY
from langchain_community.utilities import GoogleSerperAPIWrapper
from src.utils.logger import get_logger


logger = get_logger(__name__)   

def google_serper_search_tool(query: str) -> str:
    """
    Search google via serper api to fetch the recent and 
    reliable real- world travel information for the given query.
    """
    search = GoogleSerperAPIWrapper(
        serper_api_key= SERPER_API_KEY
    )
    return search.run(query)

logger.info("SERPER TOOL ALL SET")