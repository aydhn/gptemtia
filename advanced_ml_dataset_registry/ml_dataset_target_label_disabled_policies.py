import pandas as pd
from typing import Dict, Tuple, Union
from advanced_ml_dataset_registry.advanced_ml_dataset_config import get_default_advanced_ml_dataset_profile

TARGET_LABEL_FORBIDDEN_KEYWORDS = [
    "target", "label", "future_return", "forward_return", "next_return",
    "classification_label", "regression_target", "directional_label",
    "signal", "prediction",
]

_TARGET_LABEL_POLICIES = [
    {"policy_name": "target_label_generation_blocked", "description": "Target/label generation is blocked in Phase 137."},
    {"policy_name": "future_return_label_blocked", "description": "Future return label is blocked. No forward_return, next_return or shift(-1) usage."},
    {"policy_name": "directional_label_blocked", "description": "Directional label generation is blocked."},
    {"policy_name": "classification_label_blocked", "description": "Classification label generation is blocked."},
    {"policy_name": "regression_target_blocked", "description": "Regression target generation is blocked."},
]

def build_ml_dataset_target_label_disabled_policy_registry(profile=None) -> Tuple[pd.DataFrame, Dict]:
    if profile is None:
        profile = get_default_advanced_ml_dataset_profile()
    rows = []
    for p in _TARGET_LABEL_POLICIES:
        rows.append({
            "policy_name": p["policy_name"],
            "description": p["description"],
            "forbidden_keywords": ", ".join(TARGET_LABEL_FORBIDDEN_KEYWORDS),
            "target_label_allowed": False,
            "future_return_allowed": False,
            "non_signal": True,
            "manual_review_required": True,
            "current_phase": 137,
        })
    df = pd.DataFrame(rows)
    summary = {
        "total_policies": len(rows),
        "current_phase": 137,
        "non_signal": True,
        "target_label_allowed": False,
        "target_label_generation_allowed": False,
        "all_enforced": True,
        "status": "READY",
    }
    return df, summary

def validate_no_target_label_request(request: Union[Dict, str]) -> Dict:
    issues = []
    text = str(request).lower()
    for kw in TARGET_LABEL_FORBIDDEN_KEYWORDS:
        if kw in text:
            issues.append(f"Forbidden target/label keyword detected: {kw}")
    return {"valid": len(issues) == 0, "issues": issues, "target_label_blocked": True, "non_signal": True}

def summarize_ml_dataset_target_label_disabled_policies(df: pd.DataFrame) -> Dict:
    return {
        "total_policies": len(df),
        "current_phase": 137,
        "non_signal": True,
        "target_label_allowed": False,
        "target_label_generation_allowed": False,
        "all_enforced": True,
        "status": "READY",
    }
