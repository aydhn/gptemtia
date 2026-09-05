from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.data_usage_boundary_registry import (
    build_data_usage_boundary_registry,
    summarize_data_usage_boundary_registry,
)


def test_data_usage_boundary():
    profile = get_default_data_lineage_profile()
    df, summary = build_data_usage_boundary_registry(profile)
    assert len(df) >= 8
    assert summary["all_enforced"] is True
    assert "research_only" in summary["boundary_types"]
    assert "no_trading_signal" in summary["boundary_types"]
