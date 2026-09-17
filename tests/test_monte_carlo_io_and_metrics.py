# -*- coding: utf-8 -*-
"""Phase 149 Unit Tests: Monte Carlo IO Contracts and Metric Placeholders."""

from advanced_monte_carlo_robustness.monte_carlo_config import get_default_monte_carlo_profile
from advanced_monte_carlo_robustness.monte_carlo_input_data_contracts import (
    build_monte_carlo_input_data_contract_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_feature_input_contracts import (
    build_monte_carlo_feature_input_contract_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_signal_input_contracts import (
    build_monte_carlo_signal_input_contract_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_output_contracts import (
    build_monte_carlo_output_contract_registry,
)
from advanced_monte_carlo_robustness.robustness_output_contracts import (
    build_robustness_output_contract_registry,
)
from advanced_monte_carlo_robustness.parameter_stability_output_contracts import (
    build_parameter_stability_output_contract_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_metric_placeholders import (
    build_monte_carlo_metric_placeholder_registry,
)
from advanced_monte_carlo_robustness.robustness_metric_placeholders import (
    build_robustness_metric_placeholder_registry,
)
from advanced_monte_carlo_robustness.parameter_stability_metric_placeholders import (
    build_parameter_stability_metric_placeholder_registry,
)
from advanced_monte_carlo_robustness.fragility_metric_placeholders import (
    build_fragility_metric_placeholder_registry,
)
from advanced_monte_carlo_robustness.distribution_metric_placeholders import (
    build_distribution_metric_placeholder_registry,
)


def test_input_and_output_contracts():
    profile = get_default_monte_carlo_profile()
    df_in, s_in = build_monte_carlo_input_data_contract_registry(profile)
    df_fin, s_fin = build_monte_carlo_feature_input_contract_registry(profile)
    df_sin, s_sin = build_monte_carlo_signal_input_contract_registry(profile)
    df_out, s_out = build_monte_carlo_output_contract_registry(profile)
    df_rout, s_rout = build_robustness_output_contract_registry(profile)
    df_pout, s_pout = build_parameter_stability_output_contract_registry(profile)

    assert not df_in.empty and s_in["status"] == "monte_carlo_contract_ready"
    assert not df_fin.empty and s_fin["status"] == "monte_carlo_contract_ready"
    assert not df_sin.empty and s_sin["status"] == "monte_carlo_contract_ready"
    assert not df_out.empty and s_out["status"] == "monte_carlo_contract_ready"
    assert not df_rout.empty and s_rout["status"] == "monte_carlo_contract_ready"
    assert not df_pout.empty and s_pout["status"] == "monte_carlo_contract_ready"



def test_metric_placeholders():
    profile = get_default_monte_carlo_profile()
    df_mc, s_mc = build_monte_carlo_metric_placeholder_registry(profile)
    df_rb, s_rb = build_robustness_metric_placeholder_registry(profile)
    df_ps, s_ps = build_parameter_stability_metric_placeholder_registry(profile)
    df_fg, s_fg = build_fragility_metric_placeholder_registry(profile)
    df_ds, s_ds = build_distribution_metric_placeholder_registry(profile)

    assert not df_mc.empty and s_mc["all_uncalculated"] is True
    assert not df_rb.empty and s_rb["all_uncalculated"] is True
    assert not df_ps.empty and s_ps["all_uncalculated"] is True
    assert not df_fg.empty and s_fg["all_uncalculated"] is True
    assert not df_ds.empty and s_ds["all_uncalculated"] is True
