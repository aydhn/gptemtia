from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.news_metadata_feature_catalog import (
    build_news_metadata_feature_catalog,
)


def test_news_metadata_feature_catalog():
    profile = get_default_feature_engine_profile()
    df, summary = build_news_metadata_feature_catalog(profile)

    assert not df.empty
    assert len(df) >= 5
    names = df["feature_name"].tolist()
    assert "news_topic_flag_placeholder" in names
    assert "news_asset_tag_count_placeholder" in names
    assert "news_freshness_placeholder" in names
    assert summary["zero_full_text_enforced"] is True
    assert summary["all_non_signal"] is True
