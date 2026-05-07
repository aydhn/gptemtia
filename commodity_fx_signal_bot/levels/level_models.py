from dataclasses import dataclass
import math
import numpy as np


@dataclass
class LevelInputSnapshot:
    symbol: str
    timeframe: str
    timestamp: str
    asset_class: str
    strategy_family: str
    condition_label: str
    directional_bias: str
    sizing_label: str
    risk_label: str
    latest_close: float | None
    atr_value: float | None
    atr_pct: float | None
    volatility_percentile: float | None
    sizing_readiness_score: float
    total_pretrade_risk_score: float
    theoretical_units: float
    adjusted_theoretical_units: float
    context_available: bool
    warnings: list[str]


@dataclass
class LevelCandidateSet:
    stop_levels: list[float]
    target_levels: list[float]
    invalidation_levels: list[float]
    reward_risk_values: list[float]
    method: str
    warnings: list[str]


def clamp_level_score(score: float) -> float:
    if score is None or math.isnan(score):
        return 0.0
    return max(0.0, min(1.0, float(score)))


def safe_price(value, default: float | None = None) -> float | None:
    if value is None or math.isnan(value) or math.isinf(value) or value <= 0:
        return default
    return float(value)


def calculate_distance_pct(price: float | None, level: float | None) -> float | None:
    price = safe_price(price)
    level = safe_price(level)
    if price is None or level is None:
        return None
    return abs(price - level) / price


def is_valid_level_for_direction(
    price: float | None, level: float | None, directional_bias: str, level_type: str
) -> bool:
    price = safe_price(price)
    level = safe_price(level)
    if price is None or level is None:
        return False

    if directional_bias in ["long_bias_candidate", "bullish"]:
        if level_type == "stop":
            return level < price
        elif level_type == "target":
            return level > price
    elif directional_bias in ["short_bias_candidate", "bearish"]:
        if level_type == "stop":
            return level > price
        elif level_type == "target":
            return level < price

    return False


def level_input_snapshot_to_dict(snapshot: LevelInputSnapshot) -> dict:
    return {
        "symbol": snapshot.symbol,
        "timeframe": snapshot.timeframe,
        "timestamp": snapshot.timestamp,
        "asset_class": snapshot.asset_class,
        "strategy_family": snapshot.strategy_family,
        "condition_label": snapshot.condition_label,
        "directional_bias": snapshot.directional_bias,
        "sizing_label": snapshot.sizing_label,
        "risk_label": snapshot.risk_label,
        "latest_close": snapshot.latest_close,
        "atr_value": snapshot.atr_value,
        "atr_pct": snapshot.atr_pct,
        "volatility_percentile": snapshot.volatility_percentile,
        "sizing_readiness_score": snapshot.sizing_readiness_score,
        "total_pretrade_risk_score": snapshot.total_pretrade_risk_score,
        "theoretical_units": snapshot.theoretical_units,
        "adjusted_theoretical_units": snapshot.adjusted_theoretical_units,
        "context_available": snapshot.context_available,
        "warnings": snapshot.warnings.copy(),
    }


def level_candidate_set_to_dict(candidate_set: LevelCandidateSet) -> dict:
    return {
        "stop_levels": candidate_set.stop_levels.copy(),
        "target_levels": candidate_set.target_levels.copy(),
        "invalidation_levels": candidate_set.invalidation_levels.copy(),
        "reward_risk_values": candidate_set.reward_risk_values.copy(),
        "method": candidate_set.method,
        "warnings": candidate_set.warnings.copy(),
    }
