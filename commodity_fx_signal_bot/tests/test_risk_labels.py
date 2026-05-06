import pytest
from risk.risk_labels import (
    list_risk_candidate_labels,
    validate_risk_candidate_label,
    severity_from_score,
    is_blocking_risk_label,
)


def test_list_risk_candidate_labels():
    labels = list_risk_candidate_labels()
    assert "risk_approval_candidate" in labels


def test_validate_risk_candidate_label():
    validate_risk_candidate_label("risk_approval_candidate")  # Should pass
    with pytest.raises(ValueError):
        validate_risk_candidate_label("invalid")


def test_severity_from_score():
    assert severity_from_score(0.1) == "low"
    assert severity_from_score(0.9) == "extreme"


def test_is_blocking_risk_label():
    assert is_blocking_risk_label("risk_rejection_candidate")
    assert not is_blocking_risk_label("risk_approval_candidate")
