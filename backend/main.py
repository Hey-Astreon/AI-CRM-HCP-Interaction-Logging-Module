from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
from database import get_db, engine
import models
import schemas
from agent.langgraph_agent import run_agent

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI-First CRM HCP API")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Change to specific origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ai/chat")
async def ai_chat(message: schemas.ChatMessage, db: Session = Depends(get_db)):
    """Receives user message and sends it to the LangGraph agent."""
    try:
        response = run_agent(message.message, db)
        return response
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print(f"Error in ai_chat: {error_details}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/interaction/log", response_model=schemas.Interaction)
def log_interaction(interaction: schemas.InteractionCreate, db: Session = Depends(get_db)):
    """Creates a new interaction manually."""
    db_interaction = models.Interaction(**interaction.model_dump())
    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)
    return db_interaction

@app.post("/interaction/edit/{interaction_id}", response_model=schemas.Interaction)
def edit_interaction(interaction_id: int, interaction: schemas.InteractionUpdate, db: Session = Depends(get_db)):
    """Updates an existing interaction."""
    db_interaction = db.query(models.Interaction).filter(models.Interaction.id == interaction_id).first()
    if not db_interaction:
        raise HTTPException(status_code=404, detail="Interaction not found")
    
    update_data = interaction.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_interaction, key, value)
        
    db.commit()
    db.refresh(db_interaction)
    return db_interaction

@app.get("/interaction/history", response_model=List[schemas.Interaction])
def get_history(hcp_name: str, db: Session = Depends(get_db)):
    """Returns interaction history for a doctor."""
    interactions = db.query(models.Interaction).filter(models.Interaction.hcp_name.ilike(f"%{hcp_name}%")).all()
    return interactions
