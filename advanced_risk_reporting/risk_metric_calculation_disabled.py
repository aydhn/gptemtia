# -*- coding: utf-8 -*-
"""Phase 155: Risk Metric Calculation Disabled Report."""

from typing import Any, Dict, Tuple, Union
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import RiskReportingDisabledExecutionItem


def build_risk_metric_calculation_disabled_report(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary confirming risk metric calculation is disabled."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        RiskReportingDisabledExecutionItem(
            component_name="risk_metric_calculator",
            prohibited_actions=[
                "calculate_var",
                "calculate_expected_shortfall",
                "calculate_volatility",
                "calculate_drawdown",
            ],
            enforcement_mechanism="STRICT_SAFETY_GATE_CALCULATION_BLOCKED",
            is_disabled=True,
            status="execution_contract_only",
        ).model_dump()
    ]
    df = pd.DataFrame(rows)
    df["current_phase"] = profile.current_phase
    df["target_final_phase"] = profile.target_final_phase
    df["next_phase"] = profile.next_phase
    return df, {"is_disabled": True, "status": "execution_blocked_no_metric_calculation"}


def validate_no_risk_metric_calculation_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that request does not attempt risk metric calculation."""
    prohibited = [
        "calculate_var",
        "calculate_expected_shortfall",
        "calculate_volatility",
        "calculate_drawdown",
        "calculate_metric",
    ]
    text = str(request).lower()
    blocked = any(p in text for p in prohibited)
    return {
        "is_blocked": blocked,
        "is_safe": not blocked,
        "action": "BLOCK" if blocked else "ALLOW",
        "reason": "Risk metric calculation strictly disabled" if blocked else "No violation",
    }
