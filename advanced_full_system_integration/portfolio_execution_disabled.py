# -*- coding: utf-8 -*-
"""Phase 158: Portfolio Execution Disabled Report.

Certifies and enforces that portfolio construction and optimization executions are disabled.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemDisabledExecutionItem


def build_portfolio_execution_disabled_report(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build portfolio execution disabled report DataFrame and summary."""
    items = [
        SystemDisabledExecutionItem(
            item_id="PXD-001",
            execution_type="portfolio_optimizer_run",
            is_disabled=True,
            blocking_reason="Portfolio quadratic/convex optimization execution is disabled.",
        ),
        SystemDisabledExecutionItem(
            item_id="PXD-002",
            execution_type="capital_allocation_generation",
            is_disabled=True,
            blocking_reason="Generating active capital allocation weights is disabled.",
        ),
    ]
    df = pd.DataFrame([item.__dict__ for item in items])
    summary = {
        "active_profile": profile.profile_name,
        "total_items": len(df),
        "all_disabled": bool(df["is_disabled"].all()),
        "status": "execution_blocked_no_portfolio",
        "non_signal": True,
    }
    return df, summary
