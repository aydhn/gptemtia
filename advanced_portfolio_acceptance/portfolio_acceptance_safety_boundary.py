# -*- coding: utf-8 -*-
"""Phase 157: Portfolio Acceptance Safety Boundary.

Compiles consolidated safety boundaries, NO-GO prohibitions, and SAFE-GO principles.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from .portfolio_acceptance_config import (
    PortfolioAcceptanceProfile,
    get_portfolio_acceptance_profile,
)
from .portfolio_acceptance_labels import (
    SAFETY_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)

NO_GO_CONDITIONS = [
    ("NOGO-01", "live_trading", "Live trading and order routing strictly prohibited"),
    ("NOGO-02", "broker_execution", "Broker API integration and transmission strictly prohibited"),
    ("NOGO-03", "investment_advice", "Investment advice and market opinions strictly prohibited"),
    ("NOGO-04", "signal_generation", "Directional signal generation strictly prohibited"),
    ("NOGO-05", "portfolio_construction", "Real portfolio construction and sizing strictly prohibited"),
    ("NOGO-06", "position_sizing", "Real position sizing execution strictly prohibited"),
    ("NOGO-07", "portfolio_optimization", "Real mathematical optimization and solver execution strictly prohibited"),
    ("NOGO-08", "capital_allocation", "Capital allocation generation strictly prohibited"),
    ("NOGO-09", "weight_generation", "Live portfolio weight generation strictly prohibited"),
    ("NOGO-10", "allocation_generation", "Asset allocation generation strictly prohibited"),
    ("NOGO-11", "rebalance_generation", "Rebalance trade generation strictly prohibited"),
    ("NOGO-12", "order_generation", "Order generation strictly prohibited"),
    ("NOGO-13", "risk_reporting_execution", "Real risk reporting execution strictly prohibited"),
    ("NOGO-14", "exposure_attribution_execution", "Real exposure attribution calculation strictly prohibited"),
    ("NOGO-15", "limit_monitoring_execution", "Real limit monitoring execution strictly prohibited"),
    ("NOGO-16", "scenario_execution", "Real scenario shock execution strictly prohibited"),
    ("NOGO-17", "drawdown_calculation", "Real drawdown calculation strictly prohibited"),
    ("NOGO-18", "drawdown_control_execution", "Real drawdown control execution strictly prohibited"),
    ("NOGO-19", "portfolio_adjustment", "Automated portfolio adjustment strictly prohibited"),
    ("NOGO-20", "hedge_derisk", "Automated hedging or de-risking actions strictly prohibited"),
    ("NOGO-21", "alert_generation", "Live alert broadcasting strictly prohibited"),
    ("NOGO-22", "dashboard_generation", "Live dashboard publishing strictly prohibited"),
    ("NOGO-23", "metric_calculation", "Real Sharpe, VaR, ES metric calculation strictly prohibited"),
    ("NOGO-24", "optimizer_execution", "Solver optimizer execution strictly prohibited"),
    ("NOGO-25", "model_training_prediction", "Model training, fitting, and prediction strictly prohibited"),
    ("NOGO-26", "target_label_generation", "Target/label generation strictly prohibited"),
    ("NOGO-27", "model_registry_write", "Writing model artifacts to registry strictly prohibited"),
    ("NOGO-28", "deployment", "Production deployment strictly prohibited"),
    ("NOGO-29", "scraping_credential_source_overwrite", "Web scraping, credential exposure, and source overwrite strictly prohibited"),
]

SAFE_GO_CONDITIONS = [
    ("SAFEGO-01", "local_offline_acceptance_report", "Generate local/offline Portfolio Acceptance Report"),
    ("SAFEGO-02", "component_completeness_checks", "Verify Phase 153-156 component contract completeness"),
    ("SAFEGO-03", "non_production_readiness_score", "Compute non-production contract readiness score"),
    ("SAFEGO-04", "manual_review_queue", "Maintain human-in-the-loop manual review queue"),
    ("SAFEGO-05", "blocker_gap_warning_registry", "Maintain blocker, gap, and warning registries"),
    ("SAFEGO-06", "validation_evidence_summary", "Compile validation evidence summary"),
    ("SAFEGO-07", "safety_boundary_summary", "Compile safety boundary summary"),
    ("SAFEGO-08", "phase_158_handoff", "Prepare Phase 158 full-system integration contract handoff"),
]


def build_portfolio_acceptance_no_go_conditions(
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of NO-GO conditions."""
    active = profile or get_portfolio_acceptance_profile()
    records = []
    for cond_id, rule_name, desc in NO_GO_CONDITIONS:
        records.append({
            "condition_id": cond_id,
            "type": "NO-GO",
            "rule_name": rule_name,
            "description": desc,
            "enforced": True,
            "current_phase": active.current_phase,
        })
    df = pd.DataFrame(records)
    summary = {
        "total_no_go": len(df),
        "all_enforced": True,
    }
    return df, summary


def build_portfolio_acceptance_safe_go_conditions(
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of SAFE-GO conditions."""
    active = profile or get_portfolio_acceptance_profile()
    records = []
    for cond_id, principle, desc in SAFE_GO_CONDITIONS:
        records.append({
            "condition_id": cond_id,
            "type": "SAFE-GO",
            "principle": principle,
            "description": desc,
            "permitted": True,
            "current_phase": active.current_phase,
        })
    df = pd.DataFrame(records)
    summary = {
        "total_safe_go": len(df),
        "all_permitted": True,
    }
    return df, summary


def build_portfolio_acceptance_safety_boundary(
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build unified safety boundary report."""
    active = profile or get_portfolio_acceptance_profile()
    df_nogo, s_nogo = build_portfolio_acceptance_no_go_conditions(active)
    df_safego, s_safego = build_portfolio_acceptance_safe_go_conditions(active)

    combined_df = pd.concat([df_nogo, df_safego], ignore_index=True)
    summary = {
        "domain": SAFETY_DOMAIN,
        "total_rules": len(combined_df),
        "no_go_count": s_nogo["total_no_go"],
        "safe_go_count": s_safego["total_safe_go"],
        "safety_status": "SAFETY_BOUNDARY_ENFORCED",
        "live_trading_prohibited": True,
        "broker_execution_prohibited": True,
        "portfolio_execution_prohibited": True,
        "status": PORTFOLIO_ACCEPTANCE_READY,
    }
    return combined_df, summary
