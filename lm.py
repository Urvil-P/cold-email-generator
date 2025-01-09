import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()

groq_api_key = os.getenv("groq_api_key")

llm = ChatGroq(
    temperature=1,
    groq_api_key = groq_api_key,
    model_name = "llama3-70b-8192"
)