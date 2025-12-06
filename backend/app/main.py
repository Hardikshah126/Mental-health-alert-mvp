# backend/app/main.py
import traceback
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# local imports
from .emotion_inference import get_emotion_scores
from .utils import compute_text_score, compute_sleep_score, aggregate_risk, risk_level
from .llm_gemini import build_prompt, get_suggestions_gemini

# ------------------ APP SETUP ------------------

app = FastAPI(title="Mental Health Early-Warning Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # you can later restrict to your Vercel URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("CORS enabled for all origins (dev)")

# ------------------ MODELS ------------------

class AnalyzeInput(BaseModel):
    user_id: str = "demo"
    text: str
    sleep_hours: float | None = None

# ------------------ ROUTES ------------------

@app.get("/")
def root():
    return {"status": "ok", "note": "MH-EW backend running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze")
def analyze(payload: AnalyzeInput):
    try:
        # 0. Basic validation
        if not payload.text or not payload.text.strip():
            raise HTTPException(status_code=400, detail="text is required")

        # 1. Emotion model inference
        emotions = get_emotion_scores(payload.text)

        # 2. Compute scores & risk
        text_score = compute_text_score(emotions)

        # make sure sleep_hours None doesn't break scoring
        try:
            sleep_score = compute_sleep_score(payload.sleep_hours)
        except TypeError:
            # if your compute_sleep_score doesn't like None, handle here
            sleep_score = compute_sleep_score(0.0)

        risk_val = aggregate_risk(text_score, sleep_score)
        level = risk_level(risk_val)

        # 3. (Optional) RAG context – empty for now
        retrieved_context = []

        # 4. Build prompt and call Gemini (fail gracefully)
        suggestions = ""
        try:
            prompt = build_prompt(
                payload.text,
                retrieved_context=retrieved_context,
                sleep_hours=payload.sleep_hours,
                risk=level,
            )
            suggestions = get_suggestions_gemini(prompt)
        except Exception as e:
            traceback.print_exc()
            suggestions = f"(LLM error or GEMINI_API_KEY issue) {str(e)}"

        return {
            "emotions": emotions,
            "text_score": round(text_score, 3),
            "sleep_score": round(sleep_score, 3),
            "risk_value": round(risk_val, 3),
            "risk_level": level,
            "retrieved_context": retrieved_context,
            "suggestions": suggestions,
        }

    except HTTPException:
        # re-raise explicit HTTP errors (like 400)
        raise
    except Exception as e:
        # log full traceback to Render logs
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error in /analyze: {str(e)}",
        )
