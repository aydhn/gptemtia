"""Tests for News Asset Tag Feature Fusion."""

import pandas as pd
from advanced_feature_fusion.news_asset_tag_feature_fusion import (
    build_news_asset_tag_feature_fusion_registry,
    summarize_news_asset_tag_feature_fusion,
    add_news_asset_tag_count_placeholder,
    add_news_macro_tag_count_placeholder,
)


def test_news_asset_tag_registry():
    df, summary = build_news_asset_tag_feature_fusion_registry()
    assert len(df) == 2
    assert summary["total_features"] == 2
    assert summary["non_signal_guaranteed"] is True


def test_tag_count_placeholders():
    df = pd.DataFrame({
        "asset_tags": ["XAU,USD", "EUR", ""],
        "macro_tags": ["inflation,rates,oil", None, "growth"],
    })
    asset_res = add_news_asset_tag_count_placeholder(df, tag_field="asset_tags")
    assert "news_asset_tag_count_placeholder" in asset_res.columns
    assert asset_res["news_asset_tag_count_placeholder"].iloc[0] == 2
    assert asset_res["news_asset_tag_count_placeholder"].iloc[1] == 1
    assert asset_res["news_asset_tag_count_placeholder"].iloc[2] == 0

    macro_res = add_news_macro_tag_count_placeholder(df, tag_field="macro_tags")
    assert "news_macro_tag_count_placeholder" in macro_res.columns
    assert macro_res["news_macro_tag_count_placeholder"].iloc[0] == 3
    assert macro_res["news_macro_tag_count_placeholder"].iloc[1] == 0
    assert macro_res["news_macro_tag_count_placeholder"].iloc[2] == 1
