from pydantic import BaseModel
from typing import Optional
from datetime import date, time, datetime

class InteractionBase(BaseModel):
    hcp_name: str
    interaction_type: Optional[str] = None
    date: Optional[date] = None
    time: Optional[time] = None
    topics_discussed: Optional[str] = None
    materials_shared: Optional[str] = None
    samples_distributed: Optional[str] = None
    sentiment: Optional[str] = None
    outcome: Optional[str] = None
    follow_up: Optional[str] = None

class InteractionCreate(InteractionBase):
    pass

class InteractionUpdate(InteractionBase):
    hcp_name: Optional[str] = None # Make hcp_name optional for updates

class Interaction(InteractionBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class ChatMessage(BaseModel):
    message: str
