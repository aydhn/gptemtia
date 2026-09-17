# -*- coding: utf-8 -*-
"""Phase 150: Backtest Metadata-Only News Guards.

Enforces strict metadata-only constraints on news and unstructured text inputs,
blocking raw article text, scraped HTML, vectors, embeddings, and sentiment model outputs.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    SAFETY_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

METADATA_ONLY_RULES: List[Dict[str, Any]] = [
    {
        "guard_id": "NEWS_01_NO_FULL_TEXT",
        "guard_name": "full_article_text_prohibition",
        "description": "Prohibit storing, indexing, or processing raw news article body text or full text.",
        "enforcement": "BLOCKING_ZERO_TOLERANCE",
    },
    {
        "guard_id": "NEWS_02_NO_SCRAPED_HTML",
        "guard_name": "scraped_html_prohibition",
        "description": "Forbid raw HTML pages, DOM scraping dumps, or browser page dumps.",
        "enforcement": "BLOCKING_ZERO_TOLERANCE",
    },
    {
        "guard_id": "NEWS_03_NO_EMBEDDINGS_VECTORS",
        "guard_name": "embedding_vector_prohibition",
        "description": "Prohibit generating or storing LLM dense embeddings or vector database representations.",
        "enforcement": "BLOCKING_ZERO_TOLERANCE",
    },
    {
        "guard_id": "NEWS_04_NO_SENTIMENT_MODEL_OUTPUTS",
        "guard_name": "sentiment_score_prohibition",
        "description": "Disallow NLP model sentiment score generation; allow only structured tags and release timestamps.",
        "enforcement": "BLOCKING_ZERO_TOLERANCE",
    },
]

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


def validate_backtest_metadata_only_news_columns(column_names: List[str]) -> Dict[str, Any]:
    """Audit column names against metadata-only news boundaries."""
    violating_columns: List[str] = []
    for col in column_names:
        c_lower = col.lower()
        for forbidden in FORBIDDEN_NEWS_COLUMNS:
            if forbidden in c_lower:
                violating_columns.append(col)
                break

    is_clean = len(violating_columns) == 0
    return {
        "is_clean": is_clean,
        "is_blocked": not is_clean,
        "violating_columns": violating_columns,
        "decision": "PASS" if is_clean else "BLOCKED_BY_METADATA_ONLY_GUARD",
        "policy_message": (
            "Metadata-only audit passed. No full-text or embedding columns present."
            if is_clean
            else f"Forbidden text/embedding columns detected: {violating_columns}. Operation blocked."
        ),
        "non_signal": True,
    }


def build_backtest_metadata_only_news_guard_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for metadata-only news guards."""
    rows: List[Dict[str, Any]] = []
    for r in METADATA_ONLY_RULES:
        rows.append({
            "guard_id": r["guard_id"],
            "guard_name": r["guard_name"],
            "description": r["description"],
            "enforcement": r["enforcement"],
            "status": "ACTIVE",
            "non_signal": True,
            "local_only": True,
            "phase": profile.current_phase,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": SAFETY_DOMAIN,
        "subdomain": "metadata_only_news_guards",
        "total_guards": len(df),
        "all_active": True,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
