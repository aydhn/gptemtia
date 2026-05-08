#!/bin/bash
cd commodity_fx_signal_bot
rm -rf tests/__pycache__
rm -rf ml/__pycache__

cat << 'INNER_EOF' > tests/test_dataset_pipeline.py
import pytest
import pandas as pd
from unittest.mock import Mock
from config.symbols import SymbolSpec
from ml.dataset_pipeline import MLDatasetPipeline
from config.settings import settings

def test_build_for_symbol_timeframe():
    mock_dl = Mock()
    mock_dl.load_processed_ohlcv.return_value = pd.DataFrame({"close": range(250)}, index=pd.date_range("2020-01-01", periods=250))
    # Fake feature
    mock_dl.load_technical_indicators.return_value = pd.DataFrame({"rsi": range(250)}, index=pd.date_range("2020-01-01", periods=250))

    pipeline = MLDatasetPipeline(mock_dl, settings)
    spec = SymbolSpec(symbol="TEST", name="Test", asset_class="test", sub_class="test", currency="USD")

    dataset, summary = pipeline.build_for_symbol_timeframe(spec, "1d", save=False)

    # Check that it produces *something* without crashing
    assert "warnings" in summary

def test_build_for_universe():
    mock_dl = Mock()
    mock_dl.load_processed_ohlcv.return_value = pd.DataFrame({"close": range(250)}, index=pd.date_range("2020-01-01", periods=250))
    mock_dl.load_technical_indicators.return_value = pd.DataFrame({"rsi": range(250)}, index=pd.date_range("2020-01-01", periods=250))

    pipeline = MLDatasetPipeline(mock_dl, settings)
    specs = [SymbolSpec(symbol="TEST1", name="Test 1", asset_class="test", sub_class="test", currency="USD")]

    summary = pipeline.build_for_universe(specs, "1d", limit=1, save=False)
    assert summary["processed"] == 1
INNER_EOF

PYTHONPATH=. python -m pytest tests/test_dataset_*.py tests/test_target_engineering.py tests/test_feature_matrix_builder.py tests/test_leakage_checks.py tests/test_splitters.py tests/test_ml_dataset_scripts_contract.py
