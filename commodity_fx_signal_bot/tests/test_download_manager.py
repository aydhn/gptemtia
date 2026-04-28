import pytest
from pathlib import Path
import pandas as pd
from unittest.mock import Mock, MagicMock

from config.settings import Settings
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from data.storage.download_journal import DownloadJournal
from data.data_pipeline import DataPipeline
from data.download_manager import DownloadManager


@pytest.fixture
def mock_settings():
    settings = Settings()
    settings.data_lake_enabled = True
    settings.journal_enabled = True
    settings.skip_synthetic_downloads = True
    settings.skip_macro_downloads_in_ohlcv_pipeline = True
    return settings


@pytest.fixture
def mock_data_lake():
    lake = Mock(spec=DataLake)
    lake.save_ohlcv.return_value = Path("/fake/path.parquet")
    lake.load_metadata.return_value = {}
    return lake


@pytest.fixture
def mock_journal():
    return Mock(spec=DownloadJournal)


@pytest.fixture
def mock_pipeline():
    return Mock(spec=DataPipeline)


@pytest.fixture
def download_manager(mock_pipeline, mock_data_lake, mock_journal, mock_settings):
    return DownloadManager(
        pipeline=mock_pipeline,
        data_lake=mock_data_lake,
        journal=mock_journal,
        settings=mock_settings,
    )


@pytest.fixture
def valid_df():
    dates = pd.date_range("2023-01-01", periods=100, tz="UTC")
    df = pd.DataFrame(
        {
            "open": [10.0] * 100,
            "high": [10.5] * 100,
            "low": [9.5] * 100,
            "close": [10.2] * 100,
            "adj_close": [10.2] * 100,
            "volume": [100] * 100,
        },
        index=dates,
    )
    df.attrs["resolved_symbol"] = "GC=F"
    df.attrs["used_alias"] = False
    df.attrs["provider_interval"] = "1d"
    df.attrs["source_provider"] = "YahooProvider"
    return df


@pytest.fixture
def mock_spec():
    return SymbolSpec(
        symbol="GC=F",
        name="Gold",
        asset_class="metals",
        sub_class="precious",
        currency="USD",
        data_source="yahoo",
    )


@pytest.fixture
def synthetic_spec():
    return SymbolSpec(
        symbol="BENCHMARK",
        name="Bench",
        asset_class="synthetic",
        sub_class="index",
        currency="USD",
        data_source="synthetic",
    )


def test_download_symbol_success(
    download_manager, mock_pipeline, mock_data_lake, mock_journal, mock_spec, valid_df
):
    mock_pipeline.fetch_symbol_data.return_value = valid_df

    df = download_manager.download_symbol_timeframe(mock_spec, "1d")

    assert df is not None
    mock_pipeline.fetch_symbol_data.assert_called_once()
    mock_data_lake.save_ohlcv.assert_called_once()
    mock_data_lake.save_metadata.assert_called_once()
    mock_journal.append.assert_called_once()

    # Check journal entry
    journal_call_args = mock_journal.append.call_args[0][0]
    assert journal_call_args.success is True
    assert journal_call_args.rows == 100


def test_download_symbol_failure(
    download_manager, mock_pipeline, mock_journal, mock_spec
):
    mock_pipeline.fetch_symbol_data.side_effect = Exception("API Error")

    df = download_manager.download_symbol_timeframe(mock_spec, "1d")

    assert df is None
    mock_journal.append.assert_called_once()
    journal_call_args = mock_journal.append.call_args[0][0]
    assert journal_call_args.success is False
    assert "API Error" in journal_call_args.error


def test_skip_synthetic(download_manager, mock_pipeline, synthetic_spec):
    df = download_manager.download_symbol_timeframe(synthetic_spec, "1d")

    assert df is None
    mock_pipeline.fetch_symbol_data.assert_not_called()


def test_download_universe_no_crash(
    download_manager, mock_pipeline, mock_spec, valid_df
):
    spec2 = SymbolSpec(
        symbol="BAD", name="Bad", asset_class="metals", sub_class="", currency="USD"
    )

    def side_effect(spec, **kwargs):
        if spec.symbol == "BAD":
            raise Exception("Fail")
        return valid_df

    mock_pipeline.fetch_symbol_data.side_effect = side_effect

    specs = [mock_spec, spec2]
    timeframes_by_symbol = {"GC=F": ("1d",), "BAD": ("1d",)}

    results = download_manager.download_universe(specs, timeframes_by_symbol)

    assert results["total_attempts"] == 2
    assert results["success_count"] == 1
    assert results["failure_count"] == 1
    assert len(results["errors"]) == 1
    assert "Fetch failed" in results["errors"][0]
