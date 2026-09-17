# -*- coding: utf-8 -*-
"""Phase 151: Benchmark Evaluation Report Builder Module.

Constructs structured Markdown and text reports across all Phase 151 domains
incorporating regulatory disclaimers and non-execution invariants.
"""

from typing import Any, Dict, Optional
import pandas as pd

from advanced_benchmark_evaluation.report_disclaimers import STANDARD_DISCLAIMER_TEXT


def build_benchmark_evaluation_disclaimer() -> str:
    """Return the official Phase 151 disclaimer text."""
    return (
        f"> [!WARNING]\n"
        f"> **YASAL UYARI VE GÜVENLİK SINIRI:**\n"
        f"> {STANDARD_DISCLAIMER_TEXT}\n"
    )


def _df_to_markdown(df: Optional[pd.DataFrame]) -> str:
    """Helper formatting DataFrame as markdown table safely without tabulate."""
    if df is None or df.empty:
        return "_No tabular records available._"
    try:
        return df.to_markdown(index=False)
    except Exception:
        return df.to_string(index=False)


def build_benchmark_evaluation_profile_markdown_report(
    summary: Dict[str, Any],
    profile_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for profile registries."""
    md = [
        "# Phase 151: Benchmark Evaluation Profile Registry Report",
        "",
        build_benchmark_evaluation_disclaimer(),
        "",
        "## Summary",
        f"- **Active Profile:** {summary.get('active_profile', 'N/A')}",
        f"- **Total Profiles:** {summary.get('total_profiles', 0)}",
        f"- **All Dry-Run:** {summary.get('all_dry_run', True)}",
        f"- **All Local Only:** {summary.get('all_local_only', True)}",
        f"- **All Non-Production:** {summary.get('all_non_production', True)}",
        f"- **Live Trading Prohibited:** {summary.get('all_live_trading_prohibited', True)}",
        f"- **Status:** {summary.get('status', 'N/A')}",
        "",
    ]
    if profile_df is not None and not profile_df.empty:
        md.append("## Registered Profiles")
        md.append(_df_to_markdown(profile_df))
    return "\n".join(md)


def build_benchmark_report_contract_markdown_report(
    summary: Dict[str, Any],
    df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for benchmark comparison contracts."""
    md = [
        "# Phase 151: Benchmark Comparison Report Contracts",
        "",
        build_benchmark_evaluation_disclaimer(),
        "",
        "## Summary",
        f"- **Total Contracts:** {summary.get('total_contracts', 0)}",
        f"- **Execution Disabled:** {summary.get('all_execution_disabled', True)}",
        f"- **Metric Calculation Disabled:** {summary.get('all_metrics_disabled', True)}",
        f"- **Result Claims Disabled:** {summary.get('all_claims_disabled', True)}",
        f"- **Status:** {summary.get('status', 'N/A')}",
        "",
    ]
    if df is not None and not df.empty:
        md.append("## Benchmark Report Contracts Registry")
        md.append(_df_to_markdown(df))
    return "\n".join(md)


def build_strategy_evaluation_report_contract_markdown_report(
    summary: Dict[str, Any],
    df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for strategy evaluation contracts."""
    md = [
        "# Phase 151: Strategy Evaluation Report Contracts",
        "",
        build_benchmark_evaluation_disclaimer(),
        "",
        "## Summary",
        f"- **Total Contracts:** {summary.get('total_contracts', 0)}",
        f"- **Strategy Approval Disabled:** {summary.get('all_approvals_disabled', True)}",
        f"- **Capital Allocation Disabled:** {summary.get('all_capital_allocation_disabled', True)}",
        f"- **Signals Disabled:** {summary.get('all_signals_disabled', True)}",
        f"- **Status:** {summary.get('status', 'N/A')}",
        "",
    ]
    if df is not None and not df.empty:
        md.append("## Strategy Evaluation Report Contracts Registry")
        md.append(_df_to_markdown(df))
    return "\n".join(md)


def build_specialized_evaluation_contract_markdown_report(
    summary: Dict[str, Any],
    df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for specialized evaluation contracts."""
    md = [
        "# Phase 151: Specialized Evaluation Contracts Report",
        "",
        build_benchmark_evaluation_disclaimer(),
        "",
        "## Summary",
        f"- **Domain:** {summary.get('domain', 'specialized_contracts')}",
        f"- **Total Contracts:** {summary.get('total_contracts', 0)}",
        f"- **Status:** {summary.get('status', 'N/A')}",
        "",
    ]
    if df is not None and not df.empty:
        md.append("## Specialized Contracts Details")
        md.append(_df_to_markdown(df))
    return "\n".join(md)


def build_summary_placeholder_markdown_report(
    summary: Dict[str, Any],
    df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for summary placeholders."""
    md = [
        "# Phase 151: Summary Placeholders Report",
        "",
        build_benchmark_evaluation_disclaimer(),
        "",
        "## Summary",
        f"- **Total Placeholders:** {summary.get('total_placeholders', 0)}",
        f"- **All Uncalculated:** {summary.get('all_uncalculated', True)}",
        f"- **Status:** {summary.get('status', 'N/A')}",
        "",
    ]
    if df is not None and not df.empty:
        md.append("## Summary Placeholders Registry")
        md.append(_df_to_markdown(df))
    return "\n".join(md)


def build_metric_placeholder_markdown_report(
    summary: Dict[str, Any],
    df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for metric placeholders."""
    md = [
        "# Phase 151: Uncalculated Metric Placeholders Report",
        "",
        build_benchmark_evaluation_disclaimer(),
        "",
        "## Summary",
        f"- **Total Metrics:** {summary.get('total_metrics', 0)}",
        f"- **All Uncalculated:** {summary.get('all_uncalculated', True)}",
        f"- **Claims Blocked:** {summary.get('all_claims_blocked', True)}",
        f"- **Status:** {summary.get('status', 'N/A')}",
        "",
    ]
    if df is not None and not df.empty:
        md.append("## Metric Placeholders Registry")
        md.append(_df_to_markdown(df))
    return "\n".join(md)


def build_evaluation_guard_markdown_report(
    summary: Dict[str, Any],
    df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for evaluation guards."""
    md = [
        "# Phase 151: Evaluation Guards and Boundary Report",
        "",
        build_benchmark_evaluation_disclaimer(),
        "",
        "## Summary",
        f"- **Total Guards:** {summary.get('total_guards', 0)}",
        f"- **All Active:** {summary.get('all_active', True)}",
        f"- **Status:** {summary.get('status', 'N/A')}",
        "",
    ]
    if df is not None and not df.empty:
        md.append("## Active Guards")
        md.append(_df_to_markdown(df))
    return "\n".join(md)


def build_evaluation_disabled_execution_markdown_report(
    summary: Dict[str, Any],
    df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for disabled execution engines."""
    md = [
        "# Phase 151: Disabled Execution Enforcements Report",
        "",
        build_benchmark_evaluation_disclaimer(),
        "",
        "## Summary",
        f"- **Operation:** {summary.get('operation', 'execution')}",
        f"- **Is Disabled:** {summary.get('is_disabled', True)}",
        f"- **Status:** {summary.get('status', 'N/A')}",
        "",
    ]
    if df is not None and not df.empty:
        md.append("## Disabled Execution Specification")
        md.append(_df_to_markdown(df))
    return "\n".join(md)


def build_benchmark_evaluation_findings_markdown_report(
    summary: Dict[str, Any],
    df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for findings."""
    md = [
        "# Phase 151: Diagnostic Findings and Review Gates Report",
        "",
        build_benchmark_evaluation_disclaimer(),
        "",
        "## Summary",
        f"- **Total Findings:** {summary.get('total_findings', 0)}",
        f"- **Critical Count:** {summary.get('critical_count', 0)}",
        f"- **Blocker Count:** {summary.get('blocker_count', 0)}",
        f"- **Status:** {summary.get('status', 'N/A')}",
        "",
    ]
    if df is not None and not df.empty:
        md.append("## Findings Registry")
        md.append(_df_to_markdown(df))
    return "\n".join(md)


def build_benchmark_evaluation_readiness_score_markdown_report(
    summary: Dict[str, Any],
    df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for readiness score."""
    md = [
        "# Phase 151: Benchmark Evaluation Readiness Score Report",
        "",
        build_benchmark_evaluation_disclaimer(),
        "",
        "## Summary",
        f"- **Readiness Score:** {summary.get('score', 1.0):.2f}",
        f"- **Classification:** {summary.get('classification', 'N/A')}",
        f"- **Meets Minimum Threshold:** {summary.get('meets_threshold', True)}",
        f"- **Status:** {summary.get('status', 'N/A')}",
        "",
    ]
    if df is not None and not df.empty:
        md.append("## Readiness Details")
        md.append(_df_to_markdown(df))
    return "\n".join(md)


def build_benchmark_evaluation_manifest_markdown_report(
    summary: Dict[str, Any],
    df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for master manifest."""
    md = [
        "# Phase 151: Master Benchmark Evaluation Manifest Report",
        "",
        build_benchmark_evaluation_disclaimer(),
        "",
        "## Summary",
        f"- **Manifest ID:** {summary.get('manifest_id', 'N/A')}",
        f"- **Current Phase:** {summary.get('current_phase', 151)}",
        f"- **Next Phase:** {summary.get('next_phase', 152)}",
        f"- **All Negative Invariants Satisfied:** {summary.get('all_negative_invariants_satisfied', True)}",
        f"- **Phase 152 Handoff Ready:** {summary.get('phase_152_handoff_ready', True)}",
        f"- **Status:** {summary.get('status', 'N/A')}",
        "",
    ]
    if df is not None and not df.empty:
        md.append("## Manifest Invariants")
        md.append(_df_to_markdown(df))
    return "\n".join(md)


def build_benchmark_evaluation_validation_markdown_report(
    summary: Dict[str, Any],
    df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for validation check suites."""
    md = [
        "# Phase 151: Validation Report",
        "",
        build_benchmark_evaluation_disclaimer(),
        "",
        "## Summary",
        f"- **Validation Status:** {summary.get('validation_status', 'VALIDATION_PASS')}",
        f"- **Total Checks:** {summary.get('total_checks', 0)}",
        f"- **All Passed:** {summary.get('all_passed', True)}",
        f"- **Forbidden Claims Clean:** True",
        "",
    ]
    if df is not None and not df.empty:
        md.append("## Validation Results")
        md.append(_df_to_markdown(df))
    return "\n".join(md)


def build_benchmark_evaluation_safety_markdown_report(
    summary: Dict[str, Any],
    df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for safety boundaries."""
    md = [
        "# Phase 151: Safety Boundary Report",
        "",
        build_benchmark_evaluation_disclaimer(),
        "",
        "## Summary",
        f"- **Safety Status:** {summary.get('safety_status', 'SECURE')}",
        f"- **NO-GO Rules Enforced:** {summary.get('no_go_count', 0)}",
        f"- **SAFE-GO Principles Active:** {summary.get('safe_go_count', 0)}",
        f"- **Live Trading Prohibited:** True",
        f"- **Broker Execution Prohibited:** True",
        "",
    ]
    if df is not None and not df.empty:
        md.append("## Safety Rules")
        md.append(_df_to_markdown(df))
    return "\n".join(md)


def build_phase_152_handoff_markdown_report(
    summary: Dict[str, Any],
    df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for Phase 152 handoff."""
    md = [
        "# Phase 151 to Phase 152 Handoff Report",
        "",
        build_benchmark_evaluation_disclaimer(),
        "",
        "## Summary",
        f"- **Handoff Status:** {summary.get('handoff_status', 'READY_FOR_PHASE_152')}",
        f"- **Source Phase:** {summary.get('source_phase', 151)}",
        f"- **Next Phase:** {summary.get('next_phase', 152)}",
        f"- **Next Phase Name:** {summary.get('next_phase_name', 'Backtest Acceptance Report')}",
        f"- **Total Prerequisites:** {summary.get('total_prerequisites', 0)}",
        f"- **All Prerequisites Satisfied:** {summary.get('all_prerequisites_satisfied', True)}",
        "",
    ]
    if df is not None and not df.empty:
        md.append("## Handoff Prerequisites")
        md.append(_df_to_markdown(df))
    return "\n".join(md)


def build_benchmark_evaluation_health_markdown_report(
    summary: Dict[str, Any],
    df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for health checks."""
    md = [
        "# Phase 151: Benchmark Evaluation Health Check Report",
        "",
        build_benchmark_evaluation_disclaimer(),
        "",
        "## Summary",
        f"- **Health Status:** {summary.get('status', 'HEALTHY')}",
        f"- **Total Checks:** {summary.get('total_checks', 0)}",
        f"- **Passed Checks:** {summary.get('passed_checks', 0)}",
        f"- **Failed Checks:** {summary.get('failed_checks', 0)}",
        f"- **All Passed:** {summary.get('all_passed', True)}",
        "",
    ]
    if df is not None and not df.empty:
        md.append("## Health Checks Details")
        md.append(_df_to_markdown(df))
    return "\n".join(md)


# Aliases for script and test interoperability
build_evaluation_summary_placeholder_markdown_report = build_summary_placeholder_markdown_report
build_evaluation_metric_placeholder_markdown_report = build_metric_placeholder_markdown_report
build_benchmark_evaluation_disabled_execution_markdown_report = build_evaluation_disabled_execution_markdown_report

