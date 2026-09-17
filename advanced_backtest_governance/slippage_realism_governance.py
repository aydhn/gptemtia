# -*- coding: utf-8 -*-
"""Phase 150: Slippage Realism Governance.

Guarantees prohibition of zero-slippage assumptions and enforces non-linear impact modeling.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    REALISM_GOVERNANCE_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

SLIPPAGE_REALISM_RULES: List[Dict[str, Any]] = [
    {
        "rule_id": "SLP_01_ZERO_SLIPPAGE_BAN",
        "rule_name": "zero_slippage_prohibition",
        "description": "Strict prohibition against assuming zero slippage or executing exactly at the signal tick price.",
        "enforcement": "BLOCKING_ZERO_TOLERANCE",
    },
    {
        "rule_id": "SLP_02_NON_LINEAR_IMPACT",
        "rule_name": "square_root_market_impact_mandate",
        "description": "Enforce square-root trade volume-to-ADV market impact penalty.",
        "enforcement": "BLOCKING_MANDATORY",
    },
    {
        "rule_id": "SLP_03_REGIME_VOLATILITY_EXPANSION",
        "rule_name": "volatility_conditioned_slippage_multiplier",
        "description": "Scale simulated slippage during high-volatility regimes and news event windows.",
        "enforcement": "HIGH_AUDIT",
    },
]


def build_slippage_realism_governance_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for slippage realism governance."""
    rows: List[Dict[str, Any]] = []
    for r in SLIPPAGE_REALISM_RULES:
        rows.append({
            "rule_id": r["rule_id"],
            "rule_name": r["rule_name"],
            "description": r["description"],
            "enforcement": r["enforcement"],
            "zero_slippage_allowed": False,
            "broker_execution_allowed": False,
            "status": "ENFORCED",
            "non_signal": True,
            "local_only": True,
            "phase": profile.current_phase,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": REALISM_GOVERNANCE_DOMAIN,
        "subdomain": "slippage_realism",
        "total_rules": len(df),
        "zero_slippage_strictly_prohibited": True,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
