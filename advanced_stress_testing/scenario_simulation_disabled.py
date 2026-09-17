# -*- coding: utf-8 -*-
"""Phase 148: Scenario Simulation Disabled Report.

Strictly blocks real scenario simulation runs, keeping scenario contracts in metadata-only mode.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import StressDisabledExecutionItem


def build_scenario_simulation_disabled_report(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a report certifying that real scenario simulation execution is strictly disabled."""
    item = StressDisabledExecutionItem(
        execution_name="scenario_simulation_execution",
        prohibited_reason="Phase 148 is scenario contract layer; real scenario simulation is prohibited.",
        blocked_actions=["simulate_scenario", "run_scenario", "execute_scenario_simulation"],
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


def validate_no_scenario_simulation_request(request: Any) -> Dict[str, Any]:
    """Inspect request to ensure no real scenario simulation is requested."""
    req_text = str(request).lower()
    blocked_patterns = ["simulate_scenario", "run_scenario", "execute_scenario_simulation"]
    violations = [p for p in blocked_patterns if p in req_text]
    return {
        "is_safe": len(violations) == 0,
        "violations": violations,
        "action_taken": "BLOCKED" if len(violations) > 0 else "PASSED",
        "non_signal": True,
    }
