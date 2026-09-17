# -*- coding: utf-8 -*-
"""Phase 155: Risk Alert Placeholder Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import LimitMonitoringPlaceholder


def build_risk_alert_placeholder_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for risk alert placeholders."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        LimitMonitoringPlaceholder(
            placeholder_name="general_risk_alert_placeholder",
            limit_type="risk_alert",
            description="Genel risk bildirim sozlesme yer tutucusu (canli alarm kapali)",
            is_placeholder=True,
            is_enforced=False,
        ).model_dump()
    ]
    df = pd.DataFrame(rows)
    df["current_phase"] = profile.current_phase
    df["target_final_phase"] = profile.target_final_phase
    df["next_phase"] = profile.next_phase
    return df, {"placeholder_count": len(df), "is_enforced": False}
