from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile
from advanced_data_normalization.normalization_rule_registry import (
    build_normalization_rule_registry,
    build_default_normalization_rules,
    summarize_normalization_rule_registry,
)


def test_rule_registry():
    prof = get_default_data_normalization_profile()
    df, summary = build_normalization_rule_registry(prof)
    assert not df.empty
    assert len(df) >= 20
    assert summary["all_non_destructive"] is True
    assert "fx_symbol" in summary["domains"]
