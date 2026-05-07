from typing import Tuple, Dict, Any
from sizing.sizing_config import SizingProfile
from sizing.sizing_models import RiskBudgetAllocation


def build_risk_budget_allocation(profile: SizingProfile) -> RiskBudgetAllocation:
    """Builds a risk budget allocation from a profile."""
    equity = profile.theoretical_account_equity
    return RiskBudgetAllocation(
        theoretical_account_equity=equity,
        risk_per_candidate_amount=equity * profile.risk_per_candidate,
        max_symbol_risk_amount=equity * profile.max_risk_per_symbol,
        max_asset_class_risk_amount=equity * profile.max_risk_per_asset_class,
        max_total_portfolio_risk_amount=equity * profile.max_total_portfolio_risk,
        base_currency=profile.base_currency,
    )


def calculate_symbol_budget_remaining(
    existing_symbol_risk: float, max_symbol_risk_amount: float
) -> float:
    """Calculates remaining budget for a symbol."""
    remaining = max_symbol_risk_amount - existing_symbol_risk
    return max(0.0, remaining)


def calculate_asset_class_budget_remaining(
    existing_asset_class_risk: float, max_asset_class_risk_amount: float
) -> float:
    """Calculates remaining budget for an asset class."""
    remaining = max_asset_class_risk_amount - existing_asset_class_risk
    return max(0.0, remaining)


def calculate_total_budget_remaining(
    existing_total_risk: float, max_total_risk_amount: float
) -> float:
    """Calculates remaining total portfolio budget."""
    remaining = max_total_risk_amount - existing_total_risk
    return max(0.0, remaining)


def cap_risk_amount_by_budgets(
    requested_risk_amount: float,
    symbol_budget_remaining: float,
    asset_class_budget_remaining: float,
    total_budget_remaining: float,
) -> Tuple[float, Dict[str, Any]]:
    """Caps the requested risk amount by the remaining budgets."""

    cap_reasons = []
    capped_amount = requested_risk_amount

    if capped_amount > symbol_budget_remaining:
        capped_amount = symbol_budget_remaining
        cap_reasons.append("Capped by symbol budget limit.")

    if capped_amount > asset_class_budget_remaining:
        capped_amount = asset_class_budget_remaining
        cap_reasons.append("Capped by asset class budget limit.")

    if capped_amount > total_budget_remaining:
        capped_amount = total_budget_remaining
        cap_reasons.append("Capped by total portfolio budget limit.")

    return capped_amount, {
        "requested_risk_amount": requested_risk_amount,
        "capped_amount": capped_amount,
        "cap_reasons": cap_reasons,
        "was_capped": len(cap_reasons) > 0,
    }
