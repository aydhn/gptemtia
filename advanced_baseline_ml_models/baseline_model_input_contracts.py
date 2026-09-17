# -*- coding: utf-8 -*-
"""Phase 138 Baseline Model Input Contracts Registry.

Defines the linkage and requirements for input data streams from FeatureStore,
Regime metadata, and ML dataset contracts without performing data materialization.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)

INPUT_CONTRACT_DEFINITIONS = [
    {
        "input_contract_id": "input_contract_commodity_fx_v1",
        "dataset_contract_ref": "ds_contract_commodity_fx_daily",
        "feature_snapshot_contract_ref": "snapshot_contract_multi_window_features",
        "runtime_input_ref": "runtime_contract_gpu_ml_accelerators",
        "regime_acceptance_ref": "regime_acceptance_manifest_phase_135",
        "feature_store_catalog_ref": "feature_store_catalog_phase_134",
        "quality_drift_ref": "feature_quality_drift_phase_123",
        "validation_no_lookahead_ref": "feature_validation_no_lookahead_phase_121",
        "dataset_materialized": False,
        "feature_snapshot_materialized": False,
    },
    {
        "input_contract_id": "input_contract_macro_event_v1",
        "dataset_contract_ref": "ds_contract_macro_event_daily",
        "feature_snapshot_contract_ref": "snapshot_contract_macro_calendar_features",
        "runtime_input_ref": "runtime_contract_cpu_memory_capabilities",
        "regime_acceptance_ref": "regime_acceptance_manifest_phase_135",
        "feature_store_catalog_ref": "feature_store_catalog_phase_134",
        "quality_drift_ref": "feature_quality_drift_phase_123",
        "validation_no_lookahead_ref": "feature_validation_no_lookahead_phase_121",
        "dataset_materialized": False,
        "feature_snapshot_materialized": False,
    },
    {
        "input_contract_id": "input_contract_cross_asset_regime_v1",
        "dataset_contract_ref": "ds_contract_cross_asset_regime_daily",
        "feature_snapshot_contract_ref": "snapshot_contract_cross_asset_features",
        "runtime_input_ref": "runtime_contract_environment_snapshot",
        "regime_acceptance_ref": "regime_acceptance_manifest_phase_135",
        "feature_store_catalog_ref": "feature_store_catalog_phase_134",
        "quality_drift_ref": "feature_quality_drift_phase_123",
        "validation_no_lookahead_ref": "feature_validation_no_lookahead_phase_121",
        "dataset_materialized": False,
        "feature_snapshot_materialized": False,
    },
]


def build_baseline_model_input_contract_registry(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build input contract DataFrame and summary."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    rows = []
    for item in INPUT_CONTRACT_DEFINITIONS:
        rows.append({
            "input_contract_id": item["input_contract_id"],
            "dataset_contract_ref": item["dataset_contract_ref"],
            "feature_snapshot_contract_ref": item["feature_snapshot_contract_ref"],
            "runtime_input_ref": item["runtime_input_ref"],
            "regime_acceptance_ref": item["regime_acceptance_ref"],
            "feature_store_catalog_ref": item["feature_store_catalog_ref"],
            "quality_drift_ref": item["quality_drift_ref"],
            "validation_no_lookahead_ref": item["validation_no_lookahead_ref"],
            "dataset_materialized": False,
            "feature_snapshot_materialized": False,
            "is_validated": True,
            "non_signal": True,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_baseline_model_input_contracts(df)
    return df, summary


def summarize_baseline_model_input_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize baseline model input contracts."""
    return {
        "total_input_contracts": len(df),
        "all_materialization_blocked": bool((~df["dataset_materialized"]).all() and (~df["feature_snapshot_materialized"]).all()) if not df.empty else True,
        "all_validated": bool(df["is_validated"].all()) if not df.empty else True,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
