# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Portfolio Execution Disabled Report.

Documents that live portfolio construction, sizing, and optimization are disabled.
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


def build_final_delivery_portfolio_execution_disabled_report(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build portfolio execution disabled report DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = [
        {"action": "portfolio_construction", "disabled": True, "reason": "Real portfolio construction disabled"},
        {"action": "portfolio_optimization", "disabled": True, "reason": "Real portfolio optimization disabled"},
        {"action": "capital_allocation", "disabled": True, "reason": "Real capital allocation disabled"},
    ]

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "portfolio_execution_disabled": True,
        "actions_blocked": len(rows),
        "execution_code": EXECUTION_CONTRACT_ONLY,
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
