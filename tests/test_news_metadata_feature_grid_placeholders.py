from advanced_feature_grid.news_metadata_feature_grid_placeholders import build_news_metadata_feature_grid_placeholder_registry


def test_news_metadata_feature_grid_placeholders():
    df, summary = build_news_metadata_feature_grid_placeholder_registry()
    assert not df.empty
    assert summary["status"] == "PLACEHOLDER_ONLY"
    assert summary["no_full_text"] is True
    assert summary["non_signal"] is True
    assert (df["no_full_text"] == True).all()
