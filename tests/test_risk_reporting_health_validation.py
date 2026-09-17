# -*- coding: utf-8 -*-
"""Unit tests for Risk Reporting Health, Validation and Safety Boundary."""

from pathlib import Path
from advanced_risk_reporting.risk_reporting_config import get_default_risk_reporting_profile
from advanced_risk_reporting.risk_reporting_health import build_risk_reporting_health_check
from advanced_risk_reporting.risk_reporting_validation import build_risk_reporting_validation_report
from advanced_risk_reporting.risk_reporting_safety_boundary import build_risk_reporting_safety_boundary
from advanced_risk_reporting.risk_reporting_profile_registry import build_risk_reporting_profile_registry
from advanced_risk_reporting.risk_report_contracts import build_risk_report_contract_registry
from advanced_risk_reporting.exposure_attribution_contracts import build_exposure_attribution_contract_registry
from advanced_risk_reporting.limit_monitoring_contracts import build_limit_monitoring_contract_registry
from advanced_risk_reporting.risk_reporting_manifest import build_risk_reporting_manifest


def test_build_health_validation_safety():
    profile = get_default_risk_reporting_profile()
    root = Path(__file__).resolve().parents[1]

    df_hlth, s_hlth = build_risk_reporting_health_check(root, profile)
    assert not df_hlth.empty
    assert s_hlth["all_passed"] is True

    p_df, _ = build_risk_reporting_profile_registry(profile)
    c_df, _ = build_risk_report_contract_registry(profile)
    e_df, _ = build_exposure_attribution_contract_registry(profile)
    l_df, _ = build_limit_monitoring_contract_registry(profile)
    m_df, _ = build_risk_reporting_manifest(profile)

    tables = {
        "profiles": p_df,
        "contracts": c_df,
        "exposure_contracts": e_df,
        "limit_contracts": l_df,
        "manifest": m_df,
    }
    df_val, s_val = build_risk_reporting_validation_report(tables, profile)
    assert not df_val.empty
    assert s_val["all_passed"] is True

    df_safe, s_safe = build_risk_reporting_safety_boundary(profile)
    assert not df_safe.empty
    assert s_safe["status"] == "SAFETY_BOUNDARY_ACTIVE"
    assert s_safe["no_go_count"] >= 1
    assert s_safe["safe_go_count"] >= 1
