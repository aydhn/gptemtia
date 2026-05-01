import pytest
import pandas as pd
import numpy as np

from regimes.range_regime import detect_range_regime

@pytest.fixture
def range_df():
    # Strong compressed range setup
    return pd.DataFrame({
        "adx_14": [25, 20, 15, 10, 5],
        "plus_di_14": [20, 20, 20, 20, 20],
        "minus_di_14": [20, 20, 20, 20, 20],
        "percentile_bb_width_20_2_120": [0.5, 0.4, 0.3, 0.2, 0.1],
        "range_compression_20": [0, 0.5, 0.8, 0.9, 1.0],
        "percentile_atr_pct_14_120": [0.5, 0.4, 0.3, 0.2, 0.1] # low vol
    })

def test_detect_range_regime(range_df):
    out, sum_dict = detect_range_regime(range_df)

    assert "regime_range_score" in out.columns
    assert "regime_range_label" in out.columns

    # Last row should be compressed range
    assert out["regime_range_label"].iloc[-1] == "compressed_range"

def test_detect_range_regime_missing_cols():
    empty_df = pd.DataFrame({"col1": [1,2,3]})
    out, sum_dict = detect_range_regime(empty_df)

    assert len(sum_dict["warnings"]) > 0
    assert out["regime_range_label"].iloc[-1] == "unknown"
