import math
from typing import Optional, Tuple, Dict, Any
import pandas as pd
from sizing.sizing_models import safe_positive_float

def calculate_theoretical_risk_amount(equity: float, risk_fraction: float) -> float:
    """Calculates the theoretical risk amount in base currency based on account equity and a risk fraction."""
    if equity <= 0 or risk_fraction <= 0:
        return 0.0
    return equity * risk_fraction

def calculate_risk_per_unit_from_atr(atr_value: Optional[float], atr_multiplier: float = 1.0) -> Optional[float]:
    """Calculates risk per unit using ATR and a multiplier."""
    atr_safe = safe_positive_float(atr_value)
    if atr_safe is None or atr_safe <= 0:
        return None
    return atr_safe * atr_multiplier

def calculate_risk_per_unit_from_percent(price: Optional[float], risk_pct: float) -> Optional[float]:
    """Calculates risk per unit as a percentage of the price."""
    p_safe = safe_positive_float(price)
    if p_safe is None or p_safe <= 0 or risk_pct <= 0:
        return None
    return p_safe * risk_pct

def calculate_theoretical_unit_count(risk_amount: float, risk_per_unit: Optional[float]) -> float:
    """
    Calculates theoretical unit count (simulated sizing).
    This does NOT represent actual trading lots or contracts.
    """
    rpu_safe = safe_positive_float(risk_per_unit)
    if rpu_safe is None or rpu_safe <= 0:
        return 0.0
    if risk_amount <= 0:
        return 0.0
    return risk_amount / rpu_safe

def calculate_theoretical_notional(unit_count: float, price: Optional[float]) -> Optional[float]:
    """Calculates theoretical notional value for the simulated unit count."""
    p_safe = safe_positive_float(price)
    if p_safe is None or p_safe <= 0:
        return None
    if unit_count <= 0:
        return 0.0
    return unit_count * p_safe

def calculate_risk_unit_frame(
    df: pd.DataFrame,
    risk_amount: float,
    price_col: str = "close",
    atr_col: str = "atr_14"
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Calculates theoretical sizing candidate units for a dataframe over time."""

    out_df = pd.DataFrame(index=df.index)

    if len(df) == 0:
        return out_df, {"warnings": ["Empty dataframe provided to risk unit frame calculator"]}

    out_df["theoretical_risk_amount"] = risk_amount

    price_series = df[price_col] if price_col in df.columns else pd.Series(index=df.index, dtype=float)
    atr_series = df[atr_col] if atr_col in df.columns else pd.Series(index=df.index, dtype=float)

    # ATR 1x
    out_df["risk_per_unit_atr_1x"] = atr_series
    out_df["theoretical_unit_count_atr_1x"] = (risk_amount / out_df["risk_per_unit_atr_1x"]).replace([float('inf'), -float('inf')], float('nan'))
    out_df["theoretical_notional_atr_1x"] = out_df["theoretical_unit_count_atr_1x"] * price_series

    # ATR 2x
    out_df["risk_per_unit_atr_2x"] = atr_series * 2.0
    out_df["theoretical_unit_count_atr_2x"] = (risk_amount / out_df["risk_per_unit_atr_2x"]).replace([float('inf'), -float('inf')], float('nan'))
    out_df["theoretical_notional_atr_2x"] = out_df["theoretical_unit_count_atr_2x"] * price_series

    warnings = []
    if price_col not in df.columns:
        warnings.append(f"Price column '{price_col}' missing.")
    if atr_col not in df.columns:
        warnings.append(f"ATR column '{atr_col}' missing.")

    return out_df, {"warnings": warnings}
