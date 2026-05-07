import math
import numpy as np


def calculate_volatility_level_adjustment(
    atr_pct: float | None, volatility_percentile: float | None
) -> float:
    if (
        atr_pct is None
        or volatility_percentile is None
        or math.isnan(atr_pct)
        or math.isnan(volatility_percentile)
    ):
        return 1.0

    # Example logic: increase distance if volatility is high
    if volatility_percentile > 80:
        return 1.5
    elif volatility_percentile > 60:
        return 1.2
    elif volatility_percentile < 20:
        return 0.8
    return 1.0


def adjust_stop_distance_by_volatility(
    base_distance: float | None, adjustment_factor: float
) -> float | None:
    if base_distance is None or math.isnan(base_distance):
        return None
    return base_distance * adjustment_factor


def adjust_target_distance_by_volatility(
    base_distance: float | None, adjustment_factor: float
) -> float | None:
    if base_distance is None or math.isnan(base_distance):
        return None
    return base_distance * adjustment_factor


def build_volatility_adjusted_levels(
    price: float | None,
    stop_distance: float | None,
    target_distance: float | None,
    directional_bias: str,
    adjustment_factor: float,
) -> dict:

    adj_stop_dist = adjust_stop_distance_by_volatility(stop_distance, adjustment_factor)
    adj_target_dist = adjust_target_distance_by_volatility(
        target_distance, adjustment_factor
    )

    stop_level = None
    target_level = None

    if price is not None and adj_stop_dist is not None:
        if directional_bias in ["long_bias_candidate", "bullish"]:
            stop_level = price - adj_stop_dist
        elif directional_bias in ["short_bias_candidate", "bearish"]:
            stop_level = price + adj_stop_dist

    if price is not None and adj_target_dist is not None:
        if directional_bias in ["long_bias_candidate", "bullish"]:
            target_level = price + adj_target_dist
        elif directional_bias in ["short_bias_candidate", "bearish"]:
            target_level = price - adj_target_dist

    return {
        "volatility_adjusted_stop_candidate": stop_level,
        "volatility_adjusted_target_candidate": target_level,
        "adjustment_factor": adjustment_factor,
    }
