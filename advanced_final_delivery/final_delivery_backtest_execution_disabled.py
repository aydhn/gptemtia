# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Backtest Execution Disabled Report.

Documents that backtest simulations and benchmark runs are disabled.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_DISABLED_EXECUTION_DOMAIN,
    EXECUTION_CONTRACT_ONLY,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)


def build_final_delivery_backtest_execution_disabled_report(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build backtest execution disabled report DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = [
        {"action": "backtest_simulation", "disabled": True, "reason": "Real backtest simulation disabled"},
        {"action": "benchmark_execution", "disabled": True, "reason": "Real benchmark execution disabled"},
        {"action": "walk_forward_execution", "disabled": True, "reason": "Real walk-forward execution disabled"},
    ]

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "backtest_execution_disabled": True,
        "actions_blocked": len(rows),
        "execution_code": EXECUTION_CONTRACT_ONLY,
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
