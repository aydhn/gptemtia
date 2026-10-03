"""Unit tests for Phase 155 Risk Reporting Report Builder."""

from advanced_risk_reporting.risk_reporting_report_builder import (
    RISK_REPORTING_DISCLAIMER,
    build_exposure_attribution_markdown_report,
    build_exposure_placeholder_markdown_report,
    build_limit_monitoring_markdown_report,
    build_phase_156_handoff_markdown_report,
    build_risk_metric_placeholder_markdown_report,
    build_risk_monitor_placeholder_markdown_report,
    build_risk_report_contract_markdown_report,
    build_risk_reporting_disabled_execution_markdown_report,
    build_risk_reporting_disclaimer,
    build_risk_reporting_findings_markdown_report,
    build_risk_reporting_guard_markdown_report,
    build_risk_reporting_manifest_markdown_report,
    build_risk_reporting_profile_markdown_report,
    build_risk_reporting_readiness_score_markdown_report,
    build_risk_reporting_safety_markdown_report,
    build_risk_reporting_validation_markdown_report,
)


def test_build_risk_reporting_disclaimer():
    disclaimer = build_risk_reporting_disclaimer()
    assert disclaimer == RISK_REPORTING_DISCLAIMER
    assert "YASAL UYARI VE GUVENLIK SINIRI" in disclaimer
    assert "Phase 155" in disclaimer


def test_build_risk_reporting_profile_markdown_report():
    summary = {
        "active_profile": "test_profile",
        "total_profiles": 5,
        "current_phase": 155,
        "all_profiles_non_production": True,
        "zero_live_trading": True,
        "zero_broker_integration": True,
    }
    report = build_risk_reporting_profile_markdown_report(summary)
    assert "# Phase 155: Risk Reporting Profile Registry Report" in report
    assert "test_profile" in report
    assert "5" in report
    assert "155" in report
    assert RISK_REPORTING_DISCLAIMER in report


def test_build_risk_report_contract_markdown_report():
    summary = {
        "total_contracts": 10,
        "all_contracts_disallow_execution": True,
        "all_contracts_disallow_live_trading": True,
        "manual_review_required_all": True,
    }
    report = build_risk_report_contract_markdown_report(summary)
    assert "# Phase 155: Risk Report Contracts Report" in report
    assert "10" in report
    assert "True" in report


def test_build_exposure_attribution_markdown_report():
    summary = {
        "total_contracts": 8,
        "all_contracts_placeholder": True,
        "zero_exposure_calculated": True,
    }
    report = build_exposure_attribution_markdown_report(summary)
    assert "# Phase 155: Exposure Attribution Contracts Report" in report
    assert "8" in report
    assert "True" in report


def test_build_limit_monitoring_markdown_report():
    summary = {
        "total_contracts": 12,
        "zero_live_enforcement": True,
        "zero_alerting_allowed": True,
    }
    report = build_limit_monitoring_markdown_report(summary)
    assert "# Phase 155: Limit Monitoring Contracts Report" in report
    assert "12" in report


def test_build_exposure_placeholder_markdown_report():
    summary = {
        "placeholder_count": 3,
        "is_calculated": False,
    }
    report = build_exposure_placeholder_markdown_report(summary)
    assert "# Phase 155: Exposure Placeholders Report" in report
    assert "3" in report
    assert "False" in report


def test_build_risk_monitor_placeholder_markdown_report():
    summary = {
        "placeholder_count": 4,
    }
    report = build_risk_monitor_placeholder_markdown_report(summary)
    assert "# Phase 155: Risk Monitor Placeholders Report" in report
    assert "4" in report
    assert "True" in report


def test_build_risk_metric_placeholder_markdown_report():
    summary = {
        "metric_count": 6,
        "zero_calculated": True,
    }
    report = build_risk_metric_placeholder_markdown_report(summary)
    assert "# Phase 155: Risk Metric Placeholders Report" in report
    assert "6" in report
    assert "True" in report


def test_build_risk_reporting_guard_markdown_report():
    summary = {
        "guard_count": 2,
        "all_active": True,
    }
    report = build_risk_reporting_guard_markdown_report(summary)
    assert "# Phase 155: Risk Reporting Safety Guards Report" in report
    assert "2" in report
    assert "True" in report


def test_build_risk_reporting_disabled_execution_markdown_report():
    summary = {
        "status": "execution_contract_only",
        "is_disabled": True,
    }
    report = build_risk_reporting_disabled_execution_markdown_report(summary)
    assert "# Phase 155: Disabled Execution Reports" in report
    assert "execution_contract_only" in report
    assert "True" in report


def test_build_risk_reporting_findings_markdown_report():
    summary = {
        "total_findings": 7,
        "critical_count": 0,
        "manual_review_required_count": 1,
    }
    report = build_risk_reporting_findings_markdown_report(summary)
    assert "# Phase 155: Risk Reporting Diagnostic Findings" in report
    assert "7" in report
    assert "0" in report
    assert "1" in report


def test_build_risk_reporting_readiness_score_markdown_report():
    summary = {
        "readiness_score": 0.95,
        "classification": "risk_reporting_ready",
        "is_contract_ready": True,
    }
    report = build_risk_reporting_readiness_score_markdown_report(summary)
    assert "# Phase 155: Risk Reporting Readiness Score Report" in report
    assert "0.9500" in report
    assert "risk_reporting_ready" in report
    assert "True" in report


def test_build_risk_reporting_manifest_markdown_report():
    summary = {
        "manifest_name": "test_manifest",
        "current_phase": 155,
        "target_final_phase": 160,
        "next_phase": 156,
        "phase_156_handoff_ready": True,
    }
    report = build_risk_reporting_manifest_markdown_report(summary)
    assert "# Phase 155: Master Risk Reporting Manifest" in report
    assert "test_manifest" in report
    assert "155" in report
    assert "160" in report
    assert "156" in report
    assert "True" in report


def test_build_risk_reporting_validation_markdown_report():
    summary = {
        "status": "RISK_REPORT_CONTRACT_READY",
        "total_checks": 20,
        "all_passed": True,
    }
    report = build_risk_reporting_validation_markdown_report(summary)
    assert "# Phase 155: Risk Reporting Validation Report" in report
    assert "RISK_REPORT_CONTRACT_READY" in report
    assert "20" in report
    assert "True" in report


def test_build_risk_reporting_safety_markdown_report():
    summary = {
        "no_go_count": 0,
        "safe_go_count": 5,
    }
    report = build_risk_reporting_safety_markdown_report(summary)
    assert "# Phase 155: Risk Reporting Safety Boundary Report" in report
    assert "0" in report
    assert "5" in report
    assert "PASS_CONTRACT_ONLY" in report


def test_build_phase_156_handoff_markdown_report():
    summary = {
        "current_phase": 155,
        "next_phase": 156,
        "target_final_phase": 160,
        "handoff_ready": True,
    }
    report = build_phase_156_handoff_markdown_report(summary)
    assert (
        "# Phase 156: Portfolio Scenario Testing and Drawdown Control Handoff Report"
        in report
    )
    assert "155" in report
    assert "156" in report
    assert "160" in report
    assert "True" in report
