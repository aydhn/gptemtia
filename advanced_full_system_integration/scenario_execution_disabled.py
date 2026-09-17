# -*- coding: utf-8 -*-
"""Phase 158: Scenario Execution Disabled Report.

Certifies and enforces that scenario stress simulation execution is disabled.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemDisabledExecutionItem


def build_scenario_execution_disabled_report(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build scenario execution disabled report DataFrame and summary."""
    items = [
        SystemDisabledExecutionItem(
            item_id="SXD-001",
            execution_type="scenario_stress_simulation",
            is_disabled=True,
            blocking_reason="Live scenario shock simulation is disabled in Phase 158.",
        ),
        SystemDisabledExecutionItem(
            item_id="SXD-002",
            execution_type="drawdown_circuit_breaker_trigger",
            is_disabled=True,
            blocking_reason="Live circuit breaker intervention execution is disabled.",
        ),
    ]
    df = pd.DataFrame([item.__dict__ for item in items])
    summary = {
        "active_profile": profile.profile_name,
        "total_items": len(df),
        "all_disabled": bool(df["is_disabled"].all()),
        "status": "execution_blocked_no_scenario",
        "non_signal": True,
    }
    return df, summary
