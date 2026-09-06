"""Test suite for Phase 135 Regime Block Acceptance Scoring."""

from advanced_regime_acceptance.regime_block_acceptance_scoring import (
    calculate_regime_block_acceptance_score,
    build_regime_block_acceptance_score_report,
    classify_regime_block_acceptance_score,
    summarize_regime_block_acceptance_score,
)
from advanced_regime_acceptance.regime_block_acceptance_gates import (
    build_regime_block_acceptance_gate_registry,
)


def test_acceptance_scoring():
    gates_df, _ = build_regime_block_acceptance_gate_registry()
    score = calculate_regime_block_acceptance_score(gates_df)
    assert 0.0 <= score <= 1.0
    assert score == 1.0

    classification = classify_regime_block_acceptance_score(score)
    assert classification == "acceptance_pass"

    df, summary = build_regime_block_acceptance_score_report()
    assert summary["acceptance_score"] == 1.0
    assert summary["is_acceptable"] is True
    assert summary["official_approval"] is False
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
    assert summary["model_training_ready"] is False
    assert summary["non_signal"] is True

    s2 = summarize_regime_block_acceptance_score(df)
    assert s2["is_acceptable"] is True
