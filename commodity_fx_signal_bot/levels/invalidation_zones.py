import math
from levels.level_config import LevelProfile


def calculate_atr_invalidation_zone(
    price: float | None,
    atr_value: float | None,
    directional_bias: str,
    multiplier: float = 1.5,
) -> dict:
    if (
        price is None
        or atr_value is None
        or math.isnan(price)
        or math.isnan(atr_value)
        or atr_value <= 0
    ):
        return {
            "invalidation_level_candidate": None,
            "warnings": ["Missing price or ATR"],
        }

    distance = atr_value * multiplier
    if directional_bias in ["long_bias_candidate", "bullish"]:
        inv_level = price - distance
        return {
            "invalidation_level_candidate": inv_level,
            "invalidation_zone_high_candidate": inv_level,
            "invalidation_zone_low_candidate": inv_level - (atr_value * 0.5),
            "warnings": [],
        }
    elif directional_bias in ["short_bias_candidate", "bearish"]:
        inv_level = price + distance
        return {
            "invalidation_level_candidate": inv_level,
            "invalidation_zone_low_candidate": inv_level,
            "invalidation_zone_high_candidate": inv_level + (atr_value * 0.5),
            "warnings": [],
        }
    return {
        "invalidation_level_candidate": None,
        "warnings": ["Neutral or unknown bias"],
    }


def calculate_structure_invalidation_zone(
    structure_stop_level: float | None, atr_value: float | None, directional_bias: str
) -> dict:
    if structure_stop_level is None or math.isnan(structure_stop_level):
        return {
            "invalidation_level_candidate": None,
            "warnings": ["Missing structure stop"],
        }

    if atr_value is None or math.isnan(atr_value) or atr_value <= 0:
        atr_value = structure_stop_level * 0.01

    if directional_bias in ["long_bias_candidate", "bullish"]:
        return {
            "invalidation_level_candidate": structure_stop_level,
            "invalidation_zone_high_candidate": structure_stop_level,
            "invalidation_zone_low_candidate": structure_stop_level - atr_value,
            "warnings": [],
        }
    elif directional_bias in ["short_bias_candidate", "bearish"]:
        return {
            "invalidation_level_candidate": structure_stop_level,
            "invalidation_zone_low_candidate": structure_stop_level,
            "invalidation_zone_high_candidate": structure_stop_level + atr_value,
            "warnings": [],
        }
    return {"invalidation_level_candidate": None, "warnings": ["Neutral bias"]}


def calculate_regime_invalidation_context(context_snapshot: dict) -> dict:
    # Example logic: if MTF is opposite, confidence in invalidation is higher
    return {"invalidation_reason": "regime_conflict", "invalidation_confidence": 0.5}


def build_invalidation_zone_candidate(
    context_snapshot: dict, profile: LevelProfile
) -> dict:
    # Uses combinations of ATR and structure
    price = context_snapshot.get("latest_close")
    atr = context_snapshot.get("atr_value")
    bias = context_snapshot.get("directional_bias", "neutral")

    res = calculate_atr_invalidation_zone(price, atr, bias)
    res["invalidation_reason"] = "atr_invalidation"
    res["invalidation_confidence"] = 0.8
    return res
