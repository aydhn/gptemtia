# -*- coding: utf-8 -*-
"""Phase 149 Unit Tests: Monte Carlo Dependencies & Linkages."""

from advanced_monte_carlo_robustness.monte_carlo_config import get_default_monte_carlo_profile
from advanced_monte_carlo_robustness.scenario_resampling_linkage import (
    build_scenario_resampling_linkage_registry,
)
from advanced_monte_carlo_robustness.stress_monte_carlo_linkage import (
    build_stress_monte_carlo_linkage_registry,
)
from advanced_monte_carlo_robustness.walk_forward_monte_carlo_linkage import (
    build_walk_forward_monte_carlo_linkage_registry,
)
from advanced_monte_carlo_robustness.realistic_backtest_monte_carlo_dependencies import (
    build_realistic_backtest_monte_carlo_dependency_registry,
)
from advanced_monte_carlo_robustness.transaction_cost_monte_carlo_dependencies import (
    build_transaction_cost_monte_carlo_dependency_registry,
)
from advanced_monte_carlo_robustness.slippage_monte_carlo_dependencies import (
    build_slippage_monte_carlo_dependency_registry,
)
from advanced_monte_carlo_robustness.regime_monte_carlo_dependencies import (
    build_regime_monte_carlo_dependency_registry,
)
from advanced_monte_carlo_robustness.governance_monte_carlo_dependencies import (
    build_governance_monte_carlo_dependency_registry,
)


def test_monte_carlo_linkages():
    profile = get_default_monte_carlo_profile()
    df_scn, s_scn = build_scenario_resampling_linkage_registry(profile)
    df_str, s_str = build_stress_monte_carlo_linkage_registry(profile)
    df_wf, s_wf = build_walk_forward_monte_carlo_linkage_registry(profile)
    assert not df_scn.empty and s_scn["all_satisfied"] is True
    assert not df_str.empty and s_str["all_satisfied"] is True
    assert not df_wf.empty and s_wf["all_satisfied"] is True


def test_monte_carlo_dependencies():
    profile = get_default_monte_carlo_profile()
    df_bt, s_bt = build_realistic_backtest_monte_carlo_dependency_registry(profile)
    df_cst, s_cst = build_transaction_cost_monte_carlo_dependency_registry(profile)
    df_slp, s_slp = build_slippage_monte_carlo_dependency_registry(profile)
    df_reg, s_reg = build_regime_monte_carlo_dependency_registry(profile)
    df_gov, s_gov = build_governance_monte_carlo_dependency_registry(profile)

    assert not df_bt.empty and s_bt["all_satisfied"] is True
    assert not df_cst.empty and s_cst["all_satisfied"] is True
    assert not df_slp.empty and s_slp["all_satisfied"] is True
    assert not df_reg.empty and s_reg["all_satisfied"] is True
    assert not df_gov.empty and s_gov["all_satisfied"] is True
