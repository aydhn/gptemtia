# -*- coding: utf-8 -*-
"""Phase 150: Stress Testing Governance.

Governs integration with Phase 148 stress testing contracts under zero-execution boundaries.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    STRESS_GOVERNANCE_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

STRESS_GOVERNANCE_ITEMS: List[Dict[str, Any]] = [
    {
        "governance_id": "STR_01_HISTORICAL_STRESS_MANDATE",
        "name": "mandatory_historical_stress_coverage",
        "description": "Strategies must evaluate performance across Phase 148 historical shocks (2008 GFC, 2020 Covid, 2022 Inflation Spike).",
        "phase_148_ref": "PHASE_148_HISTORICAL_STRESS_CONTRACTS",
    },
    {
        "governance_id": "STR_02_HYPOTHETICAL_SHOCK_MANDATE",
        "name": "mandatory_hypothetical_shock_coverage",
        "description": "Evaluate behavior under synthetic liquidity shocks, spread widening, and flash crash scenarios.",
        "phase_148_ref": "PHASE_148_HYPOTHETICAL_STRESS_CONTRACTS",
    },
    {
        "governance_id": "STR_03_EXECUTION_LOCK",
        "name": "stress_simulation_execution_lock_policy",
        "description": "Block actual numerical stress simulations at Phase 150 governance layer.",
        "phase_148_ref": "PHASE_148_DISABLED_EXECUTION_SPECS",
    },
]


def build_stress_testing_governance_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for stress testing governance."""
    rows: List[Dict[str, Any]] = []
    for item in STRESS_GOVERNANCE_ITEMS:
        rows.append({
            "governance_id": item["governance_id"],
            "name": item["name"],
            "description": item["description"],
            "phase_148_ref": item["phase_148_ref"],
            "execution_allowed": False,
            "status": "GOVERNANCE_CONTRACT_READY",
            "non_signal": True,
            "local_only": True,
            "phase": profile.current_phase,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": STRESS_GOVERNANCE_DOMAIN,
        "total_items": len(df),
        "execution_disabled": True,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
