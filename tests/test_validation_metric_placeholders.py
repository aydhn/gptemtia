# -*- coding: utf-8 -*-
"""Unit tests for Phase 147: Metric Placeholders and Output Contracts."""

from advanced_walk_forward_validation.walk_forward_config import (
    get_default_walk_forward_profile,
)
from advanced_walk_forward_validation.benchmark_metric_placeholders import (
    build_benchmark_metric_placeholder_registry,
)
from advanced_walk_forward_validation.oos_metric_placeholders import (
    build_oos_metric_placeholder_registry,
)
from advanced_walk_forward_validation.validation_metric_placeholders import (
    build_validation_metric_placeholder_registry,
)
from advanced_walk_forward_validation.walk_forward_output_contracts import (
    build_walk_forward_output_contract_registry,
)
from advanced_walk_forward_validation.benchmark_output_contracts import (
    build_benchmark_output_contract_registry,
)


def test_metric_placeholders_and_outputs():
    prof = get_default_walk_forward_profile()

    df_bm, s_bm = build_benchmark_metric_placeholder_registry(prof)
    assert not df_bm.empty
    assert s_bm["all_metrics_uncalculated"] is True
    assert (df_bm["metric_calculated"] == False).all()

    df_oos, s_oos = build_oos_metric_placeholder_registry(prof)
    assert not df_oos.empty
    assert s_oos["all_metrics_uncalculated"] is True

    df_vm, s_vm = build_validation_metric_placeholder_registry(prof)
    assert not df_vm.empty
    assert s_vm["all_metrics_uncalculated"] is True

    df_wfo, s_wfo = build_walk_forward_output_contract_registry(prof)
    assert not df_wfo.empty
    assert s_wfo["zero_signals"] is True
    assert s_wfo["zero_realized_returns"] is True

    df_bmo, s_bmo = build_benchmark_output_contract_registry(prof)
    assert not df_bmo.empty
    assert s_bmo["zero_alpha_claims"] is True
