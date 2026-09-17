# -*- coding: utf-8 -*-
"""Unit tests for Risk Reporting Guards."""

from advanced_risk_reporting.risk_reporting_config import get_default_risk_reporting_profile
from advanced_risk_reporting.risk_reporting_no_lookahead_guards import build_risk_reporting_no_lookahead_guard_registry
from advanced_risk_reporting.risk_reporting_exposure_claim_guards import build_risk_reporting_exposure_claim_guard_registry
from advanced_risk_reporting.risk_reporting_limit_breach_claim_guards import build_risk_reporting_limit_breach_claim_guard_registry
from advanced_risk_reporting.risk_reporting_investment_advice_guards import build_risk_reporting_investment_advice_guard_registry
from advanced_risk_reporting.risk_reporting_portfolio_adjustment_guards import build_risk_reporting_portfolio_adjustment_guard_registry
from advanced_risk_reporting.risk_reporting_alert_claim_guards import build_risk_reporting_alert_claim_guard_registry
from advanced_risk_reporting.risk_reporting_forbidden_column_policies import build_risk_reporting_forbidden_column_policy_registry


def test_build_risk_reporting_guard_registries():
    profile = get_default_risk_reporting_profile()

    df_nl, s_nl = build_risk_reporting_no_lookahead_guard_registry(profile)
    assert not df_nl.empty
    assert s_nl["all_active"] is True
    assert (df_nl["is_active"] == True).all()

    df_ec, s_ec = build_risk_reporting_exposure_claim_guard_registry(profile)
    assert not df_ec.empty
    assert s_ec["all_active"] is True
    assert (df_ec["is_active"] == True).all()

    df_lb, s_lb = build_risk_reporting_limit_breach_claim_guard_registry(profile)
    assert not df_lb.empty
    assert s_lb["all_active"] is True
    assert (df_lb["is_active"] == True).all()

    df_ia, s_ia = build_risk_reporting_investment_advice_guard_registry(profile)
    assert not df_ia.empty
    assert s_ia["all_active"] is True
    assert (df_ia["is_active"] == True).all()

    df_pa, s_pa = build_risk_reporting_portfolio_adjustment_guard_registry(profile)
    assert not df_pa.empty
    assert s_pa["all_active"] is True
    assert (df_pa["is_active"] == True).all()

    df_ac, s_ac = build_risk_reporting_alert_claim_guard_registry(profile)
    assert not df_ac.empty
    assert s_ac["all_active"] is True
    assert (df_ac["is_active"] == True).all()

    df_fc, s_fc = build_risk_reporting_forbidden_column_policy_registry(profile)
    assert not df_fc.empty
    assert s_fc["all_blocked"] is True
    assert s_fc["forbidden_column_count"] >= 1
