from advanced_feature_grid.macro_feature_grid_placeholders import build_macro_feature_grid_placeholder_registry


def test_macro_feature_grid_placeholders():
    df, summary = build_macro_feature_grid_placeholder_registry()
    assert not df.empty
    assert summary["status"] == "PLACEHOLDER_ONLY"
    assert summary["non_signal"] is True
    assert (df["is_placeholder"] == True).all()
    assert (df["directional_claim"] == False).all()
