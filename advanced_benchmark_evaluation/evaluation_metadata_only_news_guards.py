# -*- coding: utf-8 -*-
"""Phase 151: Evaluation Metadata-Only News Guards Module.

Guards against raw news text, article bodies, scraped HTML, and sentiment model outputs.
Enforces strict metadata-only news usage.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_CLAIM_GUARD_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

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
    "body_text",
    "article_text",
]

NEWS_METADATA_GUARDS: List[Dict[str, Any]] = [
    {
        "guard_id": "GUARD_NO_FULL_ARTICLE_BODY",
        "guard_name": "No Full Article Body Guard",
        "detection_target": "article_body_and_raw_content",
        "description": "Telif hakkı korumalı haber metinlerinin veri çerçevelerine girmesini engelleyen muhafız.",
    },
    {
        "guard_id": "GUARD_NO_SCRAPED_HTML",
        "guard_name": "No Scraped HTML Content Guard",
        "detection_target": "html_and_scraped_markup",
        "description": "Scraped HTML ve web kazıma içeriklerini engelleyen muhafız.",
    },
    {
        "guard_id": "GUARD_NO_EMBEDDINGS_OR_SENTIMENT",
        "guard_name": "No Text Embeddings or Sentiment Models Guard",
        "detection_target": "vector_embeddings_and_nlp_scores",
        "description": "NLP embedding ve duygu modelleri çıktılarının izinsiz kullanımını engelleyen muhafız.",
    },
]


def build_evaluation_metadata_only_news_guard_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of metadata-only news guards."""
    rows: List[Dict[str, Any]] = []

    for g in NEWS_METADATA_GUARDS:
        rows.append(
            {
                "guard_id": g["guard_id"],
                "guard_name": g["guard_name"],
                "detection_target": g["detection_target"],
                "description": g["description"],
                "is_active": True,
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_CLAIM_GUARD_DOMAIN,
        "total_guards": len(df),
        "all_active": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary


def validate_evaluation_metadata_only_news_columns(column_names: List[str]) -> Dict[str, Any]:
    """Validate that columns do not contain raw text, article bodies, or embeddings."""
    detected: List[str] = []
    for col in column_names:
        c_lower = str(col).lower()
        for forbidden in FORBIDDEN_NEWS_COLUMNS:
            if forbidden in c_lower:
                detected.append(col)
                break

    is_clean = len(detected) == 0
    return {
        "is_clean": is_clean,
        "forbidden_news_detected": not is_clean,
        "detected_columns": detected,
        "status": "PASS" if is_clean else "BLOCKED_BY_NEWS_METADATA_GUARD",
        "policy_action": "ALLOW" if is_clean else "NEWS_TEXT_BLOCKED_BY_POLICY",
        "non_signal": True,
    }
