import pytest
from advanced_regime_foundation.regime_namespace_registry import (
    build_regime_namespace_registry,
    build_regime_state_name,
    validate_regime_state_name,
    summarize_regime_namespace_registry,
)


def test_regime_namespace_registry():
    df, summary = build_regime_namespace_registry()
    assert not df.empty
    assert summary["mandatory_prefix"] == "regime_state_"
    assert summary["all_non_signal"] is True

    # Valid name check
    valid_name = "regime_state_trend_alignment_score"
    res_valid = validate_regime_state_name(valid_name)
    assert res_valid["is_valid"] is True

    # Invalid prefix check
    res_invalid_prefix = validate_regime_state_name("trend_alignment_score")
    assert res_invalid_prefix["is_valid"] is False

    # Forbidden word check
    res_forbidden = validate_regime_state_name("regime_state_buy_signal")
    assert res_forbidden["is_valid"] is False
    assert any("forbidden" in iss for iss in res_forbidden["issues"])

    # Construction helper
    constructed = build_regime_state_name("regime_family_trend", "sma_slope_context")
    assert constructed == "regime_state_trend_sma_slope_context"

    with pytest.raises(ValueError):
        build_regime_state_name("regime_family_trend", "buy_signal")

    summ = summarize_regime_namespace_registry(df)
    assert summ["mandatory_prefix"] == "regime_state_"
