from advanced_feature_grid.calendar_feature_grid_placeholders import build_calendar_feature_grid_placeholder_registry


def test_calendar_feature_grid_placeholders():
    df, summary = build_calendar_feature_grid_placeholder_registry()
    assert not df.empty
    assert summary["status"] == "PLACEHOLDER_ONLY"
    assert summary["non_signal"] is True
    assert (df["is_placeholder"] == True).all()
