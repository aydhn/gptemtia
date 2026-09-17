# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Metric Placeholders and Bias Guards."""

import pytest
from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_metric_placeholders import (
    build_stress_metric_placeholder_registry,
)
from advanced_stress_testing.scenario_metric_placeholders import (
    build_scenario_metric_placeholder_registry,
)
from advanced_stress_testing.robustness_metric_placeholders import (
    build_robustness_metric_placeholder_registry,
)
from advanced_stress_testing.stressed_pnl_placeholders import (
    build_stressed_pnl_placeholder_registry,
)
from advanced_stress_testing.stressed_drawdown_placeholders import (
    build_stressed_drawdown_placeholder_registry,
)
from advanced_stress_testing.stressed_liquidity_placeholders import (
    build_stressed_liquidity_placeholder_registry,
)
from advanced_stress_testing.stressed_exposure_placeholders import (
    build_stressed_exposure_placeholder_registry,
)
from advanced_stress_testing.stressed_cost_impact_placeholders import (
    build_stressed_cost_impact_placeholder_registry,
)
from advanced_stress_testing.stress_no_lookahead_guards import (
    build_stress_no_lookahead_guard_registry,
    validate_stress_no_lookahead_columns,
)
from advanced_stress_testing.stress_scenario_leakage_guards import (
    build_stress_scenario_leakage_guard_registry,
)
from advanced_stress_testing.stress_forbidden_column_policies import (
    build_stress_forbidden_column_policy_registry,
    validate_stress_forbidden_columns,
)
from advanced_stress_testing.stress_data_snooping_bias_guards import (
    build_stress_data_snooping_bias_guard_registry,
)
from advanced_stress_testing.stress_survivorship_bias_guards import (
    build_stress_survivorship_bias_guard_registry,
)
from advanced_stress_testing.stress_metadata_only_news_guards import (
    build_stress_metadata_only_news_guard_registry,
    validate_stress_metadata_only_news_columns,
)
from advanced_stress_testing.stress_source_preservation_guards import (
    build_stress_source_preservation_guard_registry,
)


@pytest.fixture
def profile():
    return get_default_stress_testing_profile()


def test_metric_placeholders(profile):
    df_met, sum_met = build_stress_metric_placeholder_registry(profile)
    assert not df_met.empty
    assert sum_met["all_calculation_blocked"] is True
    assert sum_met["zero_performance_claims"] is True
    assert sum_met["non_signal"] is True

    df_scen, sum_scen = build_scenario_metric_placeholder_registry(profile)
    assert not df_scen.empty
    assert sum_scen["all_calculation_blocked"] is True

    df_rob, sum_rob = build_robustness_metric_placeholder_registry(profile)
    assert not df_rob.empty
    assert sum_rob["all_calculation_blocked"] is True


def test_specific_metric_placeholders(profile):
    df_pnl, sum_pnl = build_stressed_pnl_placeholder_registry(profile)
    assert not df_pnl.empty
    assert sum_pnl["all_calculation_blocked"] is True

    df_dd, sum_dd = build_stressed_drawdown_placeholder_registry(profile)
    assert not df_dd.empty
    assert sum_dd["all_calculation_blocked"] is True

    df_liq, sum_liq = build_stressed_liquidity_placeholder_registry(profile)
    assert not df_liq.empty
    assert sum_liq["all_calculation_blocked"] is True

    df_exp, sum_exp = build_stressed_exposure_placeholder_registry(profile)
    assert not df_exp.empty
    assert sum_exp["all_calculation_blocked"] is True

    df_cost, sum_cost = build_stressed_cost_impact_placeholder_registry(profile)
    assert not df_cost.empty
    assert sum_cost["all_calculation_blocked"] is True


def test_no_lookahead_guards(profile):
    df_nl, sum_nl = build_stress_no_lookahead_guard_registry(profile)
    assert not df_nl.empty
    assert sum_nl["guard_active"] is True
    assert sum_nl["non_signal"] is True

    # Validate column check
    safe_cols = ["timestamp_utc", "open", "high", "low", "close", "volume"]
    res_safe = validate_stress_no_lookahead_columns(safe_cols)
    assert res_safe["is_safe"] is True
    assert res_safe["has_violations"] is False

    unsafe_cols = ["close", "future_return", "shift(-1)_close"]
    res_unsafe = validate_stress_no_lookahead_columns(unsafe_cols)
    assert res_unsafe["is_safe"] is False
    assert res_unsafe["has_violations"] is True


def test_scenario_leakage_and_forbidden_columns(profile):
    df_leak, sum_leak = build_stress_scenario_leakage_guard_registry(profile)
    assert not df_leak.empty
    assert sum_leak["guard_active"] is True

    df_forb, sum_forb = build_stress_forbidden_column_policy_registry(profile)
    assert not df_forb.empty
    assert sum_forb["total_forbidden_columns"] >= 30
    assert sum_forb["guard_active"] is True

    # Validate forbidden columns
    safe = validate_stress_forbidden_columns(["symbol", "open", "volatility_w20"])
    assert safe["is_safe"] is True
    assert safe["has_violations"] is False

    violated = validate_stress_forbidden_columns(["open", "buy", "stressed_pnl"])
    assert violated["is_safe"] is False
    assert violated["has_violations"] is True
    assert len(violated["violating_columns"]) == 2


def test_bias_and_preservation_guards(profile):
    df_snoop, sum_snoop = build_stress_data_snooping_bias_guard_registry(profile)
    assert not df_snoop.empty
    assert sum_snoop["guard_active"] is True

    df_surv, sum_surv = build_stress_survivorship_bias_guard_registry(profile)
    assert not df_surv.empty
    assert sum_surv["guard_active"] is True

    df_news, sum_news = build_stress_metadata_only_news_guard_registry(profile)
    assert not df_news.empty
    assert sum_news["guard_active"] is True

    news_safe = validate_stress_metadata_only_news_columns(["headline_count", "urgency_score"])
    assert news_safe["is_safe"] is True

    news_unsafe = validate_stress_metadata_only_news_columns(["full_text", "article_body"])
    assert news_unsafe["is_safe"] is False

    df_src, sum_src = build_stress_source_preservation_guard_registry(profile)
    assert not df_src.empty
    assert sum_src["guard_active"] is True
