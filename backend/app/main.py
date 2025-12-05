# backend/app/main.py
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

# load .env variables
load_dotenv()

# local imports (make sure these filenames exist in backend/app/)
from .emotion_inference import get_emotion_scores
from .utils import compute_text_score, compute_sleep_score, aggregate_risk, risk_level
from .llm_gemini import build_prompt, get_suggestions_gemini



app = FastAPI(title="Mental Health Early-Warning Backend")

# backend/app/main.py
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # ALLOW ALL ORIGINS (DEV)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("CORS enabled for all origins")

print("DEBUG: CORS set to allow * (dev temporary)")


class AnalyzeInput(BaseModel):
    user_id: str = "demo"
    text: str
    sleep_hours: float = None

@app.get("/")
def root():
    return {"status": "ok", "note": "MH-EW backend running"}

@app.post("/analyze")
def analyze(payload: AnalyzeInput):
    if not payload.text or not payload.text.strip():
        raise HTTPException(status_code=400, detail="text is required")

    # 1. emotion model inference (returns list of {'label','score'})
    emotions = get_emotion_scores(payload.text)

    # 2. compute scores & risk
    text_score = compute_text_score(emotions)
    sleep_score = compute_sleep_score(payload.sleep_hours)
    risk_val = aggregate_risk(text_score, sleep_score)
    level = risk_level(risk_val)

    # 3. optional RAG retrieval (empty for now)
    retrieved_context = []

    # 4. Build prompt and call Gemini (if key set)
    suggestions = ""
    try:
        prompt = build_prompt(payload.text, retrieved_context=retrieved_context, sleep_hours=payload.sleep_hours, risk=level)
        suggestions = get_suggestions_gemini(prompt)
    except Exception as e:
        suggestions = f"(LLM error or GEMINI_API_KEY not set) {str(e)}"

    return {
        "emotions": emotions,
        "text_score": round(text_score, 3),
        "sleep_score": round(sleep_score, 3),
        "risk_value": round(risk_val, 3),
        "risk_level": level,
        "retrieved_context": retrieved_context,
        "suggestions": suggestions,
    }
