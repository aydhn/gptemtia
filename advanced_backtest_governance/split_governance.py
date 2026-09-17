# -*- coding: utf-8 -*-
"""Phase 150: Split Governance.

Governs train/validation/test chronological splits, embargo boundaries, and purge rules.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    SPLIT_GOVERNANCE_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

SPLIT_RULES: List[Dict[str, Any]] = [
    {
        "rule_id": "SPL_01_CHRONOLOGICAL_SPLIT_ONLY",
        "rule_name": "chronological_split_mandate",
        "description": "Strict prohibition of random k-fold or shuffled splits; all partitions must respect temporal ordering.",
        "enforcement": "BLOCKING_ZERO_TOLERANCE",
    },
    {
        "rule_id": "SPL_02_PURGE_OVERLAPPING_LABELS",
        "rule_name": "label_overlap_purging_rule",
        "description": "Purge training samples whose evaluation window overlaps with the start of the test split.",
        "enforcement": "BLOCKING_MANDATORY",
    },
    {
        "rule_id": "SPL_03_EMBARGO_PERIOD_ENFORCEMENT",
        "rule_name": "post_split_embargo_quarantine",
        "description": "Enforce mandatory embargo buffer bars immediately following test splits to neutralize autoregressive leakage.",
        "enforcement": "BLOCKING_MANDATORY",
    },
]


def build_split_governance_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for split governance."""
    rows: List[Dict[str, Any]] = []
    for r in SPLIT_RULES:
        rows.append({
            "rule_id": r["rule_id"],
            "rule_name": r["rule_name"],
            "description": r["description"],
            "enforcement": r["enforcement"],
            "execution_allowed": False,
            "status": "ACTIVE",
            "non_signal": True,
            "local_only": True,
            "phase": profile.current_phase,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": SPLIT_GOVERNANCE_DOMAIN,
        "total_split_rules": len(df),
        "random_splits_prohibited": True,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
