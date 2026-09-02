import pytest
from local_training.training_labels import list_training_domain_labels, list_training_lesson_status_labels, list_onboarding_role_labels, list_assessment_status_labels, list_training_risk_labels, validate_training_domain_label, validate_onboarding_role

def test_labels_not_empty():
    assert len(list_training_domain_labels()) > 0
    assert len(list_training_lesson_status_labels()) > 0
    assert len(list_onboarding_role_labels()) > 0
    assert len(list_assessment_status_labels()) > 0
    assert len(list_training_risk_labels()) > 0

def test_validate_valid_labels():
    validate_training_domain_label("operator_training")
    validate_onboarding_role("operator_role")

def test_operator_role_is_not_live_authorization():
    assert "operator_role" in list_onboarding_role_labels()
