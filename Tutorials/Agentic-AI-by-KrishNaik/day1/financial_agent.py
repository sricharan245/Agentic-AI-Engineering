from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

from dotenv import load_dotenv

load_dotenv()

MODEL_ID = 'llama-3.1-70b-versatile'

# Web search agent
websearch_agent = Agent(
    name = "web search agent",
    role = "Search the web for the information",
    model = Groq( id = MODEL_ID),
    tools = [ DuckDuckGo() ],
    instructions = ["Always include sources"],
    show_tools_calls = True,
    markdown = True
)


# Financial agent
financial_agent = Agent(
    name = "financial agent",
    role = "Get financial information",
    model = Groq( id = MODEL_ID),
    tools = [
        YFinanceTools(stock_price=True, analyst_recommendations=True, company_news=True)
    ],
    instructions = ["Use tables to display the data"],
    show_tools_calls = True,
    markdown = True
)

multi_ai_agent = Agent(
    team = [websearch_agent, financial_agent],
    model = Groq( id = MODEL_ID),
    instructions = ["always include sources", "use tables to display the data"],
    show_tools_calls = True,
    markdown = True,
)

multi_ai_agent.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream = True)