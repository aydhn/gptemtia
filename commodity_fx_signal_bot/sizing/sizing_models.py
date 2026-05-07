from dataclasses import dataclass, asdict
from typing import Optional, List, Dict, Any
import math

@dataclass
class SizingInputSnapshot:
    symbol: str
    timeframe: str
    timestamp: str
    asset_class: str
    strategy_family: str
    condition_label: str
    directional_bias: str
    risk_label: str
    risk_severity: str
    total_pretrade_risk_score: float
    risk_readiness_score: float
    latest_close: Optional[float]
    atr_value: Optional[float]
    atr_pct: Optional[float]
    volatility_percentile: Optional[float]
    context_available: bool
    warnings: List[str]

@dataclass
class RiskBudgetAllocation:
    theoretical_account_equity: float
    risk_per_candidate_amount: float
    max_symbol_risk_amount: float
    max_asset_class_risk_amount: float
    max_total_portfolio_risk_amount: float
    base_currency: str

def clamp_sizing_score(score: float) -> float:
    """Clamps a score between 0.0 and 1.0."""
    if math.isnan(score):
        return 0.0
    return max(0.0, min(1.0, score))

def safe_positive_float(value: Any, default: Optional[float] = None) -> Optional[float]:
    """Safely converts a value to a positive float, handling NaNs and infinites."""
    try:
        f_val = float(value)
        if math.isnan(f_val) or math.isinf(f_val):
            return default
        if f_val < 0:
            return default
        return f_val
    except (TypeError, ValueError):
        return default

def calculate_notional_from_risk_unit(risk_amount: float, risk_per_unit: float) -> float:
    """
    Calculates the total theoretical notional value from a target risk amount and risk per unit.
    This is entirely theoretical and not a real position size.
    """
    if not risk_per_unit or math.isnan(risk_per_unit) or risk_per_unit <= 0:
        return 0.0

    if not risk_amount or math.isnan(risk_amount) or risk_amount <= 0:
        return 0.0

    return risk_amount / risk_per_unit

def sizing_input_snapshot_to_dict(snapshot: SizingInputSnapshot) -> Dict[str, Any]:
    return asdict(snapshot)

def risk_budget_allocation_to_dict(allocation: RiskBudgetAllocation) -> Dict[str, Any]:
    return asdict(allocation)
