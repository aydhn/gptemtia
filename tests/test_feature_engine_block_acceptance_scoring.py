from advanced_feature_factor_acceptance.feature_engine_block_acceptance_scoring import (
    calculate_feature_engine_block_acceptance_score,
    build_feature_engine_block_acceptance_score_report,
    classify_acceptance_score,
    summarize_acceptance_score,
)
from advanced_feature_factor_acceptance.feature_engine_block_acceptance_gates import (
    build_feature_engine_block_acceptance_gate_registry,
)

def test_acceptance_scoring():
    gates_df, _ = build_feature_engine_block_acceptance_gate_registry()
    score = calculate_feature_engine_block_acceptance_score(gates_df)
    assert 0.0 <= score <= 1.0
    assert score >= 0.9

    tier = classify_acceptance_score(score)
    assert tier == "EXCELLENT_READINESS"

    df, summary = build_feature_engine_block_acceptance_score_report()
    assert summary["overall_score"] == score
    assert summary["meets_profile_minimum"] is True
    assert summary["non_signal"] is True
    assert summary["official_approval"] is False
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False

    s = summarize_acceptance_score(df)
    assert s["overall_score"] == score
    assert s["non_signal"] is True
