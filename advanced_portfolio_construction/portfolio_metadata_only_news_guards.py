# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Metadata-Only News Guards Module.

Guards that any news or sentiment context used in portfolio construction contracts
remains strictly metadata-only, with no raw text scraping or copyright infringement.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_GUARD_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)

NEWS_METADATA_ALLOWED_FIELDS = [
    "news_id",
    "timestamp",
    "source_domain",
    "sentiment_score",
    "relevance_score",
    "topic_cluster",
    "entity_mentions_count",
]

NEWS_FORBIDDEN_TEXT_FIELDS = [
    "full_article_body",
    "raw_html",
    "scraped_content",
    "copyrighted_text",
    "full_article_text",
]


def build_portfolio_metadata_only_news_guard_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of portfolio metadata-only news guards."""
    rows = [
        {
            "guard_id": "GUARD_PORTFOLIO_METADATA_ONLY_NEWS",
            "guard_name": "Portfolio Metadata-Only News Guard",
            "detection_target": "raw_scraped_text_columns",
            "description": "Portfoy veri setlerinde yalnizca haber metadatasinin kullanilmasini denetleyen muhafiz.",
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "is_active": True,
            "status": PORTFOLIO_CONTRACT_READY,
        },
        {
            "guard_id": "GUARD_NO_FULL_TEXT_SCRAPING",
            "guard_name": "No Full-Text Scraping Guard",
            "detection_target": "article_body_and_raw_html",
            "description": "Haber govde metinleri veya raw HTML'in yuklenmesini engelleyen muhafiz.",
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "is_active": True,
            "status": PORTFOLIO_CONTRACT_READY,
        },
    ]

    df = pd.DataFrame(rows)
    summary = {
        "domain": PORTFOLIO_GUARD_DOMAIN,
        "guard_category": "metadata_only_news",
        "active_profile": profile.profile_name,
        "total_guards": len(df),
        "all_active": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary


def validate_portfolio_news_columns(column_names: List[str]) -> Dict[str, Any]:
    """Validate that columns do not contain raw full-text news fields."""
    detected: List[str] = []
    for col in column_names:
        c_low = str(col).lower()
        for forbidden in NEWS_FORBIDDEN_TEXT_FIELDS:
            if forbidden in c_low:
                detected.append(col)
                break

    is_clean = len(detected) == 0
    return {
        "is_clean": is_clean,
        "violations_detected": not is_clean,
        "detected_columns": detected,
        "status": "PASS" if is_clean else "BLOCKED_BY_METADATA_ONLY_NEWS_GUARD",
        "contract_only": True,
    }
