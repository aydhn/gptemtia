# -*- coding: utf-8 -*-
"""Phase 155: Risk Reporting Metadata-Only News Guards."""

from typing import Any, Dict, List, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import RiskReportingGuardItem


def build_risk_reporting_metadata_only_news_guard_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for metadata-only news guards."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        RiskReportingGuardItem(
            guard_name="metadata_only_news_guard",
            domain="news_guard",
            guard_rule="Prohibits full article bodies, scraped HTML, and raw text in risk reporting",
            is_active=True,
            action_on_violation="BLOCK",
        ).model_dump()
    ]
    df = pd.DataFrame(rows)
    df["current_phase"] = profile.current_phase
    df["target_final_phase"] = profile.target_final_phase
    df["next_phase"] = profile.next_phase
    return df, {"guard_count": len(df), "all_active": True}


def validate_risk_reporting_metadata_only_news_columns(column_names: List[str]) -> Dict[str, Any]:
    """Validate that news columns contain only allowed metadata."""
    forbidden_news_terms = [
        "full_text",
        "article_body",
        "raw_content",
        "scraped_html",
        "page_html",
        "html",
        "raw_text",
        "body_text",
    ]
    violations = [c for c in column_names if any(t in c.lower() for t in forbidden_news_terms)]
    return {
        "is_valid": len(violations) == 0,
        "violations": violations,
        "action": "BLOCK" if violations else "ALLOW",
    }
