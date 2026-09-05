import pytest
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.data_quality_profile_registry import (
    build_data_quality_profile_registry,
    build_default_data_quality_profile_items,
    summarize_data_quality_profile_registry,
)


def test_data_quality_profile_registry():
    profile = get_default_data_quality_profile()
    items = build_default_data_quality_profile_items(profile)
    assert len(items) >= 3

    df, summary = build_data_quality_profile_registry(profile)
    assert len(df) >= 3
    assert summary["total_profiles"] >= 3
    assert summary["current_phase"] == 112
    assert summary["target_final_phase"] == 160
    assert summary["dry_run_all"] is True
