import pandas as pd
from typing import Dict, Tuple
from advanced_ml_dataset_registry.advanced_ml_dataset_config import get_default_advanced_ml_dataset_profile

_VAL_DEPS = [
    {"dep_key": "phase_121_validation", "source_phase": "phase_121", "description": "Phase 121 Feature Validation output dependency."},
    {"dep_key": "phase_133_regime_validation", "source_phase": "phase_133", "description": "Phase 133 Regime Validation Acceptance output dependency."},
    {"dep_key": "phase_134_featurestore_validation", "source_phase": "phase_134", "description": "Phase 134 FeatureStore Integration Validation output dependency."},
    {"dep_key": "phase_135_acceptance_validation", "source_phase": "phase_135", "description": "Phase 135 Regime Acceptance output dependency."},
    {"dep_key": "phase_136_runtime_validation", "source_phase": "phase_136", "description": "Phase 136 GPU/ML Runtime validation output dependency."},
    {"dep_key": "phase_137_validation", "source_phase": "phase_137", "description": "Phase 137 Advanced ML Dataset Registry validation output dependency."},
    {"dep_key": "phase_125_factor_validation", "source_phase": "phase_125", "description": "Phase 125 Feature Factor Acceptance validation dependency."},
]

def build_ml_dataset_validation_dependency_registry(profile=None) -> Tuple[pd.DataFrame, Dict]:
    if profile is None:
        profile = get_default_advanced_ml_dataset_profile()
    rows = []
    for d in _VAL_DEPS:
        rows.append({
            "dep_key": d["dep_key"],
            "source_phase": d["source_phase"],
            "description": d["description"],
            "non_signal": True,
            "manual_review_required": True,
            "current_phase": 137,
        })
    df = pd.DataFrame(rows)
    summary = {
        "total_validation_dependencies": len(rows),
        "total_val_deps": len(rows),
        "current_phase": 137,
        "non_signal": True,
        "status": "READY",
    }
    return df, summary

def summarize_ml_dataset_validation_dependencies(df: pd.DataFrame) -> Dict:
    return {
        "total_validation_dependencies": len(df),
        "total_val_deps": len(df),
        "current_phase": 137,
        "non_signal": True,
        "status": "READY",
    }
