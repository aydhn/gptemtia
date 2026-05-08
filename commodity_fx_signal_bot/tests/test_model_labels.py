import pytest
from ml.model_labels import list_task_type_labels, list_model_family_labels, list_model_status_labels, validate_task_type, validate_model_family, validate_model_status, is_classification_task, is_regression_task

def test_list_labels():
    assert len(list_task_type_labels()) > 0
    assert len(list_model_family_labels()) > 0
    assert len(list_model_status_labels()) > 0

def test_validate_task_type():
    validate_task_type("classification")
    validate_task_type("regression")
    with pytest.raises(ValueError):
        validate_task_type("unknown")

def test_validate_model_family():
    validate_model_family("dummy")
    validate_model_family("random_forest")
    with pytest.raises(ValueError):
        validate_model_family("unknown")

def test_is_classification_task():
    assert is_classification_task("classification")
    assert not is_classification_task("regression")
    assert not is_regression_task("classification")
    assert is_regression_task("regression")
