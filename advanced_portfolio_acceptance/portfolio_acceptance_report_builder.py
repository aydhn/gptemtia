# -*- coding: utf-8 -*-
"""Phase 157: Portfolio Acceptance Report Builder.

Generates structured Markdown reports for all acceptance registries, readiness scoring,
manifests, and handoff documentation with strict non-production disclaimers.
"""

from typing import Any, Dict, Optional
import pandas as pd

DISCLAIMER_TEXT = (
    "> [!WARNING]\n"
    "> **YASAL UYARI VE NON-PRODUCTION / RESEARCH-ONLY KURALI**:\n"
    "> Bu çıktı Phase 157 Portfolio Acceptance Report çıktısıdır. Canlı emir, broker talimatı, "
    "> kesin AL/SAT, yatırım tavsiyesi, portfolio/acceptance/readiness değerini trade sinyali veya "
    "> production-ready/broker-ready/onay olarak kullanma, gerçek portfolio construction, position sizing, "
    "> portfolio optimization, allocation generation, rebalance, risk reporting, exposure attribution, "
    "> limit monitoring, scenario execution, drawdown control, portfolio adjustment, hedge/de-risk, "
    "> alerting, dashboard generation, optimizer, model training, model fit/predict/inference, "
    "> dataset materialization, target/label/prediction üretimi, gerçek VaR/ES/exposure/drawdown/risk metric "
    "> hesaplama, performans garantisi, strategy approval, portfolio approval, model deployment, model "
    "> registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/"
    "> scraped HTML/embedding/vector kullanımı veya gerçek provider API çağrısı değildir.\n"
)


def _df_to_markdown(df: Optional[pd.DataFrame]) -> str:
    """Safely format DataFrame as markdown without requiring tabulate."""
    if df is None or df.empty:
        return ""
    try:
        return df.to_markdown(index=False)
    except Exception:
        cols = [str(c) for c in df.columns]
        header = "| " + " | ".join(cols) + " |"
        sep = "| " + " | ".join(["---"] * len(cols)) + " |"
        rows = []
        for _, row in df.iterrows():
            rows.append("| " + " | ".join(str(row[c]) for c in df.columns) + " |")
        return "\n".join([header, sep] + rows)


def build_portfolio_acceptance_disclaimer() -> str:
    """Return the standardized Phase 157 markdown disclaimer."""
    return DISCLAIMER_TEXT


def build_portfolio_acceptance_profile_markdown_report(
    summary: Dict[str, Any],
    profile_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for profile registry."""
    lines = [
        "# Phase 157: Portfolio Acceptance Profile Registry Report",
        "",
        DISCLAIMER_TEXT,
        "",
        f"- **Active Profile**: `{summary.get('active_profile', '')}`",
        f"- **Total Profiles**: `{summary.get('total_profiles', 0)}`",
        f"- **All Dry-Run**: `{summary.get('all_dry_run', True)}`",
        f"- **All Local-Only**: `{summary.get('all_local_only', True)}`",
        f"- **All Non-Production**: `{summary.get('all_non_production', True)}`",
        f"- **Status**: `{summary.get('status', '')}`",
        "",
    ]
    if profile_df is not None and not profile_df.empty:
        lines.append("## Configured Profiles")
        lines.append("")
        lines.append(_df_to_markdown(profile_df))
        lines.append("")
    return "\n".join(lines)


def build_portfolio_acceptance_component_markdown_report(
    summary: Dict[str, Any],
    component_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for component registry."""
    lines = [
        "# Phase 157: Portfolio Acceptance Component Registry Report",
        "",
        DISCLAIMER_TEXT,
        "",
        f"- **Total Components**: `{summary.get('total_components', 0)}`",
        f"- **Phases Covered**: `{summary.get('phases_covered', [])}`",
        f"- **All Contract Only**: `{summary.get('all_contract_only', True)}`",
        f"- **All Non-Production**: `{summary.get('all_non_production', True)}`",
        f"- **None Production-Ready**: `{summary.get('none_production_ready', True)}`",
        f"- **None Broker-Ready**: `{summary.get('none_broker_ready', True)}`",
        f"- **Status**: `{summary.get('status', '')}`",
        "",
    ]
    if component_df is not None and not component_df.empty:
        lines.append("## Registered Portfolio Components")
        lines.append("")
        lines.append(_df_to_markdown(component_df))
        lines.append("")
    return "\n".join(lines)


def build_portfolio_phase_acceptance_markdown_report(
    summary: Dict[str, Any],
    phase_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for individual phase acceptance."""
    p_num = summary.get("phase_number", "All")
    lines = [
        f"# Phase 157: Phase {p_num} Acceptance Evaluation Report",
        "",
        DISCLAIMER_TEXT,
        "",
        f"- **Phase**: `Phase {p_num}`",
        f"- **Total Criteria**: `{summary.get('total_criteria', 0)}`",
        f"- **Satisfied Criteria**: `{summary.get('satisfied_criteria', 0)}`",
        f"- **All Satisfied**: `{summary.get('all_satisfied', True)}`",
        f"- **Status**: `{summary.get('status', '')}`",
        "",
    ]
    if phase_df is not None and not phase_df.empty:
        lines.append("## Phase Acceptance Criteria")
        lines.append("")
        lines.append(_df_to_markdown(phase_df))
        lines.append("")
    return "\n".join(lines)


def build_portfolio_acceptance_dependency_markdown_report(
    summary: Dict[str, Any],
    dependency_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for dependency registry."""
    lines = [
        "# Phase 157: Portfolio Acceptance Dependency Report",
        "",
        DISCLAIMER_TEXT,
        "",
        f"- **Total Dependencies**: `{summary.get('total_dependencies', 0)}`",
        f"- **Satisfied Dependencies**: `{summary.get('satisfied_dependencies', 0)}`",
        f"- **All Satisfied**: `{summary.get('all_satisfied', True)}`",
        f"- **Status**: `{summary.get('status', '')}`",
        "",
    ]
    if dependency_df is not None and not dependency_df.empty:
        lines.append("## Dependency Sources")
        lines.append("")
        lines.append(_df_to_markdown(dependency_df))
        lines.append("")
    return "\n".join(lines)


def build_portfolio_validation_evidence_markdown_report(
    summary: Dict[str, Any],
    evidence_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for validation evidence."""
    lines = [
        "# Phase 157: Portfolio Acceptance Validation Evidence Report",
        "",
        DISCLAIMER_TEXT,
        "",
        f"- **Total Evidence Items**: `{summary.get('total_evidence_items', 0)}`",
        f"- **Present Evidence Items**: `{summary.get('present_evidence_items', 0)}`",
        f"- **All Evidence Present**: `{summary.get('all_evidence_present', True)}`",
        f"- **Status**: `{summary.get('status', '')}`",
        "",
    ]
    if evidence_df is not None and not evidence_df.empty:
        lines.append("## Evidence Checklist")
        lines.append("")
        lines.append(_df_to_markdown(evidence_df))
        lines.append("")
    return "\n".join(lines)


def build_portfolio_acceptance_boundary_markdown_report(
    summary: Dict[str, Any],
    boundary_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for boundaries."""
    lines = [
        "# Phase 157: Portfolio Acceptance Boundaries Report",
        "",
        DISCLAIMER_TEXT,
        "",
        f"- **Total Rules**: `{summary.get('total_rules', 0)}`",
        f"- **Status**: `{summary.get('status', '')}`",
        "",
    ]
    if boundary_df is not None and not boundary_df.empty:
        lines.append("## Boundary Rules")
        lines.append("")
        lines.append(_df_to_markdown(boundary_df))
        lines.append("")
    return "\n".join(lines)


def build_portfolio_blocker_gap_warning_markdown_report(
    summary: Dict[str, Any],
    df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for blockers, gaps, or warnings."""
    title = summary.get("domain", "Blockers/Gaps/Warnings")
    lines = [
        f"# Phase 157: Portfolio Acceptance {title} Report",
        "",
        DISCLAIMER_TEXT,
        "",
        f"- **Status**: `{summary.get('status', '')}`",
        "",
    ]
    if df is not None and not df.empty:
        lines.append("## Monitored Items")
        lines.append("")
        lines.append(_df_to_markdown(df))
        lines.append("")
    return "\n".join(lines)


def build_portfolio_acceptance_findings_markdown_report(
    summary: Dict[str, Any],
    findings_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for findings registry."""
    lines = [
        "# Phase 157: Portfolio Acceptance Findings Report",
        "",
        DISCLAIMER_TEXT,
        "",
        f"- **Total Findings**: `{summary.get('total_findings', 0)}`",
        f"- **Blocking Findings**: `{summary.get('blocking_findings_count', 0)}`",
        f"- **Manual Review Required**: `{summary.get('manual_review_required_count', 0)}`",
        f"- **Status**: `{summary.get('status', '')}`",
        "",
    ]
    if findings_df is not None and not findings_df.empty:
        lines.append("## Findings Registry")
        lines.append("")
        lines.append(_df_to_markdown(findings_df))
        lines.append("")
    return "\n".join(lines)


def build_portfolio_acceptance_readiness_score_markdown_report(
    summary: Dict[str, Any],
    score_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for readiness scoring."""
    lines = [
        "# Phase 157: Portfolio Acceptance Readiness Score Report",
        "",
        DISCLAIMER_TEXT,
        "",
        f"- **Readiness Score**: `{summary.get('readiness_score', 0.0):.4f}`",
        f"- **Classification**: `{summary.get('classification', '')}`",
        f"- **Meets Threshold**: `{summary.get('meets_threshold', False)}`",
        f"- **Total Checks**: `{summary.get('total_checks', 0)}`",
        f"- **Passed Checks**: `{summary.get('passed_checks', 0)}`",
        f"- **Blockers**: `{summary.get('blocker_count', 0)}`",
        f"- **Warnings**: `{summary.get('warning_count', 0)}`",
        f"- **Non-Signal Guarantee**: `True`",
        f"- **Non-Production Guarantee**: `True`",
        f"- **Status**: `{summary.get('status', '')}`",
        "",
    ]
    if score_df is not None and not score_df.empty:
        lines.append("## Score Details")
        lines.append("")
        lines.append(_df_to_markdown(score_df))
        lines.append("")
    return "\n".join(lines)


def build_portfolio_acceptance_manifest_markdown_report(
    summary: Dict[str, Any],
    manifest_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for master manifest."""
    lines = [
        "# Phase 157: Portfolio Acceptance Master Manifest Report",
        "",
        DISCLAIMER_TEXT,
        "",
        f"- **Manifest ID**: `{summary.get('manifest_id', '')}`",
        f"- **Current Phase**: `{summary.get('current_phase', 157)}`",
        f"- **Target Final Phase**: `{summary.get('target_final_phase', 160)}`",
        f"- **Next Phase**: `{summary.get('next_phase', 158)}`",
        f"- **Portfolio Block Completed**: `{summary.get('portfolio_block_completed', True)}`",
        f"- **Production Ready**: `{summary.get('production_ready', False)}`",
        f"- **Broker Ready**: `{summary.get('broker_ready', False)}`",
        f"- **Live Trading Ready**: `{summary.get('live_trading_ready', False)}`",
        f"- **Phase 158 Handoff Ready**: `{summary.get('phase_158_handoff_ready', True)}`",
        f"- **Status**: `{summary.get('status', '')}`",
        "",
    ]
    if manifest_df is not None and not manifest_df.empty:
        lines.append("## Manifest Configuration")
        lines.append("")
        lines.append(_df_to_markdown(manifest_df))
        lines.append("")
    return "\n".join(lines)


def build_portfolio_acceptance_validation_markdown_report(
    summary: Dict[str, Any],
    validation_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for validation report."""
    lines = [
        "# Phase 157: Portfolio Acceptance Validation Report",
        "",
        DISCLAIMER_TEXT,
        "",
        f"- **Validation Status**: `{summary.get('validation_status', '')}`",
        f"- **All Rules Passed**: `{summary.get('all_passed', True)}`",
        f"- **Forbidden Claims Found**: `{summary.get('forbidden_claims_found', False)}`",
        f"- **Status**: `{summary.get('status', '')}`",
        "",
    ]
    if validation_df is not None and not validation_df.empty:
        lines.append("## Validation Rules")
        lines.append("")
        lines.append(_df_to_markdown(validation_df))
        lines.append("")
    return "\n".join(lines)


def build_portfolio_acceptance_safety_markdown_report(
    summary: Dict[str, Any],
    safety_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for safety boundary."""
    lines = [
        "# Phase 157: Portfolio Acceptance Safety Boundary Report",
        "",
        DISCLAIMER_TEXT,
        "",
        f"- **Safety Status**: `{summary.get('safety_status', '')}`",
        f"- **No-Go Rules Enforced**: `{summary.get('no_go_count', 0)}`",
        f"- **Safe-Go Principles Active**: `{summary.get('safe_go_count', 0)}`",
        f"- **Live Trading Prohibited**: `True`",
        f"- **Broker Execution Prohibited**: `True`",
        f"- **Portfolio Execution Prohibited**: `True`",
        f"- **Status**: `{summary.get('status', '')}`",
        "",
    ]
    if safety_df is not None and not safety_df.empty:
        lines.append("## Safety Rules Table")
        lines.append("")
        lines.append(_df_to_markdown(safety_df))
        lines.append("")
    return "\n".join(lines)


def build_phase_158_handoff_markdown_report(
    summary: Dict[str, Any],
    handoff_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for Phase 158 handoff."""
    lines = [
        "# Phase 157: Phase 158 Full-System Integration & Acceptance Rehearsal Handoff Report",
        "",
        DISCLAIMER_TEXT,
        "",
        f"- **Current Phase**: `{summary.get('current_phase', 157)}`",
        f"- **Next Phase**: `{summary.get('next_phase', 158)}`",
        f"- **Target Final Phase**: `{summary.get('target_final_phase', 160)}`",
        f"- **Total Prerequisites**: `{summary.get('total_prerequisites', 0)}`",
        f"- **Satisfied Prerequisites**: `{summary.get('satisfied_prerequisites', 0)}`",
        f"- **Handoff Ready**: `{summary.get('handoff_ready', True)}`",
        f"- **Non-Signal Guarantee**: `True`",
        f"- **Status**: `{summary.get('status', '')}`",
        "",
    ]
    if handoff_df is not None and not handoff_df.empty:
        lines.append("## Handoff Prerequisites Table")
        lines.append("")
        lines.append(_df_to_markdown(handoff_df))
        lines.append("")
    return "\n".join(lines)


def build_portfolio_acceptance_full_markdown_report(
    tables: Dict[str, pd.DataFrame],
    summary: Dict[str, Any],
) -> str:
    """Build consolidated master portfolio acceptance report in Markdown."""
    lines = [
        "# Phase 157: Consolidated Portfolio Acceptance Report",
        "",
        DISCLAIMER_TEXT,
        "",
        "## Executive Summary",
        "",
        f"- **Active Profile**: `{summary.get('active_profile', 'balanced_local_portfolio_acceptance_contracts')}`",
        f"- **Current Phase**: `157`",
        f"- **Target Final Phase**: `160`",
        f"- **Next Phase**: `158 (Full-System Integration and Advanced Acceptance Rehearsal)`",
        f"- **Readiness Score**: `{summary.get('readiness_score', 1.0):.4f}`",
        f"- **Classification**: `{summary.get('classification', 'portfolio_acceptance_contract_ready_non_production')}`",
        f"- **Portfolio/Risk Block (153-157)**: `ACCEPTED (CONTRACT-ONLY)`",
        f"- **Live Trading / Broker Ready**: `FALSE`",
        f"- **Production Deployment Ready**: `FALSE`",
        "",
    ]

    for name, df in tables.items():
        if df is not None and not df.empty:
            lines.append(f"### {name.replace('_', ' ').title()}")
            lines.append("")
            lines.append(_df_to_markdown(df))
            lines.append("")

    lines.append("---")
    lines.append("*Report generated under strict local/offline research and zero-trust non-production policies.*")
    return "\n".join(lines)
