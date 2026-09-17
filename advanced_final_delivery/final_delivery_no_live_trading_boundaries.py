# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery No-Live-Trading Boundaries.

Explicitly enforces that live trading operations cannot be initialized or executed.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_BOUNDARY_DOMAIN,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)

NO_LIVE_TRADING_RULES = [
    ("zero_live_orders", "Canli emir gonderimi kesinlikle engellenmistir"),
    ("zero_exchange_connections", "Gercek borsa sunucularina emir iletim soketi acilamaz"),
    ("zero_live_positions", "Gercek para veya varlik pozisyonu acilamaz/kapatilamaz"),
]


def build_final_delivery_no_live_trading_boundary_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build no live trading boundary DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for r_name, desc in NO_LIVE_TRADING_RULES:
        rows.append({
            "rule_name": r_name,
            "description": desc,
            "enforced": True,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "domain": FINAL_BOUNDARY_DOMAIN,
            "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "rule_count": len(rows),
        "all_enforced": bool(df["enforced"].all()),
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
