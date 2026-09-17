# -*- coding: utf-8 -*-
"""Phase 155: Monitoring Schedule Placeholder Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import RiskReportingDisabledExecutionItem


def build_monitoring_schedule_placeholder_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for monitoring schedule placeholders."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        RiskReportingDisabledExecutionItem(
            component_name="cron_monitoring_scheduler",
            prohibited_actions=[
                "schedule_cron_job",
                "spawn_daemon_worker",
                "run_continuous_monitor_loop",
            ],
            enforcement_mechanism="STRICT_SAFETY_GATE_SCHEDULER_DISABLED",
            is_disabled=True,
            status="execution_contract_only",
        ).model_dump()
    ]
    df = pd.DataFrame(rows)
    df["current_phase"] = profile.current_phase
    df["target_final_phase"] = profile.target_final_phase
    df["next_phase"] = profile.next_phase
    return df, {"is_disabled": True, "component_count": len(df)}
