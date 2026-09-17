# -*- coding: utf-8 -*-
"""Phase 158: Full-System Integration Report Builder.

Generates comprehensive Markdown reports and attaches strict governance disclaimers.
"""

from typing import Any, Dict, Optional
import pandas as pd


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


def build_full_system_integration_disclaimer() -> str:
    """Return the mandatory Phase 158 governance disclaimer."""
    return (
        "> **UYARI VE KAPSAM SINIRI**:\n"
        "> Bu çıktı Phase 158 Full-System Integration and Advanced Acceptance Rehearsal çıktısıdır. "
        "Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, full-system/readiness/integration/rehearsal "
        "değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gerçek full-system execution, "
        "end-to-end bot run, live trading, broker execution, order generation, signal generation, model training, "
        "model fit/predict/inference, target/label/prediction üretimi, backtest, benchmark, optimizer, "
        "portfolio construction, risk reporting, scenario execution, metric calculation, model deployment, "
        "model registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/scraped "
        "HTML/embedding/vector kullanımı veya gerçek provider API çağrısı değildir."
    )


def build_full_system_integration_profile_markdown_report(
    summary: Dict[str, Any], profile_df: Optional[pd.DataFrame] = None
) -> str:
    """Build profile registry Markdown report."""
    md = f"# Phase 158: Full-System Integration Profiles\n\n{build_full_system_integration_disclaimer()}\n\n"
    md += f"- **Active Profile**: `{summary.get('active_profile', 'N/A')}`\n"
    md += f"- **Total Profiles**: `{summary.get('total_profiles', 0)}`\n"
    md += f"- **Status**: `{summary.get('status', 'N/A')}`\n\n"
    if profile_df is not None and not profile_df.empty:
        md += "### Profiles Table\n\n"
        md += _df_to_markdown(profile_df) + "\n\n"
    return md


def build_system_component_markdown_report(
    summary: Dict[str, Any], component_df: Optional[pd.DataFrame] = None
) -> str:
    """Build component registry Markdown report."""
    md = f"# Phase 158: System Component Registry\n\n{build_full_system_integration_disclaimer()}\n\n"
    md += f"- **Total Components**: `{summary.get('total_components', 0)}`\n"
    md += f"- **All Contract Only**: `{summary.get('all_contract_only', True)}`\n"
    md += f"- **All Non-Production**: `{summary.get('all_non_production', True)}`\n\n"
    if component_df is not None and not component_df.empty:
        md += "### Registered Components\n\n"
        md += _df_to_markdown(component_df) + "\n\n"
    return md


def build_system_dependency_markdown_report(
    summary: Dict[str, Any], dependency_df: Optional[pd.DataFrame] = None
) -> str:
    """Build system dependency graph Markdown report."""
    md = f"# Phase 158: System Dependency Architecture\n\n{build_full_system_integration_disclaimer()}\n\n"
    md += f"- **Total Dependencies**: `{summary.get('total_dependencies', 0)}`\n"
    md += f"- **Hard Dependencies**: `{summary.get('hard_dependencies', 0)}`\n"
    md += f"- **Soft Dependencies**: `{summary.get('soft_dependencies', 0)}`\n\n"
    if dependency_df is not None and not dependency_df.empty:
        md += "### Dependency Graph\n\n"
        md += _df_to_markdown(dependency_df) + "\n\n"
    return md


def build_system_contract_integration_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Build contract integration Markdown report."""
    md = f"# Phase 158: System Contract Integration\n\n{build_full_system_integration_disclaimer()}\n\n"
    md += f"- **Total Contracts**: `{summary.get('total_contracts', 0)}`\n"
    md += f"- **Zero Execution Guaranteed**: `{summary.get('all_zero_execution', True)}`\n\n"
    if df is not None and not df.empty:
        md += "### Integrated Contracts\n\n"
        md += _df_to_markdown(df) + "\n\n"
    return md


def build_system_manifest_integration_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Build manifest integration Markdown report."""
    md = f"# Phase 158: System Manifest Integration\n\n{build_full_system_integration_disclaimer()}\n\n"
    md += f"- **Total Manifests Integrated**: `{summary.get('total_manifests_integrated', 0)}`\n"
    md += f"- **All Verified**: `{summary.get('all_manifests_verified', True)}`\n\n"
    if df is not None and not df.empty:
        md += "### Reconciled Manifests\n\n"
        md += _df_to_markdown(df) + "\n\n"
    return md


def build_advanced_acceptance_rehearsal_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Build advanced acceptance rehearsal Markdown report."""
    md = f"# Phase 158: Advanced Acceptance Rehearsal\n\n{build_full_system_integration_disclaimer()}\n\n"
    md += f"- **Total Rehearsals**: `{summary.get('total_rehearsals', 0)}`\n"
    md += f"- **Satisfied**: `{summary.get('satisfied_count', 0)}`\n"
    md += f"- **All Zero-Execution Verified**: `{summary.get('all_zero_execution_verified', True)}`\n\n"
    if df is not None and not df.empty:
        md += "### Rehearsal Checklist\n\n"
        md += _df_to_markdown(df) + "\n\n"
    return md


def build_system_boundary_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Build system boundary rules Markdown report."""
    md = f"# Phase 158: System Boundaries\n\n{build_full_system_integration_disclaimer()}\n\n"
    md += f"- **Total Rules**: `{summary.get('total_rules', 0)}`\n"
    md += f"- **Prohibited Count**: `{summary.get('prohibited_actions_count', 0)}`\n"
    md += f"- **Allowed Count**: `{summary.get('allowed_actions_count', 0)}`\n\n"
    if df is not None and not df.empty:
        md += "### Enforced Boundaries\n\n"
        md += _df_to_markdown(df) + "\n\n"
    return md


def build_system_disabled_execution_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Build disabled execution guarantees Markdown report."""
    md = f"# Phase 158: Disabled Execution Guarantees\n\n{build_full_system_integration_disclaimer()}\n\n"
    md += f"- **Status**: `{summary.get('status', 'DISABLED')}`\n"
    md += f"- **All Disabled**: `{summary.get('all_disabled', True)}`\n\n"
    if df is not None and not df.empty:
        md += "### Execution Disablement\n\n"
        md += _df_to_markdown(df) + "\n\n"
    return md


def build_system_findings_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Build findings and review items Markdown report."""
    md = f"# Phase 158: System Integration Findings\n\n{build_full_system_integration_disclaimer()}\n\n"
    md += f"- **Total Findings**: `{summary.get('total_findings', 0)}`\n"
    md += f"- **Blocking Findings**: `{summary.get('blocking_findings_count', 0)}`\n"
    md += f"- **Manual Review Required**: `{summary.get('manual_review_required_count', 0)}`\n\n"
    if df is not None and not df.empty:
        md += "### Findings Catalog\n\n"
        md += _df_to_markdown(df) + "\n\n"
    return md


def build_system_readiness_score_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Build readiness score Markdown report."""
    md = f"# Phase 158: System Integration Readiness Score\n\n{build_full_system_integration_disclaimer()}\n\n"
    md += f"- **Readiness Score**: `{summary.get('readiness_score', 0.0):.4f}`\n"
    md += f"- **Classification**: `{summary.get('classification', 'N/A')}`\n"
    md += f"- **Meets Threshold**: `{summary.get('meets_threshold', False)}`\n"
    md += f"- **Passed Checks**: `{summary.get('passed_checks', 0)} / {summary.get('total_checks', 0)}`\n\n"
    if df is not None and not df.empty:
        md += "### Scoring Breakdown\n\n"
        md += _df_to_markdown(df) + "\n\n"
    return md


def build_full_system_integration_manifest_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Build master manifest Markdown report."""
    md = f"# Phase 158: Full-System Integration Master Manifest\n\n{build_full_system_integration_disclaimer()}\n\n"
    md += f"- **Manifest ID**: `{summary.get('manifest_id', 'N/A')}`\n"
    md += f"- **Completed**: `{summary.get('full_system_integration_completed', False)}`\n"
    md += f"- **Current / Target Phase**: `158 / 160`\n"
    md += f"- **Next Phase**: `159`\n"
    md += f"- **Phase 159 Handoff Ready**: `{summary.get('phase_159_handoff_ready', False)}`\n\n"
    if df is not None and not df.empty:
        md += "### Master Manifest Properties\n\n"
        md += _df_to_markdown(df) + "\n\n"
    return md


def build_full_system_integration_validation_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Build validation report Markdown report."""
    md = f"# Phase 158: Full-System Integration Validation Report\n\n{build_full_system_integration_disclaimer()}\n\n"
    md += f"- **Validation Status**: `{summary.get('validation_status', 'VALID')}`\n"
    md += f"- **Total Rules**: `{summary.get('total_rules', 0)}`\n"
    md += f"- **All Passed**: `{summary.get('all_passed', True)}`\n\n"
    if df is not None and not df.empty:
        md += "### Validation Rules Table\n\n"
        md += _df_to_markdown(df) + "\n\n"
    return md


def build_full_system_integration_safety_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Build safety boundary Markdown report."""
    md = f"# Phase 158: Full-System Integration Safety Boundary\n\n{build_full_system_integration_disclaimer()}\n\n"
    md += f"- **Safety Status**: `{summary.get('safety_status', 'SECURE')}`\n"
    md += f"- **NO-GO Conditions Count**: `{summary.get('no_go_count', 0)}`\n"
    md += f"- **SAFE-GO Principles Count**: `{summary.get('safe_go_count', 0)}`\n\n"
    if df is not None and not df.empty:
        md += "### Safety Rules\n\n"
        md += _df_to_markdown(df) + "\n\n"
    return md


def build_phase_159_handoff_markdown_report(
    summary: Dict[str, Any], df: Optional[pd.DataFrame] = None
) -> str:
    """Build Phase 159 handoff Markdown report."""
    md = f"# Phase 158 to Phase 159 Handoff Report\n\n{build_full_system_integration_disclaimer()}\n\n"
    md += f"- **Current Phase**: `158`\n"
    md += f"- **Next Phase**: `159: Final Hardening, Operator Runbook and Release Candidate`\n"
    md += f"- **Target Final Phase**: `160: Full Advanced Bot Final Delivery`\n"
    md += f"- **All Prerequisites Satisfied**: `{summary.get('all_satisfied', True)}`\n"
    md += f"- **Handoff Status**: `{summary.get('status', 'ACCEPTED')}`\n\n"
    if df is not None and not df.empty:
        md += "### Handoff Prerequisites Table\n\n"
        md += _df_to_markdown(df) + "\n\n"
    return md


def build_full_system_integration_full_markdown_report(
    tables: Dict[str, Any], summary: Dict[str, Any]
) -> str:
    """Assemble complete consolidated Phase 158 Full-System Integration Report."""
    md = (
        f"# Phase 158: Consolidated Full-System Integration & Advanced Acceptance Rehearsal Report\n\n"
        f"{build_full_system_integration_disclaimer()}\n\n"
        f"## Executive Governance Summary\n\n"
        f"- **Active Profile**: `{summary.get('active_profile', 'N/A')}`\n"
        f"- **Readiness Score**: `{summary.get('readiness_score', 0.0):.4f}`\n"
        f"- **Classification**: `{summary.get('classification', 'N/A')}`\n"
        f"- **Meets Threshold**: `{summary.get('meets_threshold', True)}`\n"
        f"- **Handoff Ready**: `{summary.get('handoff_ready', True)}`\n"
        f"- **Phase Flow**: Current Phase 158 -> Next Phase 159 -> Target Final Phase 160\n"
        f"- **Operational Mode**: Strictly Local/Offline Dry-Run (Zero Real Execution)\n\n"
        f"## Key Architectural Sections\n\n"
        f"1. System Component Registry\n"
        f"2. Architectural Dependency Graph\n"
        f"3. Component Checkpoints & Verification\n"
        f"4. Contract & Manifest Integration\n"
        f"5. Advanced Acceptance Rehearsal\n"
        f"6. Disabled Execution Guarantees\n"
        f"7. Findings & Manual Review Gates\n"
        f"8. Health Check, Validation & Safety Boundaries\n"
        f"9. Phase 159 Release Candidate Handoff\n\n"
    )

    if "components" in tables:
        md += "### Registered System Components\n\n"
        md += _df_to_markdown(tables["components"]) + "\n\n"
    if "dependencies" in tables:
        md += "### System Dependency Graph\n\n"
        md += _df_to_markdown(tables["dependencies"]) + "\n\n"
    if "rehearsal" in tables:
        md += "### Advanced Acceptance Rehearsal Checklist\n\n"
        md += _df_to_markdown(tables["rehearsal"]) + "\n\n"
    if "manifest" in tables:
        md += "### Full-System Master Manifest\n\n"
        md += _df_to_markdown(tables["manifest"]) + "\n\n"
    if "handoff" in tables:
        md += "### Phase 159 Handoff Status\n\n"
        md += _df_to_markdown(tables["handoff"]) + "\n\n"

    return md
