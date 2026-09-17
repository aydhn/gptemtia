# -*- coding: utf-8 -*-
"""Phase 150: Backtest Governance Execution Disabled Report.

Documents the complete disabling of backtest and benchmark execution engines in Phase 150.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    DISABLED_EXECUTION_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
    EXEC_BLOCKED_NO_BACKTEST,
)

DISABLED_BACKTEST_OPS: List[Dict[str, Any]] = [
    {
        "operation_name": "run_backtest",
        "description": "Historical backtest execution engine across bar feeds.",
        "status": "DISABLED",
    },
    {
        "operation_name": "execute_backtest",
        "description": "Execution wrapper for multi-asset strategy runs.",
        "status": "DISABLED",
    },
    {
        "operation_name": "run_benchmark",
        "description": "Benchmark simulation and relative return generation.",
        "status": "DISABLED",
    },
]

FORBIDDEN_EXEC_WORDS = ["run_backtest", "execute_backtest", "run_benchmark"]


def validate_no_backtest_governance_execution_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate request ensures zero backtest or benchmark execution."""
    text = str(request).lower()
    blocked = False
    violating_words: List[str] = []

    for word in FORBIDDEN_EXEC_WORDS:
        if word in text:
            blocked = True
            violating_words.append(word)

    return {
        "is_allowed": not blocked,
        "is_blocked": blocked,
        "violating_words": violating_words,
        "decision": EXEC_BLOCKED_NO_BACKTEST if blocked else "ALLOWED_CONTRACT_ONLY",
        "policy_message": (
            f"Backtest execution is disabled: violating words {violating_words}. Phase 150 is contract-only."
            if blocked
            else "Complies with zero backtest execution policy."
        ),
        "non_signal": True,
    }


def build_backtest_governance_execution_disabled_report(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for backtest execution disabled report."""
    rows: List[Dict[str, Any]] = []
    for op in DISABLED_BACKTEST_OPS:
        rows.append({
            "operation_name": op["operation_name"],
            "description": op["description"],
            "status": op["status"],
            "execution_permitted": False,
            "phase": profile.current_phase,
            "non_signal": True,
            "local_only": True,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": DISABLED_EXECUTION_DOMAIN,
        "subdomain": "backtest_execution_disabled",
        "total_disabled_operations": len(df),
        "all_executions_disabled": True,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
