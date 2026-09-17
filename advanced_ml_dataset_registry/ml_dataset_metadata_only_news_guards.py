import pandas as pd
from typing import Dict, List, Optional, Tuple
from advanced_ml_dataset_registry.advanced_ml_dataset_config import get_default_advanced_ml_dataset_profile

NEWS_FORBIDDEN_COLUMNS = [
    "full_text", "article_body", "raw_content", "scraped_html",
    "page_html", "html", "embedding", "vector", "sentiment", "sentiment_score",
]

_NEWS_GUARDS = [
    {"guard_name": "macro_event_metadata_only_news_guard", "description": "Macro event news: metadata only. No full text, article body, scraped HTML, embedding or sentiment."},
    {"guard_name": "news_metadata_only_guard", "description": "General news: metadata only. Full article content forbidden."},
    {"guard_name": "economic_calendar_metadata_only_guard", "description": "Economic calendar: metadata only."},
]

def build_ml_dataset_metadata_only_news_guard_registry(profile=None) -> Tuple[pd.DataFrame, Dict]:
    if profile is None:
        profile = get_default_advanced_ml_dataset_profile()
    rows = []
    for g in _NEWS_GUARDS:
        rows.append({
            "guard_name": g["guard_name"],
            "description": g["description"],
            "forbidden_columns": ", ".join(NEWS_FORBIDDEN_COLUMNS),
            "full_text_allowed": False,
            "article_body_allowed": False,
            "scraped_html_allowed": False,
            "embedding_allowed": False,
            "sentiment_allowed": False,
            "non_signal": True,
            "manual_review_required": True,
            "current_phase": 137,
        })
    df = pd.DataFrame(rows)
    summary = {"total_news_guards": len(rows), "current_phase": 137, "non_signal": True, "status": "READY"}
    return df, summary

def validate_ml_dataset_metadata_only_news_columns(column_names: List[str]) -> Dict:
    found = [c for c in column_names if any(f in c.lower() for f in NEWS_FORBIDDEN_COLUMNS)]
    return {"valid": len(found) == 0, "forbidden_found": found, "non_signal": True}

def validate_no_forbidden_news_content(text: Optional[str] = None, df: Optional[pd.DataFrame] = None) -> Dict:
    issues = []
    if text:
        for kw in NEWS_FORBIDDEN_COLUMNS:
            if kw in text.lower():
                issues.append(f"Forbidden news content keyword detected: {kw}")
    if df is not None and hasattr(df, 'columns'):
        found = [c for c in df.columns if any(f in c.lower() for f in NEWS_FORBIDDEN_COLUMNS)]
        if found:
            issues.append(f"Forbidden news columns found: {found}")
    return {"valid": len(issues) == 0, "issues": issues, "non_signal": True}

def summarize_ml_dataset_metadata_only_news_guards(df: pd.DataFrame) -> Dict:
    return {"total_news_guards": len(df), "current_phase": 137, "non_signal": True, "status": "READY"}
