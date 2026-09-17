# -*- coding: utf-8 -*-
"""Unit tests for Phase 147: OOS Benchmark Contracts and Placeholders."""

from advanced_walk_forward_validation.walk_forward_config import (
    get_default_walk_forward_profile,
)
from advanced_walk_forward_validation.oos_benchmark_contracts import (
    build_oos_benchmark_contract_registry,
)
from advanced_walk_forward_validation.benchmark_universe_contracts import (
    build_benchmark_universe_contract_registry,
)
from advanced_walk_forward_validation.benchmark_baseline_contracts import (
    build_benchmark_baseline_contract_registry,
)
from advanced_walk_forward_validation.benchmark_comparison_contracts import (
    build_benchmark_comparison_contract_registry,
)
from advanced_walk_forward_validation.naive_baseline_placeholders import (
    build_naive_baseline_placeholder_registry,
)
from advanced_walk_forward_validation.buy_and_hold_benchmark_placeholders import (
    build_buy_and_hold_benchmark_placeholder_registry,
)
from advanced_walk_forward_validation.cash_benchmark_placeholders import (
    build_cash_benchmark_placeholder_registry,
)
from advanced_walk_forward_validation.equal_weight_benchmark_placeholders import (
    build_equal_weight_benchmark_placeholder_registry,
)
from advanced_walk_forward_validation.regime_benchmark_placeholders import (
    build_regime_benchmark_placeholder_registry,
)
from advanced_walk_forward_validation.cost_aware_benchmark_placeholders import (
    build_cost_aware_benchmark_placeholder_registry,
)


def test_benchmark_contracts_and_placeholders():
    prof = get_default_walk_forward_profile()

    df_bm, s_bm = build_oos_benchmark_contract_registry(prof)
    assert not df_bm.empty
    assert s_bm["all_execution_blocked"] is True

    df_uni, s_uni = build_benchmark_universe_contract_registry(prof)
    assert not df_uni.empty

    df_base, s_base = build_benchmark_baseline_contract_registry(prof)
    assert not df_base.empty
    assert s_base["all_execution_disabled"] is True

    df_comp, s_comp = build_benchmark_comparison_contract_registry(prof)
    assert not df_comp.empty
    assert s_comp["zero_metric_calculated"] is True

    df_nv, s_nv = build_naive_baseline_placeholder_registry(prof)
    assert not df_nv.empty

    df_bah, s_bah = build_buy_and_hold_benchmark_placeholder_registry(prof)
    assert not df_bah.empty

    df_csh, s_csh = build_cash_benchmark_placeholder_registry(prof)
    assert not df_csh.empty

    df_eqw, s_eqw = build_equal_weight_benchmark_placeholder_registry(prof)
    assert not df_eqw.empty

    df_rgb, s_rgb = build_regime_benchmark_placeholder_registry(prof)
    assert not df_rgb.empty

    df_cab, s_cab = build_cost_aware_benchmark_placeholder_registry(prof)
    assert not df_cab.empty
