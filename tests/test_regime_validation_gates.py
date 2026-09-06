"""Tests for Regime Validation Gates."""

from advanced_regime_validation_acceptance.regime_validation_gates import (
    build_regime_validation_gate_registry,
    validate_regime_validation_gate,
    summarize_regime_validation_gates,
    GATE_DEFINITIONS,
)


def test_validation_gates():
    assert len(GATE_DEFINITIONS) == 19

    df, summary = build_regime_validation_gate_registry()
    assert len(df) == 19
    assert summary["total_gates"] == 19
    assert summary["all_passed"] is True
    assert summary["failed_gates"] == 0
    assert summary["non_signal"] is True

    s_df = summarize_regime_validation_gates(df)
    assert s_df["all_passed"] is True
    assert s_df["total_gates"] == 19

    # Test single gate validation
    valid_res = validate_regime_validation_gate({"gate_name": "test_gate"})
    assert valid_res["passed"] is True

    invalid_res = validate_regime_validation_gate({"gate_name": ""})
    assert invalid_res["passed"] is False
