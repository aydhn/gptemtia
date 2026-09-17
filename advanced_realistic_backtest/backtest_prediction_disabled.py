# -*- coding: utf-8 -*-
"""Phase 146: Backtest Prediction Disabled Report.

Enforces zero model inference, zero prediction generation, and zero target/label creation.
"""

from typing import Any, Dict, Tuple, Union
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

BLOCKED_PREDICTION_ACTIONS = [
    "predict",
    "inference",
    "forecast",
    "generate_target",
    "generate_label",
    "target",
    "label",
]


def build_backtest_prediction_disabled_report(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of disabled prediction rules."""
    rows = [
        {
            "execution_type": "MODEL_PREDICTION_EXECUTION",
            "status": "BLOCKED_BY_POLICY",
            "reason": "Model prediction and target label generation are strictly disabled.",
            "blocked_actions": str(BLOCKED_PREDICTION_ACTIONS),
            "is_blocked": True,
            "non_signal": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "execution_type": "MODEL_PREDICTION_EXECUTION",
        "is_blocked": True,
        "policy_active": True,
        "non_signal": True,
    }
    return df, summary


def validate_no_prediction_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that request does not trigger model predictions."""
    req_str = str(request).lower()
    for action in BLOCKED_PREDICTION_ACTIONS:
        if action in req_str:
            return {
                "permitted": False,
                "action_found": action,
                "reason": f"Prediction request '{action}' is strictly prohibited in Phase 146.",
            }
    return {"permitted": True, "reason": "No prediction request detected."}
