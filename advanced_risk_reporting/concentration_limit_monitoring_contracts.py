# -*- coding: utf-8 -*-
"""Phase 155: Concentration Limit Monitoring Contracts Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import LimitMonitoringContract


def build_concentration_limit_monitoring_contract_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for concentration limit monitoring contracts."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        LimitMonitoringContract(
            contract_name="single_asset_concentration_limit",
            limit_family="concentration_limit",
            description="Tekil varlik azami agirlik siniri",
            limit_type="hard_limit",
            threshold_metadata="max_single_weight <= 0.25",
            is_placeholder=True,
            is_enforced_live=False,
            allows_execution=False,
            allows_alerting=False,
        ).model_dump(),
        LimitMonitoringContract(
            contract_name="top3_asset_concentration_limit",
            limit_family="concentration_limit",
            description="Ilk 3 varlik toplam agirlik siniri",
            limit_type="hard_limit",
            threshold_metadata="top3_weight <= 0.60",
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
