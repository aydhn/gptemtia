# -*- coding: utf-8 -*-
"""Phase 141: Uncertainty Input Contracts."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

UNCERTAINTY_INPUT_CONTRACTS: List[Dict[str, Any]] = [
    {
        "input_contract_name": "candidate_predictions_uncertainty_input",
        "source_phase_ref": "Phase 140 Candidate Model Contracts",
        "description": "Candidate model score vectors as uncertainty inputs.",
        "allows_target": False,
        "allows_prediction": False,
    },
    {
        "input_contract_name": "calibrated_scores_uncertainty_input",
        "source_phase_ref": "Phase 141 Probability Calibration Contracts",
        "description": "Calibrated score metadata references as uncertainty inputs.",
        "allows_target": False,
        "allows_prediction": False,
    },
    {
        "input_contract_name": "featurestore_uncertainty_feature_input",
        "source_phase_ref": "Phase 134 FeatureStore Catalog",
        "description": "FeatureStore feature tensors for uncertainty modeling.",
        "allows_target": False,
        "allows_prediction": False,
    },
]


def build_uncertainty_input_contract_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for all uncertainty input contracts."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for item in UNCERTAINTY_INPUT_CONTRACTS:
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
    summary = summarize_uncertainty_input_contracts(df)
    return df, summary


def summarize_uncertainty_input_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize uncertainty input contracts DataFrame."""
    return {
        "total_inputs": len(df),
        "inputs": df["input_contract_name"].tolist() if not df.empty else [],
        "all_zero_target": bool((~df["allows_target"]).all()) if not df.empty else True,
        "all_zero_prediction": bool((~df["allows_prediction"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
