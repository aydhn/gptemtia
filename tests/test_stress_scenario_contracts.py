# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Scenario Contracts and Shock Placeholders."""

import pytest
from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_scenario_contracts import (
    build_stress_scenario_contract_registry,
)
from advanced_stress_testing.historical_stress_scenario_contracts import (
    build_historical_stress_scenario_contract_registry,
)
from advanced_stress_testing.hypothetical_stress_scenario_contracts import (
    build_hypothetical_stress_scenario_contract_registry,
)
from advanced_stress_testing.regime_shock_scenario_contracts import (
    build_regime_shock_scenario_contract_registry,
)
from advanced_stress_testing.volatility_shock_scenario_contracts import (
    build_volatility_shock_scenario_contract_registry,
)
from advanced_stress_testing.liquidity_shock_scenario_contracts import (
    build_liquidity_shock_scenario_contract_registry,
)
from advanced_stress_testing.spread_widening_scenario_contracts import (
    build_spread_widening_scenario_contract_registry,
)
from advanced_stress_testing.gap_risk_scenario_placeholders import (
    build_gap_risk_scenario_placeholder_registry,
)
from advanced_stress_testing.correlation_breakdown_scenario_placeholders import (
    build_correlation_breakdown_scenario_placeholder_registry,
)
from advanced_stress_testing.macro_shock_scenario_placeholders import (
    build_macro_shock_scenario_placeholder_registry,
)
from advanced_stress_testing.cross_asset_contagion_scenario_placeholders import (
    build_cross_asset_contagion_scenario_placeholder_registry,
)
from advanced_stress_testing.transaction_cost_shock_contracts import (
    build_transaction_cost_shock_contract_registry,
)
from advanced_stress_testing.slippage_shock_contracts import (
    build_slippage_shock_contract_registry,
)
from advanced_stress_testing.stress_scenario_library import (
    build_stress_scenario_library_registry,
)
from advanced_stress_testing.stress_scenario_groups import (
    build_stress_scenario_group_registry,
)
from advanced_stress_testing.stress_scenario_severity_policies import (
    build_stress_scenario_severity_policy_registry,
)


@pytest.fixture
def profile():
    return get_default_stress_testing_profile()


def test_core_stress_scenario_contracts(profile):
    df, summary = build_stress_scenario_contract_registry(profile)
    assert not df.empty
    assert len(df) >= 5
    assert summary["total_contracts"] == len(df)
    assert summary["all_stress_execution_blocked"] is True
    assert summary["all_scenario_simulation_blocked"] is True
    assert summary["non_signal"] is True


def test_historical_scenario_contracts(profile):
    df, summary = build_historical_stress_scenario_contract_registry(profile)
    assert not df.empty
    assert summary["total_historical_scenarios"] == len(df)
    assert summary["all_execution_blocked"] is True
    assert summary["non_signal"] is True
    # Verify presence of GFC 2008 and COVID 2020
    scenarios = df["scenario_name"].values
    assert any("2008" in str(s) for s in scenarios)
    assert any("covid" in str(s).lower() or "2020" in str(s) for s in scenarios)


def test_hypothetical_contracts(profile):
    df_hypo, sum_hypo = build_hypothetical_stress_scenario_contract_registry(profile)
    assert not df_hypo.empty
    assert sum_hypo["total_hypothetical_scenarios"] == len(df_hypo)
    assert sum_hypo["all_execution_blocked"] is True
    assert sum_hypo["non_signal"] is True


def test_shock_contracts(profile):
    # Regime, Volatility, Liquidity, Spread Shocks
    df_reg, sum_reg = build_regime_shock_scenario_contract_registry(profile)
    assert not df_reg.empty
    assert sum_reg["non_signal"] is True

    df_vol, sum_vol = build_volatility_shock_scenario_contract_registry(profile)
    assert not df_vol.empty
    assert sum_vol["all_execution_blocked"] is True
    assert sum_vol["non_signal"] is True

    df_liq, sum_liq = build_liquidity_shock_scenario_contract_registry(profile)
    assert not df_liq.empty
    assert sum_liq["all_execution_blocked"] is True
    assert sum_liq["non_signal"] is True

    df_spr, sum_spr = build_spread_widening_scenario_contract_registry(profile)
    assert not df_spr.empty
    assert sum_spr["all_execution_blocked"] is True
    assert sum_spr["non_signal"] is True


def test_shock_placeholders(profile):
    # Gap risk, correlation breakdown, macro, contagion
    df_gap, sum_gap = build_gap_risk_scenario_placeholder_registry(profile)
    assert not df_gap.empty
    assert sum_gap["all_execution_blocked"] is True
    assert sum_gap["non_signal"] is True

    df_corr, sum_corr = build_correlation_breakdown_scenario_placeholder_registry(profile)
    assert not df_corr.empty
    assert sum_corr["all_execution_blocked"] is True
    assert sum_corr["non_signal"] is True

    df_mac, sum_mac = build_macro_shock_scenario_placeholder_registry(profile)
    assert not df_mac.empty
    assert sum_mac["all_execution_blocked"] is True
    assert sum_mac["non_signal"] is True

    df_cnt, sum_cnt = build_cross_asset_contagion_scenario_placeholder_registry(profile)
    assert not df_cnt.empty
    assert sum_cnt["all_execution_blocked"] is True
    assert sum_cnt["non_signal"] is True


def test_cost_and_slippage_shocks(profile):
    df_cost, sum_cost = build_transaction_cost_shock_contract_registry(profile)
    assert not df_cost.empty
    assert sum_cost["all_execution_blocked"] is True
    assert sum_cost["non_signal"] is True

    df_slip, sum_slip = build_slippage_shock_contract_registry(profile)
    assert not df_slip.empty
    assert sum_slip["all_execution_blocked"] is True
    assert sum_slip["non_signal"] is True


def test_library_groups_severity_policies(profile):
    df_lib, sum_lib = build_stress_scenario_library_registry(profile)
    assert not df_lib.empty
    assert sum_lib["total_library_scenarios"] == len(df_lib)
    assert sum_lib["all_execution_blocked"] is True
    assert sum_lib["non_signal"] is True

    df_grp, sum_grp = build_stress_scenario_group_registry(profile)
    assert not df_grp.empty

    df_sev, sum_sev = build_stress_scenario_severity_policy_registry(profile)
    assert not df_sev.empty
