# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Scenario Execution Disabled Report.

Documents that real portfolio scenario simulation and stress execution are disabled.
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


def build_final_delivery_scenario_execution_disabled_report(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build scenario execution disabled report DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = [
        {"action": "scenario_simulation", "disabled": True, "reason": "Real scenario simulation disabled"},
        {"action": "crisis_replay_execution", "disabled": True, "reason": "Real crisis replay disabled"},
        {"action": "drawdown_control_execution", "disabled": True, "reason": "Real drawdown control disabled"},
    ]

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "scenario_execution_disabled": True,
        "actions_blocked": len(rows),
        "execution_code": EXECUTION_CONTRACT_ONLY,
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
