"""Test suite for Phase 135 Regime Block Acceptance Gates."""

from advanced_regime_acceptance.regime_block_acceptance_gates import (
    build_regime_block_acceptance_gate_registry,
    validate_regime_acceptance_gate,
    summarize_regime_acceptance_gates,
)


def test_acceptance_gates():
    df, summary = build_regime_block_acceptance_gate_registry()
    assert len(df) == 17
    assert summary["total_gates"] == 17
    assert summary["all_passed"] is True
    assert summary["non_signal"] is True

    s2 = summarize_regime_acceptance_gates(df)
    assert s2["total_gates"] == 17
    assert s2["all_passed"] is True

    sample_gate = df.iloc[0].to_dict()
    v = validate_regime_acceptance_gate(sample_gate)
    assert v["is_valid"] is True
    assert v["passed"] is True
