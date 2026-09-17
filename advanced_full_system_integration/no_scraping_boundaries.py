# -*- coding: utf-8 -*-
"""Phase 158: No Scraping Boundaries.

Prohibits web scraping, browser automation, paywall bypassing, and hidden API reverse engineering.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemBoundaryItem

SCRAPING_RULES = [
    ("NSC-001", "scraping_boundary", "no_html_scraping", "network", False, "Scraping raw HTML from websites is strictly prohibited."),
    ("NSC-002", "scraping_boundary", "no_browser_automation", "runtime", False, "Using Selenium, Playwright, or Puppeteer is prohibited."),
    ("NSC-003", "scraping_boundary", "no_paywall_bypass", "security", False, "Attempting paywall bypass is strictly prohibited."),
    ("NSC-004", "scraping_boundary", "offline_fixture_usage_permitted", "runtime", True, "Using offline mock fixtures is permitted."),
]


def build_no_scraping_boundary_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build no-scraping boundary registry DataFrame and summary."""
    items = []
    for bid, btype, rname, atype, is_allowed, reason in SCRAPING_RULES:
        item = SystemBoundaryItem(
            boundary_id=bid,
            boundary_type=btype,
            rule_name=rname,
            action_type=atype,
            is_allowed=is_allowed,
            reason=reason,
        )
        items.append(item.__dict__)

    df = pd.DataFrame(items)
    summary = {
        "active_profile": profile.profile_name,
        "total_rules": len(df),
        "prohibited_actions_count": int((df["is_allowed"] == False).sum()),
        "allowed_actions_count": int((df["is_allowed"] == True).sum()),
        "status": "full_system_integration_ready",
        "non_signal": True,
    }
    return df, summary
