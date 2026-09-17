# -*- coding: utf-8 -*-
"""Phase 148: Stress Live Trading Disabled Report.

Strictly blocks live trading, real capital execution, and position management.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import StressDisabledExecutionItem


def build_stress_live_trading_disabled_report(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a report certifying that live trading is strictly disabled."""
    item = StressDisabledExecutionItem(
        execution_name="stress_live_trading",
        prohibited_reason="Phase 148 is local/offline research only; live trading is strictly prohibited.",
        blocked_actions=["live_trade", "open_position", "execute_trade", "buy", "sell", "long", "short"],
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


def validate_no_stress_live_trading_request(request: Any) -> Dict[str, Any]:
    """Inspect request to ensure no live trading action is requested."""
    req_text = str(request).lower()
    blocked_patterns = ["live_trade", "open_position", "execute_trade", "buy", "sell", "long", "short"]
    violations = [p for p in blocked_patterns if p in req_text]
    return {
        "is_safe": len(violations) == 0,
        "violations": violations,
        "action_taken": "BLOCKED" if len(violations) > 0 else "PASSED",
        "non_signal": True,
    }
