import math
import numpy as np


def calculate_target_from_stop_distance(
    price: float | None,
    stop_distance: float | None,
    directional_bias: str,
    rr_multiplier: float,
) -> float | None:
    if (
        price is None
        or stop_distance is None
        or math.isnan(price)
        or math.isnan(stop_distance)
        or stop_distance <= 0
    ):
        return None

    if directional_bias in ["long_bias_candidate", "bullish"]:
        return price + (stop_distance * rr_multiplier)
    elif directional_bias in ["short_bias_candidate", "bearish"]:
        return price - (stop_distance * rr_multiplier)
    return None


def build_target_ladder(
    price: float | None,
    stop_level: float | None,
    directional_bias: str,
    rr_multipliers: tuple[float, ...],
) -> list[float]:
    if (
        price is None
        or stop_level is None
        or math.isnan(price)
        or math.isnan(stop_level)
    ):
        return []

    stop_distance = abs(price - stop_level)
    if stop_distance <= 0:
        return []

    targets = []
    for m in rr_multipliers:
        t = calculate_target_from_stop_distance(
            price, stop_distance, directional_bias, m
        )
        if t is not None:
            targets.append(t)

    return targets


def build_strategy_family_target_context(
    price: float | None,
    stop_level: float | None,
    directional_bias: str,
    strategy_family: str,
    rr_multipliers: tuple[float, ...],
) -> dict:

    # Example logic mapping family to a specific profile of target ladders
    # For trend_following we might include up to the max multiplier
    # For mean_reversion we might just take the first two

    all_targets = build_target_ladder(
        price, stop_level, directional_bias, rr_multipliers
    )
    if not all_targets:
        return {"target_ladder_candidate": [], "primary_target_candidate": None}

    if strategy_family == "mean_reversion":
        targets = all_targets[:2]
    elif strategy_family == "breakout":
        targets = all_targets
    else:
        targets = all_targets

    return {
        "target_ladder_candidate": targets,
        "primary_target_candidate": targets[0] if targets else None,
    }
