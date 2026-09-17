# -*- coding: utf-8 -*-
"""Phase 146: Backtest Model Training Disabled Report.

Enforces zero model training, zero model fitting, and zero weights persistence in backtesting phase.
"""

from typing import Any, Dict, Tuple, Union
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

BLOCKED_TRAINING_ACTIONS = [
    "train",
    "fit",
    "retrain",
    "fine_tune",
    "learn",
]


def build_backtest_model_training_disabled_report(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of disabled model training rules."""
    rows = [
        {
            "execution_type": "MODEL_TRAINING_EXECUTION",
            "status": "BLOCKED_BY_POLICY",
            "reason": "Model training and fitting are strictly disabled in Phase 146.",
            "blocked_actions": str(BLOCKED_TRAINING_ACTIONS),
            "is_blocked": True,
            "non_signal": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "execution_type": "MODEL_TRAINING_EXECUTION",
        "is_blocked": True,
        "policy_active": True,
        "non_signal": True,
    }
    return df, summary


def validate_no_model_training_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that request does not trigger model training."""
    req_str = str(request).lower()
    for action in BLOCKED_TRAINING_ACTIONS:
        if action in req_str:
            return {
                "permitted": False,
                "action_found": action,
                "reason": f"Model training action '{action}' is strictly prohibited in Phase 146.",
            }
    return {"permitted": True, "reason": "No model training detected."}
