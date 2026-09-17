# -*- coding: utf-8 -*-
"""Phase 138 Baseline Model FeatureStore Inputs Registry.

Maintains registry references to FeatureStore catalogs, namespaces, and schemas
for baseline model training plans.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)

FEATURESTORE_INPUT_CATALOG = [
    {"feature_namespace": "price_technical", "feature_count_placeholder": 45, "catalog_ref": "feature_store_catalog_phase_134", "no_lookahead_verified": True},
    {"feature_namespace": "volatility_range", "feature_count_placeholder": 30, "catalog_ref": "feature_store_catalog_phase_134", "no_lookahead_verified": True},
    {"feature_namespace": "momentum_trend", "feature_count_placeholder": 35, "catalog_ref": "feature_store_catalog_phase_134", "no_lookahead_verified": True},
    {"feature_namespace": "cross_asset_alignment", "feature_count_placeholder": 25, "catalog_ref": "feature_store_catalog_phase_134", "no_lookahead_verified": True},
    {"feature_namespace": "macro_event_context", "feature_count_placeholder": 20, "catalog_ref": "feature_store_catalog_phase_134", "no_lookahead_verified": True},
]


def build_baseline_model_featurestore_input_registry(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build FeatureStore input registry."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    rows = []
    for item in FEATURESTORE_INPUT_CATALOG:
        rows.append({
            "feature_namespace": item["feature_namespace"],
            "feature_count_placeholder": item["feature_count_placeholder"],
            "catalog_ref": item["catalog_ref"],
            "no_lookahead_verified": item["no_lookahead_verified"],
            "materialized": False,
            "non_signal": True,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_baseline_model_featurestore_inputs(df)
    return df, summary


def summarize_baseline_model_featurestore_inputs(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize FeatureStore inputs."""
    return {
        "total_namespaces": len(df),
        "all_no_lookahead_verified": bool(df["no_lookahead_verified"].all()) if not df.empty else True,
        "all_materialization_blocked": bool((~df["materialized"]).all()) if not df.empty else True,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
