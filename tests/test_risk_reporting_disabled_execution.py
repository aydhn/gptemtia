# -*- coding: utf-8 -*-
"""Unit tests for Risk Reporting Disabled Execution Reports."""

from advanced_risk_reporting.risk_reporting_config import get_default_risk_reporting_profile
from advanced_risk_reporting.risk_report_execution_disabled import build_risk_report_execution_disabled_report
from advanced_risk_reporting.exposure_attribution_execution_disabled import build_exposure_attribution_execution_disabled_report
from advanced_risk_reporting.limit_monitoring_execution_disabled import build_limit_monitoring_execution_disabled_report
from advanced_risk_reporting.risk_metric_calculation_disabled import build_risk_metric_calculation_disabled_report
from advanced_risk_reporting.limit_alerting_disabled import build_limit_alerting_disabled_report
from advanced_risk_reporting.dashboard_generation_disabled import build_dashboard_generation_disabled_report
from advanced_risk_reporting.portfolio_adjustment_disabled import build_portfolio_adjustment_disabled_report
from advanced_risk_reporting.risk_reporting_model_training_disabled import build_risk_reporting_model_training_disabled_report
from advanced_risk_reporting.risk_reporting_prediction_disabled import build_risk_reporting_prediction_disabled_report
from advanced_risk_reporting.risk_reporting_live_trading_disabled import build_risk_reporting_live_trading_disabled_report
from advanced_risk_reporting.risk_reporting_broker_execution_disabled import build_risk_reporting_broker_execution_disabled_report
from advanced_risk_reporting.risk_reporting_deployment_disabled import build_risk_reporting_deployment_disabled_report


def test_build_all_disabled_execution_reports():
    profile = get_default_risk_reporting_profile()

    df_rr, s_rr = build_risk_report_execution_disabled_report(profile)
    assert not df_rr.empty
    assert s_rr["is_disabled"] is True
    assert (df_rr["is_disabled"] == True).all()

    df_ea, s_ea = build_exposure_attribution_execution_disabled_report(profile)
    assert not df_ea.empty
    assert s_ea["is_disabled"] is True
    assert (df_ea["is_disabled"] == True).all()

    df_lm, s_lm = build_limit_monitoring_execution_disabled_report(profile)
    assert not df_lm.empty
    assert s_lm["is_disabled"] is True
    assert (df_lm["is_disabled"] == True).all()

    df_rm, s_rm = build_risk_metric_calculation_disabled_report(profile)
    assert not df_rm.empty
    assert s_rm["is_disabled"] is True
    assert (df_rm["is_disabled"] == True).all()

    df_la, s_la = build_limit_alerting_disabled_report(profile)
    assert not df_la.empty
    assert s_la["is_disabled"] is True
    assert (df_la["is_disabled"] == True).all()

    df_dg, s_dg = build_dashboard_generation_disabled_report(profile)
    assert not df_dg.empty
    assert s_dg["is_disabled"] is True
    assert (df_dg["is_disabled"] == True).all()

    df_pa, s_pa = build_portfolio_adjustment_disabled_report(profile)
    assert not df_pa.empty
    assert s_pa["is_disabled"] is True
    assert (df_pa["is_disabled"] == True).all()

    df_lt, s_lt = build_risk_reporting_live_trading_disabled_report(profile)
    assert not df_lt.empty
    assert s_lt["is_disabled"] is True
    assert (df_lt["is_disabled"] == True).all()

    df_be, s_be = build_risk_reporting_broker_execution_disabled_report(profile)
    assert not df_be.empty
    assert s_be["is_disabled"] is True
    assert (df_be["is_disabled"] == True).all()
