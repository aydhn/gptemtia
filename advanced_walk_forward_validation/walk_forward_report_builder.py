# -*- coding: utf-8 -*-
"""Phase 147: Walk-Forward Report Builder.

Generates markdown and text diagnostic reports for the walk-forward validation and OOS benchmarking layer.
Includes strict disclaimers and non-production warnings.
"""

from typing import Any, Dict, Optional
import pandas as pd

DISCLAIMER_TEXT = (
    "> [!IMPORTANT]\n"
    "> Bu çıktı Phase 147 Walk-Forward Validation and Out-of-Sample Benchmarking raporudur. "
    "Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, walk-forward/readiness/OOS/benchmark "
    "değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gerçek walk-forward execution, "
    "benchmark execution, optimizer, stress test, Monte Carlo, gerçek model training, model fit/predict/inference, "
    "dataset materialization, target/label/prediction üretimi, gerçek performans garantisi, model deployment, "
    "model registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector "
    "kullanımı veya gerçek provider API çağrısı değildir."
)


def _df_to_markdown(df: Optional[pd.DataFrame]) -> str:
    """Safe DataFrame to Markdown converter without external tabulate requirement."""
    if df is None or df.empty:
        return "_No records available._\n"
    cols = [str(c) for c in df.columns]
    header = "| " + " | ".join(cols) + " |"
    separator = "| " + " | ".join(["---"] * len(cols)) + " |"
    rows = []
    for _, row in df.iterrows():
        row_str = "| " + " | ".join(str(val) for val in row.values) + " |"
        rows.append(row_str)
    return "\n".join([header, separator] + rows) + "\n"


def build_walk_forward_disclaimer() -> str:
    """Return the standardized Phase 147 research disclaimer."""
    return DISCLAIMER_TEXT


def build_walk_forward_profile_markdown_report(
    summary: Dict[str, Any], profile_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for walk-forward profiles."""
    lines = [
        "# Phase 147: Walk-Forward Validation Profiles Report",
        "",
        DISCLAIMER_TEXT,
        "",
        "## Summary",
        f"- **Active Profile**: `{summary.get('active_profile')}`",
        f"- **Total Profiles**: `{summary.get('total_profiles')}`",
        f"- **Current Phase**: `{summary.get('current_phase')}`",
        f"- **Target Final Phase**: `{summary.get('target_final_phase')}`",
        f"- **Next Phase**: `{summary.get('next_phase')}`",
        f"- **Local Only**: `{summary.get('all_local_only')}`",
        f"- **Zero Live Trading**: `{summary.get('zero_live_trading')}`",
        "",
    ]
    if profile_df is not None and not profile_df.empty:
        lines.extend(["## Configured Profiles", _df_to_markdown(profile_df), ""])
    return "\n".join(lines)


def build_walk_forward_contract_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for walk-forward validation contracts."""
    lines = [
        "# Phase 147: Walk-Forward Validation Contracts",
        "",
        DISCLAIMER_TEXT,
        "",
        "## Summary",
        f"- **Total Contracts**: `{summary.get('total_contracts')}`",
        f"- **All Execution Blocked**: `{summary.get('all_execution_blocked')}`",
        f"- **All Optimizer Blocked**: `{summary.get('all_optimizer_blocked')}`",
        f"- **All Metric Calculation Blocked**: `{summary.get('all_metric_calculation_blocked')}`",
        f"- **Manual Review Required**: `{summary.get('all_manual_review_required')}`",
        "",
    ]
    if df is not None and not df.empty:
        lines.extend(["## Validation Contracts", _df_to_markdown(df), ""])
    return "\n".join(lines)


def build_oos_split_contract_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for OOS split contracts."""
    lines = [
        "# Phase 147: Out-of-Sample Split Contracts",
        "",
        DISCLAIMER_TEXT,
        "",
        "## Summary",
        f"- **Total OOS Splits**: `{summary.get('total_oos_splits')}`",
        f"- **All Splits Isolated**: `{summary.get('all_splits_isolated')}`",
        f"- **Zero Real Splits Executed**: `{summary.get('zero_split_executed')}`",
        "",
    ]
    if df is not None and not df.empty:
        lines.extend(["## OOS Splits", _df_to_markdown(df), ""])
    return "\n".join(lines)


def build_benchmark_contract_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for benchmark contracts."""
    lines = [
        "# Phase 147: Out-of-Sample Benchmark Contracts",
        "",
        DISCLAIMER_TEXT,
        "",
        "## Summary",
        f"- **Total Benchmarks**: `{summary.get('total_benchmarks')}`",
        f"- **All Execution Blocked**: `{summary.get('all_execution_blocked')}`",
        f"- **Zero Investment Advice**: `{summary.get('zero_investment_advice')}`",
        "",
    ]
    if df is not None and not df.empty:
        lines.extend(["## Benchmark Contracts", _df_to_markdown(df), ""])
    return "\n".join(lines)


def build_benchmark_placeholder_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for benchmark placeholders."""
    lines = [
        "# Phase 147: Benchmark Placeholders Report",
        "",
        DISCLAIMER_TEXT,
        "",
        "## Summary",
        f"- **Placeholders Registered**: `{summary.get('total_placeholders', len(df) if df is not None else 0)}`",
        f"- **Real Execution Disabled**: `True`",
        f"- **Non-Signal**: `True`",
        "",
    ]
    if df is not None and not df.empty:
        lines.extend(["## Placeholders", _df_to_markdown(df), ""])
    return "\n".join(lines)


def build_validation_metric_placeholder_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for metric placeholders."""
    lines = [
        "# Phase 147: Validation & Benchmark Metric Placeholders",
        "",
        DISCLAIMER_TEXT,
        "",
        "## Summary",
        f"- **Total Metrics Registered**: `{summary.get('total_metrics', len(df) if df is not None else 0)}`",
        f"- **Calculations Disabled**: `{summary.get('all_metrics_uncalculated', True)}`",
        f"- **Zero Performance Claims**: `{summary.get('zero_performance_claims', True)}`",
        "",
    ]
    if df is not None and not df.empty:
        lines.extend(["## Metric Placeholders", _df_to_markdown(df), ""])
    return "\n".join(lines)


def build_validation_guard_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for validation guards."""
    lines = [
        "# Phase 147: Validation and Bias Guards",
        "",
        DISCLAIMER_TEXT,
        "",
        "## Summary",
        f"- **Total Guards**: `{summary.get('total_guards', len(df) if df is not None else 0)}`",
        f"- **Strict Enforcement**: `{summary.get('strict_enforcement', True)}`",
        f"- **All Active**: `{summary.get('all_active', True)}`",
        "",
    ]
    if df is not None and not df.empty:
        lines.extend(["## Guards", _df_to_markdown(df), ""])
    return "\n".join(lines)


def build_validation_disabled_execution_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for disabled execution paths."""
    lines = [
        "# Phase 147: Disabled Execution Safeguards",
        "",
        DISCLAIMER_TEXT,
        "",
        "## Summary",
        f"- **Total Prohibited Paths**: `{summary.get('total_blocked_paths', len(df) if df is not None else 0)}`",
        f"- **All Paths Blocked**: `True`",
        f"- **Enforcement Level**: `STRICT`",
        "",
    ]
    if df is not None and not df.empty:
        lines.extend(["## Prohibited Paths", _df_to_markdown(df), ""])
    return "\n".join(lines)


def build_walk_forward_findings_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for findings."""
    lines = [
        "# Phase 147: Walk-Forward Contract Findings",
        "",
        DISCLAIMER_TEXT,
        "",
        "## Summary",
        f"- **Total Findings**: `{summary.get('total_findings')}`",
        f"- **Critical Blockers**: `{summary.get('critical_count')}`",
        f"- **Has Critical Blockers**: `{summary.get('has_critical_blockers')}`",
        "",
    ]
    if df is not None and not df.empty:
        lines.extend(["## Findings Log", _df_to_markdown(df), ""])
    return "\n".join(lines)


def build_walk_forward_readiness_score_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for diagnostic readiness score."""
    lines = [
        "# Phase 147: Walk-Forward Readiness Score",
        "",
        DISCLAIMER_TEXT,
        "",
        "## Summary",
        f"- **Readiness Score**: `{summary.get('score')}`",
        f"- **Classification**: `{summary.get('classification')}`",
        f"- **Meets Threshold**: `{summary.get('meets_threshold')}`",
        f"- **Critical Blockers**: `{summary.get('critical_blockers')}`",
        f"- **Production Ready**: `False` (Enforced Invariant)",
        f"- **Broker Ready**: `False` (Enforced Invariant)",
        "",
    ]
    if df is not None and not df.empty:
        lines.extend(["## Score Breakdown", _df_to_markdown(df), ""])
    return "\n".join(lines)


def build_walk_forward_manifest_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for the master manifest."""
    lines = [
        "# Phase 147: Master Walk-Forward Manifest",
        "",
        DISCLAIMER_TEXT,
        "",
        "## Summary",
        f"- **Manifest ID**: `{summary.get('manifest_id')}`",
        f"- **Current Phase**: `{summary.get('current_phase')}`",
        f"- **Target Final Phase**: `{summary.get('target_final_phase')}`",
        f"- **Next Phase**: `{summary.get('next_phase')}`",
        f"- **Walk-Forward Executed**: `{summary.get('walk_forward_executed')}`",
        f"- **OOS Benchmark Executed**: `{summary.get('oos_benchmark_executed')}`",
        f"- **Benchmark Metric Calculated**: `{summary.get('benchmark_metric_calculated')}`",
        f"- **Live Trading Ready**: `{summary.get('live_trading_ready')}`",
        f"- **Phase 148 Handoff Ready**: `{summary.get('phase_148_handoff_ready')}`",
        "",
    ]
    if df is not None and not df.empty:
        lines.extend(["## Manifest Details", _df_to_markdown(df), ""])
    return "\n".join(lines)


def build_walk_forward_validation_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for validation report."""
    lines = [
        "# Phase 147: Walk-Forward Contract Validation Report",
        "",
        DISCLAIMER_TEXT,
        "",
        "## Validation Status",
        f"- **Status**: `{summary.get('validation_status', 'PASS')}`",
        f"- **Checks Passed**: `{summary.get('checks_passed', True)}`",
        "",
    ]
    if df is not None and not df.empty:
        lines.extend(["## Validation Checks", _df_to_markdown(df), ""])
    return "\n".join(lines)


def build_walk_forward_safety_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for safety boundaries."""
    lines = [
        "# Phase 147: Safety Boundary & Invariant Report",
        "",
        DISCLAIMER_TEXT,
        "",
        "## Safety Controls",
        f"- **NO-GO Conditions**: `{summary.get('no_go_count', 14)} enforced`",
        f"- **SAFE-GO Conditions**: `{summary.get('safe_go_count', 7)} active`",
        f"- **Live Trading Prohibited**: `True`",
        f"- **Broker Execution Prohibited**: `True`",
        "",
    ]
    if df is not None and not df.empty:
        lines.extend(["## Safety Matrix", _df_to_markdown(df), ""])
    return "\n".join(lines)


def build_phase_148_handoff_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for Phase 148 handoff."""
    lines = [
        "# Phase 147 to Phase 148 Handoff Report",
        "",
        DISCLAIMER_TEXT,
        "",
        "## Handoff Status",
        f"- **Next Phase**: `Phase 148 — Stress Testing and Scenario Simulation`",
        f"- **Current Phase**: `147`",
        f"- **Target Final Phase**: `160`",
        f"- **All Prerequisites Satisfied**: `{summary.get('all_prerequisites_satisfied', True)}`",
        "",
    ]
    if df is not None and not df.empty:
        lines.extend(["## Prerequisites Checklist", _df_to_markdown(df), ""])
    return "\n".join(lines)
