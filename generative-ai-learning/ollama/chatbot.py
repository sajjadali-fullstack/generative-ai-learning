# from langchain_openai import ChatOpenAI

# Ollama 
from langchain_ollama import ChatOllama
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2:1b")

response = llm.invoke("Who is Oggy?")

print(response.content)