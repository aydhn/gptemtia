"""
Tests for Universe Analyzer
"""

from unittest.mock import MagicMock

import pandas as pd
import pytest

from config.settings import Settings
from config.symbols import SymbolSpec
from data.data_pipeline import DataPipeline
from data.universe_analyzer import SymbolReliabilityResult, UniverseAnalyzer


@pytest.fixture
def settings():
    return Settings(min_ohlcv_rows=50)


@pytest.fixture
def pipeline():
    return MagicMock(spec=DataPipeline)


def test_analyze_symbol_success(settings, pipeline):
    # Mock successful fetch
    dates = pd.date_range(start="2024-01-01", periods=60)
    df = pd.DataFrame(
        {
            "open": [10.0] * 60,
            "high": [12.0] * 60,
            "low": [9.0] * 60,
            "close": [11.0] * 60,
            "volume": [1000] * 60,
        },
        index=dates,
    )
    df.attrs = {
        "requested_symbol": "TEST",
        "resolved_symbol": "TEST",
        "used_alias": False,
        "data_source": "yahoo",
    }
    pipeline.fetch_symbol_data.return_value = df

    analyzer = UniverseAnalyzer(pipeline, settings)
    spec = SymbolSpec(
        symbol="TEST",
        name="Test Symbol",
        asset_class="metals",
        sub_class="precious",
        currency="USD",
        data_source="yahoo",
    )

    result = analyzer.analyze_symbol(spec, interval="1d", period="1y")
    assert result.success is True
    assert result.rows == 60
    assert result.reliability_score == 100.0
    assert result.reliability_grade == "A"
    assert result.used_alias is False


def test_analyze_symbol_empty_or_error(settings, pipeline):
    # Mock failed fetch
    pipeline.fetch_symbol_data.side_effect = Exception("Failed to fetch")

    analyzer = UniverseAnalyzer(pipeline, settings)
    spec = SymbolSpec(
        symbol="TEST",
        name="Test Symbol",
        asset_class="metals",
        sub_class="precious",
        currency="USD",
        data_source="yahoo",
    )

    result = analyzer.analyze_symbol(spec, interval="1d", period="1y")
    assert result.success is False
    assert result.rows == 0
    assert result.reliability_score == 0.0
    assert result.reliability_grade == "F"
    assert "Failed to fetch" in result.error


def test_analyze_symbol_used_alias(settings, pipeline):
    dates = pd.date_range(start="2024-01-01", periods=60)
    df = pd.DataFrame(
        {
            "open": [10.0] * 60,
            "high": [12.0] * 60,
            "low": [9.0] * 60,
            "close": [11.0] * 60,
            "volume": [1000] * 60,
        },
        index=dates,
    )
    df.attrs = {
        "requested_symbol": "TEST",
        "resolved_symbol": "TEST2",
        "used_alias": True,
        "data_source": "yahoo",
    }
    pipeline.fetch_symbol_data.return_value = df

    analyzer = UniverseAnalyzer(pipeline, settings)
    spec = SymbolSpec(
        symbol="TEST",
        name="Test Symbol",
        asset_class="metals",
        sub_class="precious",
        currency="USD",
        data_source="yahoo",
    )

    result = analyzer.analyze_symbol(spec, interval="1d", period="1y")
    assert result.used_alias is True
    assert result.reliability_score == 95.0  # -5 for used_alias
    assert result.reliability_grade == "A"


def test_analyze_symbol_synthetic(settings, pipeline):
    analyzer = UniverseAnalyzer(pipeline, settings)
    spec = SymbolSpec(
        symbol="TEST",
        name="Test Symbol",
        asset_class="benchmark",
        sub_class="synthetic",
        currency="USD",
        data_source="synthetic",
    )

    result = analyzer.analyze_symbol(spec, interval="1d", period="1y")
    assert result.success is True
    assert result.reliability_score == 100.0
    assert result.reliability_grade == "SYNTHETIC"


def test_results_to_dataframe():
    res1 = SymbolReliabilityResult(
        symbol="TEST1",
        requested_symbol="TEST1",
        resolved_symbol="TEST1",
        name="Test1",
        asset_class="metals",
        sub_class="precious",
        data_source="yahoo",
        success=True,
        rows=100,
        start="2024-01-01",
        end="2024-04-10",
        last_close=10.0,
        missing_close_ratio=0.0,
        duplicate_index_count=0,
        negative_price_count=0,
        high_low_error_count=0,
        used_alias=False,
        error="",
        reliability_score=100.0,
        reliability_grade="A",
    )
    df = UniverseAnalyzer.results_to_dataframe([res1])
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
    assert df.iloc[0]["symbol"] == "TEST1"


def test_summarize_results():
    res1 = SymbolReliabilityResult(
        symbol="TEST1",
        requested_symbol="TEST1",
        resolved_symbol="TEST1",
        name="Test1",
        asset_class="metals",
        sub_class="precious",
        data_source="yahoo",
        success=True,
        rows=100,
        start="2024-01-01",
        end="2024-04-10",
        last_close=10.0,
        missing_close_ratio=0.0,
        duplicate_index_count=0,
        negative_price_count=0,
        high_low_error_count=0,
        used_alias=False,
        error="",
        reliability_score=100.0,
        reliability_grade="A",
    )
    summary = UniverseAnalyzer.summarize_results([res1])
    assert summary["total_analyzed"] == 1
    assert summary["success_count"] == 1
    assert summary["fail_count"] == 0
    assert summary["avg_score"] == 100.0
    assert summary["grade_distribution"] == {"A": 1}
    assert summary["asset_class_success_rate"] == {"metals": 1.0}
    assert len(summary["best_10"]) == 1
