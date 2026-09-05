from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.news_metadata_lineage_registry import (
    build_news_metadata_lineage_registry,
    summarize_news_metadata_lineage_registry,
)


def test_news_metadata_lineage():
    profile = get_default_data_lineage_profile()
    df, summary = build_news_metadata_lineage_registry(profile)
    assert len(df) >= 3
    assert summary["zero_full_text"] is True
    assert summary["all_source_preserved"] is True
    assert summary["zero_destructive_actions"] is True
    assert "normalized_tags" in summary["canonical_fields"]
