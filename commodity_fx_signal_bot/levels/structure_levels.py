import pandas as pd
import numpy as np


def calculate_recent_swing_low(df: pd.DataFrame, window: int = 20) -> pd.Series:
    if "low" not in df.columns:
        return pd.Series(np.nan, index=df.index)
    return df["low"].rolling(window=window, min_periods=1).min()


def calculate_recent_swing_high(df: pd.DataFrame, window: int = 20) -> pd.Series:
    if "high" not in df.columns:
        return pd.Series(np.nan, index=df.index)
    return df["high"].rolling(window=window, min_periods=1).max()


def calculate_structure_stop_level(
    df: pd.DataFrame, directional_bias: str, window: int = 20
) -> pd.Series:
    # A simplified structure stop: for long, use recent low. for short, use recent high.
    # Note: df doesn't have a single directional bias typically, we might need a column.
    # We will assume df has a 'directional_bias' column or we apply it row by row.
    pass  # Wait, the signature says directional_bias: str. Let's return a series based on a fixed bias? No, let's look at the requirements.


def calculate_breakout_reference_levels(
    df: pd.DataFrame, window: int = 20
) -> pd.DataFrame:
    df_out = pd.DataFrame(index=df.index)
    df_out[f"breakout_reference_high_{window}"] = calculate_recent_swing_high(
        df, window
    )
    df_out[f"breakout_reference_low_{window}"] = calculate_recent_swing_low(df, window)
    return df_out


def build_structure_level_frame(
    df: pd.DataFrame, directional_bias_col: str = "directional_bias"
) -> tuple[pd.DataFrame, dict]:
    df_out = df.copy()
    warnings = []

    if "high" not in df.columns or "low" not in df.columns:
        warnings.append("Missing high/low columns for structure levels")
        return df_out, {"warnings": warnings}

    window = 20
    df_out[f"recent_swing_low_{window}"] = calculate_recent_swing_low(df, window)
    df_out[f"recent_swing_high_{window}"] = calculate_recent_swing_high(df, window)
    df_out[f"breakout_reference_high_{window}"] = calculate_recent_swing_high(
        df, window
    )
    df_out[f"breakout_reference_low_{window}"] = calculate_recent_swing_low(df, window)

    if directional_bias_col not in df.columns:
        df_out[directional_bias_col] = "neutral"
        warnings.append("Missing directional_bias, using neutral")

    def _get_stop(row):
        if row[directional_bias_col] in ["long_bias_candidate", "bullish"]:
            return row[f"recent_swing_low_{window}"]
        elif row[directional_bias_col] in ["short_bias_candidate", "bearish"]:
            return row[f"recent_swing_high_{window}"]
        return np.nan

    def _get_target(row):
        if row[directional_bias_col] in ["long_bias_candidate", "bullish"]:
            return row[f"recent_swing_high_{window}"]
        elif row[directional_bias_col] in ["short_bias_candidate", "bearish"]:
            return row[f"recent_swing_low_{window}"]
        return np.nan

    df_out[f"structure_stop_{window}_candidate"] = df_out.apply(_get_stop, axis=1)
    df_out[f"structure_target_{window}_candidate"] = df_out.apply(_get_target, axis=1)
    df_out[f"structure_invalidation_level_{window}_candidate"] = df_out[
        f"structure_stop_{window}_candidate"
    ]

    return df_out, {"warnings": warnings}
