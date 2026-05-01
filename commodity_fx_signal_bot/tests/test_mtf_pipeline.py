import pytest
from unittest.mock import Mock
import pandas as pd
from config.symbols import SymbolSpec
from mtf.mtf_pipeline import MTFPipeline
from config.settings import Settings


def test_mtf_pipeline_build_for_symbol():
    mock_lake = Mock()
    # Let loader find something
    mock_lake.has_features.return_value = True
    dates = pd.date_range("2023-01-01", periods=5, freq="1d")
    df = pd.DataFrame({"close": [1, 2, 3, 4, 5]}, index=dates)
    mock_lake.load_features.return_value = df

    settings = Settings()
    settings.save_mtf_features = False
    settings.save_mtf_events = False

    pipeline = MTFPipeline(mock_lake, settings)
    spec = SymbolSpec("TEST", "crypto", "crypto", "crypto", "USD")

    res_df, summ = pipeline.build_for_symbol(spec, save=False, include_events=True)

    assert not res_df.empty
    assert summ["symbol"] == "TEST"
    assert "quality_report" in summ
