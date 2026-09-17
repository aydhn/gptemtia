import pandas as pd
from typing import Dict, Tuple
from advanced_ml_dataset_registry.advanced_ml_dataset_config import (
    AdvancedMlDatasetProfile,
    get_default_advanced_ml_dataset_profile,
)

_SOURCES = [
    # Phase 116-125 feature/factor outputs
    {"source_key": "phase_116_technical_indicators", "source_phase": "phase_116", "description": "Phase 116 Technical Indicators output — metadata reference only"},
    {"source_key": "phase_117_feature_engine", "source_phase": "phase_117", "description": "Phase 117 Feature Engine output — metadata reference only"},
    {"source_key": "phase_118_feature_grid", "source_phase": "phase_118", "description": "Phase 118 Feature Grid output — metadata reference only"},
    {"source_key": "phase_119_cross_asset_alignment", "source_phase": "phase_119", "description": "Phase 119 Cross-Asset Alignment output — metadata reference only"},
    {"source_key": "phase_120_feature_fusion", "source_phase": "phase_120", "description": "Phase 120 Feature Fusion output — metadata reference only"},
    {"source_key": "phase_121_feature_validation", "source_phase": "phase_121", "description": "Phase 121 Feature Validation output — metadata reference only"},
    {"source_key": "phase_122_factor_metadata", "source_phase": "phase_122", "description": "Phase 122 Factor Metadata output — metadata reference only"},
    {"source_key": "phase_123_feature_quality_drift", "source_phase": "phase_123", "description": "Phase 123 Feature Quality Drift output — metadata reference only"},
    {"source_key": "phase_124_feature_store_integration", "source_phase": "phase_124", "description": "Phase 124 FeatureStore Integration output — metadata reference only"},
    {"source_key": "phase_125_feature_factor_acceptance", "source_phase": "phase_125", "description": "Phase 125 Feature Factor Acceptance output — metadata reference only"},
    # Phase 126-135 regime block outputs
    {"source_key": "phase_126_regime_foundation", "source_phase": "phase_126", "description": "Phase 126 Regime Foundation output — metadata reference only"},
    {"source_key": "phase_127_regime_matrix", "source_phase": "phase_127", "description": "Phase 127 Regime Matrix output — metadata reference only"},
    {"source_key": "phase_128_regime_rule_free", "source_phase": "phase_128", "description": "Phase 128 Regime Rule-Free output — metadata reference only"},
    {"source_key": "phase_129_regime_transition", "source_phase": "phase_129", "description": "Phase 129 Regime Transition output — metadata reference only"},
    {"source_key": "phase_130_market_behavior_diagnostics", "source_phase": "phase_130", "description": "Phase 130 Market Behavior Diagnostics output — metadata reference only"},
    {"source_key": "phase_131_cross_asset_regime_context", "source_phase": "phase_131", "description": "Phase 131 Cross-Asset Regime Context output — metadata reference only"},
    {"source_key": "phase_132_macro_event_news_regime", "source_phase": "phase_132", "description": "Phase 132 Macro Event News Regime output — metadata reference only"},
    {"source_key": "phase_133_regime_validation_acceptance", "source_phase": "phase_133", "description": "Phase 133 Regime Validation Acceptance output — metadata reference only"},
    {"source_key": "phase_134_featurestore_catalog", "source_phase": "phase_134", "description": "Phase 134 FeatureStore Catalog — metadata reference only"},
    {"source_key": "phase_135_acceptance_manifest", "source_phase": "phase_135", "description": "Phase 135 Acceptance Manifest — metadata reference only"},
    # Phase 136 GPU/ML runtime input contracts
    {"source_key": "phase_136_gpu_ml_runtime", "source_phase": "phase_136", "description": "Phase 136 GPU/ML Runtime Foundation output — metadata reference only"},
]


def build_ml_dataset_source_catalog_registry(
    profile: AdvancedMlDatasetProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build a registry DataFrame and summary dict for all ML dataset sources.

    Every source entry is flagged as a metadata-only reference.  No data is
    materialized, no targets/labels/predictions/embeddings are present.
    dry_run=True, local_only=True, non_production=True, research_only=True.
    """
    if profile is None:
        profile = get_default_advanced_ml_dataset_profile()

    rows = []
    for s in _SOURCES:
        rows.append({
            "source_key": s["source_key"],
            "source_phase": s["source_phase"],
            "description": s["description"],
            "source_type": "metadata_reference",
            "materialized": False,
            "contains_target": False,
            "contains_label": False,
            "contains_prediction": False,
            "contains_full_article": False,
            "contains_embedding": False,
            "non_signal": True,
            "manual_review_required": True,
            "current_phase": 137,
        })

    df = pd.DataFrame(rows)
    summary = {
        "total_sources": len(rows),
        "current_phase": 137,
        "all_metadata_reference_only": True,
        "non_signal": True,
        "materialized": False,
        "contains_target": False,
        "status": "READY",
    }
    return df, summary


def summarize_ml_dataset_source_catalog(df: pd.DataFrame) -> Dict:
    """Return a lightweight summary dict for an existing source catalog DataFrame."""
    return {
        "total_sources": len(df),
        "current_phase": 137,
        "all_metadata_reference_only": True,
        "materialized": False,
        "non_signal": True,
        "status": "READY",
    }
