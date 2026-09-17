# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery No-Scraping Boundaries.

Prohibits unauthorized web scraping, HTML downloading, and credential leakage.
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

NO_SCRAPING_RULES = [
    ("zero_web_scraping", "Web sitelerinden otomatik veri kazima yasaktir"),
    ("zero_html_downloads", "Haber tam metni veya ham HTML indirme yasaktir"),
    ("zero_credential_exposure", "API anahtarlari, token veya gizli sifreler yazdirilamaz"),
]


def build_final_delivery_no_scraping_boundary_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build no scraping boundary DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for r_name, desc in NO_SCRAPING_RULES:
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
