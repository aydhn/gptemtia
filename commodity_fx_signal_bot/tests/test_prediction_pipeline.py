import pytest
from unittest.mock import MagicMock
from ml.prediction_pipeline import MLPredictionPipeline
from config.symbols import SymbolSpec

def test_ml_prediction_pipeline_init():
    mock_lake = MagicMock()
    mock_settings = MagicMock()

    pipeline = MLPredictionPipeline(mock_lake, mock_settings)
    assert pipeline is not None
    assert pipeline.profile.name == "balanced_offline_prediction"
