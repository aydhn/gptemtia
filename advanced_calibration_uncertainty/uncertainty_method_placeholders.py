# -*- coding: utf-8 -*-
"""Phase 141: Uncertainty Method Placeholders."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

UNCERTAINTY_METHOD_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "method_name": "prediction_interval_method_placeholder",
        "method_family": "residual_prediction_interval",
        "description": "Standard error of prediction intervals; non-executing placeholder.",
        "is_bayesian": False,
        "requires_resampling": False,
    },
    {
        "method_name": "confidence_interval_method_placeholder",
        "method_family": "mean_parameter_confidence",
        "description": "Parameter estimation confidence intervals; non-executing placeholder.",
        "is_bayesian": False,
        "requires_resampling": False,
    },
    {
        "method_name": "quantile_regression_method_placeholder",
        "method_family": "pinball_quantile_regression",
        "description": "Conditional quantile loss estimation; non-executing placeholder.",
        "is_bayesian": False,
        "requires_resampling": False,
    },
    {
        "method_name": "conformal_prediction_method_placeholder",
        "method_family": "distribution_free_conformal",
        "description": "Conformalized quantile calibration set; non-executing placeholder.",
        "is_bayesian": False,
        "requires_resampling": False,
    },
    {
        "method_name": "bootstrap_uncertainty_method_placeholder",
        "method_family": "empirical_bootstrap_resampling",
        "description": "Bootstrap resampling over training data; non-executing placeholder.",
        "is_bayesian": False,
        "requires_resampling": True,
    },
    {
        "method_name": "ensemble_variance_method_placeholder",
        "method_family": "model_disagreement_dispersion",
        "description": "Candidate model disagreement spread; non-executing placeholder.",
        "is_bayesian": False,
        "requires_resampling": False,
    },
    {
        "method_name": "monte_carlo_dropout_method_placeholder",
        "method_family": "epistemic_dropout_sampling",
        "description": "Stochastic forward passes with dropout; non-executing placeholder.",
        "is_bayesian": True,
        "requires_resampling": True,
    },
    {
        "method_name": "bayesian_approximation_method_placeholder",
        "method_family": "variational_inference_approximation",
        "description": "Variational posterior approximation; non-executing placeholder.",
        "is_bayesian": True,
        "requires_resampling": False,
    },
]


def build_uncertainty_method_placeholder_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for all uncertainty method placeholders."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for item in UNCERTAINTY_METHOD_PLACEHOLDERS:
        rows.append(
            {
                "method_name": item["method_name"],
                "method_family": item["method_family"],
                "description": item["description"],
                "is_bayesian": item["is_bayesian"],
                "requires_resampling": item["requires_resampling"],
                "execution_blocked": True,
                "estimation_blocked": True,
                "non_signal": True,
                "phase": prof.current_phase,
                "status": "calibration_contract_placeholder_only",
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_uncertainty_method_placeholders(df)
    return df, summary


def summarize_uncertainty_method_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize uncertainty method placeholders DataFrame."""
    return {
        "total_methods": len(df),
        "methods": df["method_name"].tolist() if not df.empty else [],
        "all_execution_blocked": bool(df["execution_blocked"].all()) if not df.empty else True,
        "all_estimation_blocked": bool(df["estimation_blocked"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
