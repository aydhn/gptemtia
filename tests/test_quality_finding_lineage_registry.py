from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.quality_finding_lineage_registry import (
    build_quality_finding_lineage_registry,
    summarize_quality_finding_lineage_registry,
)


def test_quality_finding_lineage():
    profile = get_default_data_lineage_profile()
    df, summary = build_quality_finding_lineage_registry(profile)
    assert len(df) >= 4
    assert summary["all_source_preserved"] is True
    assert summary["zero_destructive_actions"] is True
    assert "missing_bid_quote" in summary["finding_types"]
