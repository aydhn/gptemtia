# -*- coding: utf-8 -*-
"""Phase 148: Stress Metadata-Only News Guards.

Enforces metadata-only news usage in stress scenario contexts.
Strictly blocks full articles, raw scraped HTML, body text, embeddings, and sentiment outputs.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import StressGuardItem

PROHIBITED_NEWS_COLUMNS = [
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


def build_stress_metadata_only_news_guard_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of metadata-only news guards."""
    guard = StressGuardItem(
        guard_name="stress_metadata_only_news_guard",
        guard_type="METADATA_ONLY",
        description="Stres senaryolarında haber metinleri, gövde yazıları, kazınmış HTML ve embedding kullanımını engeller.",
        enforcement_level="STRICT",
        active=True,
        violating_columns=PROHIBITED_NEWS_COLUMNS,
    )
    rows = [
        {
            "guard_name": guard.guard_name,
            "guard_type": guard.guard_type,
            "description": guard.description,
            "enforcement_level": guard.enforcement_level,
            "active": guard.active,
            "prohibited_column_count": len(guard.violating_columns),
            "non_signal": True,
            "local_only": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "guard_active": guard.active,
        "enforcement_level": guard.enforcement_level,
        "prohibited_columns": guard.violating_columns,
        "non_signal": True,
    }
    return df, summary


def validate_stress_metadata_only_news_columns(column_names: List[str]) -> Dict[str, Any]:
    """Inspect columns to ensure no prohibited full article or embedding fields are present."""
    normalized = [c.lower().strip() for c in column_names]
    violations = [c for c in normalized if c in PROHIBITED_NEWS_COLUMNS]
    return {
        "has_violations": len(violations) > 0,
        "violating_columns": violations,
        "is_safe": len(violations) == 0,
        "action_taken": "BLOCKED" if len(violations) > 0 else "PASSED",
        "non_signal": True,
    }
