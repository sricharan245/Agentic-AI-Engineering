import phi
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.playground import Playground, serve_playground_app

import os

from dotenv import load_dotenv
load_dotenv()

MODEL_ID = 'llama-3.1-70b-versatile'


phi.api = os.getenv('PHI_API_KEY')
# Groq.api = os.getenv('GROQ_API_KEY')

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


app = Playground(
    agents = [ financial_agent, websearch_agent],
).get_app()


if __name__ == '__main__':
    serve_playground_app('playground:app', reload = True)

