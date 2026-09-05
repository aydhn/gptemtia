from advanced_feature_grid.quote_feature_grid_placeholders import build_quote_feature_grid_placeholder_registry


def test_quote_feature_grid_placeholders():
    df, summary = build_quote_feature_grid_placeholder_registry()
    assert not df.empty
    assert summary["status"] == "PLACEHOLDER_ONLY"
    assert summary["non_signal"] is True
    assert (df["is_placeholder"] == True).all()
