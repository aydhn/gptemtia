# -*- coding: utf-8 -*-
"""Phase 155: Risk Reporting Safety Boundary Module."""

from typing import Any, Dict, List, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile


NO_GO_CONDITIONS = [
    "live_trading",
    "broker_integration",
    "real_order_generation",
    "investment_advice",
    "signal_generation",
    "risk_reporting_execution",
    "exposure_attribution_execution",
    "limit_monitoring_execution",
    "metric_calculation",
    "var_calculation",
    "expected_shortfall_calculation",
    "exposure_calculation",
    "limit_breach_generation",
    "alert_generation",
    "dashboard_generation",
    "portfolio_adjustment",
    "rebalance_generation",
    "model_training",
    "model_prediction",
    "target_label_generation",
    "model_registry_write",
    "production_deployment",
    "scraping",
    "credential_output",
    "source_overwrite",
]

SAFE_GO_CONDITIONS = [
    "local_offline_risk_report_contracts",
    "exposure_attribution_contracts",
    "limit_monitoring_contracts",
    "portfolio_risk_summary_contracts",
    "portfolio_exposure_summary_contracts",
    "exposure_placeholders",
    "risk_contribution_placeholders",
    "drawdown_volatility_var_es_monitors",
    "limit_definition_and_monitoring_contracts",
    "limit_breach_warning_alert_placeholders",
    "alert_routing_disabled_registry",
    "dashboard_placeholders",
    "output_contracts",
    "risk_metric_placeholders",
    "dependency_registries",
    "no_lookahead_claim_guards",
    "metadata_only_news_source_preservation",
    "disabled_execution_reports",
    "findings_manifest_readiness",
    "health_validation_safety_reports",
    "phase_156_handoff",
]


def build_risk_reporting_no_go_conditions(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of strictly prohibited NO-GO conditions."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = []
    for cond in NO_GO_CONDITIONS:
        rows.append({
            "condition": cond,
            "status": "PROHIBITED",
            "enforcement": "HARD_BLOCK",
            "current_phase": profile.current_phase,
            "target_final_phase": profile.target_final_phase,
            "next_phase": profile.next_phase,
        })
    df = pd.DataFrame(rows)
    return df, {"no_go_count": len(df), "all_blocked": True}


def build_risk_reporting_safe_go_conditions(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of permitted SAFE-GO contract layer actions."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = []
    for cond in SAFE_GO_CONDITIONS:
        rows.append({
            "condition": cond,
            "status": "PERMITTED_CONTRACT_ONLY",
            "enforcement": "NON_EXECUTING_OFFLINE",
            "current_phase": profile.current_phase,
            "target_final_phase": profile.target_final_phase,
            "next_phase": profile.next_phase,
        })
    df = pd.DataFrame(rows)
    return df, {"safe_go_count": len(df), "all_contract_only": True}


def build_risk_reporting_safety_boundary(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build combined safety boundary report."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    df_no, s_no = build_risk_reporting_no_go_conditions(profile)
    df_safe, s_safe = build_risk_reporting_safe_go_conditions(profile)

    combined = pd.concat([df_no, df_safe], ignore_index=True)
    summary = {
        "no_go_count": s_no["no_go_count"],
        "safe_go_count": s_safe["safe_go_count"],
        "total_conditions": len(combined),
        "status": "SAFETY_BOUNDARY_ACTIVE",
        "current_phase": profile.current_phase,
        "target_final_phase": profile.target_final_phase,
        "next_phase": profile.next_phase,
    }
    return combined, summary
