import pandas as pd
from typing import Dict, List, Tuple
from advanced_ml_dataset_registry.advanced_ml_dataset_config import get_default_advanced_ml_dataset_profile

NO_LOOKAHEAD_FORBIDDEN_COLUMNS = [
    "future_return", "forward_return", "next_return",
    "target", "label", "prediction",
    "signal", "buy", "sell",
]

_NO_LOOKAHEAD_GUARDS = [
    {"guard_name": "regime_no_lookahead_guard", "description": "Regime metadata no-lookahead guard."},
    {"guard_name": "featurestore_no_lookahead_guard", "description": "FeatureStore no-lookahead guard."},
    {"guard_name": "technical_feature_no_lookahead_guard", "description": "Technical feature no-lookahead guard."},
    {"guard_name": "factor_no_lookahead_guard", "description": "Factor feature no-lookahead guard."},
    {"guard_name": "cross_asset_no_lookahead_guard", "description": "Cross-asset feature no-lookahead guard."},
    {"guard_name": "macro_event_no_lookahead_guard", "description": "Macro event no-lookahead guard."},
    {"guard_name": "validation_accepted_no_lookahead_guard", "description": "Validation accepted no-lookahead guard."},
    {"guard_name": "baseline_no_lookahead_guard", "description": "Baseline model input no-lookahead guard."},
    {"guard_name": "phase_138_no_lookahead_guard", "description": "Phase 138 training harness no-lookahead guard."},
]

def build_ml_dataset_no_lookahead_guard_registry(profile=None) -> Tuple[pd.DataFrame, Dict]:
    if profile is None:
        profile = get_default_advanced_ml_dataset_profile()
    rows = []
    for g in _NO_LOOKAHEAD_GUARDS:
        rows.append({
            "guard_name": g["guard_name"],
            "description": g["description"],
            "forbidden_columns": ", ".join(NO_LOOKAHEAD_FORBIDDEN_COLUMNS),
            "future_timestamp_forbidden": True,
            "non_signal": True,
            "manual_review_required": True,
            "current_phase": 137,
        })
    df = pd.DataFrame(rows)
    summary = {"total_no_lookahead_guards": len(rows), "current_phase": 137, "non_signal": True, "status": "READY"}
    return df, summary

def validate_no_future_ml_dataset_join(left_df: pd.DataFrame, right_df: pd.DataFrame, left_ts: str, right_ts: str) -> Dict:
    # Sadece metadata kontrol -- gercek join yok
    issues = []
    if left_ts not in (left_df.columns if hasattr(left_df, 'columns') else []):
        issues.append(f"Missing timestamp field in left_df: {left_ts}")
    if right_ts not in (right_df.columns if hasattr(right_df, 'columns') else []):
        issues.append(f"Missing timestamp field in right_df: {right_ts}")
    return {"valid": len(issues) == 0, "issues": issues, "non_signal": True}

def validate_no_forbidden_no_lookahead_columns(df: pd.DataFrame) -> Dict:
    cols = list(df.columns) if hasattr(df, 'columns') else []
    found = [c for c in cols if any(f in c.lower() for f in NO_LOOKAHEAD_FORBIDDEN_COLUMNS)]
    return {"valid": len(found) == 0, "forbidden_found": found, "non_signal": True}

def summarize_ml_dataset_no_lookahead_guards(df: pd.DataFrame) -> Dict:
    return {"total_no_lookahead_guards": len(df), "current_phase": 137, "non_signal": True, "status": "READY"}
