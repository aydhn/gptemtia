from ml.dataset_labels import list_target_type_labels, list_direction_class_labels, list_candidate_outcome_labels, list_ml_split_labels, list_dataset_status_labels, validate_target_type_label, validate_direction_class_label, validate_dataset_status_label
import pytest

def test_list_labels():
    assert len(list_target_type_labels()) > 0
    assert len(list_direction_class_labels()) > 0
    assert len(list_candidate_outcome_labels()) > 0
    assert len(list_ml_split_labels()) > 0
    assert len(list_dataset_status_labels()) > 0

def test_validate_labels():
    validate_target_type_label("forward_return")
    validate_direction_class_label("up")
    validate_dataset_status_label("dataset_ready_candidate")

    with pytest.raises(ValueError):
         validate_target_type_label("invalid")
