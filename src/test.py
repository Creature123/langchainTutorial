from dotenv import load_dotenv
import os

load_dotenv()

groq_api_key = os.getenv('GROQ_API_KEY')
langsmith_api_key = os.getenv('LANGSMITH_API_KEY')

os.environ["LANGCHAIN_API_KEY"] = langsmith_api_key
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "LangChainCrashCourse"

from langchain_groq import ChatGroq


llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0.0,
    max_retries=2,
)

messages = [
    ("system", "You are a helpful translator. Translate the user sentence to French."),
    ("human", "I love programming.s"),
]

print(llm.invoke(messages).content)