import pytest
import pandas as pd
import numpy as np
from ml.model_evaluator import evaluate_classification_model, evaluate_regression_model, build_confusion_matrix_table
from ml.preprocessing import BasicPreprocessor

class MockModel:
    def predict(self, X):
        return np.zeros(len(X))

def test_evaluate_classification_model():
    model = MockModel()
    preprocessor = BasicPreprocessor()

    X = pd.DataFrame({"feat1": [1, 2, 3, 4]})
    y = pd.Series([0, 0, 1, 1])

    metrics = evaluate_classification_model(model, preprocessor, X, y)

    assert "accuracy" in metrics
    assert metrics["accuracy"] == 0.5  # All 0s predicted
    assert "balanced_accuracy" in metrics

def test_evaluate_regression_model():
    model = MockModel()
    preprocessor = BasicPreprocessor()

    X = pd.DataFrame({"feat1": [1, 2, 3, 4]})
    y = pd.Series([0.1, 0.2, 0.3, 0.4])

    metrics = evaluate_regression_model(model, preprocessor, X, y)

    assert "rmse" in metrics
    assert "mae" in metrics
    assert "r2" in metrics
