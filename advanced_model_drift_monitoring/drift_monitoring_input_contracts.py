"""Drift Monitoring Input Contracts for Phase 142.

Specifies and validates schema contracts for drift monitoring inputs:
reference windows, current evaluation windows, candidate model identifiers,
feature namespace references, and calibration metadata.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, List

from advanced_model_drift_monitoring.model_drift_models import DriftMonitoringContract


def build_drift_monitoring_input_contracts() -> List[DriftMonitoringContract]:
    """Builds standard drift monitoring input contracts."""
    contracts = [
        DriftMonitoringContract(
            contract_id="input_contract_reference_dataset",
            domain="data_drift",
            target_name="reference_dataset_manifest",
            contract_version="1.0.0",
            status="active",
            execution_mode="non_executing_contract",
            reference_window="win_ref_in_sample_baseline",
            current_window=None,
            threshold_policy=None,
            linkage_target="Phase 137 ML Dataset Contracts",
            rules={
                "required_fields": ["dataset_id", "feature_columns", "date_range", "sample_size"],
                "allowed_types": {"dataset_id": "str", "sample_size": "int"},
                "disallow_forward_labels": True,
            },
            metadata={"input_category": "reference_data"},
        ),
        DriftMonitoringContract(
            contract_id="input_contract_current_window_dataset",
            domain="data_drift",
            target_name="current_window_manifest",
            contract_version="1.0.0",
            status="active",
            execution_mode="non_executing_contract",
            reference_window=None,
            current_window="win_curr_short_term_eval",
            threshold_policy=None,
            linkage_target="Phase 137 ML Dataset Contracts",
            rules={
                "required_fields": ["window_id", "feature_columns", "start_date", "end_date"],
                "disallow_forward_labels": True,
            },
            metadata={"input_category": "current_data"},
        ),
        DriftMonitoringContract(
            contract_id="input_contract_candidate_model_metadata",
            domain="model_drift",
            target_name="candidate_model_manifest",
            contract_version="1.0.0",
            status="active",
            execution_mode="non_executing_contract",
            reference_window="win_ref_validation_baseline",
            current_window="win_curr_medium_term_eval",
            threshold_policy=None,
            linkage_target="Phase 138/140 Candidate Model Registry",
            rules={
                "required_fields": ["candidate_id", "family", "features_used", "status"],
                "allowed_statuses": ["registered", "candidate", "benchmarked"],
            },
            metadata={"input_category": "model_metadata"},
        ),
    ]
    return contracts


def validate_drift_monitoring_input(input_data: Dict[str, Any]) -> Dict[str, Any]:
    """Validates an input dictionary against input contract requirements."""
    errors = []
    if not isinstance(input_data, dict):
        return {"valid": False, "errors": ["Input data must be a dictionary."]}

    if "target_name" not in input_data:
        errors.append("Missing required field: 'target_name'.")

    # Guard against forward-looking or prediction labels in input contract
    forbidden_keys = {"target_forward", "future_price", "actual_future_return", "order_action"}
    for key in forbidden_keys:
        if key in input_data:
            errors.append(f"Forbidden forward-looking or execution key in input: '{key}'.")

    return {
        "valid": len(errors) == 0,
        "input_target": input_data.get("target_name"),
        "errors": errors,
    }
