from typing import Optional, Tuple, Dict, Any
import math
from sizing.risk_unit import (
    calculate_risk_per_unit_from_atr,
    calculate_theoretical_unit_count,
    calculate_theoretical_notional,
)
from sizing.sizing_models import safe_positive_float


def build_atr_sizing_candidate(
    risk_amount: float,
    price: Optional[float],
    atr_value: Optional[float],
    atr_multiplier: float = 1.0,
) -> Dict[str, Any]:
    """Builds a single ATR-based sizing candidate."""
    warnings = []

    price_safe = safe_positive_float(price)
    atr_safe = safe_positive_float(atr_value)

    if price_safe is None:
        warnings.append("Price is missing or invalid.")
        return {
            "atr_multiplier": atr_multiplier,
            "risk_per_unit": None,
            "theoretical_units": 0.0,
            "theoretical_notional": None,
            "valid": False,
            "warnings": warnings,
        }

    if atr_safe is None:
        warnings.append("ATR is missing or invalid.")
        return {
            "atr_multiplier": atr_multiplier,
            "risk_per_unit": None,
            "theoretical_units": 0.0,
            "theoretical_notional": None,
            "valid": False,
            "warnings": warnings,
        }

    risk_per_unit = calculate_risk_per_unit_from_atr(atr_safe, atr_multiplier)
    theoretical_units = calculate_theoretical_unit_count(risk_amount, risk_per_unit)
    theoretical_notional = calculate_theoretical_notional(theoretical_units, price_safe)

    return {
        "atr_multiplier": atr_multiplier,
        "risk_per_unit": risk_per_unit,
        "theoretical_units": theoretical_units,
        "theoretical_notional": theoretical_notional,
        "valid": True,
        "warnings": warnings,
    }


def build_multi_atr_sizing_candidates(
    risk_amount: float,
    price: Optional[float],
    atr_value: Optional[float],
    multipliers: Tuple[float, ...] = (1.0, 1.5, 2.0, 3.0),
) -> Dict[str, Dict[str, Any]]:
    """Builds multiple ATR-based sizing candidates for different multipliers."""
    results = {}
    for mult in multipliers:
        results[f"atr_{mult}x"] = build_atr_sizing_candidate(
            risk_amount=risk_amount,
            price=price,
            atr_value=atr_value,
            atr_multiplier=mult,
        )
    return results
