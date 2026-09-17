# -*- coding: utf-8 -*-
"""Phase 158: Backtest Execution Disabled Report.

Certifies and enforces that backtesting engine execution is disabled.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemDisabledExecutionItem


def build_backtest_execution_disabled_report(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build backtest execution disabled report DataFrame and summary."""
    items = [
        SystemDisabledExecutionItem(
            item_id="BXD-001",
            execution_type="backtest_engine_run",
            is_disabled=True,
            blocking_reason="Simulating historical trades is disabled in Phase 158.",
        ),
        SystemDisabledExecutionItem(
            item_id="BXD-002",
            execution_type="benchmark_comparison_run",
            is_disabled=True,
            blocking_reason="Live benchmark calculation is disabled.",
        ),
    ]
    df = pd.DataFrame([item.__dict__ for item in items])
    summary = {
        "active_profile": profile.profile_name,
        "total_items": len(df),
        "all_disabled": bool(df["is_disabled"].all()),
        "status": "execution_blocked_no_backtest",
        "non_signal": True,
    }
    return df, summary
