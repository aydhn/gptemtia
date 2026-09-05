import pytest
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.cross_provider_quality import (
    build_cross_provider_quality_comparison_placeholder,
    summarize_cross_provider_quality,
)


def test_cross_provider_quality():
    profile = get_default_data_quality_profile()
    df, summary = build_cross_provider_quality_comparison_placeholder(profile)
    assert len(df) >= 4
    assert summary["placeholder_only"] is True
    assert summary["benchmark_phase"] == 115
    assert summary["current_phase"] == 112
