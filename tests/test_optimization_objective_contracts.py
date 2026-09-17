# -*- coding: utf-8 -*-
"""Unit tests for Phase 154 Optimization Objective Contracts and Placeholders."""

from advanced_portfolio_optimization.portfolio_optimization_config import (
    get_default_portfolio_optimization_profile,
)
from advanced_portfolio_optimization.optimization_objective_contracts import (
    build_optimization_objective_contract_registry,
    summarize_optimization_objective_contracts,
)
from advanced_portfolio_optimization.mean_variance_objective_placeholders import (
    build_mean_variance_objective_placeholder_registry,
)
from advanced_portfolio_optimization.minimum_variance_objective_placeholders import (
    build_minimum_variance_objective_placeholder_registry,
)
from advanced_portfolio_optimization.maximum_sharpe_objective_placeholders import (
    build_maximum_sharpe_objective_placeholder_registry,
)
from advanced_portfolio_optimization.risk_parity_objective_placeholders import (
    build_risk_parity_objective_placeholder_registry,
)
from advanced_portfolio_optimization.cvar_objective_placeholders import (
    build_cvar_objective_placeholder_registry,
)


def test_optimization_objective_registry():
    profile = get_default_portfolio_optimization_profile()
    df, summary = build_optimization_objective_contract_registry(profile)
    assert not df.empty
    assert len(df) == 11
    assert summary["objective_count"] == 11
    assert summary["all_objectives_placeholders"] is True
    assert (df["is_placeholder"] == True).all()
    assert (df["is_calculated"] == False).all()


def test_individual_objective_placeholders():
    profile = get_default_portfolio_optimization_profile()
    df_mv, s_mv = build_mean_variance_objective_placeholder_registry(profile)
    assert not df_mv.empty
    assert (df_mv["is_calculated"] == False).all()

    df_minv, s_minv = build_minimum_variance_objective_placeholder_registry(profile)
    assert not df_minv.empty

    df_ms, s_ms = build_maximum_sharpe_objective_placeholder_registry(profile)
    assert not df_ms.empty

    df_rp, s_rp = build_risk_parity_objective_placeholder_registry(profile)
    assert not df_rp.empty

    df_cvar, s_cvar = build_cvar_objective_placeholder_registry(profile)
    assert not df_cvar.empty
