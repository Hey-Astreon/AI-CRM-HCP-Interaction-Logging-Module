import os
import json
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from sqlalchemy.orm import Session
import models
import datetime

def run_agent(user_input: str, db: Session):
    llm = ChatGroq(temperature=0, model_name="llama-3.1-8b-instant", groq_api_key=os.getenv("GROQ_API_KEY"))
    
    system_prompt = """You are a pharmaceutical sales CRM assistant.
Your job is to extract details from the rep's text and output a STRICT valid json object.
Use the following json schema format exactly:
{
  "hcp_name": "Name of doctor (or empty string)",
  "topics_discussed": "Key topics",
  "sentiment": "Positive, Neutral, or Negative",
  "follow_up": "Follow up instructions",
  "interaction_type": "Meeting, Email, Call, etc.",
  "materials_shared": "Brochures etc",
  "samples_distributed": "Samples given",
  "outcome": "Overall outcome"
}
If any information is not mentioned, use an empty string "". Do not use null or None.
ONLY return the JSON object, do not add any extra conversational text."""

    try:
        # We explicitly enforce JSON mode to bypass Groq's buggy function-calling XML parser
        response = llm.bind(response_format={"type": "json_object"}).invoke([
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_input)
        ])
        
        content = response.content.strip()
        # Remove markdown backticks if present
        if content.startswith("```json"):
            content = content[7:]
        if content.startswith("```"):
            content = content[3:]
        if content.endswith("```"):
            content = content[:-3]
        content = content.strip()
        
        # If model returned a list instead of dict, extract first dict
        if content.startswith("[") and content.endswith("]"):
            data_list = json.loads(content)
            data = data_list[0] if data_list else {}
        else:
            data = json.loads(content)
        
        # Add timestamp defaults since LLaMA no longer processes Python code blocks
        data["date"] = datetime.date.today()
        data["time"] = datetime.datetime.now().time()
        
        # Save to database
        new_interaction = models.Interaction(**data)
        db.add(new_interaction)
        db.commit()
        db.refresh(new_interaction)
        
        reply = f"Successfully logged your interaction with {data.get('hcp_name', 'HCP')}."
        return {
            "reply": reply,
            "formUpdates": data
        }
        
    except Exception as e:
        return {
            "reply": f"Could not extract interaction details reliably: {str(e)}",
            "formUpdates": None
        }

