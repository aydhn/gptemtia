# -*- coding: utf-8 -*-
"""Phase 157: Portfolio Acceptance Scope Registry.

Defines the exact operational scope and explicit exclusions for Phase 157.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from .portfolio_acceptance_config import (
    PortfolioAcceptanceProfile,
    get_portfolio_acceptance_profile,
)
from .portfolio_acceptance_labels import (
    PORTFOLIO_ACCEPTANCE_SCOPE_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)

SCOPE_ITEMS = [
    ("scope_portfolio_block_acceptance", "Phase 153-157 portfolio/risk block acceptance", True, "In-scope"),
    ("scope_local_offline_dry_run", "Local and offline dry-run verification only", True, "In-scope"),
    ("scope_non_production_boundary", "Non-production governance and contract validation", True, "In-scope"),
    ("scope_phase_158_handoff", "Phase 158 full-system integration contract handoff", True, "In-scope"),
    ("scope_live_trading", "Live trading and order routing", False, "Strictly out of scope"),
    ("scope_broker_integration", "Broker API connection and execution", False, "Strictly out of scope"),
    ("scope_investment_advice", "Investment advice or directional recommendations", False, "Strictly out of scope"),
    ("scope_signal_generation", "Trading signal generation", False, "Strictly out of scope"),
    ("scope_portfolio_construction", "Real portfolio construction and sizing", False, "Strictly out of scope"),
    ("scope_portfolio_optimization", "Real portfolio optimizer execution and rebalancing", False, "Strictly out of scope"),
    ("scope_risk_reporting_execution", "Real risk reporting and limit monitoring execution", False, "Strictly out of scope"),
    ("scope_scenario_drawdown_control", "Real scenario simulation and drawdown control execution", False, "Strictly out of scope"),
    ("scope_model_training_prediction", "Model training, fitting, or predictive inference", False, "Strictly out of scope"),
    ("scope_production_deployment", "Production deployment or broker-ready certification", False, "Strictly out of scope"),
]


def build_portfolio_acceptance_scope_registry(
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry defining portfolio acceptance scope boundaries."""
    active = profile or get_portfolio_acceptance_profile()
    records = []
    for item_id, description, in_scope, notes in SCOPE_ITEMS:
        records.append({
            "scope_id": item_id,
            "description": description,
            "in_scope": in_scope,
            "notes": notes,
            "current_phase": active.current_phase,
            "status": PORTFOLIO_ACCEPTANCE_READY,
        })
    df = pd.DataFrame(records)
    summary = summarize_portfolio_acceptance_scope(df)
    return df, summary


def summarize_portfolio_acceptance_scope(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize portfolio acceptance scope."""
    in_scope_count = int(df["in_scope"].sum()) if not df.empty and "in_scope" in df.columns else 0
    out_of_scope_count = len(df) - in_scope_count
    return {
        "domain": PORTFOLIO_ACCEPTANCE_SCOPE_DOMAIN,
        "total_scope_items": len(df),
        "in_scope_count": in_scope_count,
        "out_of_scope_count": out_of_scope_count,
        "live_trading_excluded": True,
        "portfolio_execution_excluded": True,
        "risk_execution_excluded": True,
        "scenario_execution_excluded": True,
        "status": PORTFOLIO_ACCEPTANCE_READY,
    }
