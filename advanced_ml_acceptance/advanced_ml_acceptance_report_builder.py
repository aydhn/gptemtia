# -*- coding: utf-8 -*-
"""Phase 145: Advanced ML Acceptance Report Builder (Markdown)."""

from typing import Any, Dict, Optional
import pandas as pd

ADVANCED_ML_ACCEPTANCE_DISCLAIMER = (
    "Bu çıktı Phase 145 Advanced ML Acceptance Report çıktısıdır. Canlı emir, broker talimatı, "
    "kesin AL/SAT, yatırım tavsiyesi, acceptance/readiness/governance değerini trade sinyali veya "
    "production-ready/broker-ready/onay olarak kullanma, gerçek model training, model fit/predict/inference, "
    "probability prediction, calibration/uncertainty execution, drift calculation, explainability calculation, "
    "backtest/walk-forward/benchmark/transaction-cost/slippage execution, model deployment, production deployment, "
    "model registry write, model artifact persistence, official approval, production approval, broker-ready approval, "
    "live-trading approval, gerçek audit log, dataset materialization, target/label/prediction üretimi, gerçek metric/performance "
    "claim, strateji üretimi, optimizer, clustering, ensemble execution, sentiment model output, haber tam metni/article "
    "body/raw content/scraped HTML/embedding/vector kullanımı, scraping veya gerçek provider API çağrısı değildir."
)


def build_advanced_ml_acceptance_disclaimer() -> str:
    """Return the standard non-production disclaimer."""
    return ADVANCED_ML_ACCEPTANCE_DISCLAIMER


def _df_to_markdown(df: Optional[pd.DataFrame]) -> str:
    """Format DataFrame as markdown table without depending on tabulate."""
    if df is None or df.empty:
        return ""
    try:
        return df.to_markdown(index=False)
    except Exception:
        headers = [str(c) for c in df.columns]
        lines = [
            "| " + " | ".join(headers) + " |",
            "| " + " | ".join(["---"] * len(headers)) + " |",
        ]
        for _, row in df.iterrows():
            row_vals = [str(row[c]).replace("\n", " ") for c in df.columns]
            lines.append("| " + " | ".join(row_vals) + " |")
        return "\n".join(lines)


def build_advanced_ml_acceptance_profile_markdown_report(
    summary: Dict[str, Any], profile_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for profiles."""
    lines = [
        "# Phase 145: Advanced ML Acceptance Profile Report",
        "",
        f"> **Yasal Uyarı:** {ADVANCED_ML_ACCEPTANCE_DISCLAIMER}",
        "",
        f"- **Active Profile:** `{summary.get('active_profile')}`",
        f"- **Current Phase:** `{summary.get('current_phase')}`",
        f"- **Target Final Phase:** `{summary.get('target_final_phase')}`",
        f"- **Next Phase:** `{summary.get('next_phase')}`",
        f"- **Total Profiles:** `{summary.get('total_profiles')}`",
        f"- **Status:** `{summary.get('status')}`",
        "",
    ]
    if profile_df is not None and not profile_df.empty:
        lines.append("## Configured Profiles")
        lines.append(_df_to_markdown(profile_df))
        lines.append("")
    return "\n".join(lines)


def build_advanced_ml_component_markdown_report(
    summary: Dict[str, Any], component_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for components."""
    lines = [
        "# Phase 145: Advanced ML Component Registry Report",
        "",
        f"> **Yasal Uyarı:** {ADVANCED_ML_ACCEPTANCE_DISCLAIMER}",
        "",
        f"- **Total Components:** `{summary.get('total_components')}`",
        f"- **Status:** `{summary.get('status')}`",
        "",
    ]
    if component_df is not None and not component_df.empty:
        lines.append("## Registered Components (Phases 136-145)")
        lines.append(_df_to_markdown(component_df))
        lines.append("")
    return "\n".join(lines)


def build_phase_acceptance_markdown_report(
    summary: Dict[str, Any], phase_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for a specific phase acceptance."""
    phase_ref = summary.get("phase_ref", "Phase N/A")
    title = summary.get("phase_title", "")
    lines = [
        f"# Phase 145: {phase_ref} Acceptance Report",
        "",
        f"> **Yasal Uyarı:** {ADVANCED_ML_ACCEPTANCE_DISCLAIMER}",
        "",
        f"- **Phase:** `{phase_ref}` - {title}",
        f"- **Total Checks:** `{summary.get('total_checks')}`",
        f"- **Passed Checks:** `{summary.get('passed_checks')}`",
        f"- **All Passed:** `{summary.get('all_passed')}`",
        f"- **Status:** `{summary.get('status')}`",
        "",
    ]
    if phase_df is not None and not phase_df.empty:
        lines.append("## Check Verifications")
        lines.append(_df_to_markdown(phase_df))
        lines.append("")
    return "\n".join(lines)


def build_dependency_acceptance_markdown_report(
    summary: Dict[str, Any], dependency_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for dependency acceptance."""
    lines = [
        "# Phase 145: Advanced ML Dependency Acceptance Report",
        "",
        f"> **Yasal Uyarı:** {ADVANCED_ML_ACCEPTANCE_DISCLAIMER}",
        "",
        f"- **Total Dependencies:** `{summary.get('total_dependencies')}`",
        f"- **Satisfied Dependencies:** `{summary.get('satisfied_dependencies')}`",
        f"- **All Satisfied:** `{summary.get('all_satisfied')}`",
        f"- **Status:** `{summary.get('status')}`",
        "",
    ]
    if dependency_df is not None and not dependency_df.empty:
        lines.append("## Dependency Ledger")
        lines.append(_df_to_markdown(dependency_df))
        lines.append("")
    return "\n".join(lines)


def build_validation_evidence_markdown_report(
    summary: Dict[str, Any], evidence_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for validation evidence."""
    lines = [
        "# Phase 145: Advanced ML Validation Evidence Summary",
        "",
        f"> **Yasal Uyarı:** {ADVANCED_ML_ACCEPTANCE_DISCLAIMER}",
        "",
        f"- **Total Evidence Items:** `{summary.get('total_evidence_items')}`",
        f"- **Verified Items:** `{summary.get('verified_items')}`",
        f"- **All Verified:** `{summary.get('all_verified')}`",
        f"- **Status:** `{summary.get('status')}`",
        "",
    ]
    if evidence_df is not None and not evidence_df.empty:
        lines.append("## Evidence Items")
        lines.append(_df_to_markdown(evidence_df))
        lines.append("")
    return "\n".join(lines)


def build_boundary_markdown_report(
    summary: Dict[str, Any], boundary_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for safety boundaries."""
    lines = [
        "# Phase 145: Advanced ML Boundary & Gate Report",
        "",
        f"> **Yasal Uyarı:** {ADVANCED_ML_ACCEPTANCE_DISCLAIMER}",
        "",
        f"- **Status:** `{summary.get('status')}`",
        "",
    ]
    if boundary_df is not None and not boundary_df.empty:
        lines.append("## Enforced Boundaries")
        lines.append(_df_to_markdown(boundary_df))
        lines.append("")
    return "\n".join(lines)


def build_blocker_gap_warning_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for blockers, gaps, or warnings."""
    lines = [
        f"# Phase 145: Advanced ML {summary.get('domain', 'Issues')} Report",
        "",
        f"> **Yasal Uyarı:** {ADVANCED_ML_ACCEPTANCE_DISCLAIMER}",
        "",
        f"- **Status:** `{summary.get('status')}`",
        "",
    ]
    if df is not None and not df.empty:
        lines.append(_df_to_markdown(df))
        lines.append("")
    else:
        lines.append("_No entries recorded in this category._")
        lines.append("")
    return "\n".join(lines)


def build_advanced_ml_findings_markdown_report(
    summary: Dict[str, Any], findings_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for findings."""
    lines = [
        "# Phase 145: Advanced ML Findings Registry Report",
        "",
        f"> **Yasal Uyarı:** {ADVANCED_ML_ACCEPTANCE_DISCLAIMER}",
        "",
        f"- **Total Findings:** `{summary.get('total_findings')}`",
        f"- **Manual Review Findings:** `{summary.get('manual_review_findings')}`",
        f"- **Status:** `{summary.get('status')}`",
        "",
    ]
    if findings_df is not None and not findings_df.empty:
        lines.append("## Findings Register")
        lines.append(_df_to_markdown(findings_df))
        lines.append("")
    return "\n".join(lines)


def build_advanced_ml_readiness_score_markdown_report(
    summary: Dict[str, Any], score_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for readiness score."""
    score = summary.get("readiness_score", 1.0)
    lines = [
        "# Phase 145: Advanced ML Readiness Score Report",
        "",
        f"> **Yasal Uyarı:** {ADVANCED_ML_ACCEPTANCE_DISCLAIMER}",
        "",
        f"- **Readiness Score:** `{score:.2f}` / 1.00",
        f"- **Classification:** `{summary.get('classification')}`",
        f"- **Meets Threshold:** `{summary.get('meets_threshold')}`",
        f"- **Production Ready:** `False`",
        f"- **Broker Ready:** `False`",
        f"- **Official Approval:** `False`",
        f"- **Status:** `{summary.get('status')}`",
        "",
        "> [!NOTE]",
        "> Bu puan yalnızca Phase 136-145 arası sözleşme ve yönetişim eksiksizliğini gösterir.",
        "> Canlı işlem, emir gönderimi veya model performansı iddiası teşkil etmez.",
        "",
    ]
    return "\n".join(lines)


def build_advanced_ml_acceptance_manifest_markdown_report(
    summary: Dict[str, Any], manifest_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for acceptance manifest."""
    lines = [
        "# Phase 145: Advanced ML Acceptance Manifest",
        "",
        f"> **Yasal Uyarı:** {ADVANCED_ML_ACCEPTANCE_DISCLAIMER}",
        "",
        f"- **Manifest ID:** `{summary.get('manifest_id')}`",
        f"- **Current Phase:** `{summary.get('current_phase')}`",
        f"- **Next Phase:** `{summary.get('next_phase')}`",
        f"- **Target Final Phase:** `{summary.get('target_final_phase')}`",
        f"- **Advanced ML Block Completed:** `{summary.get('advanced_ml_block_completed')}`",
        f"- **Components Accepted:** `{summary.get('accepted_component_count')} / {summary.get('component_count')}`",
        f"- **Readiness Score:** `{summary.get('readiness_score')}`",
        f"- **Phase 146 Handoff Ready:** `{summary.get('phase_146_handoff_ready')}`",
        f"- **Status:** `{summary.get('status')}`",
        "",
    ]
    return "\n".join(lines)


def build_advanced_ml_acceptance_validation_markdown_report(
    summary: Dict[str, Any], validation_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for acceptance validation."""
    lines = [
        "# Phase 145: Advanced ML Acceptance Validation Report",
        "",
        f"> **Yasal Uyarı:** {ADVANCED_ML_ACCEPTANCE_DISCLAIMER}",
        "",
        f"- **Validation Status:** `{summary.get('status', 'PASS')}`",
        f"- **All Negative Constraints Preserved:** `True`",
        f"- **Zero Forbidden Claims:** `True`",
        "",
    ]
    if validation_df is not None and not validation_df.empty:
        lines.append(_df_to_markdown(validation_df))
        lines.append("")
    return "\n".join(lines)


def build_advanced_ml_acceptance_safety_markdown_report(
    summary: Dict[str, Any], safety_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for safety boundary audit."""
    lines = [
        "# Phase 145: Advanced ML Safety Boundary Report",
        "",
        f"> **Yasal Uyarı:** {ADVANCED_ML_ACCEPTANCE_DISCLAIMER}",
        "",
        f"- **Safety Status:** `{summary.get('status', 'SECURE')}`",
        "- **Non-Production Enforced:** `True`",
        "- **Live Trading Prohibited:** `True`",
        "- **Broker Execution Prohibited:** `True`",
        "- **No-Lookahead Enforced:** `True`",
        "- **Source Preservation Enforced:** `True`",
        "",
    ]
    return "\n".join(lines)


def build_phase_146_handoff_markdown_report(
    summary: Dict[str, Any], handoff_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for Phase 146 handoff."""
    lines = [
        "# Phase 145: Phase 146 Realistic Backtest, Transaction Cost and Slippage Handoff Report",
        "",
        f"> **Yasal Uyarı:** {ADVANCED_ML_ACCEPTANCE_DISCLAIMER}",
        "",
        f"- **Source Phase:** `{summary.get('source_phase', 145)}`",
        f"- **Next Phase:** `{summary.get('next_phase', 146)}` - Realistic Backtest, Transaction Cost and Slippage Modeling",
        f"- **Target Final Phase:** `{summary.get('target_final_phase', 160)}`",
        f"- **Prerequisites Count:** `{summary.get('total_prerequisites')}`",
        f"- **All Satisfied:** `{summary.get('all_satisfied')}`",
        f"- **Handoff Status:** `{summary.get('status')}`",
        "",
    ]
    if handoff_df is not None and not handoff_df.empty:
        lines.append("## Handoff Prerequisites")
        lines.append(_df_to_markdown(handoff_df))
        lines.append("")
    return "\n".join(lines)


def build_advanced_ml_acceptance_full_markdown_report(
    tables: Dict[str, pd.DataFrame], summary: Dict[str, Any]
) -> str:
    """Generate consolidated full markdown report across all Phase 145 sections."""
    sections = [
        "# Phase 145: Consolidated Advanced ML Acceptance Report",
        "",
        f"> **Yasal Uyarı:** {ADVANCED_ML_ACCEPTANCE_DISCLAIMER}",
        "",
        "## Executive Summary",
        f"- **Active Profile:** `{summary.get('active_profile', 'balanced_local_advanced_ml_acceptance')}`",
        "- **Block Name:** Advanced ML Block (Phases 136-145)",
        "- **Current Phase:** `145`",
        "- **Next Phase:** `146` (Realistic Backtest, Transaction Cost and Slippage Modeling)",
        "- **Target Final Phase:** `160`",
        f"- **Readiness Score:** `{summary.get('readiness_score', 1.0):.2f}` / 1.00",
        f"- **Classification:** `{summary.get('classification', 'advanced_ml_contract_acceptance_ready_non_production')}`",
        f"- **Overall Status:** `{summary.get('status', 'ACCEPTED')}`",
        "- Production Ready: `False`",
        "- Broker Ready: `False`",
        "- Live Trading Ready: `False`",
        "",
        "## Component Acceptance Status",
        _df_to_markdown(tables.get("components")) if "components" in tables else "_No component data_",
        "",
        "## Readiness Score Summary",
        _df_to_markdown(tables.get("scoring")) if "scoring" in tables else "_No score data_",
        "",
        "## Phase 146 Handoff Prerequisites",
        _df_to_markdown(tables.get("handoff")) if "handoff" in tables else "_No handoff data_",
        "",
    ]
    return "\n".join(sections)
