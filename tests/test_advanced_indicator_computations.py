import pytest
import pandas as pd
from advanced_technical_indicators.advanced_indicator_computations import (
    compute_indicator_by_name,
    list_supported_indicator_computations,
    build_advanced_indicator_computation_module_report,
)
from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile
from advanced_technical_indicators.indicator_computation_rehearsal import build_synthetic_ohlcv_fixture


def test_advanced_indicator_computations():
    supported = list_supported_indicator_computations()
    assert len(supported) >= 32

    df = build_synthetic_ohlcv_fixture(30)
    out_sma = compute_indicator_by_name(df, "sma", {"window": 5})
    assert "sma_5" in out_sma.columns

    out_rsi = compute_indicator_by_name(df, "rsi", {"window": 14})
    assert "rsi_14" in out_rsi.columns

    prof = get_default_technical_indicator_profile()
    rep_df, rep_sum = build_advanced_indicator_computation_module_report(prof)
    assert not rep_df.empty
    assert rep_sum["pure_python_numpy"] is True
    assert rep_sum["ta_lib_required"] is False


def test_unknown_computation_error():
    df = build_synthetic_ohlcv_fixture(10)
    with pytest.raises(ValueError):
        compute_indicator_by_name(df, "unknown_indicator_xyz")
