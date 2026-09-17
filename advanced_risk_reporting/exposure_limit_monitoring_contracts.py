# -*- coding: utf-8 -*-
"""Phase 155: Exposure Limit Monitoring Contracts Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import LimitMonitoringContract


def build_exposure_limit_monitoring_contract_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for exposure limit monitoring contracts."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        LimitMonitoringContract(
            contract_name="gross_exposure_limit_monitoring",
            limit_family="gross_exposure",
            description="Brut exposure tavan siniri izleme sozlesmesi",
            limit_type="hard_limit",
            threshold_metadata="gross_exposure <= 1.5",
            is_placeholder=True,
            is_enforced_live=False,
            allows_execution=False,
            allows_alerting=False,
        ).model_dump(),
        LimitMonitoringContract(
            contract_name="net_exposure_limit_monitoring",
            limit_family="net_exposure",
            description="Net exposure bandi izleme sozlesmesi",
            limit_type="hard_limit",
            threshold_metadata="net_exposure in [-0.5, 0.5]",
            is_placeholder=True,
            is_enforced_live=False,
            allows_execution=False,
            allows_alerting=False,
        ).model_dump(),
    ]
    df = pd.DataFrame(rows)
    df["current_phase"] = profile.current_phase
    df["target_final_phase"] = profile.target_final_phase
    df["next_phase"] = profile.next_phase
    return df, {"contract_count": len(df), "is_enforced_live": False}
