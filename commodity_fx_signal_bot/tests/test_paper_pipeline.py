import pytest
import pandas as pd
from unittest.mock import Mock
from config.symbols import SymbolSpec
from paper.paper_pipeline import PaperTradingPipeline
from config.settings import settings

@pytest.fixture
def mock_lake():
    lake = Mock()
    df_valid = pd.DataFrame(
        {'open': [100.0, 102.0], 'high': [105.0, 105.0], 'low': [95.0, 95.0], 'close': [101.0, 103.0], 'symbol': ['GC=F', 'GC=F']},
        index=pd.to_datetime(['2024-01-01', '2024-01-02'])
    )
    lake.load_processed_ohlcv.return_value = df_valid
    lake.load_level_candidates.return_value = pd.DataFrame()
    lake.load_sizing_candidates.return_value = pd.DataFrame()
    lake.load_risk_candidates.return_value = pd.DataFrame()
    lake.load_ml_integration_features.return_value = pd.DataFrame()
    return lake

def test_pipeline_symbol(mock_lake):
    pipeline = PaperTradingPipeline(mock_lake, settings)
    spec = SymbolSpec("GC=F", "Gold", "commodity", "metals", "USD")

    arts, summ = pipeline.build_for_symbol_timeframe(spec, "1d", save=False)
    pass
    assert summ.get("input_level_candidates", 0) == 0

def test_pipeline_skip_macro(mock_lake):
    pipeline = PaperTradingPipeline(mock_lake, settings)
    spec = SymbolSpec("DXY", "Dollar Index", "macro", "currency", "USD")

    arts, summ = pipeline.build_for_symbol_timeframe(spec, "1d", save=False)
    assert "warning" in summ
    assert "Skipping" in summ["warning"]

def test_pipeline_universe(mock_lake):
    pipeline = PaperTradingPipeline(mock_lake, settings)
    specs = [
        SymbolSpec("GC=F", "Gold", "commodity", "metals", "USD"),
        SymbolSpec("DXY", "Dollar Index", "macro", "currency", "USD")
    ]

    res = pipeline.build_for_universe(specs, "1d", limit=2, save=False)
    pass
    pass
