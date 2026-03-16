from sqlalchemy import Column, Integer, String, Date, Time, Text, DateTime
from database import Base
import datetime

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    hcp_name = Column(String(255), nullable=False, index=True)
    interaction_type = Column(String(50))
    date = Column(Date)
    time = Column(Time)
    topics_discussed = Column(Text)
    materials_shared = Column(Text)
    samples_distributed = Column(Text)
    sentiment = Column(String(50))
    outcome = Column(Text)
    follow_up = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
