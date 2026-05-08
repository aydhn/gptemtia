import pytest
from unittest.mock import MagicMock
import pandas as pd
from config.settings import settings
from config.symbols import SymbolSpec
from ml.training_pipeline import MLTrainingPipeline
from ml.training_config import get_default_ml_training_profile

def test_pipeline_skip_synthetic():
    mock_lake = MagicMock()
    pipeline = MLTrainingPipeline(mock_lake, settings, get_default_ml_training_profile())

    spec = SymbolSpec("SYN_TEST", "synthetic", "synthetic", "USD", "yahoo")
    summary, res = pipeline.train_for_symbol_timeframe(spec)

    assert "Skipping ML training" in res["warnings"][0]

def test_pipeline_missing_dataset():
    mock_lake = MagicMock()
    mock_lake.load_ml_supervised_dataset.return_value = pd.DataFrame()
    pipeline = MLTrainingPipeline(mock_lake, settings, get_default_ml_training_profile())

    spec = SymbolSpec("GC=F", "metals", "gold", "USD", "yahoo")
    summary, res = pipeline.train_for_symbol_timeframe(spec)

    assert "Missing dataset" in res["warnings"][0]
