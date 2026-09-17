# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Risk Execution Disabled Report.

Documents that real risk reporting, limit enforcement, and VaR monitoring are disabled.
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


def build_final_delivery_risk_execution_disabled_report(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build risk execution disabled report DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = [
        {"action": "risk_limit_enforcement", "disabled": True, "reason": "Real risk limit enforcement disabled"},
        {"action": "exposure_attribution_execution", "disabled": True, "reason": "Real exposure attribution disabled"},
        {"action": "drawdown_monitoring_execution", "disabled": True, "reason": "Real drawdown monitoring disabled"},
    ]

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "risk_execution_disabled": True,
        "actions_blocked": len(rows),
        "execution_code": EXECUTION_CONTRACT_ONLY,
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
