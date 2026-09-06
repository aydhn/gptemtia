"""Phase 134: Regime FeatureStore Forbidden Column Policies.

Defines and scans for prohibited column names (trade signals, targets, raw news text,
embeddings, and sentiment outputs) across all FeatureStore datasets.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    RegimeFeatureStoreProfile,
    get_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_labels import (
    FORBIDDEN_COLUMN_POLICY_DOMAIN,
    REGIME_STORE_READY,
)

FORBIDDEN_COLUMNS: List[Dict[str, Any]] = [
    {"column_name": "signal", "category": "trading_signal", "reason": "Trading directive prohibited"},
    {"column_name": "buy", "category": "trading_signal", "reason": "Trade action prohibited"},
    {"column_name": "sell", "category": "trading_signal", "reason": "Trade action prohibited"},
    {"column_name": "long", "category": "trading_signal", "reason": "Position stance prohibited"},
    {"column_name": "short", "category": "trading_signal", "reason": "Position stance prohibited"},
    {"column_name": "position", "category": "trading_signal", "reason": "Positioning prohibited"},
    {"column_name": "target", "category": "machine_learning", "reason": "Supervised target prohibited"},
    {"column_name": "label", "category": "machine_learning", "reason": "Prediction label prohibited"},
    {"column_name": "prediction", "category": "machine_learning", "reason": "Model forecast prohibited"},
    {"column_name": "recommendation", "category": "advisory", "reason": "Investment recommendation prohibited"},
    {"column_name": "future_return", "category": "lookahead", "reason": "Lookahead data leakage prohibited"},
    {"column_name": "forward_return", "category": "lookahead", "reason": "Lookahead data leakage prohibited"},
    {"column_name": "next_return", "category": "lookahead", "reason": "Lookahead data leakage prohibited"},
    {"column_name": "full_text", "category": "unstructured_content", "reason": "Raw news text prohibited"},
    {"column_name": "article_body", "category": "unstructured_content", "reason": "Raw news text prohibited"},
    {"column_name": "raw_content", "category": "unstructured_content", "reason": "Uncurated raw content prohibited"},
    {"column_name": "scraped_html", "category": "unstructured_content", "reason": "Scraped HTML prohibited"},
    {"column_name": "page_html", "category": "unstructured_content", "reason": "Scraped HTML prohibited"},
    {"column_name": "html", "category": "unstructured_content", "reason": "HTML markup prohibited"},
    {"column_name": "embedding", "category": "vector_data", "reason": "Vector embeddings prohibited"},
    {"column_name": "vector", "category": "vector_data", "reason": "Vector embeddings prohibited"},
    {"column_name": "sentiment", "category": "nlp_sentiment", "reason": "NLP sentiment model output prohibited"},
    {"column_name": "sentiment_score", "category": "nlp_sentiment", "reason": "NLP sentiment score prohibited"},
]


def build_regime_featurestore_forbidden_column_policy_registry(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Construct DataFrame and summary for forbidden column policies."""
    active_profile = profile or get_regime_featurestore_profile()
    df = pd.DataFrame(FORBIDDEN_COLUMNS)
    summary = {
        "domain": FORBIDDEN_COLUMN_POLICY_DOMAIN,
        "total_forbidden_columns": len(df),
        "active_profile": active_profile.profile_name,
        "current_phase": 134,
        "target_final_phase": 160,
        "next_phase": 135,
        "status": REGIME_STORE_READY,
        "non_signal": True,
    }
    return df, summary


def validate_regime_featurestore_forbidden_columns(column_names: List[str]) -> Dict[str, Any]:
    """Validate a list of column names against the forbidden column registry."""
    forbidden_set = {item["column_name"].lower() for item in FORBIDDEN_COLUMNS}
    found = [col for col in column_names if col.lower() in forbidden_set]

    return {
        "is_valid": len(found) == 0,
        "total_checked": len(column_names),
        "found_forbidden": found,
        "non_signal": len(found) == 0,
    }


def summarize_regime_featurestore_forbidden_column_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize forbidden column policy DataFrame."""
    return {
        "total_forbidden_columns": len(df),
        "categories": df["category"].unique().tolist() if not df.empty else [],
        "all_prohibited": True,
    }
