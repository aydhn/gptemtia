# -*- coding: utf-8 -*-
"""Phase 150: Backtest Prediction Disabled Report.

Documents the complete disabling of prediction, inference, and signal generation in Phase 150.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    DISABLED_EXECUTION_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
    EXEC_BLOCKED_NO_PREDICTION,
)

DISABLED_PREDICTION_OPS: List[Dict[str, Any]] = [
    {
        "operation_name": "model_predict",
        "description": "Running forward prediction or model inference on sample bars.",
        "status": "DISABLED",
    },
    {
        "operation_name": "generate_signals",
        "description": "Generating directional buy/sell trading signals from features.",
        "status": "DISABLED",
    },
    {
        "operation_name": "predict_proba",
        "description": "Evaluating classification probabilities or forecast likelihoods.",
        "status": "DISABLED",
    },
]

FORBIDDEN_PREDICTION_WORDS = [
    "predict",
    "inference",
    "forecast",
    "generate_signals",
    "score_samples",
    "predict_proba",
    "forward_pass",
]


def validate_no_backtest_prediction_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate request ensures zero prediction, inference, or signal generation."""
    text = str(request).lower()
    blocked = False
    violating_words: List[str] = []

    for word in FORBIDDEN_PREDICTION_WORDS:
        if word in text:
            blocked = True
            violating_words.append(word)

    return {
        "is_allowed": not blocked,
        "is_blocked": blocked,
        "violating_words": violating_words,
        "decision": EXEC_BLOCKED_NO_PREDICTION if blocked else "ALLOWED_CONTRACT_ONLY",
        "policy_message": (
            f"Prediction and inference are disabled: violating words {violating_words}. Phase 150 is contract governance only."
            if blocked
            else "Complies with zero prediction policy."
        ),
        "non_signal": True,
    }


def build_backtest_prediction_disabled_report(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for prediction disabled report."""
    rows: List[Dict[str, Any]] = []
    for op in DISABLED_PREDICTION_OPS:
        rows.append({
            "operation_name": op["operation_name"],
            "description": op["description"],
            "status": op["status"],
            "prediction_permitted": False,
            "phase": profile.current_phase,
            "non_signal": True,
            "local_only": True,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": DISABLED_EXECUTION_DOMAIN,
        "subdomain": "prediction_disabled",
        "total_disabled_operations": len(df),
        "all_predictions_disabled": True,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
