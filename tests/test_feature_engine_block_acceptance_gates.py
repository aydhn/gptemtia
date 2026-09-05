from advanced_feature_factor_acceptance.feature_engine_block_acceptance_gates import (
    build_feature_engine_block_acceptance_gate_registry,
    validate_acceptance_gate,
    summarize_acceptance_gates,
)

def test_feature_engine_block_acceptance_gates():
    df, summary = build_feature_engine_block_acceptance_gate_registry()
    assert len(df) >= 16
    assert summary["passed_gates"] == len(df)
    assert summary["failed_gates"] == 0
    assert summary["all_passed"] is True
    assert summary["non_signal"] is True
    assert summary["official_approval"] is False
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False

    gate_dict = df.iloc[0].to_dict()
    v = validate_acceptance_gate(gate_dict)
    assert v["is_valid"] is True
    assert v["non_signal"] is True

    s = summarize_acceptance_gates(df)
    assert s["all_passed"] is True
    assert "safety" in s["categories"]
