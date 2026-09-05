"""News freshness feature placeholders.

Strictly metadata-only: tracks elapsed time since last news event metadata.
Non-signal, offline research only.
"""

from typing import Any, Dict, List
import pandas as pd


NEWS_FRESHNESS_FEATURES = [
    {
        "feature_id": "news_freshness_hours",
        "name": "News Freshness Hours Placeholder",
        "domain": "news_freshness",
        "description": "Elapsed hours since the most recent news metadata publication timestamp prior to base timestamp.",
        "input_columns": ["timestamp", "news_published_timestamp"],
        "is_placeholder": True,
        "is_signal": False,
    },
    {
        "feature_id": "news_freshness_decay_placeholder",
        "name": "News Freshness Decay Placeholder",
        "domain": "news_freshness",
        "description": "Exponential recency factor placeholder: exp(-decay * elapsed_hours).",
        "input_columns": ["news_freshness_hours"],
        "is_placeholder": True,
        "is_signal": False,
    },
]


def get_news_freshness_features_registry() -> List[Dict[str, Any]]:
    """Return registry of news freshness feature placeholders."""
    return [dict(f) for f in NEWS_FRESHNESS_FEATURES]


def get_news_freshness_features_summary() -> Dict[str, Any]:
    """Return summary dictionary of news freshness feature registry."""
    features = get_news_freshness_features_registry()
    return {
        "count": len(features),
        "feature_ids": [f["feature_id"] for f in features],
        "is_signal": False,
        "strictly_metadata_only": True,
    }


def add_news_freshness_placeholder(
    df: pd.DataFrame,
    timestamp_col: str = "timestamp",
    last_news_timestamp_col: str = "news_published_timestamp",
    out_col: str = "news_freshness_hours",
) -> pd.DataFrame:
    """Calculate elapsed hours since last news metadata timestamp.

    Strictly backward in time (base_timestamp - news_timestamp).
    """
    res = df.copy()
    if timestamp_col not in res.columns or last_news_timestamp_col not in res.columns:
        res[out_col] = float("nan")
        return res

    ts = pd.to_datetime(res[timestamp_col], utc=True)
    news_ts = pd.to_datetime(res[last_news_timestamp_col], utc=True)
    diff_sec = (ts - news_ts).dt.total_seconds()
    # If news_ts is after ts (which shouldn't happen), set to NaN or 0
    diff_sec = diff_sec.apply(lambda x: x if pd.notna(x) and x >= 0 else float("nan"))
    res[out_col] = diff_sec / 3600.0
    return res
