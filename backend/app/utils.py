from typing import List

NEGATIVE_LABELS = {'sadness','anger','fear','disgust','guilt','shame','annoyance','negative'}

def compute_text_score(emotion_scores: List[dict]) -> float:
    s = 0.0
    for e in emotion_scores:
        lab = e.get('label','').lower()
        if lab in NEGATIVE_LABELS:
            try:
                s += float(e.get('score', 0.0))
            except:
                pass
    return min(max(s, 0.0), 1.0)

def compute_sleep_score(hours: float) -> float:
    if hours is None:
        return 0.0
    try:
        h = float(hours)
    except:
        return 0.0
    if h < 4: return 1.0
    if h < 5: return 0.9
    if h < 6: return 0.6
    if h < 7: return 0.3
    if h <= 9: return 0.0
    return 0.4

def aggregate_risk(text_score: float, sleep_score: float, trend_score: float = 0.0) -> float:
    return 0.6*text_score + 0.3*sleep_score + 0.1*trend_score

def risk_level(risk_value: float) -> str:
    if risk_value > 0.6: return 'high'
    if risk_value > 0.3: return 'medium'
    return 'low'
