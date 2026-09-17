"""Drift Model Action Disabled Enforcer for Phase 142.

Enforces strict non-executing safety boundary preventing automated model deactivation,
traffic shifting, candidate model hot-swapping, or registry modifications.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict

from advanced_model_drift_monitoring.model_drift_models import DriftDisabledExecutionItem


def build_drift_model_action_disabled_item() -> DriftDisabledExecutionItem:
    """Builds the disabled execution item for automated model action."""
    return DriftDisabledExecutionItem(
        execution_id="dis_exec_model_action_004",
        execution_type="drift_model_action_disabled",
        target_component="model_lifecycle_controller",
        status="active_enforcement",
        is_disabled=True,
        disabled_reason="Automated model deactivation, switching, and registry mutations are strictly forbidden in Phase 142.",
        remediation_required="Model retirement or replacement requires explicit human review and manual governance.",
        metadata={
            "blocked_actions": ["auto_deactivate", "switch_traffic", "hot_swap", "deprecate_candidate"],
            "allow_placeholders_only": True,
            "phase": 142,
        },
    )


def assert_drift_model_action_disabled(request_params: Dict[str, Any]) -> Dict[str, Any]:
    """Validates that a request does not attempt automated model actions.

    Raises RuntimeError if automated model mutation is requested.
    """
    if request_params.get("deactivate_model", False) or request_params.get("switch_candidate", False) or request_params.get("hot_swap_model", False):
        raise RuntimeError(
            "CRITICAL SAFETY VIOLATION: Automated model actions are strictly disabled in Phase 142 offline research contracts."
        )

    return {
        "status": "passed",
        "model_action_blocked": True,
        "item": asdict(build_drift_model_action_disabled_item()),
    }
