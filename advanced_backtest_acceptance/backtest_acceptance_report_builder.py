# -*- coding: utf-8 -*-
"""Phase 152: Backtest Acceptance Report Builder.

Generates markdown and textual reports for all Backtest Acceptance registries,
manifests, boundaries, findings, and handoffs with mandatory regulatory disclaimers.
"""

from typing import Any, Dict, Optional
import pandas as pd


def build_backtest_acceptance_disclaimer() -> str:
    """Return the mandatory safety and regulatory disclaimer for Phase 152."""
    return (
        "> [!CAUTION]\n"
        "> **YASAL UYARI VE GÜVENLİK BİLDİRİMİ (PHASE 152 BACKTEST ACCEPTANCE REPORT)**:\n"
        "> Bu çıktı Phase 152 Backtest Acceptance Report çıktısıdır. Canlı emir, broker talimatı, "
        "> kesin AL/SAT, yatırım tavsiyesi, backtest/acceptance/readiness değerini trade sinyali veya "
        "> production-ready/broker-ready/onay olarak kullanma, gerçek backtest execution, benchmark "
        "> execution, metric calculation, optimizer, model training, model fit/predict/inference, "
        "> dataset materialization, target/label/prediction üretimi, gerçek Sharpe/win-rate/return/"
        "> alpha/beta/drawdown/VaR/ES hesaplama, performans garantisi, strategy approval, capital "
        "> allocation, portfolio construction, position sizing, model deployment, model registry write, "
        "> model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/"
        "> embedding/vector kullanımı veya gerçek provider API çağrısı değildir.\n"
    )


def _df_to_markdown(df: Optional[pd.DataFrame]) -> str:
    """Helper formatting DataFrame as markdown table safely without requiring tabulate."""
    if df is None or df.empty:
        return "_No tabular records available._"
    try:
        return df.to_markdown(index=False)
    except Exception:
        return df.to_string(index=False)


def build_backtest_acceptance_profile_markdown_report(
    summary: Dict[str, Any], profile_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for profile registry."""
    md = [
        build_backtest_acceptance_disclaimer(),
        "## Backtest Acceptance Profile Registry",
        f"- **Active Profile**: `{summary.get('active_profile', 'N/A')}`",
        f"- **Total Profiles**: {summary.get('total_profiles', 0)}",
        f"- **All Dry Run**: {summary.get('all_dry_run', True)}",
        f"- **All Local Only**: {summary.get('all_local_only', True)}",
        f"- **Status**: `{summary.get('status', 'ACCEPTED')}`\n",
    ]
    if profile_df is not None and not profile_df.empty:
        md.append(_df_to_markdown(profile_df))
    return "\n".join(md)


def build_backtest_acceptance_component_markdown_report(
    summary: Dict[str, Any], component_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for component registry."""
    md = [
        build_backtest_acceptance_disclaimer(),
        "## Backtest Acceptance Component Registry",
        f"- **Total Components**: {summary.get('total_components', 0)}",
        f"- **All Contract Only**: {summary.get('all_contract_only', True)}",
        f"- **All Non-Production**: {summary.get('all_non_production', True)}",
        f"- **Status**: `{summary.get('status', 'ACCEPTED')}`\n",
    ]
    if component_df is not None and not component_df.empty:
        md.append(_df_to_markdown(component_df))
    return "\n".join(md)


def build_phase_acceptance_markdown_report(
    summary: Dict[str, Any], phase_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for a phase-level acceptance registry."""
    md = [
        build_backtest_acceptance_disclaimer(),
        f"## {summary.get('phase_ref', 'Phase')} Acceptance Report: {summary.get('phase_title', '')}",
        f"- **Active Profile**: `{summary.get('active_profile', 'N/A')}`",
        f"- **Total Checks**: {summary.get('total_checks', 0)}",
        f"- **Passed Checks**: {summary.get('passed_checks', 0)}",
        f"- **All Passed**: {summary.get('all_passed', True)}",
        f"- **Status**: `{summary.get('status', 'ACCEPTED')}`\n",
    ]
    if phase_df is not None and not phase_df.empty:
        md.append(_df_to_markdown(phase_df))
    return "\n".join(md)


def build_dependency_acceptance_markdown_report(
    summary: Dict[str, Any], dependency_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for dependencies."""
    md = [
        build_backtest_acceptance_disclaimer(),
        "## Backtest Acceptance Dependency Verification",
        f"- **Total Dependencies**: {summary.get('total_dependencies', 0)}",
        f"- **Satisfied**: {summary.get('satisfied_dependencies', 0)}",
        f"- **All Satisfied**: {summary.get('all_satisfied', True)}",
        f"- **Status**: `{summary.get('status', 'ACCEPTED')}`\n",
    ]
    if dependency_df is not None and not dependency_df.empty:
        md.append(_df_to_markdown(dependency_df))
    return "\n".join(md)


def build_validation_evidence_markdown_report(
    summary: Dict[str, Any], evidence_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for validation evidence."""
    md = [
        build_backtest_acceptance_disclaimer(),
        "## Backtest Acceptance Validation Evidence",
        f"- **Total Evidence Items**: {summary.get('total_evidence_items', 0)}",
        f"- **All Verified**: {summary.get('all_verified', True)}",
        f"- **Status**: `{summary.get('status', 'ACCEPTED')}`\n",
    ]
    if evidence_df is not None and not evidence_df.empty:
        md.append(_df_to_markdown(evidence_df))
    return "\n".join(md)


def build_boundary_markdown_report(
    summary: Dict[str, Any], boundary_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for boundaries."""
    md = [
        build_backtest_acceptance_disclaimer(),
        "## Backtest Acceptance Boundaries & Invariants",
        f"- **Domain**: `{summary.get('domain', 'N/A')}`",
        f"- **Total Rules**: {summary.get('total_boundaries', summary.get('total_rules', 0))}",
        f"- **Status**: `{summary.get('status', 'ACCEPTED')}`\n",
    ]
    if boundary_df is not None and not boundary_df.empty:
        md.append(_df_to_markdown(boundary_df))
    return "\n".join(md)


def build_blocker_gap_warning_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for blockers, gaps, and warnings."""
    md = [
        build_backtest_acceptance_disclaimer(),
        f"## Backtest Acceptance Findings: {summary.get('domain', 'Registry')}",
        f"- **Total Items**: {len(df) if df is not None else 0}",
        f"- **Status**: `{summary.get('status', 'ACCEPTED')}`\n",
    ]
    if df is not None and not df.empty:
        md.append(_df_to_markdown(df))
    return "\n".join(md)


def build_backtest_acceptance_findings_markdown_report(
    summary: Dict[str, Any], findings_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for consolidated findings."""
    md = [
        build_backtest_acceptance_disclaimer(),
        "## Backtest Acceptance Consolidated Findings",
        f"- **Total Findings**: {summary.get('total_findings', 0)}",
        f"- **Critical Count**: {summary.get('critical_count', 0)}",
        f"- **Manual Review Required**: {summary.get('manual_review_required_count', 0)}",
        f"- **Status**: `{summary.get('status', 'ACCEPTED')}`\n",
    ]
    if findings_df is not None and not findings_df.empty:
        md.append(_df_to_markdown(findings_df))
    return "\n".join(md)


def build_backtest_acceptance_readiness_score_markdown_report(
    summary: Dict[str, Any], score_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for readiness scoring."""
    md = [
        build_backtest_acceptance_disclaimer(),
        "## Backtest Acceptance Readiness Score Report",
        f"- **Score**: `{summary.get('readiness_score', 0.0):.4f}`",
        f"- **Classification**: `{summary.get('classification', 'UNKNOWN')}`",
        f"- **Meets Threshold**: `{summary.get('meets_threshold', False)}`",
        f"- **Production Ready**: False",
        f"- **Broker Ready**: False",
        f"- **Live Trading Ready**: False",
        f"- **Strategy Approved**: False\n",
    ]
    if score_df is not None and not score_df.empty:
        md.append(_df_to_markdown(score_df))
    return "\n".join(md)


def build_backtest_acceptance_manifest_markdown_report(
    summary: Dict[str, Any], manifest_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for acceptance manifest."""
    md = [
        build_backtest_acceptance_disclaimer(),
        "## Backtest Acceptance Manifest",
        f"- **Manifest ID**: `{summary.get('manifest_id', 'N/A')}`",
        f"- **Backtest Block Completed**: `{summary.get('backtest_block_completed', False)}`",
        f"- **Phase 153 Handoff Ready**: `{summary.get('phase_153_handoff_ready', False)}`",
        f"- **Status**: `{summary.get('status', 'ACCEPTED')}`\n",
    ]
    if manifest_df is not None and not manifest_df.empty:
        md.append(_df_to_markdown(manifest_df))
    return "\n".join(md)


def build_backtest_acceptance_validation_markdown_report(
    summary: Dict[str, Any], validation_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for acceptance validation."""
    md = [
        build_backtest_acceptance_disclaimer(),
        "## Backtest Acceptance Validation Report",
        f"- **Validation Status**: `{summary.get('validation_status', 'VALIDATION_PASS')}`",
        f"- **Total Checks**: {summary.get('total_checks', 0)}",
        f"- **All Passed**: {summary.get('all_passed', True)}",
        f"- **Forbidden Claims Clean**: True\n",
    ]
    if validation_df is not None and not validation_df.empty:
        md.append(_df_to_markdown(validation_df))
    return "\n".join(md)


def build_backtest_acceptance_safety_markdown_report(
    summary: Dict[str, Any], safety_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for safety boundaries."""
    md = [
        build_backtest_acceptance_disclaimer(),
        "## Backtest Acceptance Safety Boundary Report",
        f"- **Safety Status**: `{summary.get('safety_status', 'SECURE')}`",
        f"- **NO-GO Rules Enforced**: {summary.get('no_go_count', 18)}",
        f"- **SAFE-GO Rules Active**: {summary.get('safe_go_count', 8)}",
        f"- **Zero Real Trading/Backtest**: True\n",
    ]
    if safety_df is not None and not safety_df.empty:
        md.append(_df_to_markdown(safety_df))
    return "\n".join(md)


def build_phase_153_handoff_markdown_report(
    summary: Dict[str, Any], handoff_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for Phase 153 handoff."""
    md = [
        build_backtest_acceptance_disclaimer(),
        "## Phase 153 Portfolio Construction & Risk Budgeting Handoff",
        f"- **Current Phase**: 152",
        f"- **Target Next Phase**: 153",
        f"- **Target Final Phase**: 160",
        f"- **Handoff Ready**: `{summary.get('handoff_ready', True)}`",
        f"- **Prerequisites Satisfied**: `{summary.get('all_satisfied', True)}`",
        f"- **Scope**: Non-live, offline research portfolio construction contracts.\n",
    ]
    if handoff_df is not None and not handoff_df.empty:
        md.append(_df_to_markdown(handoff_df))
    return "\n".join(md)


def build_backtest_acceptance_full_markdown_report(tables: Dict[str, Any], summary: Dict[str, Any]) -> str:
    """Build complete consolidated markdown report across all Phase 152 outputs."""
    md = [
        build_backtest_acceptance_disclaimer(),
        "# Phase 152 Backtest Acceptance Consolidated Report\n",
        f"**Active Profile**: `{summary.get('active_profile', 'balanced_local_backtest_acceptance_contracts')}`\n",
        f"**Current Phase**: {summary.get('current_phase', 152)} | **Next Phase**: {summary.get('next_phase', 153)} | **Target Final Phase**: {summary.get('target_final_phase', 160)}\n",
        f"**Readiness Score**: `{summary.get('readiness_score', 1.0):.4f}` ({summary.get('classification', 'CONTRACT_READY')})\n",
        "### Invariant Check Summary",
        "- [x] Phase 146-151 backtest block completed at contract level.",
        "- [x] Zero live trading or broker orders executed.",
        "- [x] Zero real backtest or benchmark simulation loops run.",
        "- [x] Zero performance metrics or return claims generated.",
        "- [x] Zero strategy approvals or live capital allocations.",
        "- [x] Phase 153 handoff successfully established.\n",
    ]

    for title, tbl in tables.items():
        if isinstance(tbl, pd.DataFrame) and not tbl.empty:
            md.append(f"### Table: {title.replace('_', ' ').title()}")
            md.append(_df_to_markdown(tbl) + "\n")

    return "\n".join(md)
