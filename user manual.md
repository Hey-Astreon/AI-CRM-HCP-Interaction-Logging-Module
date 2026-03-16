# 🚀 AI CRM HCP Interaction Module - User Manual

This guide will help you set up and run the AI CRM project from scratch in just a few minutes.

---

## 📋 Prerequisites
Before you start, make sure you have these installed:
1. **Python (3.10 or higher)**: [Download here](https://www.python.org/downloads/)
2. **Node.js**: [Download here](https://nodejs.org/)
3. **Groq API Key**: Get a free key at [console.groq.com](https://console.groq.com/keys)

---

## 🛠️ Step 1: Initial Setup (Do this once)

### 1. Configure the Backend
1. Go to the `backend/` folder.
2. Open the `.env` file and paste your Groq key:
   ```env
   GROQ_API_KEY=gsk_your_key_here
   DATABASE_URL=sqlite:///./ai_crm_hcp.db
   ```

### 2. Install Dependencies
Open a terminal in the main project folder and run these two commands:

**For the Backend:**
```powershell
cd backend
python -m pip install -r requirements.txt
cd ..
```

**For the Frontend:**
```powershell
cd frontend
npm install
cd ..
```

---

## 🏃 Step 2: Running the Program (The Easy Way)

We have created a "One-Click" launcher for you!

1. Open your File Explorer and go to the project folder: `f:\Internship Project\ai-crm-hcp-module`
2. Find the file named **`run_project.bat`**.
3. **Double-click it.**

**What happens next?**
- Two terminal windows will open automatically.
- Your browser will open to `http://localhost:3000`.
- The AI Assistant is now ready to use!

---

## 🤖 Step 3: Using the AI Assistant
The most powerful part of this CRM is the **AI Assistant** card on the right side.

1. Locate the **"AIChatPanel"** on the right.
2. In the "Describe interaction..." box, type a natural note like:
   > *"Met Dr. Sharma today. Discussed OncoBoost efficacy. She was very positive and asked for trial data next week."*
3. Click the **Log** button.
4. **Watch the magic:** The AI will automatically fill out the HCP Name, Interaction Type, Topics, Sentiment, and Follow-up fields for you!

---

## ❓ Troubleshooting
- **Error: "Failed to process text with AI"**: 
  - Check your internet connection.
  - Make sure your Groq API Key in `backend/.env` is correct.
- **Port 3000 already in use**: 
  - Close any old terminal windows and double-click `run_project.bat` again.
- **Backend not responding**: 
  - Ensure you see "Application startup complete" in the backend terminal window.

---
*Created for the HCP Interaction Logging Module Prototype.*
