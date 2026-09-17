# -*- coding: utf-8 -*-
"""Phase 148: Stress Performance Claim Disabled Report.

Strictly blocks marketing claims, return guarantees, production-ready claims, and broker-ready approvals.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import StressDisabledExecutionItem


def build_stress_performance_claim_disabled_report(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a report certifying that performance claims and production approvals are strictly disabled."""
    item = StressDisabledExecutionItem(
        execution_name="stress_performance_claim_disabled",
        prohibited_reason="Phase 148 contracts do not certify live performance or broker readiness.",
        blocked_actions=[
            "guaranteed_return",
            "stressed_return_claim",
            "sharpe_claim",
            "win_rate_claim",
            "production_ready",
            "broker_ready",
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


def validate_no_stress_performance_claim_request(request: Any) -> Dict[str, Any]:
    """Inspect request to ensure no performance or production-ready claims are made."""
    req_text = str(request).lower()
    blocked_patterns = [
        "guaranteed_return",
        "stressed_return_claim",
        "sharpe_claim",
        "win_rate_claim",
        "production_ready",
        "broker_ready",
    ]
    violations = [p for p in blocked_patterns if p in req_text]
    return {
        "is_safe": len(violations) == 0,
        "violations": violations,
        "action_taken": "BLOCKED" if len(violations) > 0 else "PASSED",
        "non_signal": True,
    }
