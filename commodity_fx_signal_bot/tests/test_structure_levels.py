import pytest
import pandas as pd
from levels.structure_levels import (
    calculate_recent_swing_high,
    calculate_recent_swing_low,
    build_structure_level_frame,
)


def test_recent_swings():
    df = pd.DataFrame({"high": [10.0, 12.0, 11.0], "low": [9.0, 8.0, 9.5]})

    highs = calculate_recent_swing_high(df, window=2)
    assert highs.iloc[1] == 12.0

    lows = calculate_recent_swing_low(df, window=2)
    assert lows.iloc[1] == 8.0


def test_build_structure_level_frame():
    df = pd.DataFrame(
        {
            "high": [10.0, 12.0],
            "low": [9.0, 8.0],
            "directional_bias": ["long_bias_candidate", "short_bias_candidate"],
        }
    )

    out_df, info = build_structure_level_frame(df)
    assert "structure_stop_20_candidate" in out_df.columns
    # Long stop -> recent low
    assert out_df["structure_stop_20_candidate"].iloc[0] == 9.0
    # Short target -> recent low
    assert out_df["structure_target_20_candidate"].iloc[1] == 8.0
