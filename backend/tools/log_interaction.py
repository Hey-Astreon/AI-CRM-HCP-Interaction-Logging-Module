from langchain_core.tools import tool
from models import Interaction
import datetime

from pydantic import BaseModel, Field

class LogInteractionInput(BaseModel):
    hcp_name: str = Field(..., description="Name of the healthcare professional")
    topics_discussed: str = Field(..., description="Topics discussed during the interaction")
    sentiment: str = Field(default="", description="Sentiment of the HCP")
    follow_up: str = Field(default="", description="Next steps or follow-up actions")
    interaction_type: str = Field(default="Meeting", description="Type of interaction")
    materials_shared: str = Field(default="", description="Materials shared")
    samples_distributed: str = Field(default="", description="Samples distributed")
    outcome: str = Field(default="", description="Outcome of the interaction")
    date: str = Field(default="", description="Date in YYYY-MM-DD format (leave empty to use today)")
    time: str = Field(default="", description="Time in HH:MM format (leave empty to use now)")

@tool(args_schema=LogInteractionInput)
def log_interaction(
    hcp_name: str,
    topics_discussed: str,
    sentiment: str = "",
    follow_up: str = "",
    interaction_type: str = "Meeting",
    materials_shared: str = "",
    samples_distributed: str = "",
    outcome: str = "",
    date: str = "",
    time: str = "",
    **kwargs
) -> dict:
    """
    Store interaction details in the database.
    Use this tool to log a new meeting or call with a Healthcare Professional.
    """
    # Note: DB session is injected in the agent context, but for langchain tools 
    # we can use a workaround or pass it through state. 
    # Here we return the intent and the agent handles DB insertion.
    
    return {
        "action": "log_interaction",
        "data": {
            "hcp_name": hcp_name,
            "interaction_type": interaction_type,
            "date": date if date else datetime.date.today().isoformat(),
            "time": time if time else datetime.datetime.now().strftime("%H:%M"),
            "topics_discussed": topics_discussed,
            "materials_shared": materials_shared,
            "samples_distributed": samples_distributed,
            "sentiment": sentiment,
            "outcome": outcome,
            "follow_up": follow_up
        }
    }
