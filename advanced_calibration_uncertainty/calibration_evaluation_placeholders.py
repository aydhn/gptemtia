# -*- coding: utf-8 -*-
"""Phase 141: Calibration Evaluation Placeholders."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

CALIBRATION_EVALUATION_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "evaluation_name": "in_domain_calibration_evaluation_placeholder",
        "scope": "test_split_calibration_stability",
        "description": "Evaluates calibration stability on in-domain test splits; unexecuted.",
    },
    {
        "evaluation_name": "multi_horizon_calibration_evaluation_placeholder",
        "scope": "multi_horizon_consistency",
        "description": "Evaluates calibration consistency across multiple forecasting horizons; unexecuted.",
    },
    {
        "evaluation_name": "regime_conditional_calibration_evaluation_placeholder",
        "scope": "regime_conditioned_reliability",
        "description": "Evaluates calibration reliability within identified market regimes; unexecuted.",
    },
    {
        "evaluation_name": "tail_event_calibration_evaluation_placeholder",
        "scope": "extreme_tail_probability_assessment",
        "description": "Evaluates probability calibration on extreme market tail events; unexecuted.",
    },
]


def build_calibration_evaluation_placeholder_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for calibration evaluation placeholders."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for item in CALIBRATION_EVALUATION_PLACEHOLDERS:
        rows.append(
            {
                "evaluation_name": item["evaluation_name"],
                "scope": item["scope"],
                "description": item["description"],
                "executed": False,
                "performance_claim": False,
                "non_signal": True,
                "phase": prof.current_phase,
                "status": "calibration_contract_placeholder_only",
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_calibration_evaluation_placeholders(df)
    return df, summary


def summarize_calibration_evaluation_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize calibration evaluation placeholders DataFrame."""
    return {
        "total_evaluations": len(df),
        "evaluations": df["evaluation_name"].tolist() if not df.empty else [],
        "all_unexecuted": bool((~df["executed"]).all()) if not df.empty else True,
        "all_zero_performance_claim": bool((~df["performance_claim"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
