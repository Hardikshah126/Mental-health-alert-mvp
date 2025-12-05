# backend/app/llm_gemini.py
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
DEFAULT_MODEL = "models/gemini-1.5-flash"   # ✅ Correct model name

print("DEBUG: GEMINI_API_KEY present?", bool(API_KEY))

# Configure Gemini
if API_KEY:
    genai.configure(api_key=API_KEY)
else:
    print("WARNING: GEMINI_API_KEY is not set; Gemini calls will return a fallback message.")


def build_prompt(user_text: str, retrieved_context=None, sleep_hours=None, risk=None):
    ctx = ""
    if retrieved_context:
        ctx = "\n\n".join([f"Past entry ({i+1}): {d}" for i, d in enumerate(retrieved_context)])

    sleep = f"Recent sleep hours: {sleep_hours}" if sleep_hours is not None else ""

    prompt = (
        "You are a kind, concise, and non-judgmental mental-health assistant.\n\n"
        f"User journal:\n{user_text}\n\n"
        f"{sleep}\n\n"
        f"Context:\n{ctx}\n\n"
        f"Risk level: {risk}\n\n"
        "Provide:\n"
        "1) A short (1-2 sentence) empathetic reflection.\n"
        "2) Three practical coping steps the user can try today (each one short).\n"
        "3) If risk is 'high', include a calm safety suggestion to contact a professional or helpline.\n"
        "Keep the language simple and supportive.\n"
    )
    return prompt


def get_suggestions_gemini(prompt: str, model: str = DEFAULT_MODEL) -> str:
    """
    Call Gemini (google-generativeai) and return generated text.
    If model fails, fallback to DEFAULT_MODEL.
    """
    if not API_KEY:
        return "(Gemini key missing - set GEMINI_API_KEY in environment variables)"

    # Ensure model name is properly prefixed
    if not model.startswith("models/"):
        model = f"models/{model}"

    try:
        try:
            gmodel = genai.GenerativeModel(model)
        except Exception:
            gmodel = genai.GenerativeModel(DEFAULT_MODEL)

        response = gmodel.generate_content(prompt)
        return (response.text or "").strip()

    except Exception as e:
        return f"(Gemini error: {e})"
