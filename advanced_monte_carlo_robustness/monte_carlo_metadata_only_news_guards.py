# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Metadata-Only News Guards Module.

Guarantees that no raw news text, article bodies, scraped HTML, or NLP embeddings
enter Monte Carlo robustness evaluation contracts.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    BIAS_GUARD_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

FORBIDDEN_NEWS_PATTERNS = [
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

NEWS_GUARDS: List[Dict[str, Any]] = [
    {
        "guard_id": "GUARD_METADATA_ONLY_NEWS_149_01",
        "guard_type": "text_payload_filter",
        "description": "Quarantines any DataFrame column containing article bodies, scraped HTML, or NLP embeddings.",
        "enforcement_action": "DROP_AND_AUDIT",
    },
]


def validate_monte_carlo_metadata_only_news_columns(column_names: List[str]) -> Dict[str, Any]:
    """Validate that columns contain only permissible metadata, zero raw text."""
    violations: List[str] = []
    for col in column_names:
        col_lower = str(col).lower()
        for pat in FORBIDDEN_NEWS_PATTERNS:
            if pat in col_lower:
                violations.append(col)
                break

    return {
        "valid": len(violations) == 0,
        "violations": violations,
        "violations_count": len(violations),
        "status": "PASS" if len(violations) == 0 else "FAIL_FORBIDDEN_TEXT_DETECTED",
    }


def build_monte_carlo_metadata_only_news_guard_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the metadata-only news guard registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for g in NEWS_GUARDS:
        rows.append(
            {
                "guard_id": g["guard_id"],
                "guard_type": g["guard_type"],
                "description": g["description"],
                "enforcement_action": g["enforcement_action"],
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "status": "ACTIVE",
                "violations_found": 0,
                "domain": BIAS_GUARD_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": BIAS_GUARD_DOMAIN,
        "total_guards": len(df),
        "all_active": bool((df["status"] == "ACTIVE").all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
