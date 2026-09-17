# -*- coding: utf-8 -*-
"""Phase 150: Backtest Result Claim Disabled Report.

Documents the prohibition of result claims and performance claims in Phase 150.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    DISABLED_EXECUTION_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
    EXEC_BLOCKED_NO_RESULT_CLAIM,
)

DISABLED_CLAIM_OPS: List[Dict[str, Any]] = [
    {"operation_name": "performance_claim", "status": "DISABLED", "reason": "Claims of verified return are forbidden."},
    {"operation_name": "proven_strategy", "status": "DISABLED", "reason": "Empirical certainty claims are forbidden."},
    {"operation_name": "guaranteed_return", "status": "DISABLED", "reason": "Profit guarantee claims are forbidden."},
    {"operation_name": "approve_strategy", "status": "DISABLED", "reason": "Automated strategy approval is forbidden."},
]

FORBIDDEN_CLAIM_WORDS = ["performance_claim", "proven_strategy", "guaranteed_return", "approve_strategy"]


def validate_no_result_claim_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate request ensures zero performance claims."""
    text = str(request).lower()
    blocked = False
    violating_words: List[str] = []

    for word in FORBIDDEN_CLAIM_WORDS:
        if word in text:
            blocked = True
            violating_words.append(word)

    return {
        "is_allowed": not blocked,
        "is_blocked": blocked,
        "violating_words": violating_words,
        "decision": EXEC_BLOCKED_NO_RESULT_CLAIM if blocked else "ALLOWED_CONTRACT_ONLY",
        "policy_message": (
            f"Result claim is disabled: violating words {violating_words}. Phase 150 is claim-free."
            if blocked
            else "Complies with zero result claim policy."
        ),
        "non_signal": True,
    }


def build_backtest_result_claim_disabled_report(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for result claim disabled report."""
    rows: List[Dict[str, Any]] = []
    for op in DISABLED_CLAIM_OPS:
        rows.append({
            "operation_name": op["operation_name"],
            "reason": op["reason"],
            "status": op["status"],
            "claim_permitted": False,
            "phase": profile.current_phase,
            "non_signal": True,
            "local_only": True,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": DISABLED_EXECUTION_DOMAIN,
        "subdomain": "result_claim_disabled",
        "total_disabled_claims": len(df),
        "all_claims_disabled": True,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
