# -*- coding: utf-8 -*-
"""Phase 158: Risk Execution Disabled Report.

Certifies and enforces that risk engine calculations are disabled.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemDisabledExecutionItem


def build_risk_execution_disabled_report(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build risk execution disabled report DataFrame and summary."""
    items = [
        SystemDisabledExecutionItem(
            item_id="RXD-001",
            execution_type="var_calculation",
            is_disabled=True,
            blocking_reason="Value-at-Risk computation is disabled.",
        ),
        SystemDisabledExecutionItem(
            item_id="RXD-002",
            execution_type="expected_shortfall_calculation",
            is_disabled=True,
            blocking_reason="Expected Shortfall computation is disabled.",
        ),
    ]
    df = pd.DataFrame([item.__dict__ for item in items])
    summary = {
        "active_profile": profile.profile_name,
        "total_items": len(df),
        "all_disabled": bool(df["is_disabled"].all()),
        "status": "execution_blocked_no_risk",
        "non_signal": True,
    }
    return df, summary
