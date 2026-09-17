# -*- coding: utf-8 -*-
"""Phase 141: Quantile Placeholders."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

QUANTILE_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "placeholder_name": "median_quantile_q50_placeholder",
        "quantile_tau": 0.50,
        "description": "Conditional median (tau=0.50) placeholder; uncalculated.",
    },
    {
        "placeholder_name": "lower_tail_quantile_q05_placeholder",
        "quantile_tau": 0.05,
        "description": "Lower tail conditional quantile (tau=0.05) placeholder; uncalculated.",
    },
    {
        "placeholder_name": "upper_tail_quantile_q95_placeholder",
        "quantile_tau": 0.95,
        "description": "Upper tail conditional quantile (tau=0.95) placeholder; uncalculated.",
    },
    {
        "placeholder_name": "interquartile_quantile_q25_placeholder",
        "quantile_tau": 0.25,
        "description": "Lower quartile conditional quantile (tau=0.25) placeholder; uncalculated.",
    },
    {
        "placeholder_name": "interquartile_quantile_q75_placeholder",
        "quantile_tau": 0.75,
        "description": "Upper quartile conditional quantile (tau=0.75) placeholder; uncalculated.",
    },
]


def build_quantile_placeholder_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for quantile placeholders."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for item in QUANTILE_PLACEHOLDERS:
        rows.append(
            {
                "placeholder_name": item["placeholder_name"],
                "quantile_tau": item["quantile_tau"],
                "description": item["description"],
                "calculated": False,
                "quantile_value": None,
                "non_signal": True,
                "production_ready": False,
                "phase": prof.current_phase,
                "status": "calibration_contract_placeholder_only",
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_quantile_placeholders(df)
    return df, summary


def summarize_quantile_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize quantile placeholders DataFrame."""
    return {
        "total_placeholders": len(df),
        "placeholders": df["placeholder_name"].tolist() if not df.empty else [],
        "all_uncalculated": bool((~df["calculated"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
