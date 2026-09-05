from advanced_feature_grid.feature_grid_quality_handoff import (
    build_feature_grid_quality_handoff_report,
    summarize_feature_grid_quality_handoff,
)


def test_feature_grid_quality_handoff():
    df, summary = build_feature_grid_quality_handoff_report()
    assert not df.empty
    assert summary["phase_119_items"] > 0
    assert summary["phase_121_items"] > 0
    assert summary["phase_124_items"] > 0
    assert summary["non_signal"] is True
    assert summary["status"] == "READY"
