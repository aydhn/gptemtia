# -*- coding: utf-8 -*-
"""Phase 147: Walk-Forward Execution Disabled Report.

Documents and strictly enforces the disabled state of actual walk-forward simulation execution.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile


def build_walk_forward_execution_disabled_report(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for disabled walk-forward execution."""
    rows = [
        {
            "execution_path": "walk_forward_simulation_engine",
            "is_blocked": True,
            "reason": "Phase 147 is strictly contract and metadata specification layer; actual walk-forward simulation is blocked by policy.",
            "enforced": True,
            "non_signal": True,
        },
        {
            "execution_path": "rolling_window_execution_runner",
            "is_blocked": True,
            "reason": "Rolling window backtest loop execution is disabled.",
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


def validate_no_walk_forward_execution_request(
    request: Union[Dict[str, Any], str],
) -> Dict[str, Any]:
    """Validate that request does not attempt walk-forward simulation execution."""
    req_str = request if isinstance(request, str) else str(request.get("command", ""))
    req_lower = req_str.lower()
    blocked_keywords = ["run_walk_forward", "execute_walk_forward", "run_oos"]
    is_blocked = any(k in req_lower for k in blocked_keywords)
    return {
        "request": req_str,
        "is_safe": not is_blocked,
        "is_blocked": is_blocked,
        "action": "BLOCKED_BY_POLICY" if is_blocked else "ALLOWED_CONTRACT_SPEC",
        "message": "Gercek walk-forward calistirma engellendi." if is_blocked else "Talep guvenli.",
        "non_signal": True,
    }
