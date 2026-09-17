import pandas as pd
from typing import Dict, List, Tuple
from advanced_ml_dataset_registry.advanced_ml_dataset_config import get_default_advanced_ml_dataset_profile

_MANIFEST_PLACEHOLDERS = [
    {"snapshot_id_placeholder": "featurestore_snapshot_ph_001", "source_catalog_refs": "phase_124_feature_store_integration, phase_125_feature_factor_acceptance"},
    {"snapshot_id_placeholder": "regime_metadata_snapshot_ph_001", "source_catalog_refs": "phase_133_regime_validation_acceptance, phase_134_featurestore_catalog, phase_135_acceptance_manifest"},
    {"snapshot_id_placeholder": "technical_feature_snapshot_ph_001", "source_catalog_refs": "phase_116_technical_indicators, phase_117_feature_engine, phase_118_feature_grid"},
    {"snapshot_id_placeholder": "factor_feature_snapshot_ph_001", "source_catalog_refs": "phase_122_factor_metadata, phase_125_feature_factor_acceptance"},
    {"snapshot_id_placeholder": "macro_event_news_metadata_snapshot_ph_001", "source_catalog_refs": "phase_126_regime_foundation, phase_132_macro_event_news_regime"},
]

def build_feature_snapshot_manifest_placeholder_registry(profile=None) -> Tuple[pd.DataFrame, Dict]:
    if profile is None:
        profile = get_default_advanced_ml_dataset_profile()
    rows = []
    for p in _MANIFEST_PLACEHOLDERS:
        rows.append({
            "snapshot_id_placeholder": p["snapshot_id_placeholder"],
            "source_catalog_refs": p["source_catalog_refs"],
            "materialized": False,
            "non_signal": True,
            "manual_review_required": True,
            "current_phase": 137,
        })
    df = pd.DataFrame(rows)
    summary = {
        "total_manifest_placeholders": len(rows),
        "current_phase": 137,
        "non_signal": True,
        "materialized": False,
        "production_ready": False,
        "status": "READY",
    }
    return df, summary

def summarize_feature_snapshot_manifest_placeholders(df: pd.DataFrame) -> Dict:
    return {
        "total_manifest_placeholders": len(df),
        "current_phase": 137,
        "non_signal": True,
        "materialized": False,
        "production_ready": False,
        "status": "READY",
    }
