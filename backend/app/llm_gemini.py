# backend/app/llm_gemini.py
import os
from dotenv import load_dotenv
load_dotenv()
import os
from dotenv import load_dotenv
load_dotenv()
print("DEBUG: GEMINI_API_KEY present?", bool(os.getenv("GEMINI_API_KEY")))


# Use the google-genai SDK
# The package name is `google-genai` on pip and imports as `from google import genai`
from google import genai

API_KEY = os.getenv("GEMINI_API_KEY")
if API_KEY:
    client = genai.Client(api_key=API_KEY)
else:
    client = None

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

def get_suggestions_gemini(prompt: str, model: str = "gemini-2.5-flash"):
    """
    Call Gemini (google-genai) and return text output.
    If API key isn't set, return a helpful message instead of raising.
    """
    if not client:
        return "(Gemini key missing - set GEMINI_API_KEY in .env)"
    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt,
        )
        # response.text contains the generated text
        return response.text
    except Exception as e:
        return f"(Gemini error: {e})"
