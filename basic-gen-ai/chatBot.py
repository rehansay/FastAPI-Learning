from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq

llm= ChatGroq(model="openai/gpt-oss-120b")

query="who is the winner of IPL?"

response=llm.invoke(query) 
print (response.content)