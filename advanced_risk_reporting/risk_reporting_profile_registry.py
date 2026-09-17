# -*- coding: utf-8 -*-
"""Phase 155: Risk Reporting Profile Registry."""

from typing import Any, Dict, List, Tuple
import pandas as pd

from .risk_reporting_config import (
    RiskReportingProfile,
    list_risk_reporting_profiles,
    get_default_risk_reporting_profile,
)
from .risk_reporting_models import RiskReportingProfileItem


def build_risk_reporting_profile_registry(
    active_profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary of registered risk reporting profiles."""
    if active_profile is None:
        active_profile = get_default_risk_reporting_profile()

    profiles = list_risk_reporting_profiles(enabled_only=True)
    rows: List[Dict[str, Any]] = []

    for p in profiles:
        item = RiskReportingProfileItem(
            profile_name=p.profile_name,
            description=p.description,
            current_phase=p.current_phase,
            target_final_phase=p.target_final_phase,
            next_phase=p.next_phase,
            dry_run_default=p.dry_run_default,
            local_only=p.local_only,
            non_production=p.non_production,
            research_only=p.research_only,
            allow_live_trading=p.allow_live_trading,
            allow_broker_integration=p.allow_broker_integration,
            allow_real_order=p.allow_real_order,
            allow_investment_advice=p.allow_investment_advice,
            allow_signal_generation=p.allow_signal_generation,
            allow_risk_reporting_execution=p.allow_risk_reporting_execution,
            allow_exposure_attribution_execution=p.allow_exposure_attribution_execution,
            allow_limit_monitoring_execution=p.allow_limit_monitoring_execution,
            allow_metric_calculation=p.allow_metric_calculation,
            min_readiness_score=p.min_readiness_score,
        )
        data = item.model_dump()
        data["is_active"] = (p.profile_name == active_profile.profile_name)
        rows.append(data)

    df = pd.DataFrame(rows)
    summary = summarize_risk_reporting_profiles(df, active_profile)
    return df, summary


def summarize_risk_reporting_profiles(
    df: pd.DataFrame, active_profile: RiskReportingProfile
) -> Dict[str, Any]:
    """Produce summary dictionary for profile registry."""
    return {
        "total_profiles": len(df),
        "profile_count": len(df),
        "active_profile": active_profile.profile_name,
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "all_profiles_non_production": bool(df["non_production"].all()) if not df.empty else True,
        "all_profiles_dry_run": bool(df["dry_run_default"].all()) if not df.empty else True,
        "all_profiles_local_only": bool(df["local_only"].all()) if not df.empty else True,
        "zero_live_trading": bool((df["allow_live_trading"] == False).all()) if not df.empty else True,
        "zero_broker_integration": bool((df["allow_broker_integration"] == False).all()) if not df.empty else True,
        "zero_execution": bool((df["allow_risk_reporting_execution"] == False).all()) if not df.empty else True,
    }
