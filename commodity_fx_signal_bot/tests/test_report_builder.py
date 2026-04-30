"""
Tests for report builder
"""

import pandas as pd

from config.symbols import DEFAULT_SYMBOL_UNIVERSE
from data.universe_analyzer import SymbolReliabilityResult
from reports.report_builder import (
    build_asset_class_summary,
    build_reliability_report,
    build_universe_report,
    save_dataframe_report,
    save_text_report,
)


def test_build_universe_report():
    report = build_universe_report(DEFAULT_SYMBOL_UNIVERSE)
    assert isinstance(report, str)
    assert "Total Symbols:" in report
    assert "Breakdown by Asset Class:" in report


def test_build_reliability_report():
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
    report = build_reliability_report([res1])
    assert isinstance(report, str)
    assert "Total Analyzed: 1" in report
    assert "Average Score: 100.00" in report


def test_build_asset_class_summary():
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
    summary = build_asset_class_summary([res1])
    assert isinstance(summary, str)
    assert "metals: 100.0%" in summary


def test_save_text_report(tmp_path):
    report_text = "Test Report"
    path = tmp_path / "report.txt"
    save_text_report(report_text, path)
    assert path.exists()
    assert path.read_text() == "Test Report"


def test_save_dataframe_report(tmp_path):
    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    path = tmp_path / "report.csv"
    save_dataframe_report(df, path)
    assert path.exists()
    loaded_df = pd.read_csv(path)
    assert len(loaded_df) == 2


def test_build_volatility_feature_preview_report():
    import pandas as pd
    from reports.report_builder import build_volatility_feature_preview_report

    summary = {"type": "compact", "input_rows": 100, "feature_count": 5}
    tail_df = pd.DataFrame({"atr_14": [1, 2]})
    rep = build_volatility_feature_preview_report("GC=F", "1d", summary, tail_df)
    assert "VOLATILITY FEATURE PREVIEW" in rep
    assert "compact" in rep
    assert "atr_14" in rep


def test_build_volatility_event_preview_report():
    import pandas as pd
    from reports.report_builder import build_volatility_event_preview_report

    summary = {"total_event_count": 5}
    tail_df = pd.DataFrame({"event_test": [1, 1]})
    rep = build_volatility_event_preview_report("GC=F", "1d", summary, tail_df)
    assert "VOLATILITY EVENT PREVIEW" in rep
    assert "event_test" in rep


def test_build_volatility_batch_report():
    from reports.report_builder import build_volatility_batch_report

    summary = {"total_attempts": 10, "success_count": 10}
    rep = build_volatility_batch_report(summary)
    assert "VOLATILITY BATCH BUILD SUMMARY" in rep


def test_build_volatility_status_report():
    import pandas as pd
    from reports.report_builder import build_volatility_status_report

    summary = {"total_symbols": 5}
    df = pd.DataFrame()
    rep = build_volatility_status_report(df, summary)
    assert "VOLATILITY STATUS REPORT" in rep


def test_build_mean_reversion_feature_preview_report():
    import pandas as pd
    from reports.report_builder import build_mean_reversion_feature_preview_report

    summary = {"type": "compact", "input_rows": 100, "feature_count": 5}
    tail_df = pd.DataFrame({"zscore_close_20": [1, 2]})
    rep = build_mean_reversion_feature_preview_report("GC=F", "1d", summary, tail_df)
    assert "MEAN REVERSION FEATURE PREVIEW" in rep
    assert "compact" in rep
    assert "zscore_close_20" in rep


def test_build_mean_reversion_event_preview_report():
    import pandas as pd
    from reports.report_builder import build_mean_reversion_event_preview_report

    summary = {"total_event_count": 5}
    tail_df = pd.DataFrame({"event_zscore_20_low_extreme": [1, 1]})
    rep = build_mean_reversion_event_preview_report("GC=F", "1d", summary, tail_df)
    assert "MEAN REVERSION EVENT PREVIEW" in rep
    assert "event_zscore_20_low_extreme" in rep


def test_build_mean_reversion_batch_report():
    from reports.report_builder import build_mean_reversion_batch_report

    summary = {"total_attempts": 10, "success_count": 10}
    rep = build_mean_reversion_batch_report(summary)
    assert "MEAN REVERSION BATCH BUILD SUMMARY" in rep


def test_build_mean_reversion_status_report():
    import pandas as pd
    from reports.report_builder import build_mean_reversion_status_report

    summary = {"total_symbols": 5}
    df = pd.DataFrame()
    rep = build_mean_reversion_status_report(df, summary)
    assert "MEAN REVERSION STATUS REPORT" in rep
