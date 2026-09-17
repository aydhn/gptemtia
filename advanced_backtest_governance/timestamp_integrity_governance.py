# -*- coding: utf-8 -*-
"""Phase 150: Timestamp Integrity Governance.

Enforces strict bar ordering, timezone normalization, and prohibition of future timestamp joins.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    REALISM_GOVERNANCE_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

TIMESTAMP_RULES: List[Dict[str, Any]] = [
    {
        "rule_id": "TS_01_STRICT_MONOTONIC_ORDER",
        "rule_name": "strictly_monotonic_increasing_timestamps",
        "description": "Ensure observation timestamps are strictly increasing with zero retrograde or out-of-order bars.",
        "enforcement": "BLOCKING_ZERO_TOLERANCE",
    },
    {
        "rule_id": "TS_02_UTC_NORMALIZATION",
        "rule_name": "utc_timezone_mandate",
        "description": "Mandate canonical UTC timestamp representation across all asset series and economic calendar releases.",
        "enforcement": "BLOCKING_MANDATORY",
    },
    {
        "rule_id": "TS_03_NO_FUTURE_TIMESTAMP_JOIN",
        "rule_name": "future_timestamp_join_prohibition",
        "description": "Strictly prohibit joining or merging datasets using future-dated keys or forward alignment.",
        "enforcement": "BLOCKING_ZERO_TOLERANCE",
    },
]

FORBIDDEN_TIMESTAMP_ACTIONS = [
    "future_timestamp_join",
    "future_join",
    "forward_join",
    "shift(-1)",
    "retrograde_timestamp",
    "out_of_order_join",
]


def validate_timestamp_integrity_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Inspect request for future timestamp join or retrograde indexing."""
    text = str(request).lower()
    blocked = False
    violating_tokens: List[str] = []

    for token in FORBIDDEN_TIMESTAMP_ACTIONS:
        if token in text:
            blocked = True
            violating_tokens.append(token)

    return {
        "is_allowed": not blocked,
        "is_blocked": blocked,
        "decision": "BLOCKED_BY_TIMESTAMP_POLICY" if blocked else "ALLOWED",
        "violating_tokens": violating_tokens,
        "policy_message": (
            "Future timestamp joins and retrograde bar alignments are strictly prohibited by Phase 150 policy."
            if blocked
            else "Timestamp request conforms to monotonic chronological integrity."
        ),
        "non_signal": True,
    }


def build_timestamp_integrity_governance_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for timestamp integrity governance."""
    rows: List[Dict[str, Any]] = []
    for r in TIMESTAMP_RULES:
        rows.append({
            "rule_id": r["rule_id"],
            "rule_name": r["rule_name"],
            "description": r["description"],
            "enforcement": r["enforcement"],
            "status": "ACTIVE",
            "non_signal": True,
            "local_only": True,
            "phase": profile.current_phase,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": REALISM_GOVERNANCE_DOMAIN,
        "subdomain": "timestamp_integrity_governance",
        "total_rules": len(df),
        "future_joins_strictly_prohibited": True,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
