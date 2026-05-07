from sizing.budget_model import (
    build_risk_budget_allocation,
    calculate_symbol_budget_remaining,
    cap_risk_amount_by_budgets,
)
from sizing.sizing_config import get_default_sizing_profile


def test_build_risk_budget_allocation():
    profile = get_default_sizing_profile()
    alloc = build_risk_budget_allocation(profile)
    assert alloc.theoretical_account_equity > 0
    assert alloc.max_symbol_risk_amount > 0


def test_calculate_symbol_budget_remaining():
    assert calculate_symbol_budget_remaining(500.0, 1000.0) == 500.0
    assert calculate_symbol_budget_remaining(1500.0, 1000.0) == 0.0


def test_cap_risk_amount_by_budgets():
    # Uncapped
    capped, details = cap_risk_amount_by_budgets(100.0, 1000.0, 5000.0, 15000.0)
    assert capped == 100.0
    assert not details["was_capped"]

    # Capped
    capped, details = cap_risk_amount_by_budgets(2000.0, 1000.0, 5000.0, 15000.0)
    assert capped == 1000.0
    assert details["was_capped"]
