# -*- coding: utf-8 -*-
"""Phase 150: Backtest Governance Report Builder Module.

Provides markdown formatting functions and formal legal disclaimers for all Phase 150 reports.
Strictly non-signal, local-only, and research-governance focused.
"""

from typing import Any, Dict, Optional
import pandas as pd

from advanced_backtest_governance.backtest_report_disclaimers import DISCLAIMER_TEXT

BACKTEST_GOVERNANCE_REPORT_DISCLAIMER = DISCLAIMER_TEXT


def build_backtest_governance_disclaimer() -> str:
    """Return the standardized Phase 150 legal disclaimer."""
    return BACKTEST_GOVERNANCE_REPORT_DISCLAIMER


def _df_to_markdown(df: Optional[pd.DataFrame]) -> str:
    """Helper formatting DataFrame as markdown table."""
    if df is None or df.empty:
        return "_No tabular records available._"
    try:
        return df.to_markdown(index=False)
    except Exception:
        return df.to_string(index=False)


def build_backtest_governance_profile_markdown_report(
    summary: Dict[str, Any], profile_df: Optional[pd.DataFrame] = None
) -> str:
    return (
        f"# Phase 150: Backtest Governance Profile Registry Report\n\n"
        f"> **Disclaimer**: {BACKTEST_GOVERNANCE_REPORT_DISCLAIMER}\n\n"
        f"- **Domain**: `{summary.get('domain')}`\n"
        f"- **Active Profile**: `{summary.get('active_profile')}`\n"
        f"- **Total Profiles**: `{summary.get('total_profiles')}`\n"
        f"- **All Local Only**: `{summary.get('all_local_only')}`\n"
        f"- **All Zero Execution**: `{summary.get('all_zero_execution')}`\n"
        f"- **Status**: `{summary.get('status')}`\n\n"
        f"## Registered Profiles\n\n{_df_to_markdown(profile_df)}\n"
    )


def build_backtest_governance_contract_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    return (
        f"# Phase 150: Backtest Governance Contracts Report\n\n"
        f"> **Disclaimer**: {BACKTEST_GOVERNANCE_REPORT_DISCLAIMER}\n\n"
        f"- **Domain**: `{summary.get('domain')}`\n"
        f"- **Total Contracts**: `{summary.get('total_contracts')}`\n"
        f"- **All Executions Disabled**: `{summary.get('all_executions_disabled')}`\n"
        f"- **Status**: `{summary.get('status')}`\n\n"
        f"## Contracts Matrix\n\n{_df_to_markdown(df)}\n"
    )


def build_backtest_bias_control_contract_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    return (
        f"# Phase 150: Backtest Bias Control Contracts Report\n\n"
        f"> **Disclaimer**: {BACKTEST_GOVERNANCE_REPORT_DISCLAIMER}\n\n"
        f"- **Domain**: `{summary.get('domain')}`\n"
        f"- **Total Controls**: `{summary.get('total_controls')}`\n"
        f"- **All Claims Blocked**: `{summary.get('all_claims_blocked')}`\n"
        f"- **Status**: `{summary.get('status')}`\n\n"
        f"## Bias Controls Matrix\n\n{_df_to_markdown(df)}\n"
    )


def build_backtest_result_reporting_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    return (
        f"# Phase 150: Result Reporting Governance Report\n\n"
        f"> **Disclaimer**: {BACKTEST_GOVERNANCE_REPORT_DISCLAIMER}\n\n"
        f"- **Domain**: `{summary.get('domain')}`\n"
        f"- **Total Requirements**: `{summary.get('total_requirements')}`\n"
        f"- **All Claims Prohibited**: `{summary.get('all_claims_prohibited')}`\n"
        f"- **Status**: `{summary.get('status')}`\n\n"
        f"## Reporting Standards\n\n{_df_to_markdown(df)}\n"
    )


def build_backtest_claim_boundary_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    return (
        f"# Phase 150: Backtest Claim Boundaries Report\n\n"
        f"> **Disclaimer**: {BACKTEST_GOVERNANCE_REPORT_DISCLAIMER}\n\n"
        f"- **Domain**: `{summary.get('domain')}`\n"
        f"- **Total Boundaries**: `{summary.get('total_boundaries')}`\n"
        f"- **All Claims Blocked**: `{summary.get('all_claims_blocked')}`\n"
        f"- **Status**: `{summary.get('status')}`\n\n"
        f"## Boundary Enforcement\n\n{_df_to_markdown(df)}\n"
    )


def build_backtest_realism_governance_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    return (
        f"# Phase 150: Execution Realism Governance Report\n\n"
        f"> **Disclaimer**: {BACKTEST_GOVERNANCE_REPORT_DISCLAIMER}\n\n"
        f"- **Domain**: `{summary.get('domain')}`\n"
        f"- **Subdomain**: `{summary.get('subdomain')}`\n"
        f"- **Status**: `{summary.get('status')}`\n\n"
        f"## Realism Rules\n\n{_df_to_markdown(df)}\n"
    )


def build_backtest_manual_review_gate_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    return (
        f"# Phase 150: Manual Review Gates Report\n\n"
        f"> **Disclaimer**: {BACKTEST_GOVERNANCE_REPORT_DISCLAIMER}\n\n"
        f"- **Domain**: `{summary.get('domain')}`\n"
        f"- **Total Gates**: `{summary.get('total_gates')}`\n"
        f"- **Mandatory Human Verification**: `{summary.get('all_require_manual_review')}`\n"
        f"- **Status**: `{summary.get('status')}`\n\n"
        f"## Armed Gates\n\n{_df_to_markdown(df)}\n"
    )


def build_backtest_go_no_go_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    return (
        f"# Phase 150: Backtest Go/No-Go Decision Boundaries Report\n\n"
        f"> **Disclaimer**: {BACKTEST_GOVERNANCE_REPORT_DISCLAIMER}\n\n"
        f"- **Domain**: `{summary.get('domain')}`\n"
        f"- **Total Criteria**: `{summary.get('total_criteria')}`\n"
        f"- **All Hard Stops Active**: `{summary.get('all_hard_stops_active')}`\n"
        f"- **Status**: `{summary.get('status')}`\n\n"
        f"## Decision Criteria\n\n{_df_to_markdown(df)}\n"
    )


def build_backtest_disabled_execution_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    return (
        f"# Phase 150: Disabled Execution Report\n\n"
        f"> **Disclaimer**: {BACKTEST_GOVERNANCE_REPORT_DISCLAIMER}\n\n"
        f"- **Domain**: `{summary.get('domain')}`\n"
        f"- **Total Disabled Operations**: `{summary.get('total_disabled_operations')}`\n"
        f"- **All Executions Disabled**: True\n"
        f"- **Status**: `{summary.get('status')}`\n\n"
        f"## Blocked Execution Engines\n\n{_df_to_markdown(df)}\n"
    )


def build_backtest_governance_findings_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    return (
        f"# Phase 150: Backtest Governance Findings Report\n\n"
        f"> **Disclaimer**: {BACKTEST_GOVERNANCE_REPORT_DISCLAIMER}\n\n"
        f"- **Domain**: `{summary.get('domain')}`\n"
        f"- **Total Findings**: `{summary.get('total_findings')}`\n"
        f"- **Critical Count**: `{summary.get('critical_count')}`\n"
        f"- **High Count**: `{summary.get('high_count')}`\n"
        f"- **Manual Review Required Count**: `{summary.get('manual_review_count')}`\n"
        f"- **Status**: `{summary.get('status')}`\n\n"
        f"## Findings Registry\n\n{_df_to_markdown(df)}\n"
    )


def build_backtest_governance_readiness_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    return (
        f"# Phase 150: Backtest Governance Readiness Scoring Report\n\n"
        f"> **Disclaimer**: {BACKTEST_GOVERNANCE_REPORT_DISCLAIMER}\n\n"
        f"- **Domain**: `{summary.get('domain')}`\n"
        f"- **Score**: `{summary.get('score')}`\n"
        f"- **Classification**: `{summary.get('classification')}`\n"
        f"- **Meets Threshold**: `{summary.get('meets_threshold')}`\n"
        f"- **Broker Ready**: `{summary.get('broker_ready')}`\n"
        f"- **Production Ready**: `{summary.get('production_ready')}`\n"
        f"- **Live Trading Ready**: `{summary.get('live_trading_ready')}`\n"
        f"- **Official Approval**: `{summary.get('official_approval')}`\n"
        f"- **Status**: `{summary.get('status')}`\n\n"
        f"## Readiness Metrics\n\n{_df_to_markdown(df)}\n"
    )


def build_backtest_governance_manifest_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    return (
        f"# Phase 150: Backtest Governance Manifest Report\n\n"
        f"> **Disclaimer**: {BACKTEST_GOVERNANCE_REPORT_DISCLAIMER}\n\n"
        f"- **Domain**: `{summary.get('domain')}`\n"
        f"- **Manifest ID**: `{summary.get('manifest_id')}`\n"
        f"- **Current Phase**: `{summary.get('current_phase')}`\n"
        f"- **Next Phase**: `{summary.get('next_phase')}`\n"
        f"- **All Negative Invariants Satisfied**: `{summary.get('all_negative_invariants_satisfied')}`\n"
        f"- **Phase 151 Handoff Ready**: `{summary.get('phase_151_handoff_ready')}`\n"
        f"- **Status**: `{summary.get('status')}`\n\n"
        f"## Manifest Entries\n\n{_df_to_markdown(df)}\n"
    )


def build_backtest_governance_health_markdown_report(summary: Dict[str, Any]) -> str:
    checks = summary.get("checks", {})
    checks_md = "\n".join([f"- **{k}**: `{v}`" for k, v in checks.items()])
    return (
        f"# Phase 150: Backtest Governance Health Check Report\n\n"
        f"> **Disclaimer**: {BACKTEST_GOVERNANCE_REPORT_DISCLAIMER}\n\n"
        f"- **Overall Health**: `{summary.get('overall_health')}`\n"
        f"- **Profile Name**: `{summary.get('profile_name')}`\n"
        f"- **Current Phase**: `{summary.get('current_phase')}`\n"
        f"- **All Checks Passed**: `{summary.get('all_checks_passed')}`\n\n"
        f"## Detailed Invariant Checks\n\n{checks_md}\n"
    )


def build_backtest_governance_validation_markdown_report(summary: Dict[str, Any]) -> str:
    checks = summary.get("validations", {})
    checks_md = "\n".join([f"- **{k}**: `{v}`" for k, v in checks.items()])
    return (
        f"# Phase 150: Backtest Governance Validation Report\n\n"
        f"> **Disclaimer**: {BACKTEST_GOVERNANCE_REPORT_DISCLAIMER}\n\n"
        f"- **Validation Status**: `{summary.get('validation_status')}`\n"
        f"- **Profile Name**: `{summary.get('profile_name')}`\n"
        f"- **Current Phase**: `{summary.get('current_phase')}`\n"
        f"- **All Validations Passed**: `{summary.get('all_validations_passed')}`\n\n"
        f"## Validation Results\n\n{checks_md}\n"
    )


def build_phase_151_handoff_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    return (
        f"# Phase 150 -> Phase 151: Benchmark Comparison and Strategy Evaluation Handoff Report\n\n"
        f"> **Disclaimer**: {BACKTEST_GOVERNANCE_REPORT_DISCLAIMER}\n\n"
        f"- **Source Phase**: `{summary.get('source_phase')}`\n"
        f"- **Next Phase**: `{summary.get('next_phase')}` (`{summary.get('next_phase_name')}`)\n"
        f"- **Total Prerequisites**: `{summary.get('total_prerequisites')}`\n"
        f"- **All Prerequisites Satisfied**: `{summary.get('all_prerequisites_satisfied')}`\n"
        f"- **Status**: `{summary.get('status')}`\n\n"
        f"## Handoff Prerequisites\n\n{_df_to_markdown(df)}\n"
    )


def build_backtest_governance_pipeline_markdown_report(pipeline_result: Dict[str, Any]) -> str:
    profile = pipeline_result.get("profile", {})
    summary = pipeline_result.get("summary", {})
    return (
        f"# Phase 150: Backtest Governance Master Pipeline Report\n\n"
        f"> **Disclaimer**: {BACKTEST_GOVERNANCE_REPORT_DISCLAIMER}\n\n"
        f"## Pipeline Execution Summary\n\n"
        f"- **Active Profile**: `{profile.get('profile_name', 'unknown')}`\n"
        f"- **Current Phase**: `{profile.get('current_phase', 150)}`\n"
        f"- **Pipeline Status**: `{pipeline_result.get('status', 'unknown')}`\n"
        f"- **Readiness Score**: `{summary.get('readiness_score', {}).get('score', 0.0)}` "
        f"(`{summary.get('readiness_score', {}).get('classification', 'unknown')}`)\n"
        f"- **Phase 151 Handoff Ready**: `{summary.get('handoff', {}).get('phase_151_handoff_ready', True)}`\n"
        f"- **Local Research Only**: `{profile.get('local_only', True)}`\n"
        f"- **Zero Live Trading**: `{not profile.get('allow_live_trading', False)}`\n"
    )
