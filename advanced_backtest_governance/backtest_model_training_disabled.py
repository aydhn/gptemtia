# -*- coding: utf-8 -*-
"""Phase 150: Backtest Model Training Disabled Report.

Documents the complete disabling of model training and fitting operations in Phase 150.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    DISABLED_EXECUTION_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
    EXEC_BLOCKED_NO_MODEL_TRAINING,
)

DISABLED_TRAINING_OPS: List[Dict[str, Any]] = [
    {
        "operation_name": "train_model",
        "description": "Fitting supervised or unsupervised ML models on dataset splits.",
        "status": "DISABLED",
    },
    {
        "operation_name": "fine_tune",
        "description": "Fine-tuning pre-trained weights or representations.",
        "status": "DISABLED",
    },
    {
        "operation_name": "gradient_update",
        "description": "Gradient descent step or backpropagation execution.",
        "status": "DISABLED",
    },
]

FORBIDDEN_TRAINING_WORDS = [
    "train_model",
    "model.fit",
    "fit(",
    "train_network",
    "sgd_step",
    "backprop",
    "fine_tune",
    "gradient_descent",
    "xgboost.train",
    "lightgbm.train",
    "fit_classifier",
]


def validate_no_backtest_model_training_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate request ensures zero ML model training or fitting."""
    text = str(request).lower()
    blocked = False
    violating_words: List[str] = []

    for word in FORBIDDEN_TRAINING_WORDS:
        if word in text:
            blocked = True
            violating_words.append(word)

    return {
        "is_allowed": not blocked,
        "is_blocked": blocked,
        "violating_words": violating_words,
        "decision": EXEC_BLOCKED_NO_MODEL_TRAINING if blocked else "ALLOWED_CONTRACT_ONLY",
        "policy_message": (
            f"Model training is disabled: violating words {violating_words}. Phase 150 is contract governance only."
            if blocked
            else "Complies with zero model training policy."
        ),
        "non_signal": True,
    }


def build_backtest_model_training_disabled_report(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for model training disabled report."""
    rows: List[Dict[str, Any]] = []
    for op in DISABLED_TRAINING_OPS:
        rows.append({
            "operation_name": op["operation_name"],
            "description": op["description"],
            "status": op["status"],
            "training_permitted": False,
            "phase": profile.current_phase,
            "non_signal": True,
            "local_only": True,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": DISABLED_EXECUTION_DOMAIN,
        "subdomain": "model_training_disabled",
        "total_disabled_operations": len(df),
        "all_model_training_disabled": True,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
