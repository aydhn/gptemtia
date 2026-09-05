import pandas as pd
from advanced_regime_foundation.regime_state_output_schema import (
    build_regime_state_output_schema_registry,
    validate_regime_state_output_schema,
    summarize_regime_state_output_schema,
)


def test_regime_state_output_schema():
    df, summary = build_regime_state_output_schema_registry()
    assert not df.empty
    assert summary["all_non_signal"] is True
    assert summary["no_forbidden_fields"] is True

    # Test validator with clean dataframe
    clean_df = pd.DataFrame(columns=["timestamp", "symbol", "regime_state_trend_context"])
    assert validate_regime_state_output_schema(clean_df)["is_valid"] is True

    # Test validator with forbidden columns
    forbidden_df = pd.DataFrame(columns=["timestamp", "symbol", "buy_signal", "future_return"])
    res = validate_regime_state_output_schema(forbidden_df)
    assert res["is_valid"] is False
    assert res["violations_count"] >= 2

    summ = summarize_regime_state_output_schema(df)
    assert summ["forbidden_fields_count"] == 0
