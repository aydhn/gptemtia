from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.data_lineage_profile_registry import (
    build_data_lineage_profile_registry,
    build_default_data_lineage_profile_items,
    summarize_data_lineage_profile_registry,
)


def test_profile_registry():
    profile = get_default_data_lineage_profile()
    items = build_default_data_lineage_profile_items(profile)
    assert len(items) >= 3

    df, summary = build_data_lineage_profile_registry(profile)
    assert len(df) >= 3
    assert summary["all_local_only"] is True
    assert summary["all_non_destructive"] is True
    assert summary["current_phase"] == 114
