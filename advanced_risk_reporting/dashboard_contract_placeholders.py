# -*- coding: utf-8 -*-
"""Phase 155: Dashboard Contract Placeholder Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import RiskReportingDisabledExecutionItem


def build_dashboard_contract_placeholder_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for dashboard contract placeholders."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        RiskReportingDisabledExecutionItem(
            component_name="risk_monitoring_dashboard",
            prohibited_actions=[
                "generate_dashboard",
                "launch_web_server",
                "render_live_ui",
                "stream_realtime_metrics",
            ],
            enforcement_mechanism="STRICT_SAFETY_GATE_DASHBOARD_GENERATION_DISABLED",
            is_disabled=True,
            status="execution_contract_only",
        ).model_dump()
    ]
    df = pd.DataFrame(rows)
    df["current_phase"] = profile.current_phase
    df["target_final_phase"] = profile.target_final_phase
    df["next_phase"] = profile.next_phase
    return df, {"is_disabled": True, "component_count": len(df)}
