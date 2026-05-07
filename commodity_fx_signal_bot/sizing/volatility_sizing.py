import math
from typing import Optional, Dict, Any
from sizing.sizing_models import safe_positive_float


def calculate_volatility_adjustment_factor(
    atr_pct: Optional[float], volatility_percentile: Optional[float]
) -> float:
    """Calculates an adjustment factor to scale sizing based on volatility."""
    atr_pct_safe = safe_positive_float(atr_pct)
    vol_pct_safe = safe_positive_float(volatility_percentile)

    factor = 1.0

    if vol_pct_safe is not None:
        if vol_pct_safe > 0.90:
            factor *= 0.5
        elif vol_pct_safe > 0.80:
            factor *= 0.75
        elif vol_pct_safe < 0.20:
            factor *= 1.25  # Slightly increased sizing for low volatility

    if atr_pct_safe is not None:
        # Penalize extremely high ATR percentage moves
        if atr_pct_safe > 0.05:  # >5% ATR is quite high for many pairs
            factor *= 0.6
        elif atr_pct_safe > 0.03:
            factor *= 0.8

    return max(0.1, min(1.5, factor))


def calculate_risk_readiness_adjustment(risk_readiness_score: Optional[float]) -> float:
    """Calculates an adjustment factor based on the overall risk readiness score."""
    readiness_safe = safe_positive_float(risk_readiness_score)
    if readiness_safe is None:
        return 0.5

    if readiness_safe < 0.50:
        return 0.25
    elif readiness_safe < 0.65:
        return 0.75
    elif readiness_safe > 0.85:
        return 1.10

    return 1.0


def calculate_pretrade_risk_adjustment(
    total_pretrade_risk_score: Optional[float],
) -> float:
    """Calculates an adjustment factor based on total pretrade risk."""
    risk_safe = safe_positive_float(total_pretrade_risk_score)
    if risk_safe is None:
        return 0.5

    if risk_safe > 0.80:
        return 0.25
    elif risk_safe > 0.60:
        return 0.60
    elif risk_safe < 0.30:
        return 1.20

    return 1.0


def calculate_combined_sizing_adjustment(context: Dict[str, Any]) -> float:
    """Calculates the final combined sizing adjustment factor."""
    vol_factor = calculate_volatility_adjustment_factor(
        context.get("atr_pct"), context.get("volatility_percentile")
    )
    readiness_factor = calculate_risk_readiness_adjustment(
        context.get("risk_readiness_score")
    )
    risk_factor = calculate_pretrade_risk_adjustment(
        context.get("total_pretrade_risk_score")
    )

    combined = vol_factor * readiness_factor * risk_factor
    return max(0.0, min(1.0, combined))


def apply_sizing_adjustment(base_units: float, adjustment_factor: float) -> float:
    """Applies the adjustment factor to the base units."""
    if math.isnan(base_units) or base_units <= 0:
        return 0.0

    if math.isnan(adjustment_factor) or adjustment_factor <= 0:
        return 0.0

    return base_units * adjustment_factor
