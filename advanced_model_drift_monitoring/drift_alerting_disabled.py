"""Drift Alerting Disabled Enforcer for Phase 142.

Enforces strict non-executing safety boundary preventing live alerting,
webhook calls, email dispatches, or notification channel broadcasting.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict

from advanced_model_drift_monitoring.model_drift_models import DriftDisabledExecutionItem


def build_drift_alerting_disabled_item() -> DriftDisabledExecutionItem:
    """Builds the disabled execution item for drift alerting."""
    return DriftDisabledExecutionItem(
        execution_id="dis_exec_alerting_002",
        execution_type="drift_alerting_disabled",
        target_component="drift_alerting_service",
        status="active_enforcement",
        is_disabled=True,
        disabled_reason="Live drift alerting and notification dispatch are strictly forbidden in Phase 142.",
        remediation_required="Do not invoke alert dispatchers, email hooks, or webhook endpoints.",
        metadata={
            "blocked_channels": ["slack", "email", "webhook", "pagerduty", "sms"],
            "allow_placeholders_only": True,
            "phase": 142,
        },
    )


def assert_drift_alerting_disabled(request_params: Dict[str, Any]) -> Dict[str, Any]:
    """Validates that a request does not attempt live alert dispatch.

    Raises RuntimeError if alerting is requested.
    """
    if request_params.get("send_alert", False) or request_params.get("dispatch_notification", False) or request_params.get("trigger_webhook", False):
        raise RuntimeError(
            "CRITICAL SAFETY VIOLATION: Live drift alerting is strictly disabled in Phase 142 offline research contracts."
        )

    return {
        "status": "passed",
        "alerting_blocked": True,
        "item": asdict(build_drift_alerting_disabled_item()),
    }
