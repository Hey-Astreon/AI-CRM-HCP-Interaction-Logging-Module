<<<<<<< HEAD
# AI-First CRM HCP Interaction Logging Module

## Project Overview
This project is an AI-first prototype for a CRM module designed for pharmaceutical field representatives to log interactions with Healthcare Professionals (HCPs). It features a dual-interface approach:
1.  **A structured form** for manual data entry.
2.  **An AI conversational assistant** that extracts key information from natural language input to automatically populate the form and log the interaction.

## Tech Stack
-   **Frontend:** React.js, Redux Toolkit, Axios, CSS (Vanilla, styled with Inter font)
-   **Backend:** Python, FastAPI, Uvicorn, SQLAlchemy, Pydantic
-   **AI Framework:** LangGraph, LangChain
-   **LLM:** Groq API (`gemma2-9b-it`)
-   **Database:** PostgreSQL

## Architecture Diagram
```text
[ React Frontend ] (Redux State)
       |
  (REST API / Axios)
       v
[ FastAPI Backend ]
       |
[ LangGraph Agent ] <--> [ Groq LLM (gemma2-9b-it) ]
       |
  (SQLAlchemy ORM)
       v
[ PostgreSQL Database ]
```

## Setup & Installation

### 1. Database Setup
1. Ensure PostgreSQL is installed and running.
2. Create a database named `ai_crm_hcp`.
3. Apply the schema:
   ```bash
   psql -U postgres -d ai_crm_hcp -f database/schema.sql
   ```

### 2. Backend Setup
1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure environment variables in `backend/.env`:
   ```env
   GROQ_API_KEY=your_groq_api_key
   DATABASE_URL=postgresql://postgres:password@localhost/ai_crm_hcp
   ```
5. Run the server:
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at `http://localhost:8000`.

### 3. Frontend Setup
1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm start
   ```
   The app will be available at `http://localhost:3000`.

## Example API Requests

### Log a new interaction directly via API
```bash
curl -X POST "http://localhost:8000/interaction/log" \
     -H "Content-Type: application/json" \
     -d '{
           "hcp_name": "Dr. Smith",
           "interaction_type": "Meeting",
           "date": "2024-05-20",
           "time": "14:00",
           "topics_discussed": "Product X efficacy",
           "materials_shared": "Brochure",
           "samples_distributed": "2 boxes",
           "sentiment": "Positive",
           "outcome": "Interested in trial data",
           "follow_up": "Send clinical trial report"
         }'
```

### Chat with the AI Assistant
```bash
curl -X POST "http://localhost:8000/ai/chat" \
     -H "Content-Type: application/json" \
     -d '{
           "message": "Met Dr Smith today and discussed Product X efficacy. He seemed interested and asked for clinical trial data."
         }'
```
=======
# ai-crm-hcp-log-interaction
>>>>>>> 385b6d0ca234643df7619381d105d5b36a1460ec
