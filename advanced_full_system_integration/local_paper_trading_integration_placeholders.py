# -*- coding: utf-8 -*-
"""Phase 158: Local Paper Trading Integration Placeholders.

Registers contracts and placeholders for local offline simulated trade replay.
Does NOT generate real orders, execute live trades, or touch broker APIs.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile


def build_local_paper_trading_integration_placeholder_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build local paper trading placeholder DataFrame and summary."""
    items = [
        {"item_id": "PTR-001", "capability": "simulated_order_buffer", "execution_allowed": False, "status": "PLACEHOLDER_READY", "notes": "In-memory simulation buffer only."},
        {"item_id": "PTR-002", "capability": "fill_simulation_model", "execution_allowed": False, "status": "PLACEHOLDER_READY", "notes": "Offline transaction cost and slippage replay."},
        {"item_id": "PTR-003", "capability": "position_tracker_mock", "execution_allowed": False, "status": "PLACEHOLDER_READY", "notes": "Local mock portfolio balance tracker."},
    ]
    df = pd.DataFrame(items)
    summary = {
        "active_profile": profile.profile_name,
        "total_capabilities": len(df),
        "all_execution_blocked": not bool(df["execution_allowed"].any()),
        "status": "full_system_integration_ready",
        "non_signal": True,
    }
    return df, summary
