# backend/app/emotion_inference.py
import os
import json
from functools import lru_cache
from typing import List, Dict

import google.generativeai as genai
from dotenv import load_dotenv

# Load .env locally (Render will use env vars directly)
load_dotenv()

# Configure Gemini from env
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY is not set in environment variables")

genai.configure(api_key=GEMINI_API_KEY)

# We’ll imitate the original HF model’s labels
EMOTION_LABELS = [
    "anger",
    "disgust",
    "fear",
    "joy",
    "neutral",
    "sadness",
    "surprise",
]

# 🔥 IMPORTANT: use a valid, current model
GEMINI_MODEL_NAME = "gemini-2.5-flash"


@lru_cache()
def get_model(model_name: str = GEMINI_MODEL_NAME) -> genai.GenerativeModel:
    """
    Cached Gemini model instance.
    """
    print("DEBUG emotion_inference: using model", model_name)
    return genai.GenerativeModel(model_name)


def _clean_json_text(text: str) -> str:
    """
    Remove ```json ... ``` fences if Gemini wraps the JSON.
    """
    text = text.strip()
    if text.startswith("```"):
        text = text.strip("`").strip()
        if text.lower().startswith("json"):
            text = text[4:].strip()
    return text


def get_emotion_scores(text: str, model_name: str = GEMINI_MODEL_NAME) -> List[Dict[str, float]]:
    """
    Analyze text with Gemini and return a list of {label, score} dicts,
    similar to the original Hugging Face pipeline output.
    """
    if not isinstance(text, str):
        raise ValueError("text must be a string")

    model = get_model(model_name)

    prompt = f"""
    You are an emotion analysis model.

    For the f
