# -*- coding: utf-8 -*-
"""Phase 146: Backtest Benchmark Disabled Report.

Enforces that strategy benchmarking and alpha comparison are deferred until subsequent phases.
"""

from typing import Any, Dict, Tuple, Union
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

BLOCKED_BENCHMARK_ACTIONS = [
    "benchmark",
    "run_benchmark",
    "compare_benchmark",
    "sp500_benchmark",
]


def build_backtest_benchmark_disabled_report(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of disabled benchmark rules."""
    rows = [
        {
            "execution_type": "BENCHMARK_COMPARISON_EXECUTION",
            "status": "DEFERRED_TO_PHASE_147_151",
            "reason": "Strategy benchmarking is deferred to Phase 147 (OOS Benchmarking) and Phase 151.",
            "blocked_actions": str(BLOCKED_BENCHMARK_ACTIONS),
            "is_blocked": True,
            "non_signal": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "execution_type": "BENCHMARK_COMPARISON_EXECUTION",
        "is_blocked": True,
        "policy_active": True,
        "non_signal": True,
    }
    return df, summary


def validate_no_benchmark_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that request does not trigger benchmark execution."""
    req_str = str(request).lower()
    for action in BLOCKED_BENCHMARK_ACTIONS:
        if action in req_str:
            return {
                "permitted": False,
                "action_found": action,
                "reason": f"Benchmark comparison request '{action}' is deferred.",
            }
    return {"permitted": True, "reason": "No benchmark request detected."}
