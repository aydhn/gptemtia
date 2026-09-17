# -*- coding: utf-8 -*-
"""Phase 146: Backtest Metadata-Only News Guards.

Enforces strict metadata-only usage for news inputs in backtesting (zero full-text, zero raw HTML, zero embeddings).
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

FORBIDDEN_NEWS_COLUMNS = [
    "full_text",
    "article_body",
    "raw_content",
    "scraped_html",
    "page_html",
    "html",
    "embedding",
    "vector",
    "sentiment",
    "sentiment_score",
]


def build_backtest_metadata_only_news_guard_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of metadata-only news guards."""
    rules = [
        {
            "guard_name": "metadata_only_news_compliance",
            "enforcement": "STRICT",
            "description": "Haber verilerinde yalnizca baslik, zaman, kaynak ve etiketlerin kullanilmasi zorunlulugu.",
            "forbidden_columns": str(FORBIDDEN_NEWS_COLUMNS),
            "active": True,
        }
    ]
    df = pd.DataFrame(rules)
    summary = summarize_backtest_metadata_only_news_guards(df)
    return df, summary


def validate_backtest_metadata_only_news_columns(column_names: List[str]) -> Dict[str, Any]:
    """Validate that news columns contain zero full-text or embedding attributes."""
    violations = []
    col_lower = [c.lower() for c in column_names]
    for pattern in FORBIDDEN_NEWS_COLUMNS:
        for c in col_lower:
            if pattern == c or pattern in c:
                violations.append(c)
    violations = sorted(list(set(violations)))
    return {
        "is_clean": len(violations) == 0,
        "violations": violations,
        "checked_columns_count": len(column_names),
    }


def validate_news_payload_metadata_only(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Validate that news payload dict does not contain forbidden keys."""
    res = validate_backtest_metadata_only_news_columns(list(payload.keys()))
    return {
        "is_valid": res["is_clean"],
        "violations": res["violations"],
    }


def summarize_backtest_metadata_only_news_guards(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize metadata-only news guards."""
    return {
        "total_guards": len(df),
        "zero_full_text_enforced": True,
        "zero_html_scraping_enforced": True,
        "non_signal": True,
    }

