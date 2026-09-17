import pandas as pd
from typing import Dict, List, Tuple
from advanced_ml_dataset_registry.advanced_ml_dataset_config import get_default_advanced_ml_dataset_profile

LEAKAGE_FORBIDDEN_FIELDS = [
    "target", "label", "prediction", "future_return", "forward_return", "next_return",
    "signal", "buy", "sell", "long", "short", "position", "recommendation",
]

_LEAKAGE_GUARDS = [
    {"guard_name": "no_target_label_leakage_guard", "description": "Prevents target/label columns from being in feature sets."},
    {"guard_name": "no_future_return_leakage_guard", "description": "Prevents future_return/forward_return/next_return columns."},
    {"guard_name": "no_signal_leakage_guard", "description": "Prevents signal/buy/sell/long/short/position columns."},
    {"guard_name": "no_negative_shift_leakage_guard", "description": "Prevents shift(-1) or negative lag usage that causes lookahead bias."},
]

def build_ml_dataset_leakage_guard_registry(profile=None) -> Tuple[pd.DataFrame, Dict]:
    if profile is None:
        profile = get_default_advanced_ml_dataset_profile()
    rows = []
    for g in _LEAKAGE_GUARDS:
        rows.append({
            "guard_name": g["guard_name"],
            "description": g["description"],
            "blocked_keywords": ", ".join(LEAKAGE_FORBIDDEN_FIELDS),
            "non_signal": True,
            "manual_review_required": True,
            "current_phase": 137,
        })
    df = pd.DataFrame(rows)
    summary = {"total_leakage_guards": len(rows), "current_phase": 137, "non_signal": True, "status": "READY"}
    return df, summary

def validate_ml_dataset_leakage_fields(column_names: List[str]) -> Dict:
    found = [c for c in column_names if any(f in c.lower() for f in LEAKAGE_FORBIDDEN_FIELDS)]
    return {"valid": len(found) == 0, "forbidden_found": found, "non_signal": True}

def validate_no_negative_shift_usage(source_text: str) -> Dict:
    issues = []
    if "shift(-" in source_text:
        issues.append("Negative shift detected: shift(-N) causes lookahead bias")
    for kw in ["future_return", "forward_return", "next_return"]:
        if kw in source_text:
            issues.append(f"Forbidden leakage keyword detected: {kw}")
    return {"valid": len(issues) == 0, "issues": issues, "non_signal": True}

def summarize_ml_dataset_leakage_guards(df: pd.DataFrame) -> Dict:
    return {"total_leakage_guards": len(df), "current_phase": 137, "non_signal": True, "status": "READY"}
