import re

def normalize_report_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def split_text_into_sentences(text: str) -> list[str]:
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sentences if len(s.strip()) > 10]

def score_sentence_importance(sentence: str, keywords: list[str] | None = None) -> float:
    score = 0.0
    s_lower = sentence.lower()

    default_keywords = [
        "warning", "failed", "missing", "blocked", "gap", "risk", "quality",
        "safety", "regression", "drift", "stale", "over_budget", "audit_failed",
        "critical", "follow-up", "next step", "offline", "dry-run", "error", "exception"
    ]

    kw = keywords if keywords else default_keywords

    for k in kw:
        if k in s_lower:
            score += 1.0

    if 20 < len(sentence) < 150:
        score += 0.5

    return score

def extract_top_sentences(text: str, max_sentences: int = 8, keywords: list[str] | None = None) -> list[str]:
    sentences = split_text_into_sentences(normalize_report_text(text))
    if not sentences:
        return []

    scored = [(score_sentence_importance(s, keywords), i, s) for i, s in enumerate(sentences)]
    scored.sort(key=lambda x: (x[0], -x[1]), reverse=True)

    top = scored[:max_sentences]
    top.sort(key=lambda x: x[1])

    return [mask_sensitive_summary_text(x[2]) for x in top]

def build_rule_based_summary(text: str, max_bullets: int = 8) -> tuple[str, list[str], dict]:
    top_sentences = extract_top_sentences(text, max_sentences=max_bullets)
    if not top_sentences:
        return "No summary could be generated.", [], {"status": "empty"}

    summary_text = " ".join(top_sentences)
    bullets = [f"- {s}" for s in top_sentences]

    return summary_text, bullets, {"status": "success", "bullet_count": len(bullets)}

def mask_sensitive_summary_text(text: str) -> str:
    text = re.sub(r'(api_key|token|password|secret|chat_id)\s*[:=]\s*["\'][^"\']+["\']', r'\1: "***MASKED***"', text, flags=re.IGNORECASE)
    text = re.sub(r'(api_key|token|password|secret|chat_id)\s*[:=]\s*\S+', r'\1: ***MASKED***', text, flags=re.IGNORECASE)

    forbidden_terms = [
        "canli emir", "live order", "buy now", "sell now",
        "gercek islem", "real trade", "yatirim tavsiyesidir"
    ]

    for term in forbidden_terms:
        if term in text.lower():
            text = re.sub(term, f"[{term}_DETECTED_AS_TEXT]", text, flags=re.IGNORECASE)

    return text
