"""Phase 135: Regime Acceptance Markdown and Text Report Builder.

Generates standardized human-readable reports across all Phase 135 artifacts,
prepending the mandatory non-signal and non-trading disclaimer to every document.
"""

from typing import Any, Dict, Optional
import pandas as pd


REGIME_ACCEPTANCE_DISCLAIMER: str = (
    "> [!CAUTION]\n"
    "> **PHASE 135 YÖNETİŞİM VE NON-SIGNAL UYARISI**\n"
    "> Bu çıktı Phase 135 Regime Classification Acceptance Report raporudur. "
    "Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, "
    "rejim/validation/acceptance/FeatureStore değerini trade sinyali olarak kullanma, "
    "strateji üretimi, backtest, optimizer, model training, clustering execution, "
    "prediction/target/label üretimi, sentiment model output, "
    "haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı, "
    "production-ready/official approval/broker-ready iddiası, production deployment, "
    "model deployment, scraping veya gerçek provider API çağrısı değildir."
)


def build_regime_acceptance_disclaimer() -> str:
    """Return the canonical Phase 135 governance disclaimer."""
    return REGIME_ACCEPTANCE_DISCLAIMER


def _df_to_markdown(df: Optional[pd.DataFrame]) -> str:
    """Format DataFrame as markdown table without requiring optional tabulate."""
    if df is None or df.empty:
        return "_Boş tablo_"
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


def build_regime_acceptance_profile_markdown_report(
    summary: Dict[str, Any],
    profile_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for acceptance profiles."""
    lines = [
        "# Phase 135: Regime Acceptance Profile Registry Report",
        "",
        build_regime_acceptance_disclaimer(),
        "",
        "## Summary",
        f"- **Active Profile**: {summary.get('active_profile', 'N/A')}",
        f"- **Total Profiles**: {summary.get('total_profiles', 0)}",
        f"- **Current Phase**: {summary.get('current_phase', 135)}",
        f"- **Target Final Phase**: {summary.get('target_final_phase', 160)}",
        f"- **Next Phase**: {summary.get('next_phase', 136)}",
        f"- **Status**: {summary.get('status', 'READY')}",
        "",
    ]
    if profile_df is not None and not profile_df.empty:
        lines.append("## Registered Profiles")
        lines.append(_df_to_markdown(profile_df))
    return "\n".join(lines)


def build_regime_block_inventory_markdown_report(
    summary: Dict[str, Any],
    inventory_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for regime block module inventory."""
    lines = [
        "# Phase 135: Regime Classification Block Module Inventory Report",
        "",
        build_regime_acceptance_disclaimer(),
        "",
        "## Summary",
        f"- **Total Modules in Block**: {summary.get('total_modules', 0)}",
        f"- **Expected Scripts**: {summary.get('total_expected_scripts', 0)}",
        f"- **Expected Tests**: {summary.get('total_expected_tests', 0)}",
        f"- **Expected Reports**: {summary.get('total_expected_reports', 0)}",
        f"- **Expected DataLake Outputs**: {summary.get('total_expected_datalake_outputs', 0)}",
        f"- **Phase Range**: {summary.get('phase_range', '126-135')}",
        "",
    ]
    if inventory_df is not None and not inventory_df.empty:
        lines.append("## Module Inventory")
        lines.append(_df_to_markdown(inventory_df))
    return "\n".join(lines)


def build_regime_block_dependency_markdown_report(
    summary: Dict[str, Any],
    dependency_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for regime block dependencies."""
    lines = [
        "# Phase 135: Regime Block Dependency Map Report",
        "",
        build_regime_acceptance_disclaimer(),
        "",
        "## Summary",
        f"- **Total Dependency Steps**: {summary.get('total_dependency_steps', 0)}",
        f"- **All Satisfied**: {summary.get('all_satisfied', False)}",
        f"- **Flow**: `{summary.get('flow', '126 -> ... -> 136')}`",
        "",
    ]
    if dependency_df is not None and not dependency_df.empty:
        lines.append("## Dependency Details")
        lines.append(_df_to_markdown(dependency_df))
    return "\n".join(lines)


def build_regime_acceptance_gate_markdown_report(
    summary: Dict[str, Any],
    gate_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for acceptance gates."""
    lines = [
        "# Phase 135: Regime Block Acceptance Gate Evaluation Report",
        "",
        build_regime_acceptance_disclaimer(),
        "",
        "## Summary",
        f"- **Total Gates**: {summary.get('total_gates', 0)}",
        f"- **Passed Gates**: {summary.get('passed_gates', 0)}",
        f"- **All Passed**: {summary.get('all_passed', False)}",
        "",
    ]
    if gate_df is not None and not gate_df.empty:
        lines.append("## Gate Evaluations")
        lines.append(_df_to_markdown(gate_df))
    return "\n".join(lines)


def build_regime_acceptance_score_markdown_report(
    summary: Dict[str, Any],
    score_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for acceptance scoring."""
    lines = [
        "# Phase 135: Regime Block Acceptance Score Report",
        "",
        build_regime_acceptance_disclaimer(),
        "",
        "## Summary",
        f"- **Acceptance Score**: {summary.get('acceptance_score', 0.0)}",
        f"- **Classification**: {summary.get('classification', 'N/A')}",
        f"- **Is Acceptable**: {summary.get('is_acceptable', False)}",
        "- **Non-Signal Certified**: True",
        "- **Official Approval**: False (Governance only)",
        "- **Production Ready**: False (Offline research only)",
        "- **Broker Ready**: False",
        "",
    ]
    if score_df is not None and not score_df.empty:
        lines.append("## Score Matrix")
        lines.append(_df_to_markdown(score_df))
    return "\n".join(lines)


def build_regime_manual_review_markdown_report(
    summary: Dict[str, Any],
    review_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for manual review queue."""
    lines = [
        "# Phase 135: Regime Block Manual Review Queue Report",
        "",
        build_regime_acceptance_disclaimer(),
        "",
        "## Summary",
        f"- **Total Review Items**: {summary.get('total_review_items', 0)}",
        f"- **Auto-Destructive Allowed**: {summary.get('auto_destructive_allowed', False)}",
        "- **Forbidden Suggestions Enforced**: True",
        "",
    ]
    if review_df is not None and not review_df.empty:
        lines.append("## Pending Review Queue")
        lines.append(_df_to_markdown(review_df))
    return "\n".join(lines)


def build_regime_compliance_markdown_report(
    summary: Dict[str, Any],
    compliance_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for compliance checks."""
    lines = [
        "# Phase 135: Regime Block Compliance Verification Report",
        "",
        build_regime_acceptance_disclaimer(),
        "",
        "## Summary",
        f"- **Domain**: {summary.get('domain', 'compliance')}",
        f"- **Total Checks**: {summary.get('total_checks', 0)}",
        f"- **All Compliant**: {summary.get('all_compliant', False)}",
        "",
    ]
    if compliance_df is not None and not compliance_df.empty:
        lines.append("## Compliance Check Ledger")
        lines.append(_df_to_markdown(compliance_df))
    return "\n".join(lines)


def build_regime_component_acceptance_markdown_report(
    summary: Dict[str, Any],
    component_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for individual component acceptance."""
    lines = [
        "# Phase 135: Regime Block Component Acceptance Report",
        "",
        build_regime_acceptance_disclaimer(),
        "",
        "## Summary",
        f"- **Total Components**: {summary.get('total_components', 0)}",
        f"- **All Accepted**: {summary.get('all_accepted', False)}",
        f"- **Phase Range**: {summary.get('phase_start', 126)}-{summary.get('phase_end', 135)}",
        "",
    ]
    if component_df is not None and not component_df.empty:
        lines.append("## Component Acceptance Matrix")
        lines.append(_df_to_markdown(component_df))
    return "\n".join(lines)


def build_regime_contract_markdown_report(
    summary: Dict[str, Any],
    contract_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for script/test/docs contracts."""
    lines = [
        "# Phase 135: Regime Block Contract Audit Report",
        "",
        build_regime_acceptance_disclaimer(),
        "",
        "## Summary",
        f"- **Domain**: {summary.get('domain', 'contract')}",
        f"- **Status**: {summary.get('status', 'READY')}",
        "",
    ]
    if contract_df is not None and not contract_df.empty:
        lines.append("## Contract Audit Ledger")
        lines.append(_df_to_markdown(contract_df))
    return "\n".join(lines)


def build_regime_acceptance_manifest_markdown_report(
    summary: Dict[str, Any],
    manifest_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for block acceptance manifest."""
    lines = [
        "# Phase 135: Phase 126-135 Regime Block Acceptance Manifest",
        "",
        build_regime_acceptance_disclaimer(),
        "",
        "## Block Acceptance Certification",
        f"- **Block Name**: {summary.get('block_name', 'N/A')}",
        f"- **Phases**: {summary.get('phase_start', 126)} through {summary.get('phase_end', 135)}",
        f"- **Target Final Phase**: {summary.get('target_final_phase', 160)}",
        f"- **Next Phase**: {summary.get('next_phase', 136)}",
        f"- **Modules Count**: {summary.get('module_count', 0)}",
        f"- **Gates Evaluated**: {summary.get('gate_count', 0)}",
        f"- **Acceptance Score**: {summary.get('acceptance_score', 0.0)}",
        f"- **Non-Signal Certified**: {summary.get('non_signal', True)}",
        f"- **Source Preserved**: {summary.get('source_preserved', True)}",
        f"- **Official Approval**: {summary.get('official_approval', False)} (No legal sign-off claimed)",
        f"- **Production Ready**: {summary.get('production_ready', False)} (Offline research only)",
        f"- **Broker Ready**: {summary.get('broker_ready', False)}",
        "",
    ]
    if manifest_df is not None and not manifest_df.empty:
        lines.append("## Manifest Record")
        lines.append(_df_to_markdown(manifest_df))
    return "\n".join(lines)


def build_regime_health_markdown_report(
    summary: Dict[str, Any],
    health_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for health checks."""
    lines = [
        "# Phase 135: Regime Acceptance Health Check Report",
        "",
        build_regime_acceptance_disclaimer(),
        "",
        "## Summary",
        f"- **All Healthy**: {summary.get('all_healthy', False)}",
        f"- **Total Checks**: {summary.get('total_checks', 0)}",
        "",
    ]
    if health_df is not None and not health_df.empty:
        lines.append("## Health Status")
        lines.append(_df_to_markdown(health_df))
    return "\n".join(lines)


def build_regime_validation_markdown_report(
    summary: Dict[str, Any],
    validation_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for validation findings."""
    lines = [
        "# Phase 135: Regime Acceptance Validation Report",
        "",
        build_regime_acceptance_disclaimer(),
        "",
        "## Summary",
        f"- **Validation Passed**: {summary.get('all_passed', False)}",
        f"- **Total Validations**: {summary.get('total_validations', 0)}",
        "",
    ]
    if validation_df is not None and not validation_df.empty:
        lines.append("## Validation Results")
        lines.append(_df_to_markdown(validation_df))
    return "\n".join(lines)


def build_phase_136_handoff_markdown_report(
    summary: Dict[str, Any],
    handoff_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for Phase 136 ML/GPU handoff."""
    lines = [
        "# Phase 135: Phase 136 Advanced ML and GPU Runtime Handoff Report",
        "",
        build_regime_acceptance_disclaimer(),
        "",
        "## Handoff Overview",
        f"- **Source Phase**: {summary.get('source_phase', 135)}",
        f"- **Next Phase**: {summary.get('next_phase', 136)} ({summary.get('next_phase_title', '')})",
        f"- **Target Final Phase**: {summary.get('target_final_phase', 160)}",
        f"- **Prerequisites Total**: {summary.get('total_prerequisites', 0)}",
        f"- **Prerequisites Satisfied**: {summary.get('satisfied_prerequisites', 0)}",
        f"- **Status**: {summary.get('status', 'READY')}",
        "",
        "### Phase 136 Transition Notes",
        "- Phase 136 will establish GPU acceleration discovery and advanced ML runtime foundation.",
        "- Experiments, tensors, and models prepared in Phase 136 will remain strictly non-signal research artifacts.",
        "- Zero live orders, broker connections, or capital risks will be permitted.",
        "",
    ]
    if handoff_df is not None and not handoff_df.empty:
        lines.append("## Prerequisite Checklist")
        lines.append(_df_to_markdown(handoff_df))
    return "\n".join(lines)
