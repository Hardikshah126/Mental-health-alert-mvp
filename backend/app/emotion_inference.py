# backend/app/emotion_inference.py
from transformers import pipeline
from functools import lru_cache

# Choose a compact CPU-friendly HF model for emotion classification.
# You can change this later. This is known to work for dev.
DEFAULT_MODEL = "j-hartmann/emotion-english-distilroberta-base"

@lru_cache()
def get_classifier(model_name: str = DEFAULT_MODEL):
    """
    Return a Hugging Face text-classification pipeline.
    Using lru_cache so model loads only once.
    """
    try:
        clf = pipeline("text-classification", model=model_name, truncation=True, return_all_scores=True)
        return clf
    except Exception as e:
        # surface a helpful error if model load fails
        raise RuntimeError(f"Failed to load HF model '{model_name}': {e}")

def get_emotion_scores(text: str, model_name: str = DEFAULT_MODEL):
    """
    Run the classifier on `text` and return a list of {label, score} dicts.
    """
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    clf = get_classifier(model_name)
    out = clf(text)
    if isinstance(out, list) and len(out) > 0:
        return out[0]
    return out
