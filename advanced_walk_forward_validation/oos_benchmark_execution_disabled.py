# -*- coding: utf-8 -*-
"""Phase 147: Out-of-Sample Benchmark Execution Disabled Report.

Documents and strictly enforces the disabled state of actual benchmark execution.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile


def build_oos_benchmark_execution_disabled_report(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for disabled benchmark execution."""
    rows = [
        {
            "execution_path": "oos_benchmark_runner",
            "is_blocked": True,
            "reason": "Phase 147 restricts benchmarks to contract/stub mode; real benchmark execution is blocked.",
            "enforced": True,
            "non_signal": True,
        },
        {
            "execution_path": "buy_and_hold_execution_engine",
            "is_blocked": True,
            "reason": "Buy & Hold benchmark backtest execution is disabled.",
            "enforced": True,
            "non_signal": True,
        },
    ]
    df = pd.DataFrame(rows)
    summary = {
        "total_blocked_paths": len(df),
        "all_blocked": True,
        "non_signal": True,
    }
    return df, summary


def validate_no_oos_benchmark_execution_request(
    request: Union[Dict[str, Any], str],
) -> Dict[str, Any]:
    """Validate that request does not attempt benchmark execution."""
    req_str = request if isinstance(request, str) else str(request.get("command", ""))
    req_lower = req_str.lower()
    blocked_keywords = ["run_benchmark", "execute_benchmark", "calculate_benchmark"]
    is_blocked = any(k in req_lower for k in blocked_keywords)
    return {
        "request": req_str,
        "is_safe": not is_blocked,
        "is_blocked": is_blocked,
        "action": "BLOCKED_BY_POLICY" if is_blocked else "ALLOWED_CONTRACT_SPEC",
        "message": "Gercek benchmark calistirma engellendi." if is_blocked else "Talep guvenli.",
        "non_signal": True,
    }
