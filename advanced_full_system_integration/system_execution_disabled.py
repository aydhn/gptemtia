# -*- coding: utf-8 -*-
"""Phase 158: System Execution Disabled Report.

Certifies and enforces that system-wide execution is disabled at contract layer.
"""

from typing import Any, Dict, Tuple, Union
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemDisabledExecutionItem


def build_system_execution_disabled_report(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build system execution disabled report DataFrame and summary."""
    items = [
        SystemDisabledExecutionItem(
            item_id="SED-001",
            execution_type="full_system_execution",
            is_disabled=True,
            blocking_reason="Phase 158 operates strictly as a contract and rehearsal layer.",
        ),
        SystemDisabledExecutionItem(
            item_id="SED-002",
            execution_type="end_to_end_bot_run",
            is_disabled=True,
            blocking_reason="Automated bot execution is forbidden prior to Phase 160.",
        ),
    ]
    df = pd.DataFrame([item.__dict__ for item in items])
    summary = {
        "active_profile": profile.profile_name,
        "total_items": len(df),
        "all_disabled": bool(df["is_disabled"].all()),
        "status": "execution_blocked_no_system_execution",
        "non_signal": True,
    }
    return df, summary


def validate_no_system_execution_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that incoming payload does not request full system execution."""
    text = str(request).lower()
    forbidden_tokens = ["run_system", "execute_system", "end_to_end_run"]
    found = [t for t in forbidden_tokens if t in text]
    return {
        "is_safe": len(found) == 0,
        "forbidden_tokens_detected": found,
        "blocked_by_policy": len(found) > 0,
        "non_signal": True,
    }
