from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile
from advanced_data_normalization.data_normalization_profile_registry import (
    build_data_normalization_profile_registry,
    build_default_data_normalization_profile_items,
    summarize_data_normalization_profile_registry,
)


def test_profile_registry():
    prof = get_default_data_normalization_profile()
    df, summary = build_data_normalization_profile_registry(prof)
    assert not df.empty
    assert len(df) >= 3
    assert summary["all_non_destructive"] is True
    assert summary["all_dry_run"] is True
    assert summary["current_phase"] == 113
    assert summary["target_final_phase"] == 160
