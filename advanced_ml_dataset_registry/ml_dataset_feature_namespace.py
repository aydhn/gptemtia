import pandas as pd
from typing import Dict, List, Tuple
from advanced_ml_dataset_registry.advanced_ml_dataset_config import get_default_advanced_ml_dataset_profile

FORBIDDEN_NAMESPACE_WORDS = [
    "signal", "buy", "sell", "long", "short", "position",
    "target", "label", "prediction", "recommendation",
]

_NAMESPACES = [
    {"namespace": "ml_feature_regime_metadata", "description": "Regime metadata features", "source_phase": "phase_126-135"},
    {"namespace": "ml_feature_technical", "description": "Technical indicator features", "source_phase": "phase_116-118"},
    {"namespace": "ml_feature_factor", "description": "Factor features", "source_phase": "phase_122-125"},
    {"namespace": "ml_feature_cross_asset", "description": "Cross-asset features", "source_phase": "phase_119-120"},
    {"namespace": "ml_feature_macro_event_metadata", "description": "Macro event metadata features", "source_phase": "phase_126-132"},
    {"namespace": "ml_feature_featurestore", "description": "FeatureStore features", "source_phase": "phase_124-125"},
    {"namespace": "ml_feature_validation_accepted", "description": "Validation accepted features", "source_phase": "phase_133-135"},
    {"namespace": "ml_feature_dry_run_baseline", "description": "Dry-run baseline model input features", "source_phase": "phase_136"},
]


def build_ml_dataset_feature_namespace_registry(profile=None) -> Tuple[pd.DataFrame, Dict]:
    if profile is None:
        profile = get_default_advanced_ml_dataset_profile()
    rows = []
    for n in _NAMESPACES:
        rows.append({
            "namespace": n["namespace"],
            "description": n["description"],
            "source_phase": n["source_phase"],
            "prefix_required": "ml_feature_",
            "forbidden_words": ", ".join(FORBIDDEN_NAMESPACE_WORDS),
            "non_signal": True,
            "manual_review_required": True,
            "current_phase": 137,
        })
    df = pd.DataFrame(rows)
    summary = {"total_namespaces": len(rows), "current_phase": 137, "non_signal": True, "status": "READY"}
    return df, summary


def build_ml_dataset_feature_key(namespace: str, feature_name: str) -> str:
    if namespace.startswith("ml_feature_"):
        ns = namespace
    else:
        ns = f"ml_feature_{namespace}"
    return f"{ns}_{feature_name}"


def validate_ml_dataset_feature_key(key: str) -> Dict:
    issues = []
    if not key.startswith("ml_feature_"):
        issues.append(f"Feature key must start with ml_feature_: {key}")
    if not key.islower() or " " in key:
        issues.append(f"Feature key must be lowercase snake_case: {key}")
    for w in FORBIDDEN_NAMESPACE_WORDS:
        if w in key.lower():
            issues.append(f"Forbidden word in feature key: {w}")
    return {"valid": len(issues) == 0, "key": key, "issues": issues, "non_signal": True}


def summarize_ml_dataset_feature_namespace(df: pd.DataFrame) -> Dict:
    return {"total_namespaces": len(df), "current_phase": 137, "non_signal": True, "status": "READY"}
