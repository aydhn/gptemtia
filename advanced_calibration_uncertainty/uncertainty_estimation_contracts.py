# -*- coding: utf-8 -*-
"""Phase 141: Uncertainty Estimation Contracts."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

UNCERTAINTY_CONTRACT_DEFINITIONS: List[Dict[str, Any]] = [
    {
        "contract_name": "prediction_interval_contract",
        "uncertainty_method_family": "residual_prediction_interval",
        "candidate_model_contract_ref": "linear_candidate_contract",
        "ensemble_contract_ref": "voting_ensemble_strategy_contract",
        "calibration_contract_ref": "platt_scaling_contract",
        "dataset_contract_ref": "commodity_fx_split_contract",
        "required_no_lookahead_guard_ref": "uncert_guard_no_lookahead_strict",
        "required_metadata_only_news_guard_ref": "uncert_guard_news_metadata_strict",
        "required_source_preservation_guard_ref": "uncert_guard_source_preservation_strict",
    },
    {
        "contract_name": "confidence_interval_contract",
        "uncertainty_method_family": "mean_parameter_confidence",
        "candidate_model_contract_ref": "linear_candidate_contract",
        "ensemble_contract_ref": "blending_ensemble_strategy_contract",
        "calibration_contract_ref": "temperature_scaling_contract",
        "dataset_contract_ref": "commodity_fx_split_contract",
        "required_no_lookahead_guard_ref": "uncert_guard_no_lookahead_strict",
        "required_metadata_only_news_guard_ref": "uncert_guard_news_metadata_strict",
        "required_source_preservation_guard_ref": "uncert_guard_source_preservation_strict",
    },
    {
        "contract_name": "quantile_interval_contract",
        "uncertainty_method_family": "pinball_quantile_regression",
        "candidate_model_contract_ref": "tree_ensemble_candidate_contract",
        "ensemble_contract_ref": "stacking_ensemble_strategy_contract",
        "calibration_contract_ref": "isotonic_calibration_contract",
        "dataset_contract_ref": "macro_event_split_contract",
        "required_no_lookahead_guard_ref": "uncert_guard_no_lookahead_strict",
        "required_metadata_only_news_guard_ref": "uncert_guard_news_metadata_strict",
        "required_source_preservation_guard_ref": "uncert_guard_source_preservation_strict",
    },
    {
        "contract_name": "conformal_prediction_contract",
        "uncertainty_method_family": "distribution_free_conformal",
        "candidate_model_contract_ref": "neural_candidate_contract",
        "ensemble_contract_ref": "blending_ensemble_strategy_contract",
        "calibration_contract_ref": "isotonic_calibration_contract",
        "dataset_contract_ref": "cross_asset_regime_split_contract",
        "required_no_lookahead_guard_ref": "uncert_guard_no_lookahead_strict",
        "required_metadata_only_news_guard_ref": "uncert_guard_news_metadata_strict",
        "required_source_preservation_guard_ref": "uncert_guard_source_preservation_strict",
    },
    {
        "contract_name": "bootstrap_uncertainty_contract",
        "uncertainty_method_family": "empirical_bootstrap_resampling",
        "candidate_model_contract_ref": "boosting_candidate_contract",
        "ensemble_contract_ref": "dynamic_weighting_ensemble_strategy_contract",
        "calibration_contract_ref": "beta_calibration_contract",
        "dataset_contract_ref": "commodity_fx_split_contract",
        "required_no_lookahead_guard_ref": "uncert_guard_no_lookahead_strict",
        "required_metadata_only_news_guard_ref": "uncert_guard_news_metadata_strict",
        "required_source_preservation_guard_ref": "uncert_guard_source_preservation_strict",
    },
    {
        "contract_name": "ensemble_variance_contract",
        "uncertainty_method_family": "model_disagreement_dispersion",
        "candidate_model_contract_ref": "tree_ensemble_candidate_contract",
        "ensemble_contract_ref": "voting_ensemble_strategy_contract",
        "calibration_contract_ref": "ensemble_calibration_contract",
        "dataset_contract_ref": "commodity_fx_split_contract",
        "required_no_lookahead_guard_ref": "uncert_guard_no_lookahead_strict",
        "required_metadata_only_news_guard_ref": "uncert_guard_news_metadata_strict",
        "required_source_preservation_guard_ref": "uncert_guard_source_preservation_strict",
    },
    {
        "contract_name": "monte_carlo_dropout_contract",
        "uncertainty_method_family": "epistemic_dropout_sampling",
        "candidate_model_contract_ref": "neural_candidate_contract",
        "ensemble_contract_ref": "stacking_ensemble_strategy_contract",
        "calibration_contract_ref": "temperature_scaling_contract",
        "dataset_contract_ref": "macro_event_split_contract",
        "required_no_lookahead_guard_ref": "uncert_guard_no_lookahead_strict",
        "required_metadata_only_news_guard_ref": "uncert_guard_news_metadata_strict",
        "required_source_preservation_guard_ref": "uncert_guard_source_preservation_strict",
    },
    {
        "contract_name": "bayesian_approximation_contract",
        "uncertainty_method_family": "variational_inference_approximation",
        "candidate_model_contract_ref": "neural_candidate_contract",
        "ensemble_contract_ref": "stacking_ensemble_strategy_contract",
        "calibration_contract_ref": "temperature_scaling_contract",
        "dataset_contract_ref": "cross_asset_regime_split_contract",
        "required_no_lookahead_guard_ref": "uncert_guard_no_lookahead_strict",
        "required_metadata_only_news_guard_ref": "uncert_guard_news_metadata_strict",
        "required_source_preservation_guard_ref": "uncert_guard_source_preservation_strict",
    },
]


def build_uncertainty_estimation_contract_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for all uncertainty estimation contracts."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for item in UNCERTAINTY_CONTRACT_DEFINITIONS:
        contract_data = {
            "contract_name": item["contract_name"],
            "uncertainty_method_family": item["uncertainty_method_family"],
            "candidate_model_contract_ref": item["candidate_model_contract_ref"],
            "ensemble_contract_ref": item["ensemble_contract_ref"],
            "calibration_contract_ref": item["calibration_contract_ref"],
            "dataset_contract_ref": item["dataset_contract_ref"],
            "required_no_lookahead_guard_ref": item["required_no_lookahead_guard_ref"],
            "required_metadata_only_news_guard_ref": item["required_metadata_only_news_guard_ref"],
            "required_source_preservation_guard_ref": item["required_source_preservation_guard_ref"],
            "uncertainty_estimation_allowed": False,
            "prediction_interval_allowed": False,
            "conformal_prediction_allowed": False,
            "quantile_prediction_allowed": False,
            "probability_prediction_allowed": False,
            "metric_calculation_allowed": False,
            "artifact_persistence_allowed": False,
            "signal_generation_allowed": False,
            "non_signal_required": True,
            "manual_review_required": True,
            "contract_status": "calibration_contract_ready",
            "phase": prof.current_phase,
        }
        validated = validate_uncertainty_estimation_contract(contract_data)
        rows.append(contract_data)

    df = pd.DataFrame(rows)
    summary = summarize_uncertainty_estimation_contracts(df)
    return df, summary


def validate_uncertainty_estimation_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Validate single uncertainty estimation contract ensuring zero execution."""
    violations = []
    if contract.get("uncertainty_estimation_allowed", False):
        violations.append("uncertainty_estimation_allowed must be False")
    if contract.get("prediction_interval_allowed", False):
        violations.append("prediction_interval_allowed must be False")
    if contract.get("conformal_prediction_allowed", False):
        violations.append("conformal_prediction_allowed must be False")
    if contract.get("quantile_prediction_allowed", False):
        violations.append("quantile_prediction_allowed must be False")
    if contract.get("signal_generation_allowed", False):
        violations.append("signal_generation_allowed must be False")
    if not contract.get("non_signal_required", True):
        violations.append("non_signal_required must be True")

    return {
        "is_valid": len(violations) == 0,
        "contract_name": contract.get("contract_name", "unknown"),
        "violations": violations,
    }


def summarize_uncertainty_estimation_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize uncertainty estimation contracts DataFrame."""
    return {
        "total_contracts": len(df),
        "contracts": df["contract_name"].tolist() if not df.empty else [],
        "all_zero_uncertainty": bool((~df["uncertainty_estimation_allowed"]).all()) if not df.empty else True,
        "all_zero_prediction_interval": bool((~df["prediction_interval_allowed"]).all()) if not df.empty else True,
        "all_zero_conformal": bool((~df["conformal_prediction_allowed"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal_required"].all()) if not df.empty else True,
        "all_manual_review": bool(df["manual_review_required"].all()) if not df.empty else True,
    }
