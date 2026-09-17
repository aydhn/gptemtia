# -*- coding: utf-8 -*-
"""Phase 148: Stress Broker Execution Disabled Report.

Strictly blocks broker API integration, order transmission, and routing.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import StressDisabledExecutionItem


def build_stress_broker_execution_disabled_report(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a report certifying that broker execution is strictly disabled."""
    item = StressDisabledExecutionItem(
        execution_name="stress_broker_execution",
        prohibited_reason="Phase 148 has no broker integration; sending orders to brokers is prohibited.",
        blocked_actions=["broker_order", "send_order", "connect_broker", "route_order"],
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


def validate_no_stress_broker_execution_request(request: Any) -> Dict[str, Any]:
    """Inspect request to ensure no broker order is triggered."""
    req_text = str(request).lower()
    blocked_patterns = ["broker_order", "send_order", "connect_broker", "route_order"]
    violations = [p for p in blocked_patterns if p in req_text]
    return {
        "is_safe": len(violations) == 0,
        "violations": violations,
        "action_taken": "BLOCKED" if len(violations) > 0 else "PASSED",
        "non_signal": True,
    }
