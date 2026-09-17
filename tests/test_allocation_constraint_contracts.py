# -*- coding: utf-8 -*-
"""Unit tests for Phase 154 Allocation Constraint Contracts and Placeholders."""

from advanced_portfolio_optimization.portfolio_optimization_config import (
    get_default_portfolio_optimization_profile,
)
from advanced_portfolio_optimization.allocation_constraint_contracts import (
    build_allocation_constraint_contract_registry,
    summarize_allocation_constraint_contracts,
)
from advanced_portfolio_optimization.long_only_constraint_placeholders import (
    build_long_only_constraint_placeholder_registry,
)
from advanced_portfolio_optimization.max_weight_constraint_placeholders import (
    build_max_weight_constraint_placeholder_registry,
)
from advanced_portfolio_optimization.turnover_constraint_placeholders import (
    build_turnover_constraint_placeholder_registry,
)
from advanced_portfolio_optimization.risk_budget_constraint_placeholders import (
    build_risk_budget_constraint_placeholder_registry,
)


def test_allocation_constraint_registry():
    profile = get_default_portfolio_optimization_profile()
    df, summary = build_allocation_constraint_contract_registry(profile)
    assert not df.empty
    assert len(df) == 22
    assert summary["constraint_count"] == 22
    assert summary["all_constraints_placeholders"] is True
    assert (df["is_placeholder"] == True).all()
    assert (df["is_enforced_live"] == False).all()


def test_individual_constraint_placeholders():
    profile = get_default_portfolio_optimization_profile()
    df_lo, s_lo = build_long_only_constraint_placeholder_registry(profile)
    assert not df_lo.empty
    assert (df_lo["is_enforced_live"] == False).all()

    df_maxw, s_maxw = build_max_weight_constraint_placeholder_registry(profile)
    assert not df_maxw.empty

    df_to, s_to = build_turnover_constraint_placeholder_registry(profile)
    assert not df_to.empty

    df_rb, s_rb = build_risk_budget_constraint_placeholder_registry(profile)
    assert not df_rb.empty
