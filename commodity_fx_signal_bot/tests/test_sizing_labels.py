from sizing.sizing_labels import (
    list_sizing_candidate_labels,
    validate_sizing_candidate_label,
    sizing_severity_from_risk,
    is_blocking_sizing_label
)
import pytest

def test_list_sizing_candidate_labels():
    labels = list_sizing_candidate_labels()
    assert len(labels) > 0
    assert "sizing_approved_candidate" in labels

def test_validate_sizing_candidate_label():
    # Should not raise
    validate_sizing_candidate_label("sizing_approved_candidate")

    with pytest.raises(ValueError):
        validate_sizing_candidate_label("invalid_label")

def test_sizing_severity_from_risk():
    assert sizing_severity_from_risk(0.1) == "low"
    assert sizing_severity_from_risk(0.9) == "extreme"

def test_is_blocking_sizing_label():
    assert is_blocking_sizing_label("sizing_rejected_candidate") is True
    assert is_blocking_sizing_label("invalid_risk_candidate") is True
    assert is_blocking_sizing_label("sizing_approved_candidate") is False
