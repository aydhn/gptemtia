# -*- coding: utf-8 -*-
"""Phase 143: Explainability Report Contracts."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_explainability_report_contract_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of explainability report contracts."""
    prof = profile or get_explainability_profile()

    contracts_data = [
        (
            "global_explainability_report_contract",
            "global_explanation",
            "candidate_baseline_all_v1",
            "ensemble_voting_blending_v1",
            "dataset_contract_regime_features_v1",
            "featurestore_catalog_v1",
            "drift_contract_feature_distribution_v1",
            "calibration_contract_isotonic_platt_v1",
            "guard_no_lookahead_v1",
            "guard_metadata_only_news_v1",
            "guard_source_preservation_v1",
        ),
        (
            "local_explainability_report_contract",
            "local_explanation",
            "candidate_baseline_instance_v1",
            "ensemble_candidate_instance_v1",
            "dataset_contract_instance_v1",
            "featurestore_catalog_v1",
            "drift_contract_instance_v1",
            "uncertainty_contract_conformal_v1",
            "guard_no_lookahead_v1",
            "guard_metadata_only_news_v1",
            "guard_source_preservation_v1",
        ),
        (
            "candidate_model_explainability_report_contract",
            "candidate_model_explanation",
            "candidate_model_registry_v1",
            "ensemble_not_applicable",
            "dataset_contract_training_v1",
            "featurestore_catalog_v1",
            "drift_contract_candidate_v1",
            "calibration_contract_candidate_v1",
            "guard_no_lookahead_v1",
            "guard_metadata_only_news_v1",
            "guard_source_preservation_v1",
        ),
        (
            "ensemble_explainability_report_contract",
            "ensemble_model_explanation",
            "candidate_model_components_v1",
            "ensemble_strategy_contracts_v1",
            "dataset_contract_ensemble_v1",
            "featurestore_catalog_v1",
            "drift_contract_ensemble_v1",
            "calibration_contract_ensemble_v1",
            "guard_no_lookahead_v1",
            "guard_metadata_only_news_v1",
            "guard_source_preservation_v1",
        ),
        (
            "drift_linked_explainability_report_contract",
            "drift_attribution_shift_explanation",
            "candidate_drift_monitored_v1",
            "ensemble_drift_monitored_v1",
            "dataset_contract_drift_window_v1",
            "featurestore_catalog_v1",
            "model_drift_monitoring_contract_v1",
            "calibration_drift_contract_v1",
            "guard_no_lookahead_v1",
            "guard_metadata_only_news_v1",
            "guard_source_preservation_v1",
        ),
        (
            "calibration_uncertainty_explainability_report_contract",
            "calibration_uncertainty_explanation",
            "candidate_calibrated_v1",
            "ensemble_calibrated_v1",
            "dataset_contract_calibration_v1",
            "featurestore_catalog_v1",
            "drift_contract_uncertainty_v1",
            "uncertainty_estimation_contract_v1",
            "guard_no_lookahead_v1",
            "guard_metadata_only_news_v1",
            "guard_source_preservation_v1",
        ),
        (
            "model_governance_explainability_report_contract",
            "model_governance_explanation",
            "candidate_governance_set_v1",
            "ensemble_governance_set_v1",
            "dataset_contract_governance_v1",
            "featurestore_catalog_v1",
            "drift_contract_governance_v1",
            "calibration_contract_governance_v1",
            "guard_no_lookahead_v1",
            "guard_metadata_only_news_v1",
            "guard_source_preservation_v1",
        ),
    ]

    rows: List[Dict[str, Any]] = []
    for (
        name,
        fam,
        c_ref,
        e_ref,
        d_ref,
        fs_ref,
        dr_ref,
        cal_ref,
        look_ref,
        news_ref,
        src_ref,
    ) in contracts_data:
        rows.append({
            "contract_name": name,
            "explanation_family": fam,
            "candidate_model_contract_ref": c_ref,
            "ensemble_contract_ref": e_ref,
            "dataset_contract_ref": d_ref,
            "featurestore_contract_ref": fs_ref,
            "drift_contract_ref": dr_ref,
            "calibration_uncertainty_contract_ref": cal_ref,
            "required_no_lookahead_guard_ref": look_ref,
            "required_metadata_only_news_guard_ref": news_ref,
            "required_source_preservation_guard_ref": src_ref,
            "explainability_calculation_allowed": False,
            "attribution_calculation_allowed": False,
            "metric_calculation_allowed": False,
            "model_action_allowed": False,
            "signal_generation_allowed": False,
            "non_signal_required": True,
            "manual_review_required": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_explainability_report_contracts(df)
    return df, summary


def validate_explainability_report_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Validate a single explainability report contract dictionary."""
    is_valid = True
    issues: List[str] = []

    if not contract.get("contract_name"):
        is_valid = False
        issues.append("contract_name is required")

    if contract.get("explainability_calculation_allowed", True):
        is_valid = False
        issues.append("explainability_calculation_allowed must be False")

    if contract.get("attribution_calculation_allowed", True):
        is_valid = False
        issues.append("attribution_calculation_allowed must be False")

    if contract.get("signal_generation_allowed", True):
        is_valid = False
        issues.append("signal_generation_allowed must be False")

    if not contract.get("non_signal_required", False):
        is_valid = False
        issues.append("non_signal_required must be True")

    if contract.get("production_ready", False) or contract.get("broker_ready", False):
        is_valid = False
        issues.append("production_ready and broker_ready must be False")

    return {
        "contract_name": contract.get("contract_name", "unknown"),
        "is_valid": is_valid,
        "issues": issues,
        "non_signal": True,
    }


def summarize_explainability_report_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize explainability report contracts statistics."""
    total_contracts = len(df)
    all_zero_calculation = bool(
        (~df["explainability_calculation_allowed"]).all() and
        (~df["attribution_calculation_allowed"]).all()
    ) if not df.empty else True

    return {
        "total_contracts": total_contracts,
        "total_report_contracts": total_contracts,
        "all_zero_calculation": all_zero_calculation,
        "all_non_signal": bool(df["non_signal_required"].all()) if not df.empty else True,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }


# Convenience alias
build_explainability_report_contracts = build_explainability_report_contract_registry
