# -*- coding: utf-8 -*-
"""Phase 148: Stress Metric Calculation Disabled Report.

Strictly blocks real computation of stress PnL, VaR, Expected Shortfall, and Drawdown.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import StressDisabledExecutionItem


def build_stress_metric_calculation_disabled_report(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a report certifying that real stress metric calculation is strictly disabled."""
    item = StressDisabledExecutionItem(
        execution_name="stress_metric_calculation",
        prohibited_reason="Phase 148 defines metric placeholders; real calculation is prohibited.",
        blocked_actions=[
            "calculate_stressed_pnl",
            "calculate_var",
            "calculate_expected_shortfall",
            "calculate_drawdown",
        ],
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


def validate_no_stress_metric_calculation_request(request: Any) -> Dict[str, Any]:
    """Inspect request to ensure no real stress metric computation is triggered."""
    req_text = str(request).lower()
    blocked_patterns = [
        "calculate_stressed_pnl",
        "calculate_var",
        "calculate_expected_shortfall",
        "calculate_drawdown",
    ]
    violations = [p for p in blocked_patterns if p in req_text]
    return {
        "is_safe": len(violations) == 0,
        "violations": violations,
        "action_taken": "BLOCKED" if len(violations) > 0 else "PASSED",
        "non_signal": True,
    }
