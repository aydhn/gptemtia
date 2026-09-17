import pandas as pd
from typing import Dict, Tuple
from advanced_ml_dataset_registry.advanced_ml_dataset_config import get_default_advanced_ml_dataset_profile

_LINEAGE = [
    {"lineage_key": "phase_116_125_feature_factor_lineage", "description": "Phase 116-125 feature/factor lineage.", "source_phases": "phase_116-phase_125"},
    {"lineage_key": "phase_126_135_regime_lineage", "description": "Phase 126-135 regime lineage.", "source_phases": "phase_126-phase_135"},
    {"lineage_key": "phase_136_gpu_ml_runtime_lineage", "description": "Phase 136 GPU/ML runtime lineage.", "source_phases": "phase_136"},
    {"lineage_key": "phase_137_ml_dataset_registry_lineage", "description": "Phase 137 Advanced ML Dataset Registry lineage.", "source_phases": "phase_137"},
    {"lineage_key": "phase_138_baseline_model_contract_lineage", "description": "Future Phase 138 Baseline ML Model Contract lineage placeholder.", "source_phases": "phase_138 (future)"},
]

def build_ml_dataset_lineage_registry(profile=None) -> Tuple[pd.DataFrame, Dict]:
    if profile is None:
        profile = get_default_advanced_ml_dataset_profile()
    rows = []
    for l in _LINEAGE:
        rows.append({
            "lineage_key": l["lineage_key"],
            "description": l["description"],
            "source_phases": l["source_phases"],
            "non_signal": True,
            "manual_review_required": True,
            "current_phase": 137,
        })
    df = pd.DataFrame(rows)
    summary = {
        "total_lineage_records": len(rows),
        "total_lineage_entries": len(rows),
        "current_phase": 137,
        "non_signal": True,
        "status": "READY",
    }
    return df, summary

def summarize_ml_dataset_lineage(df: pd.DataFrame) -> Dict:
    return {
        "total_lineage_records": len(df),
        "total_lineage_entries": len(df),
        "current_phase": 137,
        "non_signal": True,
        "status": "READY",
    }
