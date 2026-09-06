import pandas as pd
from advanced_regime_featurestore_integration.regime_featurestore_forbidden_column_policies import (
    build_regime_featurestore_forbidden_column_policy_registry,
    validate_regime_featurestore_forbidden_columns,
    summarize_regime_featurestore_forbidden_column_policies,
    FORBIDDEN_COLUMNS,
)


def test_build_regime_featurestore_forbidden_column_policy_registry():
    df, summary = build_regime_featurestore_forbidden_column_policy_registry()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 23
    assert summary["total_forbidden_columns"] == 23
    assert summary["non_signal"] is True
    assert summary["current_phase"] == 134


def test_validate_regime_featurestore_forbidden_columns():
    safe_cols = ["store_key", "entity_id", "timestamp_utc", "regime_label"]
    res_safe = validate_regime_featurestore_forbidden_columns(safe_cols)
    assert res_safe["is_valid"] is True
    assert len(res_safe["found_forbidden"]) == 0
    assert res_safe["non_signal"] is True

    bad_cols = ["store_key", "buy", "sell_signal", "future_return", "full_text"]
    res_bad = validate_regime_featurestore_forbidden_columns(bad_cols)
    assert res_bad["is_valid"] is False
    assert "buy" in res_bad["found_forbidden"]
    assert "future_return" in res_bad["found_forbidden"]
    assert "full_text" in res_bad["found_forbidden"]


def test_summarize_regime_featurestore_forbidden_column_policies():
    df, _ = build_regime_featurestore_forbidden_column_policy_registry()
    summary = summarize_regime_featurestore_forbidden_column_policies(df)
    assert summary["total_forbidden_columns"] == 23
    assert "trading_signal" in summary["categories"]
    assert "lookahead" in summary["categories"]
