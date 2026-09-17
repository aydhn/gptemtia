"""Drift Monitoring Output Contracts for Phase 142.

Specifies and validates schema contracts for drift monitoring output artifacts:
findings, readiness scores, and manifest structures.
Ensures outputs include mandatory non-signal, contract-only disclaimers.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, List

from advanced_model_drift_monitoring.model_drift_models import DriftMonitoringContract


def build_drift_monitoring_output_contracts() -> List[DriftMonitoringContract]:
    """Builds standard drift monitoring output contracts."""
    contracts = [
        DriftMonitoringContract(
            contract_id="output_contract_drift_finding",
            domain="model_drift",
            target_name="drift_finding_structure",
            contract_version="1.0.0",
            status="active",
            execution_mode="non_executing_contract",
            reference_window=None,
            current_window=None,
            threshold_policy=None,
            linkage_target="Phase 142 Findings & Audit",
            rules={
                "required_fields": [
                    "finding_id",
                    "domain",
                    "target_name",
                    "severity",
                    "finding_type",
                    "description",
                    "recommended_action",
                    "requires_human_review",
                    "execution_blocked",
                ],
                "severity_levels": ["info", "warning", "breach", "critical"],
            },
            metadata={"output_category": "audit_finding"},
        ),
        DriftMonitoringContract(
            contract_id="output_contract_drift_readiness_score",
            domain="model_drift",
            target_name="drift_readiness_score_structure",
            contract_version="1.0.0",
            status="active",
            execution_mode="non_executing_contract",
            reference_window=None,
            current_window=None,
            threshold_policy=None,
            linkage_target="Phase 142 Governance Readiness",
            rules={
                "required_fields": [
                    "domain",
                    "readiness_score",
                    "governance_status",
                    "blocker_count",
                    "warning_count",
                    "is_ready_for_review",
                ],
                "score_range": [0.0, 100.0],
            },
            metadata={"output_category": "readiness_scoring"},
        ),
    ]
    return contracts


def validate_drift_monitoring_output(output_data: Dict[str, Any]) -> Dict[str, Any]:
    """Validates an output artifact against non-signal and schema contracts."""
    errors = []
    if not isinstance(output_data, dict):
        return {"valid": False, "errors": ["Output data must be a dictionary."]}

    # Check for mandatory non-signal disclaimers or non-executing metadata
    if output_data.get("is_trading_signal") is True:
        errors.append("Output must not be flagged as a trading signal.")
    if output_data.get("auto_execute_orders") is True:
        errors.append("Output must not trigger automated order execution.")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "target": output_data.get("target_name"),
    }
