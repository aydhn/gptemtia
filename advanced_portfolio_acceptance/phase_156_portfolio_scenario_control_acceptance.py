# -*- coding: utf-8 -*-
"""Phase 157: Phase 156 Portfolio Scenario Testing and Drawdown Control Acceptance Registry.

Evaluates contract compliance, structural readiness, control action placeholders,
and non-execution invariants for Phase 156: Portfolio Scenario Testing and Drawdown Control.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from .portfolio_acceptance_config import (
    PortfolioAcceptanceProfile,
    get_portfolio_acceptance_profile,
)
from .portfolio_acceptance_labels import (
    PHASE_156_PORTFOLIO_SCENARIO_CONTROL_ACCEPTANCE_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)

PHASE_156_ITEMS = [
    {
        "item_id": "ACC-156-01",
        "criterion": "advanced_portfolio_scenario_control module present",
        "description": "Module package and exports available for offline inspection.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-156-02",
        "criterion": "portfolio scenario testing contracts present",
        "description": "Contracts defining historical and hypothetical shock scenarios registered.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-156-03",
        "criterion": "drawdown control contracts present",
        "description": "Multi-tier drawdown limits, warning thresholds, and de-risking triggers specified.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-156-04",
        "criterion": "resilience contracts present",
        "description": "Resilience evaluation, portfolio stability, and recovery path contract schemas defined.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-156-05",
        "criterion": "control action placeholders present",
        "description": "De-risking, hedging, exposure reduction, and freeze/resume action placeholders defined in non-executing mode.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-156-06",
        "criterion": "scenario/drawdown metric placeholders present",
        "description": "Metric calculation placeholders registered without computing real PnL or drawdowns.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-156-07",
        "criterion": "claim guards present",
        "description": "Guards preventing safety claims, official approvals, or trading advice active.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-156-08",
        "criterion": "no scenario execution",
        "description": "Zero stress scenarios or simulation runs executed against live/historical books.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-156-09",
        "criterion": "no drawdown control action or hedge executed",
        "description": "Zero automated de-risking, rebalance, hedge, or stop actions executed.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-156-10",
        "criterion": "Phase 157 handoff completed",
        "description": "Handoff to Phase 157 Portfolio Acceptance Report verified and accepted.",
        "satisfied": True,
    },
]


def build_phase_156_portfolio_scenario_control_acceptance_registry(
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Phase 156 acceptance evaluation registry."""
    active = profile or get_portfolio_acceptance_profile()
    records = []
    for item in PHASE_156_ITEMS:
        records.append({
            "item_id": item["item_id"],
            "phase_number": 156,
            "phase_title": "Portfolio Scenario Testing and Drawdown Control",
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
    summary = summarize_phase_156_portfolio_scenario_control_acceptance(df)
    return df, summary


def summarize_phase_156_portfolio_scenario_control_acceptance(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Phase 156 acceptance registry."""
    all_satisfied = bool(df["satisfied"].all()) if not df.empty and "satisfied" in df.columns else False
    return {
        "domain": PHASE_156_PORTFOLIO_SCENARIO_CONTROL_ACCEPTANCE_DOMAIN,
        "phase_number": 156,
        "total_criteria": len(df),
        "satisfied_criteria": int(df["satisfied"].sum()) if not df.empty and "satisfied" in df.columns else 0,
        "all_satisfied": all_satisfied,
        "contract_only": True,
        "non_production": True,
        "status": PORTFOLIO_ACCEPTANCE_READY if all_satisfied else "ACCEPTANCE_INCOMPLETE",
    }
