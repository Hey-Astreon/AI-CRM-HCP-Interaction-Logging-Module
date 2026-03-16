from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import os

@tool
def summarize_interaction(text: str) -> str:
    """
    Uses the LLM to generate a concise summary of the interaction.
    """
    llm = ChatGroq(temperature=0, model_name="llama-3.1-8b-instant", groq_api_key=os.getenv("GROQ_API_KEY"))
    prompt = f"Summarize the following interaction between a medical rep and an HCP in one short sentence: {text}"
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content
