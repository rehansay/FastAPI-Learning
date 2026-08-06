from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from langserve import add_routes

from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_community.utilities import GoogleSerperAPIWrapper

search= GoogleSerperAPIWrapper()



llm= ChatGroq(model="openai/gpt-oss-120b")

tools=[search.run]
prompt="You are a assistant and can search on google for user queries."

agent=create_agent(
    model=llm,
    tools=tools,
    system_prompt=prompt
)
# app=FastAPI(
#     title="My AI Agent"
# )

# add_routes(
#     app,
#     agent,
#     path="/agent"
# )


# query="who is the winner of IPL 2026?"

# response=agent.invoke(
#     {"messages":[{"role":"user", "content":query}]}

# ) 
# print (response["messages"][-1].content)