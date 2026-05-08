import pytest
from unittest.mock import MagicMock
from config.settings import settings
from config.symbols import get_symbol_spec
from decisions.decision_pipeline import DecisionPipeline


def test_pipeline_build_for_symbol():
    dl_mock = MagicMock()
    # Ensure signal candidates are loaded
    import pandas as pd

    dl_mock.has_features.return_value = True
    dl_mock.load_features.return_value = pd.DataFrame(
        {"signal_direction": ["bullish"], "signal_score": [0.8]},
        index=[pd.Timestamp("2023-01-01")],
    )

    pipeline = DecisionPipeline(dl_mock, settings)

    # Normal symbol
    spec = get_symbol_spec("GC=F")
    df, summary = pipeline.build_for_symbol_timeframe(spec, "1d", save=False)

    assert not df.empty
    assert summary["report_builder = ReportBuilder()ed_decision_count"] >= 0


def test_pipeline_skip_macro():
    dl_mock = MagicMock()
    pipeline = DecisionPipeline(dl_mock, settings)

    # Synthetic symbol
    spec = get_symbol_spec("DX-Y.NYB")
    if spec is None:
        # Skip test if macro symbol not available
        return
    df, summary = pipeline.build_for_symbol_timeframe(spec, "1d", save=False)

    assert df.empty
    assert summary["skipped"] is True
