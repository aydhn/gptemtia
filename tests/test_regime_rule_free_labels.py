import pytest
from advanced_regime_rule_free.regime_rule_free_labels import (
    list_regime_rule_free_domain_labels,
    list_regime_rule_free_status_labels,
    list_candidate_state_labels,
    validate_regime_rule_free_domain_label,
    validate_regime_rule_free_status_label,
    validate_candidate_state_label,
)


def test_regime_rule_free_domain_labels():
    labels = list_regime_rule_free_domain_labels()
    assert len(labels) >= 20
    assert "rule_free_labeling_contract_domain" in labels
    assert "candidate_state_schema_domain" in labels
    assert "pseudo_state_schema_domain" in labels
    assert "unsupervised_prep_contract_domain" in labels
    assert "clustering_input_contract_domain" in labels
    assert "phase_129_handoff_domain" in labels
    assert validate_regime_rule_free_domain_label("rule_free_labeling_contract_domain")
    assert not validate_regime_rule_free_domain_label("non_existent_domain")


def test_regime_rule_free_status_labels():
    status_labels = list_regime_rule_free_status_labels()
    assert "rule_free_ready" in status_labels
    assert "rule_free_placeholder_only" in status_labels
    assert "rule_free_manual_review_required" in status_labels
    assert validate_regime_rule_free_status_label("rule_free_ready")
    assert not validate_regime_rule_free_status_label("invalid_status")


def test_candidate_state_labels():
    candidate_labels = list_candidate_state_labels()
    assert "candidate_state_volatility_context" in candidate_labels
    assert "candidate_state_trend_context" in candidate_labels
    assert "candidate_state_range_context" in candidate_labels
    assert "candidate_state_macro_event_context" in candidate_labels
    assert "candidate_state_uncertain_context" in candidate_labels
    assert validate_candidate_state_label("candidate_state_volatility_context")
    assert not validate_candidate_state_label("arbitrary_label")
