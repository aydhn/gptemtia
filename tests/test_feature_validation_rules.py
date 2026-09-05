import pandas as pd
from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.feature_validation_rules import (
    build_feature_validation_rule_registry,
    validate_no_signal_columns,
    validate_no_lookahead_columns,
    validate_feature_dataframe,
)


def test_feature_validation_rules():
    profile = get_default_feature_engine_profile()
    df, summary = build_feature_validation_rule_registry(profile)

    assert not df.empty
    assert len(df) >= 5
    assert summary["all_enforced"] is True

    # Valid dataframe check
    good_df = pd.DataFrame({"close": [1, 2], "sma_20": [1, 2]})
    res = validate_feature_dataframe(good_df, ["close", "sma_20"])
    assert res["valid"] is True

    # Forbidden signal column check
    bad_df = pd.DataFrame({"close": [1, 2], "signal": [1, 0]})
    res_bad = validate_feature_dataframe(bad_df, ["close"])
    assert res_bad["valid"] is False
    assert "signal" in res_bad["violating_signal_columns"]

    # Forbidden lookahead column check
    lookahead_df = pd.DataFrame({"close": [1, 2], "close_future_1": [2, 3]})
    res_look = validate_feature_dataframe(lookahead_df, ["close"])
    assert res_look["valid"] is False
    assert "close_future_1" in res_look["violating_lookahead_columns"]
