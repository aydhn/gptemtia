# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Backtest Acceptance Dependencies."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    DEPENDENCY_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


BACKTEST_DEPENDENCIES = [
    {"dep_id": "DEP_BTEST_ACCEPTANCE_152", "component": "Phase 152 Backtest Acceptance", "source_module": "advanced_backtest_acceptance", "status": "SATISFIED", "description": "Phase 152 Backtest Acceptance Report ve onay manifesti."},
    {"dep_id": "DEP_REALISTIC_BTEST_146", "component": "Phase 146 Realistic Backtest", "source_module": "advanced_realistic_backtest", "status": "SATISFIED", "description": "Gercekci komisyon, kayma ve marjin simulasyon sozlesmeleri."},
    {"dep_id": "DEP_WALK_FORWARD_147", "component": "Phase 147 Walk Forward OOS", "source_module": "advanced_walk_forward_validation", "status": "SATISFIED", "description": "Orneklem disi (OOS) saglamlik ve overfit denetimi."},
    {"dep_id": "DEP_STRESS_TESTING_148", "component": "Phase 148 Stress Testing", "source_module": "advanced_stress_testing", "status": "SATISFIED", "description": "Senaryo soklari ve ekstrem kuyruk riski sinirlari."},
    {"dep_id": "DEP_MONTE_CARLO_149", "component": "Phase 149 Monte Carlo Robustness", "source_module": "advanced_monte_carlo_robustness", "status": "SATISFIED", "description": "Parametre duyarliligi ve guven araliklari."},
    {"dep_id": "DEP_BTEST_GOVERNANCE_150", "component": "Phase 150 Backtest Governance", "source_module": "advanced_backtest_governance", "status": "SATISFIED", "description": "Veri sizintisi, forward-bias ve coklu test duzeltmeleri."},
]


def build_portfolio_backtest_acceptance_dependency_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for backtest acceptance dependencies."""
    rows = []
    for d in BACKTEST_DEPENDENCIES:
        rows.append({
            "dep_id": d["dep_id"],
            "component": d["component"],
            "source_module": d["source_module"],
            "status": d["status"],
            "description": d["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "non_signal": True,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": DEPENDENCY_DOMAIN,
        "active_profile": profile.profile_name,
        "total_dependencies": len(df),
        "all_satisfied": bool((df["status"] == "SATISFIED").all()),
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
