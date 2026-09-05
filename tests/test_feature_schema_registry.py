from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.feature_schema_registry import (
    build_feature_schema_registry,
    build_default_feature_schemas,
    summarize_feature_schema_registry,
)


def test_feature_schema_registry():
    profile = get_default_feature_engine_profile()
    df, summary = build_feature_schema_registry(profile)

    assert not df.empty
    assert len(df) >= 15
    assert "feature_name" in df.columns
    assert "output_field" in df.columns
    assert "non_signal" in df.columns

    feature_names = df["feature_name"].tolist()
    assert "close_return_1" in feature_names
    assert "log_return_1" in feature_names
    assert "sma_20" in feature_names
    assert "ema_20" in feature_names
    assert "rsi_14" in feature_names
    assert "atr_14" in feature_names
    assert "quote_spread" in feature_names

    assert summary["all_non_signal"] is True
    assert summary["non_signal"] is True
