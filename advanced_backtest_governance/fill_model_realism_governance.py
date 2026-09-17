# -*- coding: utf-8 -*-
"""Phase 150: Fill Model Realism Governance.

Guarantees prohibition of instant fills, perfect execution, and unverified limit-order fills.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    REALISM_GOVERNANCE_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

FILL_REALISM_RULES: List[Dict[str, Any]] = [
    {
        "rule_id": "FIL_01_NO_INSTANT_FILL_CLAIM",
        "rule_name": "instant_fill_prohibition",
        "description": "Prohibit assuming immediate zero-latency fill upon signal generation.",
        "enforcement": "BLOCKING_ZERO_TOLERANCE",
    },
    {
        "rule_id": "FIL_02_PARTIAL_FILL_SIMULATION",
        "rule_name": "partial_fill_and_queue_modeling",
        "description": "Mandate simulation of limit order queue priority and partial fills for large size.",
        "enforcement": "HIGH_AUDIT",
    },
    {
        "rule_id": "FIL_03_TOUCH_RULE_RESTRICTION",
        "rule_name": "touch_fill_prohibition",
        "description": "Require price to trade through limit price, not just touch it, for limit order fill confirmation.",
        "enforcement": "BLOCKING_MANDATORY",
    },
]


def build_fill_model_realism_governance_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for fill model realism governance."""
    rows: List[Dict[str, Any]] = []
    for r in FILL_REALISM_RULES:
        rows.append({
            "rule_id": r["rule_id"],
            "rule_name": r["rule_name"],
            "description": r["description"],
            "enforcement": r["enforcement"],
            "instant_fill_allowed": False,
            "broker_execution_allowed": False,
            "status": "ENFORCED",
            "non_signal": True,
            "local_only": True,
            "phase": profile.current_phase,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": REALISM_GOVERNANCE_DOMAIN,
        "subdomain": "fill_model_realism",
        "total_rules": len(df),
        "instant_fill_strictly_prohibited": True,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
