import pytest
import pandas as pd
from unittest.mock import MagicMock
from commodity_fx_signal_bot.ml.inference_preprocessor import InferencePreprocessor

def test_inference_preprocessor_align_features():
    prep = MagicMock()
    schema = {"features": ["A", "B", "C"]}
    ip = InferencePreprocessor(prep, schema)

    df = pd.DataFrame({"A": [1, 2], "B": [3, 4], "D": [5, 6], "target_return": [0.1, 0.2]})

    aligned, audit = ip.align_features(df)

    assert "target_return" not in aligned.columns
    assert "D" not in aligned.columns
    assert "C" in aligned.columns
    assert list(aligned.columns) == ["A", "B", "C"]

    assert "D" in audit["dropped"]
    assert "target_return" in audit["dropped_targets"]
    assert "C" in audit["added"]

def test_inference_preprocessor_transform():
    prep = MagicMock()
    prep.transform.return_value = [[1, 2], [3, 4]]

    ip = InferencePreprocessor(prep)
    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})

    res, status = ip.transform(df)
    assert status["status"] == "success"
    prep.transform.assert_called_once()
    assert not hasattr(prep, "fit") or not prep.fit.called
