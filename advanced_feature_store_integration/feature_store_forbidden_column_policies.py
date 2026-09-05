"""Phase 124 Feature Store Forbidden Column Policies."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_feature_store_integration.feature_store_integration_config import (
    FeatureStoreIntegrationProfile,
    get_default_feature_store_integration_profile,
)

FORBIDDEN_COLUMNS: List[str] = [
    "signal",
    "buy",
    "sell",
    "long",
    "short",
    "position",
    "target",
    "label",
    "prediction",
    "recommendation",
    "future_return",
    "forward_return",
    "next_return",
    "full_text",
    "article_body",
    "raw_content",
    "scraped_html",
    "page_html",
    "embedding",
    "vector",
]


def validate_feature_store_forbidden_columns(column_names: List[str]) -> Dict[str, Any]:
    """Detect forbidden column names in a feature store dataset."""
    detected = []
    lowered_names = [c.lower().strip() for c in column_names]

    for col in lowered_names:
        for f in FORBIDDEN_COLUMNS:
            if col == f or col.startswith(f"{f}_") or col.endswith(f"_{f}") or f"__{f}__" in col:
                detected.append(col)
                break

    return {
        "total_columns_checked": len(column_names),
        "forbidden_detected": list(set(detected)),
        "is_safe": len(detected) == 0,
        "non_signal": len(detected) == 0,
    }


def build_feature_store_forbidden_column_policy_registry(
    profile: Optional[FeatureStoreIntegrationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of forbidden column policies."""
    records = []
    for f in FORBIDDEN_COLUMNS:
        records.append({
            "forbidden_column": f,
            "category": "signal_target" if f in ["signal", "buy", "sell", "target", "label", "prediction"] else "unauthorized_content",
            "policy": "strict_rejection",
            "non_signal": True,
            "source_preserved": True,
        })

    df = pd.DataFrame(records)
    summary = {
        "total_forbidden_columns": len(records),
        "all_enforced": True,
        "non_signal": True,
    }
    return df, summary


def summarize_feature_store_forbidden_column_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize forbidden column policies."""
    return {
        "total_forbidden_columns": len(df) if not df.empty else 0,
        "non_signal": True,
    }
