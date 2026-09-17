# -*- coding: utf-8 -*-
"""Phase 149 Unit Tests: Monte Carlo Bias & Lookahead Guards."""

from advanced_monte_carlo_robustness.monte_carlo_config import get_default_monte_carlo_profile
from advanced_monte_carlo_robustness.monte_carlo_no_lookahead_guards import (
    build_monte_carlo_no_lookahead_guard_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_resampling_leakage_guards import (
    build_monte_carlo_resampling_leakage_guard_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_data_snooping_bias_guards import (
    build_monte_carlo_data_snooping_bias_guard_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_overfitting_guards import (
    build_monte_carlo_overfitting_guard_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_survivorship_bias_guards import (
    build_monte_carlo_survivorship_bias_guard_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_multiple_testing_guards import (
    build_monte_carlo_multiple_testing_guard_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_metadata_only_news_guards import (
    build_monte_carlo_metadata_only_news_guard_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_source_preservation_guards import (
    build_monte_carlo_source_preservation_guard_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_forbidden_column_policies import (
    build_monte_carlo_forbidden_column_policy_registry,
)


def test_monte_carlo_guards():
    profile = get_default_monte_carlo_profile()
    df_g1, s_g1 = build_monte_carlo_no_lookahead_guard_registry(profile)
    df_g2, s_g2 = build_monte_carlo_resampling_leakage_guard_registry(profile)
    df_g3, s_g3 = build_monte_carlo_data_snooping_bias_guard_registry(profile)
    df_g4, s_g4 = build_monte_carlo_overfitting_guard_registry(profile)
    df_g5, s_g5 = build_monte_carlo_survivorship_bias_guard_registry(profile)
    df_g6, s_g6 = build_monte_carlo_multiple_testing_guard_registry(profile)
    df_g7, s_g7 = build_monte_carlo_metadata_only_news_guard_registry(profile)
    df_g8, s_g8 = build_monte_carlo_source_preservation_guard_registry(profile)
    df_g9, s_g9 = build_monte_carlo_forbidden_column_policy_registry(profile)

    assert not df_g1.empty and s_g1["all_active"] is True
    assert not df_g2.empty and s_g2["all_active"] is True
    assert not df_g3.empty and s_g3["all_active"] is True
    assert not df_g4.empty and s_g4["all_active"] is True
    assert not df_g5.empty and s_g5["all_active"] is True
    assert not df_g6.empty and s_g6["all_active"] is True
    assert not df_g7.empty and s_g7["all_active"] is True
    assert not df_g8.empty and s_g8["all_active"] is True
    assert not df_g9.empty and s_g9["all_active"] is True
