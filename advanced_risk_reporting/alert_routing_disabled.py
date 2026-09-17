# -*- coding: utf-8 -*-
"""Phase 155: Alert Routing Disabled Safety Boundary Registry."""

from typing import Any, Dict, Tuple, Union
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import RiskReportingDisabledExecutionItem


def build_alert_routing_disabled_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary confirming alert routing is completely disabled."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        RiskReportingDisabledExecutionItem(
            component_name="alert_routing_engine",
            prohibited_actions=[
                "send_alert",
                "route_notification",
                "webhook_alert",
                "email_alert",
                "sms_alert",
                "pagerduty_alert",
                "slack_alert",
            ],
            enforcement_mechanism="STRICT_SAFETY_GATE_ALERT_ROUTING_DISABLED",
            is_disabled=True,
            status="execution_contract_only",
        ).model_dump()
    ]
    df = pd.DataFrame(rows)
    df["current_phase"] = profile.current_phase
    df["target_final_phase"] = profile.target_final_phase
    df["next_phase"] = profile.next_phase
    return df, {"is_disabled": True, "component_count": len(df)}


def validate_no_alert_routing_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that no alert routing or notification request is executed."""
    prohibited_terms = [
        "send_alert",
        "route_alert",
        "notification",
        "webhook",
        "email_alert",
        "slack_alert",
        "dispatch_alert",
        "trigger_alarm",
    ]
    text = str(request).lower()
    blocked = any(t in text for t in prohibited_terms)
    return {
        "is_blocked": blocked,
        "is_safe": not blocked,
        "action_taken": "BLOCKED_BY_SAFETY_POLICY" if blocked else "ALLOWED_CONTRACT_METADATA_ONLY",
        "reason": "Alert routing is strictly disabled in local/offline contract phase" if blocked else "No violation",
    }
