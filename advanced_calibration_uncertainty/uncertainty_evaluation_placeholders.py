# -*- coding: utf-8 -*-
"""Phase 141: Uncertainty Evaluation Placeholders."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

UNCERTAINTY_EVALUATION_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "evaluation_name": "interval_coverage_evaluation_placeholder",
        "scope": "nominal_vs_empirical_coverage",
        "description": "Evaluates prediction interval coverage against nominal confidence levels; unexecuted.",
    },
    {
        "evaluation_name": "interval_efficiency_evaluation_placeholder",
        "scope": "mean_interval_width_efficiency",
        "description": "Evaluates sharpness and width of generated uncertainty bounds; unexecuted.",
    },
    {
        "evaluation_name": "conformal_validity_evaluation_placeholder",
        "scope": "finite_sample_marginal_coverage",
        "description": "Evaluates distribution-free finite sample coverage validity; unexecuted.",
    },
    {
        "evaluation_name": "ood_detection_evaluation_placeholder",
        "scope": "distribution_shift_sensitivity",
        "description": "Evaluates uncertainty response under synthetic distribution shifts; unexecuted.",
    },
]


def build_uncertainty_evaluation_placeholder_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for uncertainty evaluation placeholders."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for item in UNCERTAINTY_EVALUATION_PLACEHOLDERS:
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
    summary = summarize_uncertainty_evaluation_placeholders(df)
    return df, summary


def summarize_uncertainty_evaluation_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize uncertainty evaluation placeholders DataFrame."""
    return {
        "total_evaluations": len(df),
        "evaluations": df["evaluation_name"].tolist() if not df.empty else [],
        "all_unexecuted": bool((~df["executed"]).all()) if not df.empty else True,
        "all_zero_performance_claim": bool((~df["performance_claim"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
