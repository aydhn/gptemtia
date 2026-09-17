# -*- coding: utf-8 -*-
"""Phase 150: Transaction Cost Realism Governance.

Guarantees prohibition of zero-cost assumptions and enforces realistic fee modeling.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    REALISM_GOVERNANCE_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

COST_REALISM_RULES: List[Dict[str, Any]] = [
    {
        "rule_id": "CST_01_ZERO_COST_BAN",
        "rule_name": "zero_transaction_cost_prohibition",
        "description": "Strict prohibition against assuming zero transaction fees or commission-free trading.",
        "enforcement": "BLOCKING_ZERO_TOLERANCE",
    },
    {
        "rule_id": "CST_02_TIERED_COMMISSION_STRUCTURE",
        "rule_name": "tiered_commission_model_requirement",
        "description": "Require broker commission tiers (per-contract for commodities, bps for FX/CFD).",
        "enforcement": "BLOCKING_MANDATORY",
    },
    {
        "rule_id": "CST_03_EXCHANGE_REGULATORY_FEES",
        "rule_name": "exchange_clearing_fee_inclusion",
        "description": "Mandate inclusion of exchange, clearing, NFA/FINRA, and regulatory transaction fees.",
        "enforcement": "BLOCKING_MANDATORY",
    },
    {
        "rule_id": "CST_04_FINANCING_CARRY_FEES",
        "rule_name": "overnight_financing_and_borrow_cost_inclusion",
        "description": "Simulate swap rates, repo financing, and short-borrow carry costs across multi-day holdings.",
        "enforcement": "HIGH_AUDIT",
    },
]


def build_transaction_cost_realism_governance_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for transaction cost realism governance."""
    rows: List[Dict[str, Any]] = []
    for r in COST_REALISM_RULES:
        rows.append({
            "rule_id": r["rule_id"],
            "rule_name": r["rule_name"],
            "description": r["description"],
            "enforcement": r["enforcement"],
            "zero_cost_allowed": False,
            "broker_execution_allowed": False,
            "status": "ENFORCED",
            "non_signal": True,
            "local_only": True,
            "phase": profile.current_phase,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": REALISM_GOVERNANCE_DOMAIN,
        "subdomain": "transaction_cost_realism",
        "total_rules": len(df),
        "zero_cost_strictly_prohibited": True,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
