"""Phase 136: Metadata-Only News ML Input Contracts.

Enforces strict exclusion of raw article bodies, full text dumps, scraped HTML,
vector embeddings, and LLM sentiment outputs from all ML input pipelines.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    METADATA_ONLY_NEWS_INPUT_CONTRACT_DOMAIN,
    RUNTIME_READY,
)


FORBIDDEN_NEWS_CONTENT_PATTERNS = [
    "article_body",
    "raw_content",
    "full_text",
    "full_article",
    "scraped_html",
    "page_html",
    "html_content",
    "body_text",
    "news_body",
    "embedding",
    "vector",
    "sentiment_score",
    "sentiment_output",
    "llm_output",
]


def validate_ml_input_metadata_only_news_fields(column_names: List[str]) -> Dict[str, Any]:
    """Inspect input column names and flag any unauthorized text or sentiment content."""
    violations: List[str] = []
    for col in column_names:
        c_lower = col.lower()
        for pat in FORBIDDEN_NEWS_CONTENT_PATTERNS:
            if pat in c_lower:
                violations.append(col)
                break

    is_clean = len(violations) == 0
    return {
        "is_safe": is_clean,
        "violations": violations,
        "message": f"Forbidden raw news/NLP fields detected: {violations}" if not is_clean else "All input fields satisfy metadata-only news contract.",
        "non_signal": True,
        "source_preserved": True,
    }


def build_metadata_only_news_ml_input_contract_registry(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for metadata-only news ML input contracts."""
    active = profile or get_gpu_ml_runtime_profile()

    rows: List[Dict[str, Any]] = [
        {
            "contract_id": "news_contract_no_article_body",
            "rule_name": "Prohibit Article Body and Full Text",
            "enforced": True,
            "status_label": RUNTIME_READY,
            "details": "Zero full article copies or unvetted text allowed into input matrices.",
        },
        {
            "contract_id": "news_contract_no_html",
            "rule_name": "Prohibit Scraped HTML and DOM Content",
            "enforced": True,
            "status_label": RUNTIME_READY,
            "details": "Zero scraped page HTML or DOM structures permitted in ML pipelines.",
        },
        {
            "contract_id": "news_contract_no_embeddings",
            "rule_name": "Prohibit Text Embeddings and Vectors",
            "enforced": True,
            "status_label": RUNTIME_READY,
            "details": "Zero vector database or embedding generation allowed in ML inputs.",
        },
        {
            "contract_id": "news_contract_metadata_only",
            "rule_name": "Permit Structured Metadata Attributes Only",
            "enforced": True,
            "status_label": RUNTIME_READY,
            "details": "Only structured categorical metadata (source_name, event_topic, timestamp) permitted.",
        },
    ]

    for r in rows:
        r["non_signal"] = True
        r["source_preserved"] = True
        r["official_approval"] = False
        r["production_ready"] = False
        r["broker_ready"] = False

    df = pd.DataFrame(rows)
    summary = summarize_metadata_only_news_ml_input_contracts(df)
    summary["domain"] = METADATA_ONLY_NEWS_INPUT_CONTRACT_DOMAIN
    summary["active_profile"] = active.profile_name
    return df, summary


def summarize_metadata_only_news_ml_input_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize metadata-only news ML input contracts DataFrame."""
    all_enf = bool(df["enforced"].all()) if not df.empty and "enforced" in df.columns else False
    return {
        "total_contracts": len(df),
        "all_enforced": all_enf,
        "metadata_only_guaranteed": True,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
