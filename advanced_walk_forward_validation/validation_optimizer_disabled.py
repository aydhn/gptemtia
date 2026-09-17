# -*- coding: utf-8 -*-
"""Phase 147: Validation Optimizer Disabled Report.

Documents and strictly enforces the disabled state of optimizer and hyperparameter search.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile


def build_validation_optimizer_disabled_report(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for disabled optimizer execution."""
    rows = [
        {
            "execution_target": "strategy_optimizer_engine",
            "is_blocked": True,
            "reason": "Faz 147 sozlesme cercevesidir; parametre optimizasyonu kesinlikle yasaktir.",
            "enforced": True,
            "non_signal": True,
        },
        {
            "execution_target": "hyperparameter_grid_search",
            "is_blocked": True,
            "reason": "Hiperparametre aramasi devre disidir.",
            "enforced": True,
            "non_signal": True,
        },
    ]
    df = pd.DataFrame(rows)
    summary = {
        "total_blocked_optimizers": len(df),
        "all_blocked": True,
        "non_signal": True,
    }
    return df, summary


def validate_no_validation_optimizer_request(
    request: Union[Dict[str, Any], str],
) -> Dict[str, Any]:
    """Validate that request does not attempt optimization."""
    req_str = request if isinstance(request, str) else str(request.get("command", ""))
    req_lower = req_str.lower()
    blocked_keywords = ["optimize", "hyperparameter_search", "grid_search", "bayesian_opt"]
    is_blocked = any(k in req_lower for k in blocked_keywords)
    return {
        "request": req_str,
        "is_safe": not is_blocked,
        "is_blocked": is_blocked,
        "message": "Optimizasyon istegi guvenlik geregi engellendi." if is_blocked else "Talep guvenli.",
        "non_signal": True,
    }
