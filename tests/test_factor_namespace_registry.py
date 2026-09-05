import pytest
from advanced_factor_metadata.factor_namespace_registry import (
    build_factor_name,
    build_factor_namespace_registry,
    validate_factor_name,
)


def test_build_factor_name():
    name = build_factor_name("trend", "multi_window_context")
    assert name == "factor_trend_multi_window_context"

    name2 = build_factor_name("factor_family_momentum", "rsi_roc_context")
    assert name2 == "factor_momentum_rsi_roc_context"


def test_validate_factor_name():
    valid = validate_factor_name("factor_trend_slope")
    assert valid["is_valid"] is True
    assert len(valid["errors"]) == 0

    # Forbidden token
    invalid_token = validate_factor_name("factor_trend_signal")
    assert invalid_token["is_valid"] is False
    assert any("forbidden token" in e for e in invalid_token["errors"])

    # Uppercase
    invalid_case = validate_factor_name("Factor_Trend_Slope")
    assert invalid_case["is_valid"] is False


def test_build_factor_namespace_registry():
    df, summary = build_factor_namespace_registry()
    assert not df.empty
    assert summary["all_valid"] is True
    assert summary["non_signal"] is True
