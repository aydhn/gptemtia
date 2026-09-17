import pandas as pd
from typing import Dict, List, Tuple
from advanced_ml_dataset_registry.advanced_ml_dataset_config import get_default_advanced_ml_dataset_profile

FORBIDDEN_COLUMNS = [
    "signal", "buy", "sell", "long", "short", "position",
    "target", "label", "prediction", "recommendation",
    "future_return", "forward_return", "next_return",
    "full_text", "article_body", "raw_content", "scraped_html",
    "page_html", "html", "embedding", "vector", "sentiment", "sentiment_score",
]

def build_ml_dataset_forbidden_column_policy_registry(profile=None) -> Tuple[pd.DataFrame, Dict]:
    if profile is None:
        profile = get_default_advanced_ml_dataset_profile()
    rows = [{"forbidden_column": col, "reason": "Phase 137 safety boundary", "current_phase": 137, "non_signal": True} for col in FORBIDDEN_COLUMNS]
    df = pd.DataFrame(rows)
    summary = {"total_forbidden_columns": len(rows), "current_phase": 137, "non_signal": True, "status": "READY"}
    return df, summary

def validate_ml_dataset_forbidden_columns(column_names: List[str]) -> Dict:
    found = [c for c in column_names if any(f == c.lower() or c.lower().startswith(f) for f in FORBIDDEN_COLUMNS)]
    return {"valid": len(found) == 0, "forbidden_found": found, "non_signal": True}

def summarize_ml_dataset_forbidden_column_policies(df: pd.DataFrame) -> Dict:
    return {"total_forbidden_columns": len(df), "current_phase": 137, "non_signal": True, "status": "READY"}
