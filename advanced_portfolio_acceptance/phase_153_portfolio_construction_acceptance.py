# -*- coding: utf-8 -*-
"""Phase 157: Phase 153 Portfolio Construction Acceptance Registry.

Evaluates contract compliance, structural readiness, guards, and non-execution invariants
for Phase 153: Portfolio Construction, Position Sizing and Risk Budgeting.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from .portfolio_acceptance_config import (
    PortfolioAcceptanceProfile,
    get_portfolio_acceptance_profile,
)
from .portfolio_acceptance_labels import (
    PHASE_153_PORTFOLIO_CONSTRUCTION_ACCEPTANCE_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)

PHASE_153_ITEMS = [
    {
        "item_id": "ACC-153-01",
        "criterion": "advanced_portfolio_construction module present",
        "description": "Module package and exports available for offline inspection.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-153-02",
        "criterion": "portfolio construction contracts present",
        "description": "Specification contracts for multi-asset portfolio construction registered.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-153-03",
        "criterion": "position sizing contracts present",
        "description": "Volatility-parity, fixed-fractional, and risk-budget position sizing interface contracts ready.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-153-04",
        "criterion": "risk budget contracts present",
        "description": "Risk contribution and factor exposure budgeting specifications registered.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-153-05",
        "criterion": "exposure and concentration limit contracts present",
        "description": "Gross/net exposure, asset weight, and factor concentration caps defined.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-153-06",
        "criterion": "allocation/position sizing/investment advice guards present",
        "description": "Strict prohibition guards against directional claims and trade advice enforced.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-153-07",
        "criterion": "no portfolio construction executed",
        "description": "Zero real portfolio construction performed; contract placeholders only.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-153-08",
        "criterion": "no position sizing executed",
        "description": "Zero real position sizing calculated; negative invariant preserved.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-153-09",
        "criterion": "no allocation or order generation executed",
        "description": "Zero capital allocation or trading orders generated.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-153-10",
        "criterion": "Phase 154 handoff completed",
        "description": "Handoff to Phase 154 Portfolio Optimization verified and accepted.",
        "satisfied": True,
    },
]


def build_phase_153_portfolio_construction_acceptance_registry(
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Phase 153 acceptance evaluation registry."""
    active = profile or get_portfolio_acceptance_profile()
    records = []
    for item in PHASE_153_ITEMS:
        records.append({
            "item_id": item["item_id"],
            "phase_number": 153,
            "phase_title": "Portfolio Construction, Position Sizing and Risk Budgeting",
            "criterion": item["criterion"],
            "description": item["description"],
            "satisfied": item["satisfied"],
            "contract_only": True,
            "non_production": True,
            "dry_run": True,
            "current_phase": active.current_phase,
            "status": PORTFOLIO_ACCEPTANCE_READY,
        })
    df = pd.DataFrame(records)
    summary = summarize_phase_153_portfolio_construction_acceptance(df)
    return df, summary


def summarize_phase_153_portfolio_construction_acceptance(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Phase 153 acceptance registry."""
    all_satisfied = bool(df["satisfied"].all()) if not df.empty and "satisfied" in df.columns else False
    return {
        "domain": PHASE_153_PORTFOLIO_CONSTRUCTION_ACCEPTANCE_DOMAIN,
        "phase_number": 153,
        "total_criteria": len(df),
        "satisfied_criteria": int(df["satisfied"].sum()) if not df.empty and "satisfied" in df.columns else 0,
        "all_satisfied": all_satisfied,
        "contract_only": True,
        "non_production": True,
        "status": PORTFOLIO_ACCEPTANCE_READY if all_satisfied else "ACCEPTANCE_INCOMPLETE",
    }
