# -*- coding: utf-8 -*-
"""Phase 154: Metadata-Only News Guards."""

from typing import Dict, List, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_optimization_metadata_only_news_guard_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build metadata-only news guard registry."""
    records = [{
        "guard_name": "optimization_metadata_only_news_guard",
        "description": "Haber tam metni, HTML ve NLP gomulmelerini engelleme",
        "is_active": True,
        "action_on_violation": "BLOCK",
    }]
    df = pd.DataFrame(records)
    summary = {
        "guard_name": "optimization_metadata_only_news_guard",
        "is_active": True,
    }
    return df, summary


def validate_optimization_metadata_only_news_columns(column_names: List[str]) -> Dict:
    """Detect and block prohibited raw news text columns."""
    forbidden = ["full_text", "article_body", "raw_content", "scraped_html", "page_html", "html", "embedding", "vector"]
    detected = [c for c in column_names if any(f in c.lower() for f in forbidden)]
    return {
        "is_clean": len(detected) == 0,
        "detected_columns": detected,
        "message": f"Raw news text columns detected: {detected}" if detected else "OK",
    }
