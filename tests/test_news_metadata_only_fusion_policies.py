"""Tests for News Metadata-Only Fusion Policies."""

import pandas as pd
from advanced_feature_fusion.news_metadata_only_fusion_policies import (
    build_news_metadata_only_fusion_policy_registry,
    get_news_metadata_only_policies,
    validate_news_metadata_only_dataframe,
)


def test_news_metadata_only_policies():
    df, summary = build_news_metadata_only_fusion_policy_registry()
    assert len(df) == 3
    assert summary["total_policies"] == 3
    assert summary["zero_full_text_enforced"] is True


def test_validate_news_metadata_only():
    valid_df = pd.DataFrame({
        "news_id": ["N1"],
        "topic": ["rate_decision"],
        "published_timestamp": ["2025-01-01 10:00:00"],
    })
    res_valid = validate_news_metadata_only_dataframe(valid_df)
    assert res_valid["valid"] is True

    # Violating df with full article text column
    invalid_df = pd.DataFrame({
        "news_id": ["N1"],
        "full_text": ["This is the full article content..."],
    })
    res_invalid = validate_news_metadata_only_dataframe(invalid_df)
    assert res_invalid["valid"] is False
    assert len(res_invalid["forbidden_columns_found"]) > 0
