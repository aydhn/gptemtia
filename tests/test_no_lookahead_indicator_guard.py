import pandas as pd
from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile
from advanced_technical_indicators.no_lookahead_indicator_guard import (
    build_no_lookahead_indicator_guard_registry,
    validate_no_negative_shift_usage,
    validate_no_forward_return_columns,
    validate_no_target_label_prediction_columns,
    summarize_no_lookahead_guard,
)


def test_no_lookahead_indicator_guard():
    prof = get_default_technical_indicator_profile()
    df, summary = build_no_lookahead_indicator_guard_registry(prof)
    assert not df.empty
    assert summary["status"] == "READY"

    # Negative shift detection
    bad_code = "out['next_val'] = df['close'].shift(-1)"
    res_shift = validate_no_negative_shift_usage(bad_code)
    assert res_shift["valid"] is False
    assert res_shift["violation_count"] == 1

    good_code = "out['prev_val'] = df['close'].shift(1)"
    assert validate_no_negative_shift_usage(good_code)["valid"] is True

    # Forward return column detection
    bad_fwd = pd.DataFrame({"future_return_5": [0.01, 0.02]})
    assert validate_no_forward_return_columns(bad_fwd)["valid"] is False

    # Target / label / prediction column detection
    bad_target = pd.DataFrame({"target_binary": [1, 0], "model_prediction": [0.5, 0.6]})
    assert validate_no_target_label_prediction_columns(bad_target)["valid"] is False
