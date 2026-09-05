from advanced_regime_rule_free.regime_rule_free_models import (
    RegimeRuleFreeProfileItem,
    RuleFreeLabelingContract,
    CandidateStateAssignmentPolicy,
    CandidateStateSchemaItem,
    PseudoStateSchemaItem,
    UnsupervisedPrepContract,
    ClusteringInputContract,
    AlgorithmPlaceholder,
    CandidateStateMetadataItem,
    CandidateStateIntegrityManifest,
    CandidateStateManualReviewItem,
)


def test_regime_rule_free_profile_item_invariants():
    item = RegimeRuleFreeProfileItem(
        profile_name="test_profile",
        description="test",
    )
    assert item.current_phase == 128
    assert item.target_final_phase == 160
    assert item.next_phase == 129
    assert item.non_signal is True
    assert item.source_preserved is True
    assert item.clustering_allowed is False
    assert item.model_training_allowed is False


def test_rule_free_labeling_contract_invariants():
    c = RuleFreeLabelingContract(
        contract_name="test_contract",
        candidate_state_family="volatility",
        source_matrix_contract_ref="technical_indicator_matrix_contract",
    )
    assert c.non_signal_required is True
    assert c.target_label_forbidden is True
    assert c.prediction_forbidden is True
    assert c.model_training_allowed is False
    assert c.clustering_allowed is False


def test_candidate_state_integrity_manifest_invariants():
    m = CandidateStateIntegrityManifest(manifest_name="test_manifest")
    assert m.current_phase == 128
    assert m.next_phase == 129
    assert m.target_final_phase == 160
    assert m.non_signal is True
    assert m.source_preserved is True
    assert m.official_approval is False
    assert m.production_ready is False
    assert m.broker_ready is False
    assert m.contains_target_or_prediction is False
    assert m.contains_trading_recommendation is False
    assert m.contains_full_article_text is False
    assert m.model_training_executed is False
    assert m.model_fit_executed is False
    assert m.model_predict_executed is False
    assert m.clustering_executed is False
    assert m.unsupervised_execution is False
    assert m.destructive_action_allowed is False
    assert m.auto_fix_allowed is False
    assert m.auto_drop_allowed is False
