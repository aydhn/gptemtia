import pytest
from ml.baseline_models import create_dummy_model, create_logistic_regression_model, create_random_forest_model, create_hist_gradient_boosting_model, create_baseline_model

def test_create_dummy_model():
    model = create_dummy_model("classification")
    assert model is not None
    model = create_dummy_model("regression")
    assert model is not None

def test_create_logistic_regression_model():
    model = create_logistic_regression_model()
    assert model is not None

def test_create_random_forest_model():
    model = create_random_forest_model("classification")
    assert model is not None

def test_create_hist_gradient_boosting_model():
    model = create_hist_gradient_boosting_model("regression")
    assert model is not None

def test_create_baseline_model():
    model = create_baseline_model("dummy", "classification")
    assert model is not None
    with pytest.raises(ValueError):
        create_baseline_model("unknown", "classification")
