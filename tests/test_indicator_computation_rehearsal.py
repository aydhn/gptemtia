from advanced_technical_indicators.indicator_computation_rehearsal import (
    build_synthetic_ohlcv_fixture,
    build_synthetic_quote_fixture,
    run_indicator_rehearsal_suite,
    build_indicator_computation_rehearsal_report,
)
from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile


def test_indicator_computation_rehearsal():
    ohlcv = build_synthetic_ohlcv_fixture(40)
    assert len(ohlcv) == 40
    assert "close" in ohlcv.columns

    quotes = build_synthetic_quote_fixture(30)
    assert len(quotes) == 30
    assert "bid" in quotes.columns

    prof = get_default_technical_indicator_profile()
    df, summary = run_indicator_rehearsal_suite(prof)
    assert not df.empty
    assert summary["all_passed"] is True
    assert summary["no_mutation_guaranteed"] is True
    assert summary["non_signal"] is True
