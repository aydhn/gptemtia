from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.calendar_lineage_registry import (
    build_calendar_lineage_registry,
    summarize_calendar_lineage_registry,
)


def test_calendar_lineage():
    profile = get_default_data_lineage_profile()
    df, summary = build_calendar_lineage_registry(profile)
    assert len(df) >= 3
    assert summary["all_source_preserved"] is True
    assert summary["zero_destructive_actions"] is True
    assert "normalized_event" in summary["canonical_fields"]
