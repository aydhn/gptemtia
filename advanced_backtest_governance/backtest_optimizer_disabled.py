# -*- coding: utf-8 -*-
"""Phase 150: Backtest Optimizer Disabled Report.

Documents the complete disabling of parameter optimization and tuning engines in Phase 150.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    DISABLED_EXECUTION_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
    EXEC_BLOCKED_NO_OPTIMIZER,
)

DISABLED_OPTIMIZER_OPS: List[Dict[str, Any]] = [
    {
        "operation_name": "grid_search",
        "description": "Exhaustive grid search across strategy parameter grids.",
        "status": "DISABLED",
    },
    {
        "operation_name": "random_search",
        "description": "Random sampling optimization over parameter spaces.",
        "status": "DISABLED",
    },
    {
        "operation_name": "bayesian_optimization",
        "description": "Sequential model-based optimization / Gaussian process tuning.",
        "status": "DISABLED",
    },
    {
        "operation_name": "genetic_algorithm",
        "description": "Evolutionary parameter optimization and selection.",
        "status": "DISABLED",
    },
    {
        "operation_name": "optuna_tune",
        "description": "Automated hyperparameter optimization framework integration.",
        "status": "DISABLED",
    },
]

FORBIDDEN_OPTIMIZER_WORDS = [
    "optimize",
    "grid_search",
    "random_search",
    "bayesian_optimization",
    "genetic_algorithm",
    "hyperopt",
    "optuna",
    "fit_parameters",
    "tune_parameters",
    "parameter_sweep",
]


def validate_no_backtest_optimizer_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate request ensures zero parameter optimization or tuning execution."""
    text = str(request).lower()
    blocked = False
    violating_words: List[str] = []

    for word in FORBIDDEN_OPTIMIZER_WORDS:
        if word in text:
            blocked = True
            violating_words.append(word)

    return {
        "is_allowed": not blocked,
        "is_blocked": blocked,
        "violating_words": violating_words,
        "decision": EXEC_BLOCKED_NO_OPTIMIZER if blocked else "ALLOWED_CONTRACT_ONLY",
        "policy_message": (
            f"Parameter optimization is disabled: violating words {violating_words}. Phase 150 enforces fixed contract governance."
            if blocked
            else "Complies with zero parameter optimization policy."
        ),
        "non_signal": True,
    }


def build_backtest_optimizer_disabled_report(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for backtest optimizer disabled report."""
    rows: List[Dict[str, Any]] = []
    for op in DISABLED_OPTIMIZER_OPS:
        rows.append({
            "operation_name": op["operation_name"],
            "description": op["description"],
            "status": op["status"],
            "optimization_permitted": False,
            "phase": profile.current_phase,
            "non_signal": True,
            "local_only": True,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": DISABLED_EXECUTION_DOMAIN,
        "subdomain": "optimizer_disabled",
        "total_disabled_operations": len(df),
        "all_optimizers_disabled": True,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
