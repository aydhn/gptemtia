from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile
from advanced_data_normalization.data_normalization_safety_boundary import (
    build_data_normalization_safety_boundary,
    build_data_normalization_no_go_conditions,
    build_data_normalization_safe_go_conditions,
    summarize_data_normalization_safety_boundary,
)


def test_safety_boundary():
    prof = get_default_data_normalization_profile()
    no_go_df = build_data_normalization_no_go_conditions(prof)
    assert len(no_go_df) >= 30
    codes = no_go_df["rule_code"].tolist()
    assert "no_live_trading" in codes
    assert "no_broker_integration" in codes
    assert "no_web_scraping" in codes
    assert "no_source_overwrite" in codes
    assert "no_destructive_cleaning" in codes

    safe_go_df = build_data_normalization_safe_go_conditions(prof)
    assert len(safe_go_df) >= 20

    combined, summary = build_data_normalization_safety_boundary(prof)
    assert summary["source_overwrite_forbidden"] is True
    assert summary["destructive_cleaning_forbidden"] is True
