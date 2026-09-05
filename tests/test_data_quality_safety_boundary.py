import pytest
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.data_quality_safety_boundary import (
    build_data_quality_safety_boundary,
    build_data_quality_no_go_conditions,
    build_data_quality_safe_go_conditions,
    summarize_data_quality_safety_boundary,
)


def test_data_quality_safety_boundary():
    profile = get_default_data_quality_profile()
    nogos = build_data_quality_no_go_conditions(profile)
    assert len(nogos) >= 25
    assert "live_trading" in nogos["rule"].values
    assert "web_scraping" in nogos["rule"].values
    assert "auto_overwrite_cleaning" in nogos["rule"].values

    safegos = build_data_quality_safe_go_conditions(profile)
    assert len(safegos) >= 20
    assert "local_offline_engine" in safegos["rule"].values

    df, summary = build_data_quality_safety_boundary(profile)
    assert len(df) >= 45
    assert summary["no_go_count"] >= 25
    assert summary["safe_go_count"] >= 20
