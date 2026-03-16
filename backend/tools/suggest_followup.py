from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import os

@tool
def suggest_followup(topics: str, sentiment: str) -> str:
    """
    AI suggests next actions based on topics and sentiment.
    """
    llm = ChatGroq(temperature=0.2, model_name="llama-3.1-8b-instant", groq_api_key=os.getenv("GROQ_API_KEY"))
    prompt = f"Given the topics discussed ('{topics}') and the HCP's sentiment ('{sentiment}'), suggest a brief follow-up action for a pharmaceutical sales rep (e.g., Send brochure, Schedule meeting)."
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content
