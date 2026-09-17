# -*- coding: utf-8 -*-
"""Phase 143: Attribution Input Contracts."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_attribution_input_contract_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of attribution input contracts."""
    prof = profile or get_explainability_profile()

    inputs = [
        ("input_candidate_model_ref", "phase_138_candidate_model_registry", "candidate model metadata and frozen weights reference"),
        ("input_ensemble_model_ref", "phase_140_ensemble_contract_registry", "ensemble model weighting reference"),
        ("input_tabular_dataset_ref", "phase_137_dataset_contract_registry", "tabular historical feature matrix reference"),
        ("input_feature_store_ref", "phase_137_feature_store_registry", "feature definition and schema lineage reference"),
        ("input_regime_context_ref", "phase_135_macro_regime_registry", "macro regime context reference"),
        ("input_drift_monitoring_ref", "phase_142_drift_monitoring_registry", "distribution drift baseline reference"),
        ("input_calibration_ref", "phase_141_calibration_uncertainty_registry", "calibration and uncertainty reference"),
    ]

    rows: List[Dict[str, Any]] = []
    for iname, sref, desc in inputs:
        rows.append({
            "input_name": iname,
            "source_reference": sref,
            "description": desc,
            "no_lookahead_enforced": True,
            "metadata_only_enforced": True,
            "source_preserved": True,
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_attribution_input_contracts(df)
    return df, summary


def summarize_attribution_input_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize attribution input contracts."""
    return {
        "total_input_contracts": len(df),
        "all_no_lookahead_enforced": bool(df["no_lookahead_enforced"].all()) if not df.empty else True,
        "all_metadata_only_enforced": bool(df["metadata_only_enforced"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
