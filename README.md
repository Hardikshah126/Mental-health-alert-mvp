Mental Health Early-Warning System (MVP)

Project Description

The Mental Health Early-Warning System is an AI-powered application that analyzes a user’s journal entry to detect emotional patterns, estimate mental-health risk levels, and generate personalized recommendations.
It combines emotion analysis, sleep data, and risk scoring with Google Gemini 2.5 Flash to deliver supportive insights and coping suggestions — all in real time.

This project demonstrates AI engineering, prompt engineering, API development, and full-stack integration, making it a strong portfolio piece.

What This Project Does
1. Emotion Detection (Gemini)

Extracts emotional intensities from text
Labels used: anger, fear, sadness, joy, disgust, surprise, neutral

2. Risk Scoring Engine

Analyzes emotional negativity
Includes sleep-hours input
Calculates an overall risk value → low / medium / high

3. AI-Generated Suggestions

Using Gemini 2.5 Flash:
Provides empathetic responses
Gives 3 actionable coping strategies
Adds safety suggestions for high-risk users

4. Full-stack Integration

Frontend sends user journal + sleep data
Backend returns emotions, risk level, and AI-generated advice
Works seamlessly across Vercel (frontend) and Render (backend)

Live Links

Frontend (Vercel): https://mental-health-alert-mvp.vercel.app/
Backend (Render): [https://mental-health-alert-mvp-1.onrender.com](https://mental-health-alert-mvp-1.onrender.com)

Tech Stack Used

Frontend

React + Vite
Tailwind CSS
Deployed on Vercel

Backend

FastAPI
Python
Uvicorn
Deployed on Render

AI / Machine Learning

Google Gemini 2.5 Flash
Custom emotional scoring
Risk aggregation algorithm

SYSTEM ARCHITECHTURE

mental-health-alert-mvp/
│
├── backend/
│   ├── app/
│   │   ├── main.py               # FastAPI routes (/analyze)
│   │   ├── emotion_inference.py  # Emotion detection using Gemini
│   │   ├── llm_gemini.py         # Suggestion generator with Gemini 2.5 Flash
│   │   ├── utils.py              # Risk scoring logic
│   └── requirements.txt
│
└── frontend/
    ├── src/
    │   ├── api.ts                # Calls backend /analyze
    │   ├── components/
    │   └── pages/
    └── package.json


