from advanced_regime_rule_free.regime_candidate_state_integrity_manifest import (
    create_candidate_state_integrity_manifest,
    build_regime_candidate_state_integrity_manifest,
    summarize_candidate_state_integrity_manifest,
)


def test_create_candidate_state_integrity_manifest():
    m = create_candidate_state_integrity_manifest()
    assert m.current_phase == 128
    assert m.next_phase == 129
    assert m.target_final_phase == 160
    assert m.non_signal is True
    assert m.clustering_executed is False
    assert m.model_training_executed is False
    assert m.model_fit_executed is False
    assert m.model_predict_executed is False


def test_build_regime_candidate_state_integrity_manifest():
    df, summary = build_regime_candidate_state_integrity_manifest()
    assert len(df) == 1
    assert summary["is_valid"] is True
    assert summary["manifest_status"] == "MANIFEST_VALID"
    assert summary["zero_execution_guaranteed"] is True
    assert summary["non_signal"] is True
