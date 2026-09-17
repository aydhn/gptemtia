import pandas as pd
from typing import Dict, Tuple
from advanced_ml_dataset_registry.advanced_ml_dataset_config import get_default_advanced_ml_dataset_profile

SOURCE_PRESERVATION_FORBIDDEN_ACTIONS = [
    "overwrite", "delete", "move", "destructive_clean",
    "auto_impute", "auto_drop", "archive", "git_tag", "docker_push",
]

_SP_GUARDS = [
    {"guard_name": "regime_source_preservation_guard", "description": "Regime metadata source preservation."},
    {"guard_name": "featurestore_source_preservation_guard", "description": "FeatureStore source preservation."},
    {"guard_name": "technical_source_preservation_guard", "description": "Technical feature source preservation."},
    {"guard_name": "factor_source_preservation_guard", "description": "Factor feature source preservation."},
    {"guard_name": "cross_asset_source_preservation_guard", "description": "Cross-asset feature source preservation."},
    {"guard_name": "macro_event_source_preservation_guard", "description": "Macro event source preservation."},
    {"guard_name": "validation_source_preservation_guard", "description": "Validation accepted source preservation."},
    {"guard_name": "baseline_source_preservation_guard", "description": "Baseline model input source preservation."},
    {"guard_name": "phase_138_source_preservation_guard", "description": "Phase 138 training harness source preservation."},
]

def build_ml_dataset_source_preservation_guard_registry(profile=None) -> Tuple[pd.DataFrame, Dict]:
    if profile is None:
        profile = get_default_advanced_ml_dataset_profile()
    rows = []
    for g in _SP_GUARDS:
        rows.append({
            "guard_name": g["guard_name"],
            "description": g["description"],
            "forbidden_actions": ", ".join(SOURCE_PRESERVATION_FORBIDDEN_ACTIONS),
            "overwrite_allowed": False,
            "delete_allowed": False,
            "auto_impute_allowed": False,
            "auto_drop_allowed": False,
            "non_signal": True,
            "manual_review_required": True,
            "current_phase": 137,
        })
    df = pd.DataFrame(rows)
    summary = {"total_sp_guards": len(rows), "current_phase": 137, "non_signal": True, "status": "READY"}
    return df, summary

def validate_ml_dataset_source_preservation_action(action: str) -> Dict:
    forbidden = [f for f in SOURCE_PRESERVATION_FORBIDDEN_ACTIONS if f in action.lower()]
    return {"valid": len(forbidden) == 0, "forbidden_actions_found": forbidden, "non_signal": True}

def summarize_ml_dataset_source_preservation_guards(df: pd.DataFrame) -> Dict:
    return {"total_sp_guards": len(df), "current_phase": 137, "non_signal": True, "status": "READY"}
