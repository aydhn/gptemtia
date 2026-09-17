# -*- coding: utf-8 -*-
"""Phase 155: Risk Reporting Report Builder (Markdown)."""

from typing import Any, Dict, Optional
import pandas as pd


RISK_REPORTING_DISCLAIMER = (
    "> [!WARNING]\n"
    "> **YASAL UYARI VE GUVENLIK SINIRI (PHASE 155):**\n"
    "> Bu cikti Phase 155 Risk Reporting, Exposure Attribution and Limit Monitoring raporudur. "
    "Canli emir, broker talimati, kesin AL/SAT, yatirim tavsiyesi, "
    "risk-reporting/readiness/exposure/limit-monitoring degerini trade sinyali veya "
    "production-ready/broker-ready/onay olarak kullanma, gercek risk reporting, "
    "exposure attribution, limit monitoring, alerting, dashboard generation, "
    "portfolio adjustment, rebalance, hedge/de-risk, gercek VaR/ES/exposure/leverage/margin/risk metric "
    "hesaplama, model training, model fit/predict/inference, dataset materialization, "
    "target/label/prediction uretimi, performans garantisi, strategy approval, model deployment, "
    "model registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/"
    "scraped HTML/embedding/vector kullanimi veya gercek provider API cagrisi degildir.\n"
)


def build_risk_reporting_disclaimer() -> str:
    """Return standard disclaimer string."""
    return RISK_REPORTING_DISCLAIMER


def build_risk_reporting_profile_markdown_report(summary: Dict[str, Any], profile_df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 155: Risk Reporting Profile Registry Report",
        build_risk_reporting_disclaimer(),
        "## Summary",
        f"- **Active Profile**: `{summary.get('active_profile')}`",
        f"- **Total Profiles**: `{summary.get('total_profiles', summary.get('profile_count', 0))}`",
        f"- **Current Phase**: `{summary.get('current_phase', 155)}`",
        f"- **Non-Production Invariant**: `{summary.get('all_profiles_non_production', True)}`",
        f"- **Zero Live Trading**: `{summary.get('zero_live_trading', True)}`",
        f"- **Zero Broker Integration**: `{summary.get('zero_broker_integration', True)}`",
    ]
    return "\n\n".join(md)


def build_risk_report_contract_markdown_report(summary: Dict[str, Any], df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 155: Risk Report Contracts Report",
        build_risk_reporting_disclaimer(),
        "## Summary",
        f"- **Total Contracts**: `{summary.get('total_contracts', summary.get('contract_count', 0))}`",
        f"- **Zero Execution Allowed**: `{summary.get('all_contracts_disallow_execution', True)}`",
        f"- **Zero Live Trading**: `{summary.get('all_contracts_disallow_live_trading', True)}`",
        f"- **Manual Review Required All**: `{summary.get('manual_review_required_all', True)}`",
    ]
    return "\n\n".join(md)


def build_exposure_attribution_markdown_report(summary: Dict[str, Any], df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 155: Exposure Attribution Contracts Report",
        build_risk_reporting_disclaimer(),
        "## Summary",
        f"- **Total Contracts**: `{summary.get('total_contracts', summary.get('contract_count', 0))}`",
        f"- **Placeholder Mode All**: `{summary.get('all_contracts_placeholder', True)}`",
        f"- **Zero Exposure Calculated**: `{summary.get('zero_exposure_calculated', True)}`",
    ]
    return "\n\n".join(md)


def build_limit_monitoring_markdown_report(summary: Dict[str, Any], df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 155: Limit Monitoring Contracts Report",
        build_risk_reporting_disclaimer(),
        "## Summary",
        f"- **Total Contracts**: `{summary.get('total_contracts', summary.get('contract_count', 0))}`",
        f"- **Zero Live Enforcement**: `{summary.get('zero_live_enforcement', True)}`",
        f"- **Zero Alerting Allowed**: `{summary.get('zero_alerting_allowed', True)}`",
    ]
    return "\n\n".join(md)


def build_exposure_placeholder_markdown_report(summary: Dict[str, Any], df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 155: Exposure Placeholders Report",
        build_risk_reporting_disclaimer(),
        "## Summary",
        f"- **Placeholder Count**: `{summary.get('placeholder_count', 0)}`",
        f"- **Is Calculated**: `{summary.get('is_calculated', False)}`",
    ]
    return "\n\n".join(md)


def build_risk_monitor_placeholder_markdown_report(summary: Dict[str, Any], df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 155: Risk Monitor Placeholders Report",
        build_risk_reporting_disclaimer(),
        "## Summary",
        f"- **Total Monitor Placeholders**: `{summary.get('placeholder_count', 0)}`",
        f"- **Execution Blocked**: True",
    ]
    return "\n\n".join(md)


def build_risk_metric_placeholder_markdown_report(summary: Dict[str, Any], df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 155: Risk Metric Placeholders Report",
        build_risk_reporting_disclaimer(),
        "## Summary",
        f"- **Total Metric Placeholders**: `{summary.get('metric_count', 0)}`",
        f"- **Zero Calculated**: `{summary.get('zero_calculated', True)}`",
    ]
    return "\n\n".join(md)


def build_risk_reporting_guard_markdown_report(summary: Dict[str, Any], df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 155: Risk Reporting Safety Guards Report",
        build_risk_reporting_disclaimer(),
        "## Summary",
        f"- **Total Guards**: `{summary.get('guard_count', 0)}`",
        f"- **All Active**: `{summary.get('all_active', True)}`",
    ]
    return "\n\n".join(md)


def build_risk_reporting_disabled_execution_markdown_report(summary: Dict[str, Any], df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 155: Disabled Execution Reports",
        build_risk_reporting_disclaimer(),
        "## Summary",
        f"- **Status**: `{summary.get('status', 'execution_contract_only')}`",
        f"- **Is Disabled**: `{summary.get('is_disabled', True)}`",
    ]
    return "\n\n".join(md)


def build_risk_reporting_findings_markdown_report(summary: Dict[str, Any], df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 155: Risk Reporting Diagnostic Findings",
        build_risk_reporting_disclaimer(),
        "## Summary",
        f"- **Total Findings**: `{summary.get('total_findings', summary.get('finding_count', 0))}`",
        f"- **Critical Blocker Count**: `{summary.get('critical_count', 0)}`",
        f"- **Manual Review Required**: `{summary.get('manual_review_required_count', 0)}`",
    ]
    return "\n\n".join(md)


def build_risk_reporting_readiness_score_markdown_report(summary: Dict[str, Any], df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 155: Risk Reporting Readiness Score Report",
        build_risk_reporting_disclaimer(),
        "## Summary",
        f"- **Readiness Score**: `{summary.get('readiness_score', 1.0):.4f}`",
        f"- **Classification**: `{summary.get('classification', 'risk_reporting_contract_ready_non_production')}`",
        f"- **Contract Ready**: `{summary.get('is_contract_ready', True)}`",
    ]
    return "\n\n".join(md)


def build_risk_reporting_manifest_markdown_report(summary: Dict[str, Any], df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 155: Master Risk Reporting Manifest",
        build_risk_reporting_disclaimer(),
        "## Summary",
        f"- **Manifest Name**: `{summary.get('manifest_name')}`",
        f"- **Current Phase**: `{summary.get('current_phase', 155)}`",
        f"- **Target Final Phase**: `{summary.get('target_final_phase', 160)}`",
        f"- **Next Phase**: `{summary.get('next_phase', 156)}`",
        f"- **Phase 156 Handoff Ready**: `{summary.get('phase_156_handoff_ready', True)}`",
    ]
    return "\n\n".join(md)


def build_risk_reporting_validation_markdown_report(summary: Dict[str, Any], df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 155: Risk Reporting Validation Report",
        build_risk_reporting_disclaimer(),
        "## Summary",
        f"- **Validation Status**: `{summary.get('status', 'RISK_REPORT_CONTRACT_READY')}`",
        f"- **Total Checks**: `{summary.get('total_checks', 0)}`",
        f"- **All Passed**: `{summary.get('all_passed', True)}`",
    ]
    return "\n\n".join(md)


def build_risk_reporting_safety_markdown_report(summary: Dict[str, Any], df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 155: Risk Reporting Safety Boundary Report",
        build_risk_reporting_disclaimer(),
        "## Summary",
        f"- **NO-GO Conditions Count**: `{summary.get('no_go_count', 0)}`",
        f"- **SAFE-GO Conditions Count**: `{summary.get('safe_go_count', 0)}`",
        f"- **Safety Status**: `PASS_CONTRACT_ONLY`",
    ]
    return "\n\n".join(md)


def build_phase_156_handoff_markdown_report(summary: Dict[str, Any], df: Optional[pd.DataFrame] = None) -> str:
    md = [
        "# Phase 156: Portfolio Scenario Testing and Drawdown Control Handoff Report",
        build_risk_reporting_disclaimer(),
        "## Summary",
        f"- **Current Phase**: `{summary.get('current_phase', 155)}`",
        f"- **Next Phase**: `{summary.get('next_phase', 156)}`",
        f"- **Target Final Phase**: `{summary.get('target_final_phase', 160)}`",
        f"- **Handoff Ready**: `{summary.get('handoff_ready', True)}`",
    ]
    return "\n\n".join(md)
