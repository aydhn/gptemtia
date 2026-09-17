# -*- coding: utf-8 -*-
"""Phase 152: Backtest Acceptance Safety Boundary Engine."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_backtest_acceptance.backtest_acceptance_config import (
    BacktestAcceptanceProfile,
    get_backtest_acceptance_profile,
)
from advanced_backtest_acceptance.backtest_acceptance_labels import (
    SAFETY_DOMAIN,
    ACCEPTANCE_READY,
)

NO_GO_RULES: List[str] = [
    "live trading",
    "broker execution",
    "investment advice",
    "signal generation",
    "backtest execution",
    "benchmark execution",
    "metric calculation",
    "result claim",
    "performance claim",
    "strategy approval",
    "capital allocation",
    "portfolio construction",
    "position sizing",
    "optimizer execution",
    "model training",
    "prediction",
    "target label generation",
    "model registry write",
    "deployment",
    "scraping credential source overwrite",
]

SAFE_GO_RULES: List[str] = [
    "local offline Backtest Acceptance Report generation",
    "Phase 146-151 component contract completeness checks",
    "non-production readiness score",
    "manual review queue",
    "blocker gap warning registry",
    "validation evidence summary",
    "safety boundary summary",
    "Phase 153 portfolio construction contract handoff",
]


def build_backtest_acceptance_no_go_conditions(
    profile: Optional[BacktestAcceptanceProfile] = None,
) -> List[Dict[str, Any]]:
    """Return structured NO-GO conditions."""
    return [{"rule_id": f"NGO-{i+1:02d}", "name": rule, "prohibited": True} for i, rule in enumerate(NO_GO_RULES)]


def build_backtest_acceptance_safe_go_conditions(
    profile: Optional[BacktestAcceptanceProfile] = None,
) -> List[Dict[str, Any]]:
    """Return structured SAFE-GO conditions."""
    return [{"rule_id": f"SGO-{i+1:02d}", "name": rule, "permitted": True} for i, rule in enumerate(SAFE_GO_RULES)]


def build_backtest_acceptance_safety_boundary(
    profile: Optional[BacktestAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build safety boundary DataFrame and summary."""
    active = profile or get_backtest_acceptance_profile()

    records = []
    for ng in build_backtest_acceptance_no_go_conditions(active):
        records.append({
            "rule_id": ng["rule_id"],
            "rule_type": "NO-GO",
            "rule_name": ng["name"],
            "status": "ENFORCED",
            "current_phase": active.current_phase,
            "target_final_phase": active.target_final_phase,
            "next_phase": active.next_phase,
            "non_signal": True,
            "non_production": True,
            "local_only": True,
        })
    for sg in build_backtest_acceptance_safe_go_conditions(active):
        records.append({
            "rule_id": sg["rule_id"],
            "rule_type": "SAFE-GO",
            "rule_name": sg["name"],
            "status": "ACTIVE",
            "current_phase": active.current_phase,
            "target_final_phase": active.target_final_phase,
            "next_phase": active.next_phase,
            "non_signal": True,
            "non_production": True,
            "local_only": True,
        })

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": SAFETY_DOMAIN,
        "active_profile": active.profile_name,
        "total_rules": len(records),
        "no_go_count": len(NO_GO_RULES),
        "safe_go_count": len(SAFE_GO_RULES),
        "safety_status": "SECURE",
        "non_signal": True,
        "status": "ACCEPTED",
    }
    return df, summary
