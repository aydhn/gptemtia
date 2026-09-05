import pytest
from advanced_factor_metadata.calendar_event_factor_families import (
    build_calendar_event_factor_family_registry,
    summarize_calendar_event_factor_family,
)


def test_build_calendar_event_factor_family_registry():
    df, summary = build_calendar_event_factor_family_registry()
    assert not df.empty
    assert summary["total_factors"] >= 4
    assert summary["non_signal"] is True

    names = list(df["factor_name"])
    assert "factor_event_pre_release_context" in names
    assert "factor_event_post_release_context" in names
    assert "factor_event_importance_context" in names
    assert "factor_event_release_delay_context" in names

    stats = summarize_calendar_event_factor_family(df)
    assert stats["total_factors"] == len(df)
    assert stats["non_signal"] is True
