import pytest
import pandas as pd
from levels.atr_levels import (
    calculate_atr_stop_level,
    calculate_atr_target_level,
    build_atr_level_frame,
)


def test_calculate_atr_stop():
    assert calculate_atr_stop_level(100.0, 1.0, "long_bias_candidate", 1.5) == 98.5
    assert calculate_atr_stop_level(100.0, 1.0, "short_bias_candidate", 1.5) == 101.5
    assert calculate_atr_stop_level(100.0, None, "long_bias_candidate", 1.5) is None


def test_build_atr_level_frame():
    df = pd.DataFrame(
        {
            "close": [100.0, 105.0],
            "atr_14": [1.0, 1.5],
            "directional_bias": ["long_bias_candidate", "short_bias_candidate"],
        }
    )

    out_df, info = build_atr_level_frame(df)
    assert "warnings" in info
    assert "atr_stop_1_5x_candidate" in out_df.columns
    assert out_df["atr_stop_1_5x_candidate"].iloc[0] == 98.5
    assert out_df["atr_target_2x_candidate"].iloc[1] == 102.0
