from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.factor_schema_registry import (
    build_factor_schema_registry,
    build_default_factor_schemas,
    summarize_factor_schema_registry,
)


def test_factor_schema_registry():
    profile = get_default_feature_engine_profile()
    df, summary = build_factor_schema_registry(profile)

    assert not df.empty
    assert len(df) >= 8
    assert "factor_name" in df.columns
    assert "future_phase_owner" in df.columns
    assert "non_signal" in df.columns

    factor_names = df["factor_name"].tolist()
    assert "trend_factor_placeholder" in factor_names
    assert "momentum_factor_placeholder" in factor_names
    assert "volatility_factor_placeholder" in factor_names
    assert "mean_reversion_factor_placeholder" in factor_names

    assert summary["all_non_signal"] is True
    assert summary["non_signal"] is True
