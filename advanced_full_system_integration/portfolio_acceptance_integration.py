# -*- coding: utf-8 -*-
"""Phase 158: Portfolio Acceptance Integration Registry.

Integrates portfolio construction, position sizing, optimization, and acceptance contracts.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile


def build_portfolio_acceptance_integration_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build portfolio acceptance integration DataFrame and summary."""
    items = [
        {"item_id": "PAI-001", "portfolio_layer": "portfolio_construction", "status": "INTEGRATED", "execution_allowed": False, "verified": True},
        {"item_id": "PAI-002", "portfolio_layer": "portfolio_optimization", "status": "INTEGRATED", "execution_allowed": False, "verified": True},
        {"item_id": "PAI-003", "portfolio_layer": "portfolio_acceptance_report", "status": "INTEGRATED", "execution_allowed": False, "verified": True},
    ]
    df = pd.DataFrame(items)
    summary = {
        "active_profile": profile.profile_name,
        "total_layers": len(df),
        "all_execution_blocked": not bool(df["execution_allowed"].any()),
        "all_verified": bool(df["verified"].all()),
        "status": "full_system_integration_ready",
        "non_signal": True,
    }
    return df, summary
