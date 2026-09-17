# -*- coding: utf-8 -*-
"""Phase 141: Probability Calibration Contracts."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

CALIBRATION_CONTRACT_DEFINITIONS: List[Dict[str, Any]] = [
    {
        "contract_name": "platt_scaling_contract",
        "calibration_method_family": "logistic_scaling",
        "candidate_model_contract_ref": "tree_ensemble_candidate_contract",
        "ensemble_contract_ref": "voting_ensemble_strategy_contract",
        "dataset_contract_ref": "commodity_fx_split_contract",
        "experiment_registry_ref": "exp_tree_ensemble_calib_001",
        "required_no_lookahead_guard_ref": "calib_guard_no_lookahead_strict",
        "required_metadata_only_news_guard_ref": "calib_guard_news_metadata_strict",
        "required_source_preservation_guard_ref": "calib_guard_source_preservation_strict",
        "required_validation_dependency_ref": "val_dep_phase_138_140",
        "required_quality_dependency_ref": "qual_dep_phase_138_140",
    },
    {
        "contract_name": "isotonic_calibration_contract",
        "calibration_method_family": "non_parametric_isotonic",
        "candidate_model_contract_ref": "neural_candidate_contract",
        "ensemble_contract_ref": "blending_ensemble_strategy_contract",
        "dataset_contract_ref": "macro_event_split_contract",
        "experiment_registry_ref": "exp_isotonic_calib_002",
        "required_no_lookahead_guard_ref": "calib_guard_no_lookahead_strict",
        "required_metadata_only_news_guard_ref": "calib_guard_news_metadata_strict",
        "required_source_preservation_guard_ref": "calib_guard_source_preservation_strict",
        "required_validation_dependency_ref": "val_dep_phase_138_140",
        "required_quality_dependency_ref": "qual_dep_phase_138_140",
    },
    {
        "contract_name": "temperature_scaling_contract",
        "calibration_method_family": "single_parameter_temperature",
        "candidate_model_contract_ref": "boosting_candidate_contract",
        "ensemble_contract_ref": "stacking_ensemble_strategy_contract",
        "dataset_contract_ref": "cross_asset_regime_split_contract",
        "experiment_registry_ref": "exp_temp_scaling_calib_003",
        "required_no_lookahead_guard_ref": "calib_guard_no_lookahead_strict",
        "required_metadata_only_news_guard_ref": "calib_guard_news_metadata_strict",
        "required_source_preservation_guard_ref": "calib_guard_source_preservation_strict",
        "required_validation_dependency_ref": "val_dep_phase_138_140",
        "required_quality_dependency_ref": "qual_dep_phase_138_140",
    },
    {
        "contract_name": "beta_calibration_contract",
        "calibration_method_family": "beta_distribution_scaling",
        "candidate_model_contract_ref": "linear_candidate_contract",
        "ensemble_contract_ref": "dynamic_weighting_ensemble_strategy_contract",
        "dataset_contract_ref": "commodity_fx_split_contract",
        "experiment_registry_ref": "exp_beta_calib_004",
        "required_no_lookahead_guard_ref": "calib_guard_no_lookahead_strict",
        "required_metadata_only_news_guard_ref": "calib_guard_news_metadata_strict",
        "required_source_preservation_guard_ref": "calib_guard_source_preservation_strict",
        "required_validation_dependency_ref": "val_dep_phase_138_140",
        "required_quality_dependency_ref": "qual_dep_phase_138_140",
    },
    {
        "contract_name": "histogram_binning_contract",
        "calibration_method_family": "binned_empirical_mass",
        "candidate_model_contract_ref": "kernel_candidate_contract",
        "ensemble_contract_ref": "voting_ensemble_strategy_contract",
        "dataset_contract_ref": "commodity_fx_split_contract",
        "experiment_registry_ref": "exp_hist_binning_calib_005",
        "required_no_lookahead_guard_ref": "calib_guard_no_lookahead_strict",
        "required_metadata_only_news_guard_ref": "calib_guard_news_metadata_strict",
        "required_source_preservation_guard_ref": "calib_guard_source_preservation_strict",
        "required_validation_dependency_ref": "val_dep_phase_138_140",
        "required_quality_dependency_ref": "qual_dep_phase_138_140",
    },
    {
        "contract_name": "ensemble_calibration_contract",
        "calibration_method_family": "multi_calibrator_consensus",
        "candidate_model_contract_ref": "tree_ensemble_candidate_contract",
        "ensemble_contract_ref": "stacking_ensemble_strategy_contract",
        "dataset_contract_ref": "cross_asset_regime_split_contract",
        "experiment_registry_ref": "exp_ensemble_calib_006",
        "required_no_lookahead_guard_ref": "calib_guard_no_lookahead_strict",
        "required_metadata_only_news_guard_ref": "calib_guard_news_metadata_strict",
        "required_source_preservation_guard_ref": "calib_guard_source_preservation_strict",
        "required_validation_dependency_ref": "val_dep_phase_138_140",
        "required_quality_dependency_ref": "qual_dep_phase_138_140",
    },
    {
        "contract_name": "future_phase_141_contract_only_calibration",
        "calibration_method_family": "contract_only_placeholder",
        "candidate_model_contract_ref": "neural_candidate_contract",
        "ensemble_contract_ref": "blending_ensemble_strategy_contract",
        "dataset_contract_ref": "macro_event_split_contract",
        "experiment_registry_ref": "exp_future_calib_007",
        "required_no_lookahead_guard_ref": "calib_guard_no_lookahead_strict",
        "required_metadata_only_news_guard_ref": "calib_guard_news_metadata_strict",
        "required_source_preservation_guard_ref": "calib_guard_source_preservation_strict",
        "required_validation_dependency_ref": "val_dep_phase_138_140",
        "required_quality_dependency_ref": "qual_dep_phase_138_140",
    },
]


def build_probability_calibration_contract_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for all probability calibration contracts."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for item in CALIBRATION_CONTRACT_DEFINITIONS:
        contract_data = {
            "contract_name": item["contract_name"],
            "calibration_method_family": item["calibration_method_family"],
            "candidate_model_contract_ref": item["candidate_model_contract_ref"],
            "ensemble_contract_ref": item["ensemble_contract_ref"],
            "dataset_contract_ref": item["dataset_contract_ref"],
            "experiment_registry_ref": item["experiment_registry_ref"],
            "required_no_lookahead_guard_ref": item["required_no_lookahead_guard_ref"],
            "required_metadata_only_news_guard_ref": item["required_metadata_only_news_guard_ref"],
            "required_source_preservation_guard_ref": item["required_source_preservation_guard_ref"],
            "required_validation_dependency_ref": item["required_validation_dependency_ref"],
            "required_quality_dependency_ref": item["required_quality_dependency_ref"],
            "probability_prediction_allowed": False,
            "calibration_fit_allowed": False,
            "calibration_transform_allowed": False,
            "metric_calculation_allowed": False,
            "artifact_persistence_allowed": False,
            "model_registry_write_allowed": False,
            "signal_generation_allowed": False,
            "non_signal_required": True,
            "manual_review_required": True,
            "contract_status": "calibration_contract_ready",
            "phase": prof.current_phase,
        }
        validated = validate_probability_calibration_contract(contract_data)
        rows.append(contract_data)

    df = pd.DataFrame(rows)
    summary = summarize_probability_calibration_contracts(df)
    return df, summary


def validate_probability_calibration_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Validate a single calibration contract ensuring all execution flags are False."""
    violations = []
    if contract.get("probability_prediction_allowed", False):
        violations.append("probability_prediction_allowed must be False")
    if contract.get("calibration_fit_allowed", False):
        violations.append("calibration_fit_allowed must be False")
    if contract.get("calibration_transform_allowed", False):
        violations.append("calibration_transform_allowed must be False")
    if contract.get("metric_calculation_allowed", False):
        violations.append("metric_calculation_allowed must be False")
    if contract.get("artifact_persistence_allowed", False):
        violations.append("artifact_persistence_allowed must be False")
    if contract.get("signal_generation_allowed", False):
        violations.append("signal_generation_allowed must be False")
    if not contract.get("non_signal_required", True):
        violations.append("non_signal_required must be True")

    return {
        "is_valid": len(violations) == 0,
        "contract_name": contract.get("contract_name", "unknown"),
        "violations": violations,
    }


def summarize_probability_calibration_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize probability calibration contracts DataFrame."""
    return {
        "total_contracts": len(df),
        "contracts": df["contract_name"].tolist() if not df.empty else [],
        "all_zero_prediction": bool((~df["probability_prediction_allowed"]).all()) if not df.empty else True,
        "all_zero_fit": bool((~df["calibration_fit_allowed"]).all()) if not df.empty else True,
        "all_zero_transform": bool((~df["calibration_transform_allowed"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal_required"].all()) if not df.empty else True,
        "all_manual_review": bool(df["manual_review_required"].all()) if not df.empty else True,
    }
