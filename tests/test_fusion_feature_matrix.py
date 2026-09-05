"""Tests for Fusion Feature Matrix Builder."""

import pandas as pd
from advanced_feature_fusion.fusion_feature_matrix import (
    build_fusion_feature_matrix,
    get_fusion_feature_matrix_summary,
)


def test_build_fusion_feature_matrix():
    times = pd.date_range("2025-01-01 10:00:00", periods=5, freq="1h", tz="UTC")
    base_df = pd.DataFrame({
        "timestamp": times,
        "price": [100.0, 101.0, 102.0, 103.0, 104.0],
    })

    macro_df = pd.DataFrame({
        "macro_release_timestamp": times,
        "cpi": [3.0, 3.0, 3.1, 3.1, 3.2],
    })

    matrix_df, manifest = build_fusion_feature_matrix(
        base_df=base_df,
        macro_df=macro_df,
        matrix_id="test_matrix",
    )
    assert len(matrix_df) == 5
    assert "cpi" in matrix_df.columns
    assert manifest.matrix_id == "test_matrix"
    assert manifest.total_rows == 5
    assert manifest.no_lookahead_guaranteed is True
    assert manifest.is_non_signal_guaranteed is True

    summary = get_fusion_feature_matrix_summary(manifest)
    assert summary["matrix_id"] == "test_matrix"


def test_empty_base_matrix():
    empty_df = pd.DataFrame()
    matrix_df, manifest = build_fusion_feature_matrix(base_df=empty_df)
    assert len(matrix_df) == 0
    assert manifest.total_rows == 0
