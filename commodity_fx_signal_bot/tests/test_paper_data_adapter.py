import pytest
import pandas as pd
from unittest.mock import Mock
from config.symbols import SymbolSpec
from paper.paper_data_adapter import PaperDataAdapter

@pytest.fixture
def mock_lake():
    lake = Mock()
    # Mock return values for valid calls
    df_valid = pd.DataFrame({'close': [100.0, 101.0]}, index=pd.to_datetime(['2024-01-01', '2024-01-02']))
    lake.load_processed_ohlcv.return_value = df_valid
    lake.load_level_candidates.return_value = pd.DataFrame()
    lake.load_sizing_candidates.return_value = pd.DataFrame()
    lake.load_risk_candidates.return_value = pd.DataFrame()
    lake.load_ml_integration_features.return_value = pd.DataFrame()
    return lake

def test_load_price_frame(mock_lake):
    adapter = PaperDataAdapter(mock_lake)
    spec = SymbolSpec("GC=F", "Gold", "commodity", "metals", "USD")
    df, w = adapter.load_price_frame(spec, "1d")
    assert not df.empty
    assert "error" not in w

def test_missing_candidates_no_crash(mock_lake):
    adapter = PaperDataAdapter(mock_lake)
    spec = SymbolSpec("GC=F", "Gold", "commodity", "metals", "USD")
    frames, warnings = adapter.load_paper_context_frames(spec, "1d")
    assert "level_candidates" in frames
    assert "warning" in str(warnings) # expecting empty warnings
