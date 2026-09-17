# -*- coding: utf-8 -*-
"""Phase 148: Stress Execution Disabled Report.

Strictly blocks real stress test execution, ensuring contracts remain in metadata-only mode.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import StressDisabledExecutionItem


def build_stress_execution_disabled_report(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a report certifying that real stress test execution is strictly disabled."""
    item = StressDisabledExecutionItem(
        execution_name="stress_test_execution",
        prohibited_reason="Phase 148 is local/offline contract layer; real stress execution is prohibited.",
        blocked_actions=["run_stress_test", "execute_stress_test", "trigger_stress_run"],
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


def validate_no_stress_execution_request(request: Any) -> Dict[str, Any]:
    """Inspect request to ensure no real stress test run is requested."""
    req_text = str(request).lower()
    blocked_patterns = ["run_stress_test", "execute_stress_test", "trigger_stress_run"]
    violations = [p for p in blocked_patterns if p in req_text]
    return {
        "is_safe": len(violations) == 0,
        "violations": violations,
        "action_taken": "BLOCKED" if len(violations) > 0 else "PASSED",
        "non_signal": True,
    }
