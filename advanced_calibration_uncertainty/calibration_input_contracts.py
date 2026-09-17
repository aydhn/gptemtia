# -*- coding: utf-8 -*-
"""Phase 141: Calibration Input Contracts."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

CALIBRATION_INPUT_CONTRACTS: List[Dict[str, Any]] = [
    {
        "input_contract_name": "candidate_model_uncalibrated_scores_contract",
        "source_phase_ref": "Phase 140 Candidate Model Contracts",
        "description": "Uncalibrated raw decision values or logits from candidate models.",
        "allows_target": False,
        "allows_prediction": False,
    },
    {
        "input_contract_name": "ensemble_uncalibrated_consensus_contract",
        "source_phase_ref": "Phase 140 Ensemble Strategy Contracts",
        "description": "Uncalibrated ensemble aggregated consensus scores.",
        "allows_target": False,
        "allows_prediction": False,
    },
    {
        "input_contract_name": "featurestore_calibration_metadata_contract",
        "source_phase_ref": "Phase 134 FeatureStore Catalog",
        "description": "Feature store metadata and schema references for calibration splits.",
        "allows_target": False,
        "allows_prediction": False,
    },
    {
        "input_contract_name": "regime_acceptance_context_contract",
        "source_phase_ref": "Phase 135 Regime Acceptance",
        "description": "Regime acceptance boundaries and state references.",
        "allows_target": False,
        "allows_prediction": False,
    },
    {
        "input_contract_name": "no_lookahead_temporal_split_contract",
        "source_phase_ref": "Phase 121/133/137 Validation Contracts",
        "description": "Strict strictly non-overlapping temporal partition contracts.",
        "allows_target": False,
        "allows_prediction": False,
    },
]


def build_calibration_input_contract_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for all calibration input contracts."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for item in CALIBRATION_INPUT_CONTRACTS:
        rows.append(
            {
                "input_contract_name": item["input_contract_name"],
                "source_phase_ref": item["source_phase_ref"],
                "description": item["description"],
                "allows_target": item["allows_target"],
                "allows_prediction": item["allows_prediction"],
                "non_signal": True,
                "phase": prof.current_phase,
                "status": "calibration_contract_ready",
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_calibration_input_contracts(df)
    return df, summary


def summarize_calibration_input_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize calibration input contracts DataFrame."""
    return {
        "total_inputs": len(df),
        "inputs": df["input_contract_name"].tolist() if not df.empty else [],
        "all_zero_target": bool((~df["allows_target"]).all()) if not df.empty else True,
        "all_zero_prediction": bool((~df["allows_prediction"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
