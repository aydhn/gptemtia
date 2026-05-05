import pytest
import pandas as pd
from unittest.mock import Mock, patch
from config.settings import Settings
from config.symbols import SymbolSpec
from asset_profiles.asset_profile_pipeline import AssetProfilePipeline


@pytest.fixture
def mock_settings():
    return Settings()


@pytest.fixture
def mock_data_lake():
    lake = Mock()
    # Mock has_features to return true for technical
    lake.has_features.side_effect = lambda spec, tf, fset: fset == "technical"

    # Mock load_features to return a simple df
    idx = pd.date_range("2023-01-01", periods=10)
    df = pd.DataFrame(
        {
            "close": [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],
            "volume_is_usable": [1] * 10,
        },
        index=idx,
    )
    lake.load_features.return_value = df

    return lake


@pytest.fixture
def mock_symbols():
    return [
        SymbolSpec("GC=F", "Gold", "metals", "precious", "USD"),
        SymbolSpec("SI=F", "Silver", "metals", "precious", "USD"),
        SymbolSpec("HG=F", "Copper", "metals", "industrial", "USD"),
        SymbolSpec("MACRO", "Macro", "macro", "macro", "USD"),
    ]


def test_pipeline_build_symbol_input(mock_data_lake, mock_settings, mock_symbols):
    pipeline = AssetProfilePipeline(mock_data_lake, mock_settings)
    df, summary = pipeline.build_symbol_input_frame(mock_symbols[0], "1d")

    assert not df.empty
    assert "close" in df.columns
    assert "trend" in summary["missing_feature_sets"]


def test_pipeline_build_for_symbol(mock_data_lake, mock_settings, mock_symbols):
    pipeline = AssetProfilePipeline(mock_data_lake, mock_settings)

    features, summary = pipeline.build_for_symbol(
        mock_symbols[0], mock_symbols, timeframe="1d", save=False
    )

    assert not features.empty
    assert "asset_behavior_score" in features.columns
    assert summary["symbol"] == "GC=F"
    assert summary["asset_profile"] == "Metals"


def test_pipeline_skip_macro(mock_data_lake, mock_settings, mock_symbols):
    pipeline = AssetProfilePipeline(mock_data_lake, mock_settings)

    features, summary = pipeline.build_for_symbol(
        mock_symbols[3], mock_symbols, timeframe="1d", save=False
    )

    assert features.empty
    assert any("Skipped" in w for w in summary["warnings"])


def test_pipeline_build_for_asset_class(mock_data_lake, mock_settings, mock_symbols):
    pipeline = AssetProfilePipeline(mock_data_lake, mock_settings)

    summary = pipeline.build_for_asset_class("metals", mock_symbols, save=False)

    assert "GC=F" in summary["symbols"]
    assert "SI=F" in summary["symbols"]
    assert "HG=F" in summary["symbols"]
    assert "MACRO" not in summary["symbols"]
