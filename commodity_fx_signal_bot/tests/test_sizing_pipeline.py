import pandas as pd
from unittest.mock import MagicMock
from sizing.sizing_pipeline import SizingPipeline
from sizing.sizing_config import get_default_sizing_profile
from config.settings import Settings
from config.symbols import SymbolSpec

def test_sizing_pipeline_build_for_symbol_timeframe():
    mock_lake = MagicMock()

    # Mock data
    risk_df = pd.DataFrame({
        "risk_id": ["r1"], "directional_bias": ["long"], "asset_class": ["metals"],
        "risk_readiness_score": [0.9], "total_pretrade_risk_score": [0.1]
    }, index=pd.date_range("2023-01-01", periods=1))

    mock_lake.has_features.return_value = True
    mock_lake.load_features.return_value = risk_df

    ohlcv = pd.DataFrame({"close": [100.0]}, index=pd.date_range("2023-01-01", periods=1))
    mock_lake.load_processed_ohlcv.return_value = ohlcv

    pipeline = SizingPipeline(mock_lake, Settings(), get_default_sizing_profile())
    spec = SymbolSpec("GC=F", "Gold", "test", "metals", "USD")

    df, summary = pipeline.build_for_symbol_timeframe(spec, "1d", save=False)

    assert not df.empty
    assert "sizing_id" in df.columns
    assert summary["sizing_candidate_count"] > 0

def test_sizing_pipeline_skip_synthetic():
    mock_lake = MagicMock()
    pipeline = SizingPipeline(mock_lake, Settings(), get_default_sizing_profile())
    spec = SymbolSpec("SYNTH", "Synthetic", "synthetic", "benchmark", "USD", data_source="synthetic")

    df, summary = pipeline.build_for_symbol_timeframe(spec, "1d", save=False)
    assert df.empty
    assert "Skipping synthetic/macro/benchmark symbol." in summary["warnings"]
