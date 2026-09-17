# -*- coding: utf-8 -*-
"""Phase 141: Uncertainty Output Contracts."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

UNCERTAINTY_OUTPUT_CONTRACTS: List[Dict[str, Any]] = [
    {
        "output_contract_name": "uncertainty_contract_status_output",
        "description": "Metadata status indicating uncertainty estimation contract readiness; zero intervals/values produced.",
        "contains_uncertainty_values": False,
        "contains_intervals": False,
        "contains_risk_signals": False,
        "allowed_fields": ["uncertainty_contract_status", "execution_blocked_by_policy", "blocked_reason", "manual_review_required"],
    },
    {
        "output_contract_name": "uncertainty_safety_block_output",
        "description": "Execution block notification ensuring uncertainty estimation calls are safely intercepted.",
        "contains_uncertainty_values": False,
        "contains_intervals": False,
        "contains_risk_signals": False,
        "allowed_fields": ["execution_blocked_by_policy", "blocked_reason", "intercepted_action"],
    },
]


def build_uncertainty_output_contract_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for all uncertainty output contracts."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for item in UNCERTAINTY_OUTPUT_CONTRACTS:
        rows.append(
            {
                "output_contract_name": item["output_contract_name"],
                "description": item["description"],
                "contains_uncertainty_values": item["contains_uncertainty_values"],
                "contains_intervals": item["contains_intervals"],
                "contains_risk_signals": item["contains_risk_signals"],
                "allowed_fields": ", ".join(item["allowed_fields"]),
                "non_signal": True,
                "phase": prof.current_phase,
                "status": "calibration_contract_ready",
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_uncertainty_output_contracts(df)
    return df, summary


def summarize_uncertainty_output_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize uncertainty output contracts DataFrame."""
    return {
        "total_outputs": len(df),
        "outputs": df["output_contract_name"].tolist() if not df.empty else [],
        "all_zero_uncertainty_values": bool((~df["contains_uncertainty_values"]).all()) if not df.empty else True,
        "all_zero_intervals": bool((~df["contains_intervals"]).all()) if not df.empty else True,
        "all_zero_signals": bool((~df["contains_risk_signals"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
