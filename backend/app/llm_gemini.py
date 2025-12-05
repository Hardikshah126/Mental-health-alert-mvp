# backend/app/llm_gemini.py
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
DEFAULT_MODEL = "gemini-1.5-flash-latest"

print("DEBUG: GEMINI_API_KEY present?", bool(API_KEY))

if API_KEY:
    genai.configure(api_key=API_KEY)
else:
    print("WARNING: GEMINI_API_KEY is not set; Gemini calls will return a fallback message.")


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


def get_suggestions_gemini(prompt: str, model: str = DEFAULT_MODEL) -> str:
    if not API_KEY:
        return "(Gemini key missing - set GEMINI_API_KEY in environment variables)"

    try:
        try:
            gmodel = genai.GenerativeModel(model)
        except Exception:
            gmodel = genai.GenerativeModel(DEFAULT_MODEL)

        response = gmodel.generate_content(prompt)
        return (response.text or "").strip()

    except Exception as e:
        return f"(Gemini error: {e})"
