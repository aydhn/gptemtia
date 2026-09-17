"""Drift Retraining Trigger Disabled Enforcer for Phase 142.

Enforces strict non-executing safety boundary preventing automated retraining triggers,
model refitting jobs, or pipeline re-execution upon contract breach detection.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict

from advanced_model_drift_monitoring.model_drift_models import DriftDisabledExecutionItem


def build_drift_retraining_trigger_disabled_item() -> DriftDisabledExecutionItem:
    """Builds the disabled execution item for automated retraining triggers."""
    return DriftDisabledExecutionItem(
        execution_id="dis_exec_retrain_003",
        execution_type="drift_retraining_trigger_disabled",
        target_component="drift_retraining_orchestrator",
        status="active_enforcement",
        is_disabled=True,
        disabled_reason="Automated model retraining triggers are strictly forbidden in Phase 142.",
        remediation_required="Do not invoke automated training pipelines, background retrain jobs, or GPU workers.",
        metadata={
            "blocked_actions": ["auto_retrain", "refit_models", "pipeline_trigger", "schedule_fit"],
            "allow_placeholders_only": True,
            "phase": 142,
        },
    )


def assert_drift_retraining_trigger_disabled(request_params: Dict[str, Any]) -> Dict[str, Any]:
    """Validates that a request does not attempt automated retraining triggers.

    Raises RuntimeError if retraining trigger is requested.
    """
    if request_params.get("trigger_retraining", False) or request_params.get("auto_refit", False) or request_params.get("execute_pipeline_retrain", False):
        raise RuntimeError(
            "CRITICAL SAFETY VIOLATION: Automated retraining triggers are strictly disabled in Phase 142 offline research contracts."
        )

    return {
        "status": "passed",
        "retraining_trigger_blocked": True,
        "item": asdict(build_drift_retraining_trigger_disabled_item()),
    }
