import pytest
from experiments.experiment_labels import (
    list_experiment_type_labels,
    list_experiment_status_labels,
    list_hypothesis_status_labels,
    list_comparison_result_labels,
    validate_experiment_type,
    validate_experiment_status,
    validate_hypothesis_status,
    validate_comparison_result_label,
)

def test_list_experiment_type_labels():
    labels = list_experiment_type_labels()
    assert len(labels) > 0
    assert "candidate_experiment" in labels

def test_list_experiment_status_labels():
    labels = list_experiment_status_labels()
    assert len(labels) > 0
    assert "experiment_completed" in labels

def test_list_hypothesis_status_labels():
    labels = list_hypothesis_status_labels()
    assert len(labels) > 0
    assert "hypothesis_supported" in labels

def test_list_comparison_result_labels():
    labels = list_comparison_result_labels()
    assert len(labels) > 0
    assert "candidate_better" in labels

def test_validate_experiment_type():
    validate_experiment_type("baseline_experiment")
    with pytest.raises(ValueError):
        validate_experiment_type("unknown_type_999")

def test_validate_experiment_status():
    validate_experiment_status("experiment_planned")
    with pytest.raises(ValueError):
        validate_experiment_status("invalid_status")

def test_validate_hypothesis_status():
    validate_hypothesis_status("hypothesis_proposed")
    with pytest.raises(ValueError):
        validate_hypothesis_status("invalid")

def test_validate_comparison_result_label():
    validate_comparison_result_label("candidate_better")
    with pytest.raises(ValueError):
        validate_comparison_result_label("winner")
