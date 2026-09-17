# -*- coding: utf-8 -*-
"""Phase 141: Calibration Method Placeholders."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

CALIBRATION_METHOD_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "method_name": "platt_scaling_method_placeholder",
        "method_family": "logistic_scaling",
        "description": "Sigmoid fitting over uncalibrated margins; non-executing placeholder.",
        "is_parametric": True,
        "requires_optimization": True,
    },
    {
        "method_name": "isotonic_regression_method_placeholder",
        "method_family": "non_parametric_isotonic",
        "description": "Piecewise constant non-decreasing fit; non-executing placeholder.",
        "is_parametric": False,
        "requires_optimization": True,
    },
    {
        "method_name": "temperature_scaling_method_placeholder",
        "method_family": "single_parameter_temperature",
        "description": "Single scalar temperature parameter scaling logits; non-executing placeholder.",
        "is_parametric": True,
        "requires_optimization": True,
    },
    {
        "method_name": "beta_calibration_method_placeholder",
        "method_family": "beta_distribution_scaling",
        "description": "Beta distribution scaling for skewed model scores; non-executing placeholder.",
        "is_parametric": True,
        "requires_optimization": True,
    },
    {
        "method_name": "histogram_binning_method_placeholder",
        "method_family": "binned_empirical_mass",
        "description": "Fixed or quantile bin partitioning; non-executing placeholder.",
        "is_parametric": False,
        "requires_optimization": False,
    },
    {
        "method_name": "ensemble_calibration_method_placeholder",
        "method_family": "multi_calibrator_consensus",
        "description": "Consensus combination across multiple calibrators; non-executing placeholder.",
        "is_parametric": False,
        "requires_optimization": True,
    },
    {
        "method_name": "spline_calibration_method_placeholder",
        "method_family": "spline_smoothing",
        "description": "Smooth spline fitting over score quantiles; non-executing placeholder.",
        "is_parametric": False,
        "requires_optimization": True,
    },
]


def build_calibration_method_placeholder_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for all calibration method placeholders."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for item in CALIBRATION_METHOD_PLACEHOLDERS:
        rows.append(
            {
                "method_name": item["method_name"],
                "method_family": item["method_family"],
                "description": item["description"],
                "is_parametric": item["is_parametric"],
                "requires_optimization": item["requires_optimization"],
                "execution_blocked": True,
                "fit_blocked": True,
                "transform_blocked": True,
                "non_signal": True,
                "phase": prof.current_phase,
                "status": "calibration_contract_placeholder_only",
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_calibration_method_placeholders(df)
    return df, summary


def summarize_calibration_method_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize calibration method placeholders DataFrame."""
    return {
        "total_methods": len(df),
        "methods": df["method_name"].tolist() if not df.empty else [],
        "all_execution_blocked": bool(df["execution_blocked"].all()) if not df.empty else True,
        "all_fit_blocked": bool(df["fit_blocked"].all()) if not df.empty else True,
        "all_transform_blocked": bool(df["transform_blocked"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
