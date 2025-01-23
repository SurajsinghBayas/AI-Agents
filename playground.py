from phi.agent import Agent 
from phi.model.openai import OpenAIChat
from dotenv import load_dotenv
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.playground import Playground, serve_playground_app

load_dotenv()
Web_agent=Agent(
    name="Web_Agent",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[DuckDuckGo()],
    instructions=["always display source"],
    show_tool_calls=True,
    markdown=True,
    
    
)
Financial_agent=Agent(
    name="financial_Agent",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=["Use tables to diaply data"],
    debug_mode=True
)
app = Playground(agents=[Financial_agent, Web_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)