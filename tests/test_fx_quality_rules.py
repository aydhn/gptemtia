import pytest
import pandas as pd
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.fx_quality_rules import (
    build_fx_quality_rule_set,
    check_fx_quote_quality,
    check_fx_ohlcv_quality,
)


def test_fx_quality_rules():
    profile = get_default_data_quality_profile()
    df_rules, _ = build_fx_quality_rule_set(profile)
    assert len(df_rules) >= 2

    # Inverted quote: bid > ask
    inverted_quote = pd.DataFrame([
        {"pair": "USD/TRY", "timestamp": "2026-09-01", "bid": 34.50, "ask": 34.20}
    ])
    findings = check_fx_quote_quality(inverted_quote, "fx_test_prov")
    assert any(f.finding_type == "finding_quote_inconsistency" for f in findings)

    # Bad OHLCV: high < low
    bad_ohlcv = pd.DataFrame([
        {"pair": "USD/TRY", "timestamp": "2026-09-01", "open": 34.0, "high": 33.0, "low": 35.0, "close": 34.2}
    ])
    f_ohlc = check_fx_ohlcv_quality(bad_ohlcv, "fx_test_prov")
    assert any(f.finding_type == "finding_ohlc_inconsistency" for f in f_ohlc)
