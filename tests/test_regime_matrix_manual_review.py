from advanced_regime_matrix.regime_matrix_manual_review import (
    build_regime_matrix_manual_review_queue,
    is_valid_manual_review_item,
)


def test_build_regime_matrix_manual_review_queue():
    df, s = build_regime_matrix_manual_review_queue()
    assert len(df) == 8
    assert s["total_items"] == 8
    assert s["pending_items"] == 8
    assert s["all_source_preserved"] is True
    assert is_valid_manual_review_item("review_gap_brent_wti_spread") is True
    assert is_valid_manual_review_item("unknown_review_item") is False
