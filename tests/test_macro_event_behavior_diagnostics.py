from advanced_market_behavior_diagnostics.macro_event_behavior_diagnostics import (
    build_macro_event_behavior_diagnostics_report,
    summarize_macro_event_behavior_diagnostics,
)


def test_macro_event_behavior_diagnostics():
    df, summary = build_macro_event_behavior_diagnostics_report()

    assert not df.empty
    assert "context_name" in df.columns
    assert summary["all_ready"] is True
    assert summary["dependencies_passed"] is True
    assert summary["non_signal"] is True
