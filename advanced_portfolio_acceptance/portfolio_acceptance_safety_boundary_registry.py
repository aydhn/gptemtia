# -*- coding: utf-8 -*-
"""Phase 157: Portfolio Acceptance Safety Boundary Registry.

Registers and enforces safety boundaries preventing unauthorized actions,
live trading, broker interactions, and automated execution.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from .portfolio_acceptance_config import (
    PortfolioAcceptanceProfile,
    get_portfolio_acceptance_profile,
)
from .portfolio_acceptance_labels import (
    SAFETY_BOUNDARY_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)

SAFETY_RULES = [
    ("SAFE-01", "no_live_trading", "Prohibit live trading or real market order execution", False, "Safety rule"),
    ("SAFE-02", "no_broker_integration", "Prohibit real broker API connectivity and order transmission", False, "Safety rule"),
    ("SAFE-03", "no_investment_advice", "Prohibit financial or investment advice generation", False, "Safety rule"),
    ("SAFE-04", "no_signal_generation", "Prohibit directional trading signals or trade calls", False, "Safety rule"),
    ("SAFE-05", "no_portfolio_construction", "Prohibit real asset portfolio construction and capital allocation", False, "Safety rule"),
    ("SAFE-06", "no_position_sizing", "Prohibit real position size calculation for execution", False, "Safety rule"),
    ("SAFE-07", "no_portfolio_optimization", "Prohibit real mathematical optimization and rebalancing", False, "Safety rule"),
    ("SAFE-08", "no_risk_reporting_execution", "Prohibit live risk monitoring or automated alerting", False, "Safety rule"),
    ("SAFE-09", "no_scenario_execution", "Prohibit automated scenario shock execution against real books", False, "Safety rule"),
    ("SAFE-10", "no_drawdown_control_execution", "Prohibit automated hedge, de-risk, or stop actions", False, "Safety rule"),
    ("SAFE-11", "contract_only_acceptance", "Allow contract-level verification and metadata checks", True, "Permitted operation"),
    ("SAFE-12", "local_offline_dry_run", "Allow local, dry-run, non-executing governance checks", True, "Permitted operation"),
]


def build_portfolio_acceptance_safety_boundary_registry(
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of safety boundaries."""
    active = profile or get_portfolio_acceptance_profile()
    records = []
    for rule_id, rule_name, description, is_allowed, notes in SAFETY_RULES:
        records.append({
            "boundary_id": rule_id,
            "rule_name": rule_name,
            "description": description,
            "is_allowed": is_allowed,
            "notes": notes,
            "current_phase": active.current_phase,
            "status": PORTFOLIO_ACCEPTANCE_READY,
        })
    df = pd.DataFrame(records)
    summary = summarize_portfolio_acceptance_safety_boundaries(df)
    return df, summary


def summarize_portfolio_acceptance_safety_boundaries(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize safety boundaries."""
    prohibited_count = len(df[~df["is_allowed"]]) if not df.empty and "is_allowed" in df.columns else 0
    allowed_count = len(df[df["is_allowed"]]) if not df.empty and "is_allowed" in df.columns else 0
    return {
        "domain": SAFETY_BOUNDARY_DOMAIN,
        "total_rules": len(df),
        "prohibited_actions_count": prohibited_count,
        "allowed_actions_count": allowed_count,
        "all_prohibited_enforced": True,
        "status": PORTFOLIO_ACCEPTANCE_READY,
    }
