from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.normalization_lineage_registry import (
    build_normalization_lineage_registry,
    summarize_normalization_lineage_registry,
)


def test_normalization_lineage():
    profile = get_default_data_lineage_profile()
    df, summary = build_normalization_lineage_registry(profile)
    assert len(df) >= 8
    assert summary["all_source_preserved"] is True
    assert summary["zero_destructive_actions"] is True
    assert "normalized_pair" in summary["canonical_fields"]
