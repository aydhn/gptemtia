# -*- coding: utf-8 -*-
"""Phase 150: Lookahead Bias Controls.

Enforces zero lookahead tolerance across dataset structures, bar timestamps,
feature calculations, and order simulations.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    LOOKAHEAD_BIAS_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

LOOKAHEAD_CONTROLS: List[Dict[str, Any]] = [
    {
        "control_id": "LKB_01_TIMESTAMP_CHRONOLOGY",
        "name": "timestamp_chronological_integrity",
        "description": "Strict verification that features and signals at timestamp T only access data strictly prior to or at T.",
        "enforcement": "BLOCKING_ZERO_TOLERANCE",
    },
    {
        "control_id": "LKB_02_NO_NEGATIVE_SHIFTS",
        "name": "negative_shift_prohibition",
        "description": "Prohibit shift(-1) or future bar lookahead indexing in feature definitions and targets.",
        "enforcement": "BLOCKING_ZERO_TOLERANCE",
    },
    {
        "control_id": "LKB_03_EXECUTION_LAG_MANDATE",
        "name": "execution_lag_policy",
        "description": "Mandate minimum 1-bar execution delay: orders triggered on bar T close can only execute on T+1 open.",
        "enforcement": "BLOCKING_MANDATORY",
    },
    {
        "control_id": "LKB_04_ASOF_JOIN_EXPANSION",
        "name": "macro_event_asof_join_validation",
        "description": "Cross-domain macro and calendar joins must use backwards as-of joins with release lag awareness.",
        "enforcement": "BLOCKING_MANDATORY",
    },
    {
        "control_id": "LKB_05_NO_FORWARD_AGGREGATIONS",
        "name": "centered_and_forward_window_prohibition",
        "description": "Rolling calculations must use closed='left' or trailing windows; centered rolling windows are forbidden.",
        "enforcement": "BLOCKING_ZERO_TOLERANCE",
    },
]

FORBIDDEN_LOOKAHEAD_COLUMN_PATTERNS = [
    "future_return",
    "forward_return",
    "next_return",
    "lookahead_return",
    "future_pnl",
    "realized_future_pnl",
    "target_future",
    "shift_neg",
    "lead_return",
    "leak",
    "leakage",
]


def validate_lookahead_bias_columns(column_names: List[str]) -> Dict[str, Any]:
    """Inspect column names for lookahead patterns, blocking any leakage."""
    detected_leaks: List[str] = []
    for col in column_names:
        c_lower = col.lower()
        for pattern in FORBIDDEN_LOOKAHEAD_COLUMN_PATTERNS:
            if pattern in c_lower:
                detected_leaks.append(col)
                break

    is_clean = len(detected_leaks) == 0
    return {
        "is_clean": is_clean,
        "is_blocked": not is_clean,
        "detected_leaks": detected_leaks,
        "policy_decision": "PASS" if is_clean else "BLOCKED_BY_LOOKAHEAD_POLICY",
        "message": (
            "Lookahead audit passed. No forward-looking columns detected."
            if is_clean
            else f"Lookahead leakage detected in columns: {detected_leaks}. Backtest execution blocked."
        ),
        "non_signal": True,
    }


def build_lookahead_bias_control_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for lookahead bias controls."""
    rows: List[Dict[str, Any]] = []
    for c in LOOKAHEAD_CONTROLS:
        rows.append({
            "control_id": c["control_id"],
            "name": c["name"],
            "description": c["description"],
            "enforcement": c["enforcement"],
            "strictness": profile.lookahead_guard_strictness,
            "status": "ACTIVE",
            "execution_allowed": False,
            "non_signal": True,
            "local_only": True,
            "phase": profile.current_phase,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": LOOKAHEAD_BIAS_DOMAIN,
        "total_controls": len(df),
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "strictness": profile.lookahead_guard_strictness,
        "all_blocking": True,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
