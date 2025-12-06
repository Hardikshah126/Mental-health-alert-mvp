# backend/app/llm_gemini.py

import os
from dotenv import load_dotenv
from google import genai   # NEW GenAI SDK

# Load .env for local dev (Render will use real env vars)
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.5-flash"   # model you see in Google AI Studio

print("DEBUG: GEMINI_API_KEY present?", bool(API_KEY))

if not API_KEY:
    print("WARNING: GEMINI_API_KEY is not set; Gemini calls will return a fallback message.")
    client = None
else:
    # New GenAI client
    client = genai.Client(api_key=API_KEY)
    print("Gemini client initialized")


def build_prompt(user_text: str, retrieved_context=None, sleep_hours=None, risk=None):
    ctx = ""
    if retrieved_context:
        ctx = "\n\n".join([f"Past entry ({i+1}): {d}" for i, d in enumerate(retrieved_context)])

    sleep = f"Recent sleep hours: {sleep_hours}" if sleep_hours is not None else ""

    return (
        "You are a kind, concise, and non-judgmental mental-health assistant.\n\n"
        f"User journal:\n{user_text}\n\n"
        f"{sleep}\n\n"
        f"Context:\n{ctx}\n\n"
        f"Risk level: {risk}\n\n"
        "Provide:\n"
        "1) A short empathetic reflection.\n"
        "2) Three practical coping steps.\n"
        "3) If risk is 'high', include a safety suggestion.\n"
    )


def get_suggestions_gemini(prompt: str) -> str:
    """Call Gemini 2.5 Flash via the new Google GenAI SDK."""
    if client is None:
        return "(Gemini key missing - set GEMINI_API_KEY in environment variables)"

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
        )

        # google-genai responses expose .text() helper
        text_attr = getattr(response, "text", None)
        if callable(text_attr):
            return (text_attr() or "").strip()
        return (text_attr or "").strip()

    except Exception as e:
        print("Gemini error:", repr(e))
        return f"(Gemini error: {e})"
