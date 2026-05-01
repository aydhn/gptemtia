import pytest
import pandas as pd
import numpy as np

from regimes.volatility_regime import detect_volatility_regime

@pytest.fixture
def vol_df():
    # Expanding high volatility setup
    return pd.DataFrame({
        "percentile_atr_pct_14_120": [0.5, 0.6, 0.7, 0.8, 0.9],
        "event_volatility_squeeze_bb20": [0, 0, 0, 0, 0],
        "event_volatility_expansion_bb20": [0, 0, 1, 1, 1],
    })

def test_detect_volatility_regime(vol_df):
    out, sum_dict = detect_volatility_regime(vol_df)

    assert "regime_volatility_level" in out.columns
    assert "regime_is_high_volatility" in out.columns
    assert "regime_volatility_label" in out.columns

    # Check that the last row picks up high volatility or expansion
    # Depending on label hierarchy, one of these will be true
    assert out["regime_volatility_label"].iloc[-1] in ["high_volatility", "volatility_expansion"]

def test_detect_volatility_regime_missing_cols():
    empty_df = pd.DataFrame({"col1": [1,2,3]})
    out, sum_dict = detect_volatility_regime(empty_df)

    assert len(sum_dict["warnings"]) > 0
    assert out["regime_volatility_label"].iloc[-1] == "unknown"
