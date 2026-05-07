import pytest
from levels.level_labels import (
    list_level_candidate_labels,
    validate_level_candidate_label,
    list_level_type_labels,
    validate_level_type_label,
    level_severity_from_score,
    is_blocking_level_label,
)


def test_list_labels():
    labels = list_level_candidate_labels()
    assert len(labels) > 0
    assert "level_approved_candidate" in labels


def test_validate_labels():
    validate_level_candidate_label("level_approved_candidate")
    with pytest.raises(ValueError):
        validate_level_candidate_label("invalid_label_123")


def test_severity_from_score():
    assert level_severity_from_score(0.1) == "low"
    assert level_severity_from_score(0.9) == "extreme"


def test_is_blocking_label():
    assert is_blocking_level_label("level_rejected_candidate") is True
    assert is_blocking_level_label("level_approved_candidate") is False
