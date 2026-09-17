# -*- coding: utf-8 -*-
"""Phase 149 Unit Tests: Robustness Envelopes and Distributions."""

from advanced_monte_carlo_robustness.monte_carlo_config import get_default_monte_carlo_profile
from advanced_monte_carlo_robustness.robustness_envelope_placeholders import (
    build_robustness_envelope_placeholder_registry,
)
from advanced_monte_carlo_robustness.stability_band_placeholders import (
    build_stability_band_placeholder_registry,
)
from advanced_monte_carlo_robustness.confidence_interval_placeholders import (
    build_confidence_interval_placeholder_registry,
)
from advanced_monte_carlo_robustness.drawdown_distribution_placeholders import (
    build_drawdown_distribution_placeholder_registry,
)
from advanced_monte_carlo_robustness.return_distribution_placeholders import (
    build_return_distribution_placeholder_registry,
)
from advanced_monte_carlo_robustness.tail_risk_distribution_placeholders import (
    build_tail_risk_distribution_placeholder_registry,
)
from advanced_monte_carlo_robustness.worst_case_path_placeholders import (
    build_worst_case_path_placeholder_registry,
)
from advanced_monte_carlo_robustness.best_case_path_placeholders import (
    build_best_case_path_placeholder_registry,
)
from advanced_monte_carlo_robustness.median_case_path_placeholders import (
    build_median_case_path_placeholder_registry,
)


def test_robustness_envelope_placeholders():
    profile = get_default_monte_carlo_profile()
    df, summary = build_robustness_envelope_placeholder_registry(profile)
    assert not df.empty
    assert summary["total_envelope_bounds"] >= 4
    assert summary["all_uncalculated"] is True


def test_stability_band_placeholders():
    profile = get_default_monte_carlo_profile()
    df, summary = build_stability_band_placeholder_registry(profile)
    assert not df.empty
    assert summary["total_bands"] >= 3
    assert summary["all_uncalculated"] is True


def test_confidence_interval_placeholders():
    profile = get_default_monte_carlo_profile()
    df, summary = build_confidence_interval_placeholder_registry(profile)
    assert not df.empty
    assert summary["total_intervals"] >= 3
    assert summary["all_uncalculated"] is True


def test_distribution_placeholders():
    profile = get_default_monte_carlo_profile()
    df_dd, s_dd = build_drawdown_distribution_placeholder_registry(profile)
    df_ret, s_ret = build_return_distribution_placeholder_registry(profile)
    df_tl, s_tl = build_tail_risk_distribution_placeholder_registry(profile)
    assert not df_dd.empty and s_dd["all_uncalculated"] is True
    assert not df_ret.empty and s_ret["all_uncalculated"] is True
    assert not df_tl.empty and s_tl["all_uncalculated"] is True


def test_path_scenario_placeholders():
    profile = get_default_monte_carlo_profile()
    df_wc, s_wc = build_worst_case_path_placeholder_registry(profile)
    df_bc, s_bc = build_best_case_path_placeholder_registry(profile)
    df_med, s_med = build_median_case_path_placeholder_registry(profile)
    assert not df_wc.empty and s_wc["all_uncalculated"] is True
    assert not df_bc.empty and s_bc["all_uncalculated"] is True
    assert not df_med.empty and s_med["all_uncalculated"] is True
