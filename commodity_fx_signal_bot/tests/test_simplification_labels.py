import pytest
from local_simplification.simplification_labels import (
    list_simplification_domain_labels,
    list_simplification_candidate_labels,
    list_simplification_status_labels,
    list_complexity_level_labels,
    list_simplification_risk_labels,
    validate_simplification_domain_label,
    validate_simplification_candidate_label
)

def test_lists_not_empty():
    assert len(list_simplification_domain_labels()) > 0
    assert len(list_simplification_candidate_labels()) > 0
    assert len(list_simplification_status_labels()) > 0
    assert len(list_complexity_level_labels()) > 0
    assert len(list_simplification_risk_labels()) > 0

def test_validate_domain_label_passes():
    validate_simplification_domain_label(list_simplification_domain_labels()[0])

def test_validate_candidate_label_passes():
    validate_simplification_candidate_label(list_simplification_candidate_labels()[0])
