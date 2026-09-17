# -*- coding: utf-8 -*-
"""Phase 150: Backtest Governance Dependencies Module.

Tracks and validates dependencies on Phase 146 (Realistic Backtest), Phase 147
(Walk-Forward / OOS Benchmarking), Phase 148 (Stress Testing), and Phase 149 (Monte Carlo Robustness).
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    DEPENDENCY_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

DEPENDENCY_ITEMS: List[Dict[str, Any]] = [
    {
        "dependency_id": "DEP_150_01",
        "phase": 146,
        "phase_name": "Phase 146 Realistic Backtest",
        "contract_reference": "realistic_backtest_governance_contract",
        "requirement": "Transaction cost models, tiered slippage schedules, and realistic fill assumptions.",
        "status": "SATISFIED",
        "is_mocked": False,
    },
    {
        "dependency_id": "DEP_150_02",
        "phase": 147,
        "phase_name": "Phase 147 Walk-Forward and OOS Benchmarking",
        "contract_reference": "walk_forward_governance_contract",
        "requirement": "Anchored and rolling split specifications, purge/embargo windows, and out-of-sample discipline.",
        "status": "SATISFIED",
        "is_mocked": False,
    },
    {
        "dependency_id": "DEP_150_03",
        "phase": 148,
        "phase_name": "Phase 148 Stress Testing",
        "contract_reference": "stress_testing_governance_contract",
        "requirement": "Historical crisis catalogs, hypothetical shock contracts, and liquidity spread widening scenarios.",
        "status": "SATISFIED",
        "is_mocked": False,
    },
    {
        "dependency_id": "DEP_150_04",
        "phase": 149,
        "phase_name": "Phase 149 Monte Carlo Robustness",
        "contract_reference": "monte_carlo_governance_contract",
        "requirement": "Bootstrap resampling protocols, parameter stability sensitivity, and distribution envelope bounds.",
        "status": "SATISFIED",
        "is_mocked": False,
    },
]


def summarize_backtest_governance_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Phase 150 dependency satisfaction."""
    all_satisfied = bool((df["status"] == "SATISFIED").all()) if not df.empty else True
    return {
        "domain": DEPENDENCY_DOMAIN,
        "total_dependencies": len(df),
        "all_dependencies_satisfied": all_satisfied,
        "status": STATUS_GOVERNANCE_CONTRACT_READY if all_satisfied else "DEPENDENCIES_PENDING",
        "non_signal": True,
        "local_only": True,
    }


def build_backtest_governance_dependency_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the backtest governance dependency registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for dep in DEPENDENCY_ITEMS:
        rows.append({
            "dependency_id": dep["dependency_id"],
            "phase": dep["phase"],
            "phase_name": dep["phase_name"],
            "contract_reference": dep["contract_reference"],
            "requirement": dep["requirement"],
            "status": dep["status"],
            "is_mocked": dep["is_mocked"],
            "current_phase": profile.current_phase,
            "profile_name": profile.profile_name,
            "non_signal": True,
            "local_only": True,
        })
    df = pd.DataFrame(rows)
    summary = summarize_backtest_governance_dependencies(df)
    summary["profile_name"] = profile.profile_name
    return df, summary
