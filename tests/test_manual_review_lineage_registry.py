from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.manual_review_lineage_registry import (
    build_manual_review_lineage_registry,
    summarize_manual_review_lineage_registry,
)


def test_manual_review_lineage():
    profile = get_default_data_lineage_profile()
    df, summary = build_manual_review_lineage_registry(profile)
    assert len(df) >= 3
    assert summary["zero_destructive_actions"] is True
    assert summary["all_source_preserved"] is True
