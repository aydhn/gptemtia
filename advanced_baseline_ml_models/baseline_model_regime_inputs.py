# -*- coding: utf-8 -*-
"""Phase 138 Baseline Model Regime Inputs Registry.

Maintains registry references to Regime Classification and Market Behavior
metadata from Phases 126-135 for baseline model conditioning without signal leakage.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)

REGIME_INPUT_CATALOG = [
    {"regime_context": "volatility_regime_state", "source_phase": 126, "manifest_ref": "regime_acceptance_manifest_phase_135", "non_signal_certified": True},
    {"regime_context": "trend_persistence_state", "source_phase": 130, "manifest_ref": "regime_acceptance_manifest_phase_135", "non_signal_certified": True},
    {"regime_context": "range_bound_state", "source_phase": 127, "manifest_ref": "regime_acceptance_manifest_phase_135", "non_signal_certified": True},
    {"regime_context": "macro_event_regime_state", "source_phase": 132, "manifest_ref": "regime_acceptance_manifest_phase_135", "non_signal_certified": True},
    {"regime_context": "cross_asset_regime_context", "source_phase": 131, "manifest_ref": "regime_acceptance_manifest_phase_135", "non_signal_certified": True},
]


def build_baseline_model_regime_input_registry(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build regime input registry."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    rows = []
    for item in REGIME_INPUT_CATALOG:
        rows.append({
            "regime_context": item["regime_context"],
            "source_phase": item["source_phase"],
            "manifest_ref": item["manifest_ref"],
            "non_signal_certified": item["non_signal_certified"],
            "materialized": False,
            "non_signal": True,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_baseline_model_regime_inputs(df)
    return df, summary


def summarize_baseline_model_regime_inputs(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize regime inputs."""
    return {
        "total_regime_inputs": len(df),
        "all_certified_non_signal": bool(df["non_signal_certified"].all()) if not df.empty else True,
        "all_materialization_blocked": bool((~df["materialized"]).all()) if not df.empty else True,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
