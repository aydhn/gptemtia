# -*- coding: utf-8 -*-
"""Phase 155: Exposure Attribution Execution Disabled Report."""

from typing import Any, Dict, Tuple, Union
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import RiskReportingDisabledExecutionItem


def build_exposure_attribution_execution_disabled_report(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary confirming exposure attribution execution is disabled."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        RiskReportingDisabledExecutionItem(
            component_name="exposure_attribution_engine",
            prohibited_actions=["calculate_exposure", "run_attribution", "execute_exposure_analysis"],
            enforcement_mechanism="STRICT_SAFETY_GATE_EXECUTION_BLOCKED",
            is_disabled=True,
            status="execution_contract_only",
        ).model_dump()
    ]
    df = pd.DataFrame(rows)
    df["current_phase"] = profile.current_phase
    df["target_final_phase"] = profile.target_final_phase
    df["next_phase"] = profile.next_phase
    return df, {"is_disabled": True, "status": "execution_blocked_no_exposure_attribution"}


def validate_no_exposure_attribution_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that request does not attempt exposure calculation."""
    prohibited = ["calculate_exposure", "run_attribution", "execute_exposure_analysis"]
    text = str(request).lower()
    blocked = any(p in text for p in prohibited)
    return {
        "is_blocked": blocked,
        "is_safe": not blocked,
        "action": "BLOCK" if blocked else "ALLOW",
        "reason": "Exposure attribution execution strictly disabled" if blocked else "No violation",
    }
