# -*- coding: utf-8 -*-
"""Phase 138 Baseline Model Lineage Registry.

Maintains immutable provenance links from upstream feature/factor blocks,
regime classification blocks, runtime, and dataset registries to baseline models.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)

LINEAGE_STAGES = [
    {"stage": "Phase 116-125", "layer_name": "Feature & Factor Engine Block", "output_type": "feature_matrix_contracts", "target": "FeatureStore catalog & quality gates"},
    {"stage": "Phase 126-135", "layer_name": "Regime Classification Block", "output_type": "regime_acceptance_manifest", "target": "Market behavior & state sequence metadata"},
    {"stage": "Phase 136", "layer_name": "GPU ML Runtime Foundation", "output_type": "runtime_profiles_contracts", "target": "Hardware capability & safety permissions"},
    {"stage": "Phase 137", "layer_name": "ML Dataset & Experiment Registry", "output_type": "ml_dataset_contracts", "target": "Feature snapshots & experiment templates"},
    {"stage": "Phase 138", "layer_name": "Baseline ML Model Contracts", "output_type": "baseline_model_contracts", "target": "Dry-run training plans & trainer stubs"},
]


def build_baseline_model_lineage_registry(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build lineage registry DataFrame and summary."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    rows = []
    for item in LINEAGE_STAGES:
        rows.append({
            "stage": item["stage"],
            "layer_name": item["layer_name"],
            "output_type": item["output_type"],
            "target": item["target"],
            "source_preserved": True,
            "non_signal": True,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_baseline_model_lineage(df)
    return df, summary


def summarize_baseline_model_lineage(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize baseline model lineage."""
    return {
        "total_lineage_stages": len(df),
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
