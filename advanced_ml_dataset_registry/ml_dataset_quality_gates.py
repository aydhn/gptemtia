import pandas as pd
from typing import Dict, Tuple
from advanced_ml_dataset_registry.advanced_ml_dataset_config import get_default_advanced_ml_dataset_profile

_QUALITY_GATES = [
    {"gate_name": "source_catalog_present_gate", "description": "Source catalog must be present."},
    {"gate_name": "schema_contract_present_gate", "description": "Schema contract must be present."},
    {"gate_name": "time_index_policy_present_gate", "description": "Time index policy must be present."},
    {"gate_name": "split_policy_present_gate", "description": "Split policy must be present."},
    {"gate_name": "no_lookahead_guard_present_gate", "description": "No-lookahead guard must be present."},
    {"gate_name": "metadata_only_news_guard_present_gate", "description": "Metadata-only news guard must be present."},
    {"gate_name": "source_preservation_guard_present_gate", "description": "Source preservation guard must be present."},
    {"gate_name": "target_label_disabled_gate", "description": "Target/label generation must be disabled."},
    {"gate_name": "training_disabled_gate", "description": "Model training must be disabled."},
    {"gate_name": "manual_review_gate", "description": "Manual review must be required."},
]

def build_ml_dataset_quality_gate_registry(profile=None) -> Tuple[pd.DataFrame, Dict]:
    if profile is None:
        profile = get_default_advanced_ml_dataset_profile()
    rows = []
    for g in _QUALITY_GATES:
        rows.append({
            "gate_name": g["gate_name"],
            "description": g["description"],
            "passed": False,  # placeholder, acik bir pass olmadan isaretlenmesin
            "non_signal": True,
            "current_phase": 137,
        })
    df = pd.DataFrame(rows)
    summary = {
        "total_quality_gates": len(rows),
        "total_gates": len(rows),
        "current_phase": 137,
        "all_mandatory": True,
        "non_signal": True,
        "status": "READY",
    }
    return df, summary

def summarize_ml_dataset_quality_gates(df: pd.DataFrame) -> Dict:
    return {
        "total_quality_gates": len(df),
        "total_gates": len(df),
        "current_phase": 137,
        "all_mandatory": True,
        "non_signal": True,
        "status": "READY",
    }
