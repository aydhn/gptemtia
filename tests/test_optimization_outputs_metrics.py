# -*- coding: utf-8 -*-
"""Unit tests for Phase 154 Optimization Outputs and Metric Placeholders."""

from advanced_portfolio_optimization.portfolio_optimization_config import (
    get_default_portfolio_optimization_profile,
)
from advanced_portfolio_optimization.optimization_result_output_contracts import (
    build_optimization_result_output_contract_registry,
)
from advanced_portfolio_optimization.allocation_output_contracts import (
    build_allocation_output_contract_registry,
)
from advanced_portfolio_optimization.rebalance_output_contracts import (
    build_rebalance_output_contract_registry,
)
from advanced_portfolio_optimization.optimization_metric_placeholders import (
    build_optimization_metric_placeholder_registry,
)


def test_output_contracts():
    profile = get_default_portfolio_optimization_profile()
    df_res, s_res = build_optimization_result_output_contract_registry(profile)
    assert not df_res.empty
    assert (df_res["contains_actual_weights"] == False).all()

    df_alloc, s_alloc = build_allocation_output_contract_registry(profile)
    assert not df_alloc.empty
    assert (df_alloc["contains_capital_allocation"] == False).all()

    df_reb, s_reb = build_rebalance_output_contract_registry(profile)
    assert not df_reb.empty
    assert (df_reb["contains_rebalance_orders"] == False).all()


def test_metric_placeholders():
    profile = get_default_portfolio_optimization_profile()
    df_m, s_m = build_optimization_metric_placeholder_registry(profile)
    assert not df_m.empty
    assert len(df_m) == 8
    assert (df_m["is_placeholder"] == True).all()
    assert (df_m["is_calculated"] == False).all()
