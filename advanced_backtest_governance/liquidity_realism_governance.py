# -*- coding: utf-8 -*-
"""Phase 150: Liquidity Realism Governance.

Guarantees prohibition of infinite or perfect liquidity assumptions in commodity and FX trading.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    REALISM_GOVERNANCE_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

LIQUIDITY_REALISM_RULES: List[Dict[str, Any]] = [
    {
        "rule_id": "LQD_01_NO_PERFECT_LIQUIDITY",
        "rule_name": "perfect_liquidity_prohibition",
        "description": "Prohibit assuming that arbitrary trade sizes can be absorbed without price slippage.",
        "enforcement": "BLOCKING_ZERO_TOLERANCE",
    },
    {
        "rule_id": "LQD_02_ADV_PARTICIPATION_CAP",
        "rule_name": "maximum_adv_participation_rate",
        "description": "Cap simulated order size at maximum 1-2% of Average Daily Volume (ADV) for realistic fill.",
        "enforcement": "BLOCKING_MANDATORY",
    },
    {
        "rule_id": "LQD_03_OFF_HOURS_LIQUIDITY_PENALTY",
        "rule_name": "session_depth_adjustment",
        "description": "Penalize trades executed during low-liquidity Asian or holiday sessions with wider bid-ask spreads.",
        "enforcement": "HIGH_AUDIT",
    },
]


def build_liquidity_realism_governance_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for liquidity realism governance."""
    rows: List[Dict[str, Any]] = []
    for r in LIQUIDITY_REALISM_RULES:
        rows.append({
            "rule_id": r["rule_id"],
            "rule_name": r["rule_name"],
            "description": r["description"],
            "enforcement": r["enforcement"],
            "perfect_liquidity_allowed": False,
            "broker_execution_allowed": False,
            "status": "ENFORCED",
            "non_signal": True,
            "local_only": True,
            "phase": profile.current_phase,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": REALISM_GOVERNANCE_DOMAIN,
        "subdomain": "liquidity_realism",
        "total_rules": len(df),
        "perfect_liquidity_prohibited": True,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
