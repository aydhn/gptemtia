import pandas as pd
from advanced_feature_grid.feature_grid_no_lookahead_guard import (
    build_feature_grid_no_lookahead_guard_registry,
    validate_feature_grid_no_negative_shift_usage,
    validate_feature_grid_no_forward_return_columns,
    validate_feature_grid_no_target_label_prediction_columns,
    summarize_feature_grid_no_lookahead_guard,
)


def test_feature_grid_no_lookahead_guard():
    df, summary = build_feature_grid_no_lookahead_guard_registry()
    assert not df.empty
    assert summary["strictly_backward_looking"] is True
    assert summary["lookahead_forbidden"] is True

    # Test negative shift detection
    bad_code = "out['next_close'] = df['close'].shift(-1)"
    res_shift = validate_feature_grid_no_negative_shift_usage(bad_code)
    assert res_shift["valid"] is False
    assert res_shift["negative_shift_detected"] is True

    clean_code = "out['prev_close'] = df['close'].shift(1)"
    res_clean = validate_feature_grid_no_negative_shift_usage(clean_code)
    assert res_clean["valid"] is True

    # Test forward return columns
    bad_df = pd.DataFrame({"future_return_5": [0.01, 0.02]})
    res_fwd = validate_feature_grid_no_forward_return_columns(bad_df)
    assert res_fwd["valid"] is False

    # Test target/label columns
    target_df = pd.DataFrame({"target_label": [1, 0]})
    res_tgt = validate_feature_grid_no_target_label_prediction_columns(target_df)
    assert res_tgt["valid"] is False
