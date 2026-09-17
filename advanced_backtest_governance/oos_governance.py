# -*- coding: utf-8 -*-
"""Phase 150: Out-of-Sample (OOS) Governance.

Enforces strict quarantine and isolation protocols for out-of-sample data.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    OOS_GOVERNANCE_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

OOS_GOVERNANCE_ITEMS: List[Dict[str, Any]] = [
    {
        "oos_id": "OOS_01_UNTOUCHED_QUARANTINE",
        "name": "untouched_holdout_quarantine",
        "description": "Holdout dataset is sealed until all model parameters and signal rules are irreversibly frozen.",
        "enforcement": "BLOCKING_ZERO_TOLERANCE",
    },
    {
        "oos_id": "OOS_02_SINGLE_PASS_RULE",
        "name": "single_pass_oos_evaluation",
        "description": "Out-of-sample data must only be evaluated once; iterative tweaking on OOS constitutes snooping.",
        "enforcement": "BLOCKING_MANDATORY",
    },
    {
        "oos_id": "OOS_03_OOS_METRIC_CLAIM_LOCK",
        "name": "oos_metric_claim_lock_policy",
        "description": "OOS return assertions without audited log confirmation are blocked by governance policy.",
        "enforcement": "BLOCKING_ZERO_TOLERANCE",
    },
]


def build_oos_governance_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for OOS governance."""
    rows: List[Dict[str, Any]] = []
    for item in OOS_GOVERNANCE_ITEMS:
        rows.append({
            "oos_id": item["oos_id"],
            "name": item["name"],
            "description": item["description"],
            "enforcement": item["enforcement"],
            "execution_allowed": False,
            "status": "ACTIVE",
            "non_signal": True,
            "local_only": True,
            "phase": profile.current_phase,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": OOS_GOVERNANCE_DOMAIN,
        "total_rules": len(df),
        "quarantine_active": True,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
