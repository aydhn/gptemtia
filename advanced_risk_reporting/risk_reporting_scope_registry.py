# -*- coding: utf-8 -*-
"""Phase 155: Risk Reporting Scope Registry."""

from typing import Any, Dict, List, Tuple
import pandas as pd

from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile


def build_risk_reporting_scope_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary of Phase 155 scopes."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    scopes = [
        {"scope_name": "local_risk_report_contracts", "scope_type": "contract_layer", "is_in_scope": True, "notes": "Risk report templates and metadata definitions"},
        {"scope_name": "exposure_attribution_contracts", "scope_type": "contract_layer", "is_in_scope": True, "notes": "Gross/net/currency/cross-asset/concentration/liquidity/leverage templates"},
        {"scope_name": "limit_monitoring_contracts", "scope_type": "contract_layer", "is_in_scope": True, "notes": "Exposure/drawdown/volatility/turnover limit definitions"},
        {"scope_name": "monitor_placeholders", "scope_type": "placeholder_layer", "is_in_scope": True, "notes": "Drawdown/VaR/ES/risk contribution placeholders without actual computation"},
        {"scope_name": "limit_breach_placeholders", "scope_type": "placeholder_layer", "is_in_scope": True, "notes": "Limit breach and warning placeholders without live alerting"},
        {"scope_name": "alert_routing_disabled", "scope_type": "safety_boundary", "is_in_scope": True, "notes": "Alerting and notifications strictly disabled"},
        {"scope_name": "dashboard_placeholders", "scope_type": "placeholder_layer", "is_in_scope": True, "notes": "Dashboard contracts without live UI or server generation"},
        {"scope_name": "disabled_execution_reports", "scope_type": "safety_boundary", "is_in_scope": True, "notes": "Real execution blocked across all components"},
        {"scope_name": "claim_guards", "scope_type": "guard_layer", "is_in_scope": True, "notes": "No-lookahead, exposure claim, limit breach claim, investment advice guards"},
        {"scope_name": "phase_156_handoff", "scope_type": "handoff_layer", "is_in_scope": True, "notes": "Handoff to scenario testing and drawdown control"},
        {"scope_name": "real_risk_reporting", "scope_type": "out_of_scope", "is_in_scope": False, "notes": "Strictly prohibited in Phase 155"},
        {"scope_name": "real_limit_monitoring_loop", "scope_type": "out_of_scope", "is_in_scope": False, "notes": "Strictly prohibited in Phase 155"},
        {"scope_name": "live_alert_notification", "scope_type": "out_of_scope", "is_in_scope": False, "notes": "Strictly prohibited in Phase 155"},
        {"scope_name": "portfolio_adjustment_rebalance", "scope_type": "out_of_scope", "is_in_scope": False, "notes": "Strictly prohibited in Phase 155"},
        {"scope_name": "live_trading_broker_orders", "scope_type": "out_of_scope", "is_in_scope": False, "notes": "Strictly prohibited in Phase 155"},
    ]

    for s in scopes:
        s["current_phase"] = profile.current_phase
        s["target_final_phase"] = profile.target_final_phase
        s["next_phase"] = profile.next_phase
        s["non_production"] = True

    df = pd.DataFrame(scopes)
    summary = {
        "scope_count": len(df),
        "in_scope_count": int((df["is_in_scope"] == True).sum()),
        "out_of_scope_count": int((df["is_in_scope"] == False).sum()),
        "current_phase": profile.current_phase,
        "target_final_phase": profile.target_final_phase,
        "next_phase": profile.next_phase,
    }
    return df, summary
