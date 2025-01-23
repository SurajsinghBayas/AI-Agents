from phi.agent import Agent 
from phi.model.openai import OpenAIChat
from dotenv import load_dotenv
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools

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
agent_team=Agent(
    team=[Web_agent,Financial_agent],
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions=["always diaplsy source","Use tables to diaply data","be quick as posiible"],
    markdown=True,
    debug_mode=True
)
agent_team.print_response("all rohit Sharama invesments")