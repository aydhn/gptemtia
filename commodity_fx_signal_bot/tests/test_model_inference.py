import pytest
import pandas as pd
import numpy as np
from unittest.mock import MagicMock
from ml.model_inference import OfflineModelInference

def test_offline_model_inference_classification():
    model = MagicMock()
    model.predict.return_value = np.array(["predicted_up", "predicted_down"])
    model.predict_proba.return_value = np.array([[0.8, 0.2], [0.3, 0.7]])
    model.classes_ = np.array(["predicted_up", "predicted_down"])

    metadata = {"model_id": "m1", "task_type": "classification", "model_family": "rf", "target_column": "target"}

    inf = OfflineModelInference(model, None, metadata)
    df = pd.DataFrame({"A": [1, 2]})

    res, status = inf.predict_frame(df)

    assert status["status"] == "success"
    assert "class_probability_predicted_up" in res.columns
    assert "class_probability_up" in res.columns
    assert res.iloc[0]["predicted_label"] == "predicted_up"
    assert res.iloc[0]["confidence_score"] == 0.8

def test_offline_model_inference_regression():
    model = MagicMock()
    model.predict.return_value = np.array([0.05, -0.02])
    del model.predict_proba

    metadata = {"model_id": "m1", "task_type": "regression", "model_family": "rf", "target_column": "target"}

    inf = OfflineModelInference(model, None, metadata)
    df = pd.DataFrame({"A": [1, 2]})

    res, status = inf.predict_frame(df)

    assert status["status"] == "success"
    assert res.iloc[0]["predicted_value"] == 0.05
    assert res.iloc[0]["predicted_label"] is None
