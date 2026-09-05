import pandas as pd
from advanced_feature_grid.feature_grid_duplicate_detection import (
    build_feature_grid_duplicate_detection_registry,
    detect_duplicate_feature_names,
    detect_duplicate_feature_columns,
    summarize_feature_grid_duplicate_detection,
)


def test_feature_grid_duplicate_detection():
    df, summary = build_feature_grid_duplicate_detection_registry()
    assert not df.empty
    assert summary["auto_delete_allowed"] is False
    assert summary["action"] == "flag_for_manual_review"

    # Test duplicate names
    names = ["sma_w20", "ema_w50", "sma_w20"]
    res_names = detect_duplicate_feature_names(names)
    assert res_names["has_duplicates"] is True
    assert "sma_w20" in res_names["duplicates"]

    # Test duplicate columns
    test_df = pd.DataFrame({
        "col_a": [1.0, 2.0, 3.0],
        "col_b": [1.0, 2.0, 3.0],
        "col_c": [4.0, 5.0, 6.0],
    })
    res_cols = detect_duplicate_feature_columns(test_df, ["col_a", "col_b", "col_c"])
    assert res_cols["has_duplicates"] is True
    assert res_cols["duplicate_pairs_count"] == 1
