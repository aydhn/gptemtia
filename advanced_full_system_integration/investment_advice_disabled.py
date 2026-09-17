# -*- coding: utf-8 -*-
"""Phase 158: Investment Advice Disabled Report.

Certifies and enforces that investment advice generation is disabled.
"""

from typing import Any, Dict, Tuple, Union
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemDisabledExecutionItem


def build_investment_advice_disabled_report(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build investment advice disabled report DataFrame and summary."""
    items = [
        SystemDisabledExecutionItem(
            item_id="IAD-001",
            execution_type="investment_advice",
            is_disabled=True,
            blocking_reason="Providing investment advice or recommendations is forbidden.",
        ),
        SystemDisabledExecutionItem(
            item_id="IAD-002",
            execution_type="portfolio_endorsement",
            is_disabled=True,
            blocking_reason="Endorsing live portfolio allocations is forbidden.",
        ),
    ]
    df = pd.DataFrame([item.__dict__ for item in items])
    summary = {
        "active_profile": profile.profile_name,
        "total_items": len(df),
        "all_disabled": bool(df["is_disabled"].all()),
        "status": "execution_contract_only",
        "non_signal": True,
    }
    return df, summary


def validate_no_investment_advice_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that incoming payload does not request investment advice."""
    text = str(request).lower()
    forbidden_tokens = ["investment_advice", "portfolio_approved", "strategy_approved"]
    found = [t for t in forbidden_tokens if t in text]
    return {
        "is_safe": len(found) == 0,
        "forbidden_tokens_detected": found,
        "blocked_by_policy": len(found) > 0,
        "non_signal": True,
    }
