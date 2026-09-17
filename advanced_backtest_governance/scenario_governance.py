# -*- coding: utf-8 -*-
"""Phase 150: Scenario Governance.

Governs scenario selection, shock definitions, and scenario consistency.
Zero scenario simulation execution in Phase 150.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    STRESS_GOVERNANCE_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

SCENARIO_GOVERNANCE_ITEMS: List[Dict[str, Any]] = [
    {
        "scenario_id": "SCN_01_CORRELATION_BREAKDOWN",
        "name": "cross_asset_correlation_breakdown_contract",
        "description": "Governs testing under simultaneous breakdown of historical commodity-FX correlations.",
    },
    {
        "scenario_id": "SCN_02_VOLATILITY_EXPANSION",
        "name": "volatility_shock_spike_contract",
        "description": "Governs behavior during instantaneous 3-standard-deviation volatility expansion episodes.",
    },
    {
        "scenario_id": "SCN_03_LIQUIDITY_DROUGHT",
        "name": "liquidity_evaporation_contract",
        "description": "Governs model execution constraints during extreme market illiquidity and order book thinning.",
    },
]


def build_scenario_governance_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for scenario governance."""
    rows: List[Dict[str, Any]] = []
    for item in SCENARIO_GOVERNANCE_ITEMS:
        rows.append({
            "scenario_id": item["scenario_id"],
            "name": item["name"],
            "description": item["description"],
            "execution_allowed": False,
            "status": "GOVERNANCE_CONTRACT_READY",
            "non_signal": True,
            "local_only": True,
            "phase": profile.current_phase,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": STRESS_GOVERNANCE_DOMAIN,
        "subdomain": "scenario_governance",
        "total_scenarios": len(df),
        "execution_disabled": True,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
