# -*- coding: utf-8 -*-
"""Phase 141: Calibration Output Contracts."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

CALIBRATION_OUTPUT_CONTRACTS: List[Dict[str, Any]] = [
    {
        "output_contract_name": "calibration_contract_status_output",
        "description": "Metadata status indicating calibration contract readiness; zero probabilities produced.",
        "contains_probabilities": False,
        "contains_confidence_scores": False,
        "contains_signals": False,
        "allowed_fields": ["calibration_contract_status", "execution_blocked_by_policy", "blocked_reason", "manual_review_required"],
    },
    {
        "output_contract_name": "calibration_safety_block_output",
        "description": "Execution block notification ensuring fit/transform calls are safely intercepted.",
        "contains_probabilities": False,
        "contains_confidence_scores": False,
        "contains_signals": False,
        "allowed_fields": ["execution_blocked_by_policy", "blocked_reason", "intercepted_action"],
    },
]


def build_calibration_output_contract_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for all calibration output contracts."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for item in CALIBRATION_OUTPUT_CONTRACTS:
        rows.append(
            {
                "output_contract_name": item["output_contract_name"],
                "description": item["description"],
                "contains_probabilities": item["contains_probabilities"],
                "contains_confidence_scores": item["contains_confidence_scores"],
                "contains_signals": item["contains_signals"],
                "allowed_fields": ", ".join(item["allowed_fields"]),
                "non_signal": True,
                "phase": prof.current_phase,
                "status": "calibration_contract_ready",
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_calibration_output_contracts(df)
    return df, summary


def summarize_calibration_output_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize calibration output contracts DataFrame."""
    return {
        "total_outputs": len(df),
        "outputs": df["output_contract_name"].tolist() if not df.empty else [],
        "all_zero_probabilities": bool((~df["contains_probabilities"]).all()) if not df.empty else True,
        "all_zero_confidence": bool((~df["contains_confidence_scores"]).all()) if not df.empty else True,
        "all_zero_signals": bool((~df["contains_signals"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
