from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from src.tools.serper_tool import google_serper_search_tool
from src.tools.tavily_tool import tavily_search_tool    
from src.config.config import GROQ_API_KEY
from src.utils.logger import get_logger

logger = get_logger(__name__)

model= init_chat_model(
    model_provider="groq",
    model = "llama-3.3-70b-versatile",
    temperature=0.9
)

SYSTEM_PROMPT = """
    You are a travel assistant that helps users plan their trips.
    Rules :
    - Always use web search tools for real- world accuracy 
    - Create a detailed day-wise iteranery
    - Include food suggestions, local insights and tips in the iteranery

    User Inputs:
    City, Number of days, Interests, Pace, Travel style
    """
agent = create_agent(
    model = model,
    tools = [google_serper_search_tool, tavily_search_tool],
    system_prompt= SYSTEM_PROMPT    
)

logger.info("AGENT CREATED SUCCESSFULLY")