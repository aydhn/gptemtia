from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.normalized_output_lineage_registry import (
    build_normalized_output_lineage_registry,
    summarize_normalized_output_lineage_registry,
)


def test_normalized_output_lineage():
    profile = get_default_data_lineage_profile()
    df, summary = build_normalized_output_lineage_registry(profile)
    assert len(df) >= 5
    assert summary["all_source_preserved"] is True
    assert summary["zero_destructive_actions"] is True
