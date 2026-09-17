# -*- coding: utf-8 -*-
"""Unit tests for Phase 154 Optimization Guards and Policies."""

from advanced_portfolio_optimization.portfolio_optimization_config import (
    get_default_portfolio_optimization_profile,
)
from advanced_portfolio_optimization.optimization_no_lookahead_guards import (
    build_optimization_no_lookahead_guard_registry,
)
from advanced_portfolio_optimization.optimization_allocation_claim_guards import (
    build_optimization_allocation_claim_guard_registry,
)
from advanced_portfolio_optimization.optimization_weight_generation_claim_guards import (
    build_optimization_weight_generation_claim_guard_registry,
)
from advanced_portfolio_optimization.optimization_rebalance_claim_guards import (
    build_optimization_rebalance_claim_guard_registry,
)
from advanced_portfolio_optimization.optimization_investment_advice_guards import (
    build_optimization_investment_advice_guard_registry,
)
from advanced_portfolio_optimization.optimization_forbidden_column_policies import (
    build_optimization_forbidden_column_policy_registry,
    is_forbidden_optimization_column,
    FORBIDDEN_OPTIMIZATION_COLUMNS,
)


def test_guards_active():
    profile = get_default_portfolio_optimization_profile()
    df_nl, s_nl = build_optimization_no_lookahead_guard_registry(profile)
    assert s_nl["is_active"] is True

    df_alloc, s_alloc = build_optimization_allocation_claim_guard_registry(profile)
    assert s_alloc["is_active"] is True

    df_wt, s_wt = build_optimization_weight_generation_claim_guard_registry(profile)
    assert s_wt["is_active"] is True

    df_reb, s_reb = build_optimization_rebalance_claim_guard_registry(profile)
    assert s_reb["is_active"] is True

    df_adv, s_adv = build_optimization_investment_advice_guard_registry(profile)
    assert s_adv["is_active"] is True


def test_forbidden_column_policy():
    profile = get_default_portfolio_optimization_profile()
    df_forb, s_forb = build_optimization_forbidden_column_policy_registry(profile)
    assert not df_forb.empty
    assert len(df_forb) == 52
    assert s_forb["forbidden_column_count"] == 52

    # Specific tests for quarantined columns
    assert is_forbidden_optimization_column("optimal_weight") is True
    assert is_forbidden_optimization_column("optimized_weight") is True
    assert is_forbidden_optimization_column("solver_result") is True
    assert is_forbidden_optimization_column("rebalance_order") is True
    assert is_forbidden_optimization_column("safe_unrelated_column") is False
