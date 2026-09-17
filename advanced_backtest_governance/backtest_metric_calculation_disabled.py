# -*- coding: utf-8 -*-
"""Phase 150: Backtest Metric Calculation Disabled Report.

Documents the complete disabling of numerical metric calculations in Phase 150.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    DISABLED_EXECUTION_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
    EXEC_BLOCKED_NO_METRIC_CALCULATION,
)

DISABLED_METRIC_OPS: List[Dict[str, Any]] = [
    {"operation_name": "calculate_sharpe", "status": "DISABLED", "reason": "Numerical Sharpe calculation is disabled."},
    {"operation_name": "calculate_win_rate", "status": "DISABLED", "reason": "Numerical win-rate calculation is disabled."},
    {"operation_name": "calculate_alpha", "status": "DISABLED", "reason": "Numerical alpha calculation is disabled."},
    {"operation_name": "calculate_return", "status": "DISABLED", "reason": "Numerical cumulative return calculation is disabled."},
]

FORBIDDEN_METRIC_CALC_WORDS = ["calculate_sharpe", "calculate_win_rate", "calculate_alpha", "calculate_return"]


def validate_no_metric_calculation_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate request ensures zero numerical metric calculation."""
    text = str(request).lower()
    blocked = False
    violating_words: List[str] = []

    for word in FORBIDDEN_METRIC_CALC_WORDS:
        if word in text:
            blocked = True
            violating_words.append(word)

    return {
        "is_allowed": not blocked,
        "is_blocked": blocked,
        "violating_words": violating_words,
        "decision": EXEC_BLOCKED_NO_METRIC_CALCULATION if blocked else "ALLOWED_CONTRACT_ONLY",
        "policy_message": (
            f"Metric calculation is disabled: violating words {violating_words}. Phase 150 is placeholder-only."
            if blocked
            else "Complies with zero metric calculation policy."
        ),
        "non_signal": True,
    }


def build_backtest_metric_calculation_disabled_report(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for metric calculation disabled report."""
    rows: List[Dict[str, Any]] = []
    for op in DISABLED_METRIC_OPS:
        rows.append({
            "operation_name": op["operation_name"],
            "reason": op["reason"],
            "status": op["status"],
            "calculation_permitted": False,
            "phase": profile.current_phase,
            "non_signal": True,
            "local_only": True,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": DISABLED_EXECUTION_DOMAIN,
        "subdomain": "metric_calculation_disabled",
        "total_disabled_calculations": len(df),
        "all_calculations_disabled": True,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
