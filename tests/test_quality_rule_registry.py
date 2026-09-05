import pytest
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.quality_rule_registry import (
    build_quality_rule_registry,
    build_default_quality_rules,
    summarize_quality_rule_registry,
)


def test_quality_rule_registry():
    profile = get_default_data_quality_profile()
    rules = build_default_quality_rules(profile)
    assert len(rules) >= 15

    df, summary = build_quality_rule_registry(profile)
    assert len(df) >= 15
    assert "schema_compliance" in summary["domains"]
    assert "missing_data" in summary["domains"]
    assert "fx_quality" in summary["domains"]
    assert "ohlc_consistency" in summary["domains"]
    assert "news_copyright_quality" in summary["domains"]
