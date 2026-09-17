# -*- coding: utf-8 -*-
"""Unit tests for Risk Reporting Dependencies."""

from advanced_risk_reporting.risk_reporting_config import get_default_risk_reporting_profile
from advanced_risk_reporting.risk_reporting_dependencies import build_risk_reporting_dependency_registry
from advanced_risk_reporting.risk_reporting_portfolio_construction_dependencies import build_risk_reporting_portfolio_construction_dependency_registry
from advanced_risk_reporting.risk_reporting_portfolio_optimization_dependencies import build_risk_reporting_portfolio_optimization_dependency_registry
from advanced_risk_reporting.risk_reporting_backtest_acceptance_dependencies import build_risk_reporting_backtest_acceptance_dependency_registry
from advanced_risk_reporting.risk_reporting_model_governance_dependencies import build_risk_reporting_model_governance_dependency_registry
from advanced_risk_reporting.risk_reporting_regime_dependencies import build_risk_reporting_regime_dependency_registry
from advanced_risk_reporting.risk_reporting_featurestore_dependencies import build_risk_reporting_featurestore_dependency_registry


def test_build_risk_reporting_dependency_registries():
    profile = get_default_risk_reporting_profile()

    df_dep, s_dep = build_risk_reporting_dependency_registry(profile)
    assert not df_dep.empty
    assert s_dep["all_available"] is True
    assert s_dep["is_safe"] is True

    df_pc, s_pc = build_risk_reporting_portfolio_construction_dependency_registry(profile)
    assert not df_pc.empty
    assert s_pc["is_satisfied"] is True

    df_po, s_po = build_risk_reporting_portfolio_optimization_dependency_registry(profile)
    assert not df_po.empty
    assert s_po["is_satisfied"] is True

    df_ba, s_ba = build_risk_reporting_backtest_acceptance_dependency_registry(profile)
    assert not df_ba.empty
    assert s_ba["is_satisfied"] is True

    df_mg, s_mg = build_risk_reporting_model_governance_dependency_registry(profile)
    assert not df_mg.empty
    assert s_mg["is_satisfied"] is True

    df_rg, s_rg = build_risk_reporting_regime_dependency_registry(profile)
    assert not df_rg.empty
    assert s_rg["is_satisfied"] is True

    df_fs, s_fs = build_risk_reporting_featurestore_dependency_registry(profile)
    assert not df_fs.empty
    assert s_fs["is_satisfied"] is True
