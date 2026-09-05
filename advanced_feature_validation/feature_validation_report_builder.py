"""Markdown Report Builder for Phase 121 Feature Validation Layer.

Generates structured Markdown reports and audit summaries across all validation domains.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, Optional
import pandas as pd

FEATURE_VALIDATION_DISCLAIMER = (
    "Bu çıktı Phase 121 Feature Validation and No-Lookahead Guard raporudur. "
    "Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, validation score’u trade sinyali olarak kullanma, "
    "strateji üretimi, backtest, optimizer, model training, prediction/target/label üretimi, "
    "production-ready/official approval iddiası, haber tam metni kullanımı, production deployment, "
    "model deployment, scraping veya gerçek provider API çağrısı değildir."
)


def build_feature_validation_disclaimer() -> str:
    """Return standard non-signal feature validation disclaimer."""
    return FEATURE_VALIDATION_DISCLAIMER


def build_feature_validation_profile_markdown_report(
    summary: Dict[str, Any], profile_df: Optional[pd.DataFrame] = None
) -> str:
    """Build Markdown report for validation profiles."""
    lines = [
        "# Phase 121: Feature Validation Profile Registry Report",
        "",
        f"> {FEATURE_VALIDATION_DISCLAIMER}",
        "",
        "## Summary",
        f"- **Active Profile**: `{summary.get('active_profile', 'N/A')}`",
        f"- **Total Profiles**: {summary.get('total_profiles', 0)}",
        f"- **Enabled Profiles**: {summary.get('enabled_profiles', 0)}",
        f"- **Current Phase**: {summary.get('current_phase', 121)}",
        f"- **Target Final Phase**: {summary.get('target_final_phase', 160)}",
        f"- **Next Phase**: {summary.get('next_phase', 122)}",
        f"- **Non-Signal Mandate**: {summary.get('non_signal_mandate', True)}",
        f"- **Zero-Leakage Mandate**: {summary.get('no_leakage_required', True)}",
        "",
    ]
    if profile_df is not None and not profile_df.empty:
        lines.append("## Registered Profiles")
        lines.append(profile_df.to_markdown(index=False))
        lines.append("")
    return "\n".join(lines)


def build_feature_validation_rule_markdown_report(
    summary: Dict[str, Any], rule_df: Optional[pd.DataFrame] = None
) -> str:
    """Build Markdown report for validation rules."""
    lines = [
        "# Phase 121: Feature Validation Rule Registry Report",
        "",
        f"> {FEATURE_VALIDATION_DISCLAIMER}",
        "",
        "## Summary",
        f"- **Total Rules Registered**: {summary.get('total_rules', 0)}",
        f"- **Critical Rules**: {summary.get('critical_rules', 0)}",
        f"- **High Severity Rules**: {summary.get('high_rules', 0)}",
        f"- **Medium Severity Rules**: {summary.get('medium_rules', 0)}",
        f"- **Non-Signal**: {summary.get('non_signal', True)}",
        "",
    ]
    if rule_df is not None and not rule_df.empty:
        lines.append("## Validation Rules")
        lines.append(rule_df.to_markdown(index=False))
        lines.append("")
    return "\n".join(lines)


def build_forbidden_column_markdown_report(
    summary: Dict[str, Any], forbidden_df: Optional[pd.DataFrame] = None
) -> str:
    """Build Markdown report for forbidden feature column specifications."""
    lines = [
        "# Phase 121: Forbidden Feature Column Registry Report",
        "",
        f"> {FEATURE_VALIDATION_DISCLAIMER}",
        "",
        "## Summary",
        f"- **Total Forbidden Patterns**: {summary.get('total_patterns', 0)}",
        f"- **Categories**: {', '.join(summary.get('pattern_categories', []))}",
        f"- **Enforced**: {summary.get('enforced', True)}",
        f"- **Destructive Cleaning Allowed**: {summary.get('destructive_cleaning_allowed', False)}",
        "",
    ]
    if forbidden_df is not None and not forbidden_df.empty:
        lines.append("## Prohibited Column Terms")
        lines.append(forbidden_df.to_markdown(index=False))
        lines.append("")
    return "\n".join(lines)


def build_no_lookahead_markdown_report(
    summary: Dict[str, Any], no_lookahead_df: Optional[pd.DataFrame] = None
) -> str:
    """Build Markdown report for no-lookahead guard rules."""
    lines = [
        "# Phase 121: No-Lookahead Guard Registry Report",
        "",
        f"> {FEATURE_VALIDATION_DISCLAIMER}",
        "",
        "## Summary",
        f"- **Total Lookahead Defense Rules**: {summary.get('total_rules', 0)}",
        f"- **Leakage Tolerance**: {summary.get('leakage_tolerance', 'zero')}",
        f"- **Non-Signal**: {summary.get('non_signal', True)}",
        "",
    ]
    if no_lookahead_df is not None and not no_lookahead_df.empty:
        lines.append("## Active Lookahead Rules")
        lines.append(no_lookahead_df.to_markdown(index=False))
        lines.append("")
    return "\n".join(lines)


def build_matrix_integrity_markdown_report(
    summary: Dict[str, Any], manifest_df: Optional[pd.DataFrame] = None
) -> str:
    """Build Markdown report for feature matrix integrity manifests."""
    lines = [
        "# Phase 121: Feature Matrix Integrity Manifest Report",
        "",
        f"> {FEATURE_VALIDATION_DISCLAIMER}",
        "",
        "## Summary",
        f"- **Total Manifests Created**: {summary.get('total_manifests', 0)}",
        f"- **All Non-Signal Verified**: {summary.get('all_non_signal', True)}",
        f"- **All Source Preserved**: {summary.get('all_source_preserved', True)}",
        "",
    ]
    if manifest_df is not None and not manifest_df.empty:
        lines.append("## Integrity Manifests")
        lines.append(manifest_df.to_markdown(index=False))
        lines.append("")
    return "\n".join(lines)


def build_validation_findings_markdown_report(
    summary: Dict[str, Any], findings_df: Optional[pd.DataFrame] = None
) -> str:
    """Build Markdown report for validation findings."""
    lines = [
        "# Phase 121: Feature Validation Findings Report",
        "",
        f"> {FEATURE_VALIDATION_DISCLAIMER}",
        "",
        "## Summary",
        f"- **Total Findings**: {summary.get('total_findings', 0)}",
        f"- **Critical**: {summary.get('critical_count', 0)}",
        f"- **High**: {summary.get('high_count', 0)}",
        f"- **Medium**: {summary.get('medium_count', 0)}",
        f"- **Manual Review Required**: {summary.get('manual_review_required_count', 0)}",
        f"- **Destructive Action Allowed**: {summary.get('destructive_action_allowed', False)}",
        "",
    ]
    if findings_df is not None and not findings_df.empty:
        lines.append("## Recorded Findings")
        lines.append(findings_df.to_markdown(index=False))
        lines.append("")
    return "\n".join(lines)


def build_validation_score_markdown_report(
    summary: Dict[str, Any], score_df: Optional[pd.DataFrame] = None
) -> str:
    """Build Markdown report for validation quality scoring."""
    lines = [
        "# Phase 121: Feature Validation Quality Score Report",
        "",
        f"> {FEATURE_VALIDATION_DISCLAIMER}",
        "",
        "## Summary",
        f"- **Matrices Scored**: {summary.get('total_matrices_scored', 0)}",
        f"- **Average Validation Score**: {summary.get('average_validation_score', 1.0)}",
        f"- **All Passed / Compliant**: {summary.get('all_passed', True)}",
        f"- **Official Approval Claim**: {summary.get('official_approval_claim', False)}",
        f"- **Production Ready Claim**: {summary.get('production_ready_claim', False)}",
        f"- **Non-Signal**: {summary.get('non_signal', True)}",
        "",
    ]
    if score_df is not None and not score_df.empty:
        lines.append("## Matrix Scores")
        lines.append(score_df.to_markdown(index=False))
        lines.append("")
    return "\n".join(lines)


def build_domain_output_validation_markdown_report(
    summary: Dict[str, Any], domain_df: Optional[pd.DataFrame] = None
) -> str:
    """Build Markdown report for domain feature outputs validation."""
    lines = [
        "# Phase 121: Domain Feature Outputs Validation Report",
        "",
        f"> {FEATURE_VALIDATION_DISCLAIMER}",
        "",
        "## Summary",
        f"- **Domain**: `{summary.get('domain', 'multi_domain')}`",
        f"- **Status**: `{summary.get('status', 'validation_pass')}`",
        f"- **Validation Passed**: {summary.get('validation_passed', True)}",
        f"- **Non-Signal**: {summary.get('non_signal', True)}",
        "",
    ]
    if domain_df is not None and not domain_df.empty:
        lines.append("## Inspected Matrices")
        lines.append(domain_df.to_markdown(index=False))
        lines.append("")
    return "\n".join(lines)


def build_no_leakage_guard_markdown_report(
    summary: Dict[str, Any], leakage_df: Optional[pd.DataFrame] = None
) -> str:
    """Build Markdown report for unified no-leakage guard."""
    lines = [
        "# Phase 121: No-Leakage Guard Status Report",
        "",
        f"> {FEATURE_VALIDATION_DISCLAIMER}",
        "",
        "## Summary",
        f"- **Total Defenses Enforced**: {summary.get('total_guards', 0)}",
        f"- **Leakage Tolerance**: {summary.get('leakage_tolerance', 'zero')}",
        f"- **Non-Signal**: {summary.get('non_signal', True)}",
        "",
    ]
    if leakage_df is not None and not leakage_df.empty:
        lines.append("## Active Defenses")
        lines.append(leakage_df.to_markdown(index=False))
        lines.append("")
    return "\n".join(lines)


def build_feature_validation_health_markdown_report(
    summary: Dict[str, Any], health_df: Optional[pd.DataFrame] = None
) -> str:
    """Build Markdown report for system health check."""
    lines = [
        "# Phase 121: Feature Validation Health Check Report",
        "",
        f"> {FEATURE_VALIDATION_DISCLAIMER}",
        "",
        "## Summary",
        f"- **Health Status**: `{summary.get('status', 'HEALTHY')}`",
        f"- **Checks Passed**: {summary.get('checks_passed', 0)} / {summary.get('total_checks', 0)}",
        f"- **Phase Invariant**: {summary.get('current_phase', 121)} -> {summary.get('next_phase', 122)}",
        "",
    ]
    if health_df is not None and not health_df.empty:
        lines.append("## Subsystem Health Details")
        lines.append(health_df.to_markdown(index=False))
        lines.append("")
    return "\n".join(lines)


def build_feature_validation_safety_markdown_report(
    summary: Dict[str, Any], safety_df: Optional[pd.DataFrame] = None
) -> str:
    """Build Markdown report for safety boundaries."""
    lines = [
        "# Phase 121: Feature Validation Safety Boundary Report",
        "",
        f"> {FEATURE_VALIDATION_DISCLAIMER}",
        "",
        "## Summary",
        f"- **Safety Status**: `{summary.get('status', 'SECURE')}`",
        f"- **NO-GO Invariants Enforced**: {summary.get('no_go_count', 0)}",
        f"- **SAFE-GO Invariants Active**: {summary.get('safe_go_count', 0)}",
        f"- **Live Trading Allowed**: {summary.get('allow_live_trading', False)}",
        f"- **Signal Production Allowed**: {summary.get('allow_signal_generation', False)}",
        "",
    ]
    if safety_df is not None and not safety_df.empty:
        lines.append("## Boundary Details")
        lines.append(safety_df.to_markdown(index=False))
        lines.append("")
    return "\n".join(lines)


def build_phase_122_handoff_markdown_report(
    summary: Dict[str, Any], handoff_df: Optional[pd.DataFrame] = None
) -> str:
    """Build Markdown report for Phase 122 Factor Metadata handoff."""
    lines = [
        "# Phase 121 -> Phase 122 Factor Metadata Handoff Report",
        "",
        f"> {FEATURE_VALIDATION_DISCLAIMER}",
        "",
        "## Summary",
        f"- **Current Phase**: {summary.get('current_phase', 121)}",
        f"- **Next Phase**: {summary.get('next_phase', 122)} (Factor Metadata and Factor Families)",
        f"- **Handoff Status**: `{summary.get('handoff_status', 'READY')}`",
        f"- **Validated Feature Families**: {summary.get('validated_family_count', 0)}",
        f"- **Readiness Verified**: {summary.get('readiness_verified', True)}",
        "",
    ]
    if handoff_df is not None and not handoff_df.empty:
        lines.append("## Handoff Deliverables")
        lines.append(handoff_df.to_markdown(index=False))
        lines.append("")
    return "\n".join(lines)


def build_feature_validation_report(
    pipeline_result: Dict[str, Any], profile_name: str = "default"
) -> Dict[str, Any]:
    """Assemble structured feature validation report dictionary."""
    scores = pipeline_result.get("scores", {})
    manifest = pipeline_result.get("manifest", {})
    findings = pipeline_result.get("findings", [])

    return {
        "report_id": f"REP-VAL-121-{profile_name}",
        "profile_name": profile_name,
        "current_phase": 121,
        "target_final_phase": 160,
        "next_phase": 122,
        "status": pipeline_result.get("status", "PASS"),
        "scores": scores,
        "findings": findings,
        "manifest": manifest,
        "disclaimer": FEATURE_VALIDATION_DISCLAIMER,
        "destructive_action_allowed": False,
        "non_signal": True,
    }


def build_feature_validation_markdown_report(report: Dict[str, Any]) -> str:
    """Generate Markdown report from feature validation report dictionary."""
    scores = report.get("scores", {})
    overall = scores.get("overall_score", 1.0)

    lines = [
        "# Phase 121: Feature Validation and No-Lookahead Guard Report",
        "",
        f"> {report.get('disclaimer', FEATURE_VALIDATION_DISCLAIMER)}",
        "",
        "## Overall Quality Score",
        f"- **Overall Score**: `{overall}`",
        f"- **Status**: `{report.get('status', 'PASS')}`",
        f"- **Lookahead Score**: `{scores.get('lookahead_score', 1.0)}`",
        f"- **Forbidden Column Score**: `{scores.get('forbidden_column_score', 1.0)}`",
        f"- **Integrity Score**: `{scores.get('integrity_score', 1.0)}`",
        f"- **Numeric Sanity Score**: `{scores.get('numeric_sanity_score', 1.0)}`",
        f"- **Completeness Score**: `{scores.get('completeness_score', 1.0)}`",
        "",
        "## Summary",
        f"- **Profile**: `{report.get('profile_name', 'default')}`",
        f"- **Current Phase**: 121",
        f"- **Target Final Phase**: 160",
        f"- **Next Phase**: 122",
        "",
    ]
    return "\n".join(lines)


def build_feature_validation_text_summary(report: Dict[str, Any]) -> str:
    """Generate text summary of feature validation report."""
    scores = report.get("scores", {})
    return (
        f"Phase 121 Feature Validation Report | Status: {report.get('status', 'PASS')} | "
        f"Overall Score: {scores.get('overall_score', 1.0)} | Profile: {report.get('profile_name', 'default')}"
    )

