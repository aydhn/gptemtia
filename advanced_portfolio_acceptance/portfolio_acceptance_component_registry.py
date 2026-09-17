# -*- coding: utf-8 -*-
"""Phase 157: Portfolio Acceptance Component Registry.

Registers and summarizes all core components of the portfolio/risk block (Phases 153-157).
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from .portfolio_acceptance_config import (
    PortfolioAcceptanceProfile,
    get_portfolio_acceptance_profile,
)
from .portfolio_acceptance_labels import (
    COMPONENT_REGISTRY_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)

COMPONENTS = [
    {
        "component_id": "CMP-153",
        "component_name": "phase_153_portfolio_construction_position_sizing_risk_budgeting",
        "phase_number": 153,
        "module_name": "advanced_portfolio_construction",
        "description": "Portfolio construction, volatility parity/risk budget sizing contracts.",
    },
    {
        "component_id": "CMP-154",
        "component_name": "phase_154_portfolio_optimization_allocation_constraints",
        "phase_number": 154,
        "module_name": "advanced_portfolio_optimization",
        "description": "Portfolio optimization objectives, allocation constraints and solver contracts.",
    },
    {
        "component_id": "CMP-155",
        "component_name": "phase_155_risk_reporting_exposure_attribution_limit_monitoring",
        "phase_number": 155,
        "module_name": "advanced_risk_reporting",
        "description": "Risk reporting, exposure attribution, and limit monitoring contracts.",
    },
    {
        "component_id": "CMP-156",
        "component_name": "phase_156_portfolio_scenario_testing_drawdown_control",
        "phase_number": 156,
        "module_name": "advanced_portfolio_scenario_control",
        "description": "Portfolio scenario simulation, resilience testing, and drawdown control contracts.",
    },
    {
        "component_id": "CMP-157",
        "component_name": "phase_157_portfolio_acceptance_report",
        "phase_number": 157,
        "module_name": "advanced_portfolio_acceptance",
        "description": "Consolidated portfolio block acceptance report and Phase 158 handoff layer.",
    },
]


def build_portfolio_acceptance_component_registry(
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of portfolio block components."""
    active = profile or get_portfolio_acceptance_profile()
    records = []
    for c in COMPONENTS:
        records.append({
            "component_id": c["component_id"],
            "component_name": c["component_name"],
            "phase_number": c["phase_number"],
            "module_name": c["module_name"],
            "description": c["description"],
            "current_phase": active.current_phase,
            "contract_only": True,
            "non_production": True,
            "dry_run": True,
            "local_only": True,
            "production_ready": False,
            "broker_ready": False,
            "live_ready": False,
            "signal_ready": False,
            "strategy_approved": False,
            "portfolio_approved": False,
            "allocation_approved": False,
            "risk_approved": False,
            "status": PORTFOLIO_ACCEPTANCE_READY,
        })
    df = pd.DataFrame(records)
    summary = summarize_portfolio_acceptance_components(df)
    return df, summary


def summarize_portfolio_acceptance_components(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize portfolio acceptance components."""
    return {
        "domain": COMPONENT_REGISTRY_DOMAIN,
        "total_components": len(df),
        "phases_covered": [153, 154, 155, 156, 157],
        "all_contract_only": bool(df["contract_only"].all()) if not df.empty else True,
        "all_non_production": bool(df["non_production"].all()) if not df.empty else True,
        "none_production_ready": not bool(df["production_ready"].any()) if not df.empty else True,
        "none_broker_ready": not bool(df["broker_ready"].any()) if not df.empty else True,
        "status": PORTFOLIO_ACCEPTANCE_READY,
    }
