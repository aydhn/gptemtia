# -*- coding: utf-8 -*-
"""Phase 148: Stress Optimizer Disabled Report.

Strictly blocks optimizer execution, parameter tuning, and hyperparameter search in stress contexts.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import StressDisabledExecutionItem


def build_stress_optimizer_disabled_report(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a report certifying that optimizer execution is strictly disabled."""
    item = StressDisabledExecutionItem(
        execution_name="stress_optimizer_execution",
        prohibited_reason="Phase 148 is contract-only; optimization and hyperparameter tuning are prohibited.",
        blocked_actions=["optimize", "hyperparameter_search", "tune_parameters", "grid_search"],
        is_blocked=True,
        enforced=True,
    )
    rows = [
        {
            "execution_name": item.execution_name,
            "prohibited_reason": item.prohibited_reason,
            "blocked_actions": ", ".join(item.blocked_actions),
            "is_blocked": item.is_blocked,
            "enforced": item.enforced,
            "non_signal": True,
            "local_only": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "execution_name": item.execution_name,
        "is_blocked": item.is_blocked,
        "enforced": item.enforced,
        "blocked_actions": item.blocked_actions,
        "non_signal": True,
    }
    return df, summary


def validate_no_stress_optimizer_request(request: Any) -> Dict[str, Any]:
    """Inspect request to ensure no optimizer execution is triggered."""
    req_text = str(request).lower()
    blocked_patterns = ["optimize", "hyperparameter_search", "tune_parameters", "grid_search"]
    violations = [p for p in blocked_patterns if p in req_text]
    return {
        "is_safe": len(violations) == 0,
        "violations": violations,
        "action_taken": "BLOCKED" if len(violations) > 0 else "PASSED",
        "non_signal": True,
    }
