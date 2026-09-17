# -*- coding: utf-8 -*-
"""Phase 158: Telegram Interface Integration Placeholders.

Registers contracts and placeholders for the non-live Telegram interface.
Does NOT send real network messages or expose credentials.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile


def build_telegram_interface_integration_placeholder_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Telegram interface placeholder DataFrame and summary."""
    items = [
        {"item_id": "TGM-001", "feature": "status_broadcast", "placeholder_type": "contract_only", "network_call_allowed": False, "status": "PLACEHOLDER_READY"},
        {"item_id": "TGM-002", "feature": "operator_alerts", "placeholder_type": "contract_only", "network_call_allowed": False, "status": "PLACEHOLDER_READY"},
        {"item_id": "TGM-003", "feature": "summary_digest", "placeholder_type": "contract_only", "network_call_allowed": False, "status": "PLACEHOLDER_READY"},
    ]
    df = pd.DataFrame(items)
    summary = {
        "active_profile": profile.profile_name,
        "total_placeholders": len(df),
        "all_network_blocked": not bool(df["network_call_allowed"].any()),
        "status": "full_system_integration_ready",
        "non_signal": True,
    }
    return df, summary
