"""Phase 125: Feature Factor Acceptance Report Builder.

Formats human-readable markdown reports for acceptance profiles, block inventory,
acceptance gates, compliance audits, block status, manifests, and Phase 126 handoffs.
"""

from typing import Any, Dict, Optional
import pandas as pd

FEATURE_FACTOR_ACCEPTANCE_DISCLAIMER = (
    "> [!WARNING]\n"
    "> **YASAL UYARI VE NON-SIGNAL GÜVENCESİ**:\n"
    "> Bu çıktı Phase 125 Feature/Factor Engine Acceptance Report raporudur. "
    "> Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, acceptance score’u trade sinyali olarak kullanma, "
    "> strateji üretimi, backtest, optimizer, model training, prediction/target/label üretimi, "
    "> production-ready/official approval/broker-ready iddiası, otomatik feature silme/düzeltme, "
    "> haber tam metni kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.\n"
)


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


def build_feature_factor_acceptance_disclaimer() -> str:
    """Return standard research disclaimer."""
    return FEATURE_FACTOR_ACCEPTANCE_DISCLAIMER


def build_feature_factor_acceptance_profile_markdown_report(
    summary: Dict[str, Any], profile_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for acceptance profiles."""
    lines = [
        "# Phase 125 Feature/Factor Acceptance Profiles Report",
        "",
        build_feature_factor_acceptance_disclaimer(),
        "",
        "## Summary",
        f"- **Active Profile**: {summary.get('active_profile', 'unknown')}",
        f"- **Total Profiles**: {summary.get('total_profiles', 0)}",
        f"- **Current Phase**: {summary.get('current_phase', 125)}",
        f"- **Target Final Phase**: {summary.get('target_final_phase', 160)}",
        f"- **Next Phase**: {summary.get('next_phase', 126)}",
        f"- **Non-Signal Mandate**: {summary.get('non_signal', True)}",
        f"- **Source Preserved**: {summary.get('source_preserved', True)}",
        "",
    ]
    if profile_df is not None and not profile_df.empty:
        lines.append("## Profiles Table")
        lines.append(_df_to_markdown(profile_df))
    return "\n".join(lines)


def build_feature_engine_inventory_markdown_report(
    summary: Dict[str, Any], inventory_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for Phase 116-125 block inventory."""
    lines = [
        "# Phase 116-125 Feature Engine Block Inventory Report",
        "",
        build_feature_factor_acceptance_disclaimer(),
        "",
        "## Summary",
        f"- **Total Modules**: {summary.get('total_modules', 0)}",
        f"- **Phase Range**: {summary.get('phase_range', '116-125')}",
        f"- **All Modules Passed**: {summary.get('all_passed', True)}",
        f"- **Total Expected Scripts**: {summary.get('total_expected_scripts', 0)}",
        f"- **Total Expected Tests**: {summary.get('total_expected_tests', 0)}",
        f"- **Manual Reviews Needed**: {summary.get('manual_review_needed', 0)}",
        "",
    ]
    if inventory_df is not None and not inventory_df.empty:
        lines.append("## Inventory Table")
        lines.append(_df_to_markdown(inventory_df))
    return "\n".join(lines)


def build_feature_engine_dependency_markdown_report(
    summary: Dict[str, Any], dependency_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for block dependencies."""
    lines = [
        "# Phase 116-125 Feature Engine Block Dependencies Report",
        "",
        build_feature_factor_acceptance_disclaimer(),
        "",
        "## Summary",
        f"- **Total Dependency Edges**: {summary.get('total_dependencies', 0)}",
        f"- **All Contracts Satisfied**: {summary.get('all_satisfied', True)}",
        f"- **Pipeline Flow**: Phase {summary.get('phase_start', 116)} -> ... -> Phase {summary.get('phase_end', 126)}",
        "",
    ]
    if dependency_df is not None and not dependency_df.empty:
        lines.append("## Dependency Graph Table")
        lines.append(_df_to_markdown(dependency_df))
    return "\n".join(lines)


def build_acceptance_gate_markdown_report(
    summary: Dict[str, Any], gate_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for acceptance gates."""
    lines = [
        "# Phase 125 Feature Engine Block Acceptance Gate Registry",
        "",
        build_feature_factor_acceptance_disclaimer(),
        "",
        "## Summary",
        f"- **Total Gates**: {summary.get('total_gates', 0)}",
        f"- **Passed Gates**: {summary.get('passed_gates', 0)}",
        f"- **Failed Gates**: {summary.get('failed_gates', 0)}",
        f"- **All Passed**: {summary.get('all_passed', False)}",
        "",
    ]
    if gate_df is not None and not gate_df.empty:
        lines.append("## Gate Evaluations Table")
        lines.append(_df_to_markdown(gate_df))
    return "\n".join(lines)


def build_acceptance_score_markdown_report(
    summary: Dict[str, Any], score_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for acceptance scoring."""
    lines = [
        "# Phase 125 Feature Engine Block Acceptance Score Report",
        "",
        build_feature_factor_acceptance_disclaimer(),
        "",
        "## Summary",
        f"- **Overall Score**: {summary.get('overall_score', 0.0)}",
        f"- **Score Tier**: {summary.get('score_tier', 'UNKNOWN')}",
        f"- **Meets Profile Minimum**: {summary.get('meets_profile_minimum', False)} (Min: {summary.get('min_required_score', 0.45)})",
        f"- **Total Gates Evaluated**: {summary.get('total_gates', 0)}",
        f"- **Passed Gates**: {summary.get('passed_gates', 0)}",
        f"- **Official Approval**: False (Strict Non-Signal Readiness Metric Only)",
        "",
    ]
    if score_df is not None and not score_df.empty:
        lines.append("## Score Details Table")
        lines.append(_df_to_markdown(score_df))
    return "\n".join(lines)


def build_manual_review_markdown_report(
    summary: Dict[str, Any], review_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for manual review queue."""
    lines = [
        "# Phase 125 Feature Engine Block Manual Review Queue",
        "",
        build_feature_factor_acceptance_disclaimer(),
        "",
        "## Summary",
        f"- **Total Items**: {summary.get('total_items', 0)}",
        f"- **Pending Items**: {summary.get('pending_items', 0)}",
        f"- **Resolved Safe Items**: {summary.get('resolved_safe_items', 0)}",
        f"- **Destructive Actions Prevented**: {summary.get('destructive_actions_prevented', True)}",
        f"- **Auto-Imputation Prevented**: {summary.get('auto_imputation_prevented', True)}",
        f"- **Auto-Feature-Drop Prevented**: {summary.get('auto_drop_prevented', True)}",
        "",
    ]
    if review_df is not None and not review_df.empty:
        lines.append("## Manual Review Ledger")
        lines.append(_df_to_markdown(review_df))
    return "\n".join(lines)


def build_compliance_markdown_report(
    summary: Dict[str, Any], compliance_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for compliance audit."""
    lines = [
        "# Phase 125 Feature Engine Block Compliance Audit",
        "",
        build_feature_factor_acceptance_disclaimer(),
        "",
        "## Summary",
        f"- **Compliance Scope**: {summary.get('compliance_type', 'all_invariants')}",
        f"- **Total Audited**: {summary.get('total_modules_audited', summary.get('total_items', 0))}",
        f"- **Compliant Count**: {summary.get('compliant_modules', summary.get('verified_count', 0))}",
        f"- **Non-Signal Enforced**: {summary.get('non_signal', True)}",
        f"- **Source Preservation**: {summary.get('source_preserved', True)}",
        "",
    ]
    if compliance_df is not None and not compliance_df.empty:
        lines.append("## Compliance Ledger")
        lines.append(_df_to_markdown(compliance_df))
    return "\n".join(lines)


def build_contract_markdown_report(
    summary: Dict[str, Any], contract_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for script/test/docs contracts."""
    lines = [
        "# Phase 125 Feature Engine Block Contract Audit",
        "",
        build_feature_factor_acceptance_disclaimer(),
        "",
        "## Summary",
        f"- **Total Contracts Checked**: {summary.get('total_scripts_checked', summary.get('total_test_suites_checked', summary.get('total_docs_checked', 0)))}",
        f"- **All Contracts Present**: {summary.get('all_present', False)}",
        f"- **Non-Signal Mandate**: True",
        "",
    ]
    if contract_df is not None and not contract_df.empty:
        lines.append("## Contract Ledger Table")
        lines.append(_df_to_markdown(contract_df))
    return "\n".join(lines)


def build_acceptance_manifest_markdown_report(
    summary: Dict[str, Any], manifest_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for Phase 116-125 acceptance manifest."""
    lines = [
        "# Phase 116-125 Acceptance Manifest Report",
        "",
        build_feature_factor_acceptance_disclaimer(),
        "",
        "## Summary",
        f"- **Block Name**: {summary.get('block_name', 'advanced_feature_factor_engine_block')}",
        f"- **Phases Concluded**: Phase {summary.get('phase_start', 116)} to Phase {summary.get('phase_end', 125)}",
        f"- **Target Final Phase**: {summary.get('target_final_phase', 160)}",
        f"- **Next Phase**: {summary.get('next_phase', 126)}",
        f"- **Acceptance Score**: {summary.get('acceptance_score', 1.0)}",
        f"- **Non-Signal Invariant**: {summary.get('non_signal', True)}",
        f"- **Official Approval**: False (Research & Governance Only)",
        f"- **Production Ready**: False",
        f"- **Broker Ready**: False",
        f"- **Source Preserved**: {summary.get('source_preserved', True)}",
        "",
    ]
    if manifest_df is not None and not manifest_df.empty:
        lines.append("## Manifest Specifications Table")
        lines.append(_df_to_markdown(manifest_df))
    return "\n".join(lines)


def build_health_markdown_report(
    summary: Dict[str, Any], health_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for health checks."""
    lines = [
        "# Phase 125 Feature Factor Acceptance Health Report",
        "",
        build_feature_factor_acceptance_disclaimer(),
        "",
        "## Summary",
        f"- **Health Status**: {summary.get('health_status', 'HEALTHY')}",
        f"- **Total Checks**: {summary.get('total_checks', 0)}",
        f"- **Passed Checks**: {summary.get('passed_checks', 0)}",
        f"- **Non-Signal**: True",
        "",
    ]
    if health_df is not None and not health_df.empty:
        lines.append("## Health Checks Table")
        lines.append(_df_to_markdown(health_df))
    return "\n".join(lines)


def build_validation_markdown_report(
    summary: Dict[str, Any], validation_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for validation audits."""
    lines = [
        "# Phase 125 Feature Factor Acceptance Validation Report",
        "",
        build_feature_factor_acceptance_disclaimer(),
        "",
        "## Summary",
        f"- **Validation Status**: {summary.get('validation_status', 'VALIDATION_PASS')}",
        f"- **Total Rules Verified**: {summary.get('total_rules', 0)}",
        f"- **Passed Rules**: {summary.get('passed_rules', 0)}",
        f"- **Forbidden Claims Detected**: {summary.get('forbidden_claims_detected', 0)}",
        f"- **Non-Signal Invariant**: True",
        "",
    ]
    if validation_df is not None and not validation_df.empty:
        lines.append("## Validation Results Table")
        lines.append(_df_to_markdown(validation_df))
    return "\n".join(lines)


def build_phase_126_handoff_markdown_report(
    summary: Dict[str, Any], handoff_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for Phase 126 handoff."""
    lines = [
        "# Phase 126 Regime Classification Handoff Report",
        "",
        build_feature_factor_acceptance_disclaimer(),
        "",
        "## Summary",
        f"- **Handoff Status**: {summary.get('handoff_status', 'READY')}",
        f"- **Source Phase**: {summary.get('source_phase', 125)}",
        f"- **Next Phase**: {summary.get('next_phase', 126)}",
        f"- **Target Final Phase**: {summary.get('target_final_phase', 160)}",
        f"- **Total Handoff Items**: {summary.get('total_handoff_items', 0)}",
        f"- **Ready Items**: {summary.get('ready_items', 0)}",
        f"- **Non-Signal Invariant**: True",
        "",
    ]
    if handoff_df is not None and not handoff_df.empty:
        lines.append("## Handoff Items Table")
        lines.append(_df_to_markdown(handoff_df))
    return "\n".join(lines)
