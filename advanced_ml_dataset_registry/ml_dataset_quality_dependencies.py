import pandas as pd
from typing import Dict, Tuple
from advanced_ml_dataset_registry.advanced_ml_dataset_config import get_default_advanced_ml_dataset_profile

_QUAL_DEPS = [
    {"dep_key": "phase_123_quality_drift", "source_phase": "phase_123", "description": "Phase 123 Feature Quality Drift output dependency."},
    {"dep_key": "phase_124_featurestore_metadata", "source_phase": "phase_124", "description": "Phase 124 FeatureStore Metadata quality dependency."},
    {"dep_key": "phase_135_quality_dependency", "source_phase": "phase_135", "description": "Phase 135 Acceptance Manifest quality dependency."},
    {"dep_key": "phase_136_runtime_quality", "source_phase": "phase_136", "description": "Phase 136 GPU/ML Runtime readiness quality dependency."},
    {"dep_key": "phase_137_quality", "source_phase": "phase_137", "description": "Phase 137 Advanced ML Dataset Registry quality dependency."},
    {"dep_key": "manual_review_blocker", "source_phase": "manual", "description": "Manual review blockers before Phase 138 handoff."},
]

def build_ml_dataset_quality_dependency_registry(profile=None) -> Tuple[pd.DataFrame, Dict]:
    if profile is None:
        profile = get_default_advanced_ml_dataset_profile()
    rows = []
    for d in _QUAL_DEPS:
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
        "total_quality_dependencies": len(rows),
        "total_qual_deps": len(rows),
        "current_phase": 137,
        "non_signal": True,
        "status": "READY",
    }
    return df, summary

def summarize_ml_dataset_quality_dependencies(df: pd.DataFrame) -> Dict:
    return {
        "total_quality_dependencies": len(df),
        "total_qual_deps": len(df),
        "current_phase": 137,
        "non_signal": True,
        "status": "READY",
    }
