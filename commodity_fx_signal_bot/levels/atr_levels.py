import pandas as pd
import numpy as np


def calculate_atr_stop_level(
    price: float | None,
    atr_value: float | None,
    directional_bias: str,
    multiplier: float,
) -> float | None:
    if (
        price is None
        or atr_value is None
        or np.isnan(price)
        or np.isnan(atr_value)
        or atr_value <= 0
    ):
        return None

    if directional_bias in ["long_bias_candidate", "bullish"]:
        return price - (atr_value * multiplier)
    elif directional_bias in ["short_bias_candidate", "bearish"]:
        return price + (atr_value * multiplier)
    return None


def calculate_atr_target_level(
    price: float | None,
    atr_value: float | None,
    directional_bias: str,
    multiplier: float,
) -> float | None:
    if (
        price is None
        or atr_value is None
        or np.isnan(price)
        or np.isnan(atr_value)
        or atr_value <= 0
    ):
        return None

    if directional_bias in ["long_bias_candidate", "bullish"]:
        return price + (atr_value * multiplier)
    elif directional_bias in ["short_bias_candidate", "bearish"]:
        return price - (atr_value * multiplier)
    return None


def build_atr_stop_levels(
    price: float | None,
    atr_value: float | None,
    directional_bias: str,
    multipliers: tuple[float, ...],
) -> list[float]:
    levels = []
    for m in multipliers:
        lvl = calculate_atr_stop_level(price, atr_value, directional_bias, m)
        if lvl is not None:
            levels.append(lvl)
    return levels


def build_atr_target_levels(
    price: float | None,
    atr_value: float | None,
    directional_bias: str,
    multipliers: tuple[float, ...],
) -> list[float]:
    levels = []
    for m in multipliers:
        lvl = calculate_atr_target_level(price, atr_value, directional_bias, m)
        if lvl is not None:
            levels.append(lvl)
    return levels


def build_atr_level_frame(
    df: pd.DataFrame, price_col: str = "close", atr_col: str = "atr_14"
) -> tuple[pd.DataFrame, dict]:
    df_out = df.copy()
    warnings = []

    if price_col not in df.columns or atr_col not in df.columns:
        warnings.append(f"Missing columns for ATR levels: {price_col} or {atr_col}")
        return df_out, {"warnings": warnings}

    if "directional_bias" not in df.columns:
        df_out["directional_bias"] = "neutral"
        warnings.append("Missing directional_bias, using neutral")

    for m, name in [(1.0, "1x"), (1.5, "1_5x"), (2.0, "2x"), (3.0, "3x")]:
        df_out[f"atr_stop_{name}_candidate"] = df_out.apply(
            lambda row: calculate_atr_stop_level(
                row[price_col], row[atr_col], row["directional_bias"], m
            ),
            axis=1,
        )
        df_out[f"atr_target_{name}_candidate"] = df_out.apply(
            lambda row: calculate_atr_target_level(
                row[price_col], row[atr_col], row["directional_bias"], m
            ),
            axis=1,
        )

    return df_out, {"warnings": warnings}
