"""Phase 123 Feature Quality and Drift Report Builder.

Generates markdown reports and standardized diagnostic summaries with mandatory
research disclaimer banners.
"""

from typing import Any, Dict
import pandas as pd

DISCLAIMER = (
    "Bu çıktı Phase 123 Feature Quality and Drift Diagnostics raporudur. "
    "Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, quality/drift score’u trade sinyali "
    "olarak kullanma, strateji üretimi, backtest, optimizer, model training, prediction/target/label "
    "üretimi, production-ready/official approval iddiası, otomatik feature silme/düzeltme, "
    "haber tam metni kullanımı, production deployment, model deployment, scraping veya gerçek provider "
    "API çağrısı değildir."
)


def _df_to_markdown(df: pd.DataFrame | None) -> str:
    """Format DataFrame as pure markdown table without third-party dependencies."""
    if df is None or df.empty:
        return ""
    cols = [str(c) for c in df.columns]
    header_row = "| " + " | ".join(cols) + " |"
    sep_row = "| " + " | ".join(["---"] * len(cols)) + " |"
    body_rows = []
    for _, row in df.iterrows():
        body_rows.append("| " + " | ".join(str(row[c]) for c in df.columns) + " |")
    return "\n".join([header_row, sep_row] + body_rows)


def build_feature_quality_drift_disclaimer() -> str:
    """Return mandatory disclaimer banner."""
    return f"> **UYARI VE BİLGİLENDİRME:** {DISCLAIMER}\n"


def build_feature_quality_drift_profile_markdown_report(summary: Dict[str, Any], profile_df: pd.DataFrame | None = None) -> str:
    lines = [
        "# Phase 123: Feature Quality and Drift Profile Registry",
        "",
        build_feature_quality_drift_disclaimer(),
        f"- **Active Profile:** {summary.get('active_profile')}",
        f"- **Total Profiles:** {summary.get('total_profiles')}",
        f"- **Current Phase:** {summary.get('current_phase')}",
        f"- **Target Final Phase:** {summary.get('target_final_phase')}",
        f"- **Next Phase:** {summary.get('next_phase')}",
        f"- **Non-Signal Mandate:** {summary.get('non_signal')}",
        f"- **Local Only:** {summary.get('local_only')}",
        f"- **Research Only:** {summary.get('research_only')}",
        "",
    ]
    if profile_df is not None and not profile_df.empty:
        lines.append("## Configured Diagnostic Profiles")
        lines.append(_df_to_markdown(profile_df))
    return "\n".join(lines)


def build_quality_metric_markdown_report(summary: Dict[str, Any], metric_df: pd.DataFrame | None = None) -> str:
    lines = [
        "# Phase 123: Feature Quality Metric Registry",
        "",
        build_feature_quality_drift_disclaimer(),
        f"- **Active Profile:** {summary.get('active_profile')}",
        f"- **Total Quality Metrics:** {summary.get('total_quality_metrics')}",
        f"- **Current Phase:** {summary.get('current_phase')}",
        "",
    ]
    if metric_df is not None and not metric_df.empty:
        lines.append("## Registered Quality Metrics")
        lines.append(_df_to_markdown(metric_df))
    return "\n".join(lines)


def build_drift_metric_markdown_report(summary: Dict[str, Any], metric_df: pd.DataFrame | None = None) -> str:
    lines = [
        "# Phase 123: Feature Drift Metric Registry",
        "",
        build_feature_quality_drift_disclaimer(),
        f"- **Active Profile:** {summary.get('active_profile')}",
        f"- **Total Drift Metrics:** {summary.get('total_drift_metrics')}",
        f"- **Current Phase:** {summary.get('current_phase')}",
        "",
    ]
    if metric_df is not None and not metric_df.empty:
        lines.append("## Registered Drift Metrics")
        lines.append(_df_to_markdown(metric_df))
    return "\n".join(lines)


def build_missingness_markdown_report(summary: Dict[str, Any], df: pd.DataFrame | None = None) -> str:
    lines = [
        "# Phase 123: Feature Missingness Diagnostics Report",
        "",
        build_feature_quality_drift_disclaimer(),
        f"- **Total Features Evaluated:** {summary.get('total_features')}",
        f"- **Critical Missingness (>50%):** {summary.get('critical_missingness_count')}",
        f"- **Warning Missingness (>25%):** {summary.get('warning_missingness_count')}",
        f"- **Clean Features:** {summary.get('clean_features_count')}",
        f"- **Max Missingness Ratio:** {summary.get('max_missingness_ratio')}",
        f"- **Status:** {summary.get('status')}",
        f"- **Manual Review Required:** {summary.get('manual_review_required')}",
        "",
    ]
    if df is not None and not df.empty:
        lines.append("## Feature Column Missingness Details")
        lines.append(_df_to_markdown(df))
    return "\n".join(lines)


def build_distribution_drift_markdown_report(summary: Dict[str, Any], df: pd.DataFrame | None = None) -> str:
    lines = [
        "# Phase 123: Feature Distribution Drift Report",
        "",
        build_feature_quality_drift_disclaimer(),
        f"- **Features Compared:** {summary.get('total_features_compared')}",
        f"- **Critical Drift:** {summary.get('critical_drift_count')}",
        f"- **Warning Drift:** {summary.get('warning_drift_count')}",
        f"- **Stable Features:** {summary.get('stable_features_count')}",
        f"- **Status:** {summary.get('status')}",
        f"- **Manual Review Required:** {summary.get('manual_review_required')}",
        "",
    ]
    if df is not None and not df.empty:
        lines.append("## Distribution Drift Details (Baseline vs Current)")
        lines.append(_df_to_markdown(df))
    return "\n".join(lines)


def build_factor_quality_markdown_report(summary: Dict[str, Any], df: pd.DataFrame | None = None) -> str:
    lines = [
        "# Phase 123: Factor Family Quality Report",
        "",
        build_feature_quality_drift_disclaimer(),
        f"- **Total Factor Families:** {summary.get('total_families')}",
        f"- **Passed Families:** {summary.get('passed_families')}",
        f"- **Review Required Families:** {summary.get('review_required_families')}",
        f"- **Mean Quality Score:** {summary.get('mean_family_quality_score')}",
        f"- **Status:** {summary.get('status')}",
        "",
    ]
    if df is not None and not df.empty:
        lines.append("## Factor Families Quality Breakdown")
        lines.append(_df_to_markdown(df))
    return "\n".join(lines)


def build_macro_cross_asset_quality_markdown_report(summary: Dict[str, Any], df: pd.DataFrame | None = None) -> str:
    lines = [
        "# Phase 123: Macro, Calendar, News & Cross-Asset Quality Report",
        "",
        build_feature_quality_drift_disclaimer(),
        f"- **Total Checks:** {summary.get('total_checks')}",
        f"- **Passed Checks:** {summary.get('passed_checks')}",
        f"- **Failed Checks:** {summary.get('failed_checks')}",
        f"- **Metadata-Only Boundary Compliant:** {summary.get('metadata_only_boundary_compliant', True)}",
        f"- **Status:** {summary.get('status')}",
        "",
    ]
    if df is not None and not df.empty:
        lines.append("## Diagnostic Checks Breakdown")
        lines.append(_df_to_markdown(df))
    return "\n".join(lines)


def build_quality_findings_markdown_report(summary: Dict[str, Any], df: pd.DataFrame | None = None) -> str:
    lines = [
        "# Phase 123: Feature Quality Findings Registry Report",
        "",
        build_feature_quality_drift_disclaimer(),
        f"- **Total Findings:** {summary.get('total_findings')}",
        f"- **Critical Findings:** {summary.get('critical_findings')}",
        f"- **High Severity Findings:** {summary.get('high_findings')}",
        f"- **Medium Severity Findings:** {summary.get('medium_findings')}",
        f"- **Status:** {summary.get('status')}",
        f"- **Manual Review Required:** {summary.get('manual_review_required')}",
        "",
    ]
    if df is not None and not df.empty:
        lines.append("## Quality Findings Ledger")
        lines.append(_df_to_markdown(df))
    return "\n".join(lines)


def build_drift_findings_markdown_report(summary: Dict[str, Any], df: pd.DataFrame | None = None) -> str:
    lines = [
        "# Phase 123: Feature Drift Findings Registry Report",
        "",
        build_feature_quality_drift_disclaimer(),
        f"- **Total Drift Findings:** {summary.get('total_drift_findings')}",
        f"- **Critical Drift Findings:** {summary.get('critical_drift_findings')}",
        f"- **High Drift Findings:** {summary.get('high_drift_findings')}",
        f"- **Status:** {summary.get('status')}",
        f"- **Manual Review Required:** {summary.get('manual_review_required')}",
        "",
    ]
    if df is not None and not df.empty:
        lines.append("## Drift Findings Ledger")
        lines.append(_df_to_markdown(df))
    return "\n".join(lines)


def build_quality_drift_score_markdown_report(summary: Dict[str, Any], df: pd.DataFrame | None = None) -> str:
    lines = [
        "# Phase 123: Feature Quality & Drift Score Report",
        "",
        build_feature_quality_drift_disclaimer(),
        f"- **Overall Score:** {summary.get('overall_quality_score', summary.get('overall_drift_score'))}",
        f"- **Current Phase:** {summary.get('current_phase')}",
        f"- **Target Final Phase:** {summary.get('target_final_phase')}",
        f"- **Status:** {summary.get('quality_status', summary.get('drift_status', 'diagnostic_pass'))}",
        f"- **Non-Signal Mandate:** True",
        f"- **Official Approval Claim:** False",
        f"- **Production Ready Claim:** False",
        "",
    ]
    if df is not None and not df.empty:
        lines.append("## Dimension Scores Breakdown")
        lines.append(_df_to_markdown(df))
    return "\n".join(lines)


def build_quality_drift_manifest_markdown_report(summary: Dict[str, Any], df: pd.DataFrame | None = None) -> str:
    lines = [
        "# Phase 123: Feature Quality & Drift Manifest Report",
        "",
        build_feature_quality_drift_disclaimer(),
        f"- **Total Matrices Logged:** {summary.get('total_matrices')}",
        f"- **Total Features Covered:** {summary.get('total_features')}",
        f"- **Total Pending Manual Reviews:** {summary.get('total_manual_reviews')}",
        f"- **All Sources Preserved:** {summary.get('all_source_preserved')}",
        f"- **All Non-Signal:** {summary.get('all_non_signal')}",
        "",
    ]
    if df is not None and not df.empty:
        lines.append("## Quality & Drift Manifest Matrix")
        lines.append(_df_to_markdown(df))
    return "\n".join(lines)


def build_quality_drift_health_markdown_report(summary: Dict[str, Any], df: pd.DataFrame | None = None) -> str:
    lines = [
        "# Phase 123: Feature Quality & Drift Health Check Report",
        "",
        build_feature_quality_drift_disclaimer(),
        f"- **Health Status:** {summary.get('status')}",
        f"- **Total Components Verified:** {summary.get('total_components')}",
        f"- **Healthy Components:** {summary.get('healthy_components')}",
        f"- **Unhealthy Components:** {summary.get('unhealthy_components')}",
        "",
    ]
    if df is not None and not df.empty:
        lines.append("## Health Verification Details")
        lines.append(_df_to_markdown(df))
    return "\n".join(lines)


def build_quality_drift_safety_markdown_report(summary: Dict[str, Any], df: pd.DataFrame | None = None) -> str:
    lines = [
        "# Phase 123: Feature Quality & Drift Safety Boundary Report",
        "",
        build_feature_quality_drift_disclaimer(),
        f"- **Safety Status:** {summary.get('safety_status', 'SECURE')}",
        f"- **Enforced NO-GO Rules:** {summary.get('no_go_count')}",
        f"- **Active SAFE-GO Principles:** {summary.get('safe_go_count')}",
        f"- **Destructive Action Allowed:** {summary.get('destructive_action_allowed', False)}",
        f"- **Non-Signal Mandate Enforced:** {summary.get('non_signal', True)}",
        "",
    ]
    if df is not None and not df.empty:
        lines.append("## Safety Rules Ledger")
        lines.append(_df_to_markdown(df))
    return "\n".join(lines)


def build_phase_124_handoff_markdown_report(summary: Dict[str, Any], df: pd.DataFrame | None = None) -> str:
    lines = [
        "# Phase 123 -> Phase 124: Feature Store Integration Handoff Report",
        "",
        build_feature_quality_drift_disclaimer(),
        f"- **Handoff Status:** {summary.get('handoff_status')}",
        f"- **Source Phase:** {summary.get('source_phase')}",
        f"- **Next Phase:** {summary.get('next_phase')}",
        f"- **Target Final Phase:** {summary.get('target_final_phase')}",
        f"- **Total Handoff Prerequisites:** {summary.get('total_items')}",
        f"- **Ready Prerequisites:** {summary.get('ready_items')}",
        f"- **Non-Signal Invariant:** {summary.get('non_signal')}",
        "",
    ]
    if df is not None and not df.empty:
        lines.append("## Handoff Deliverables & Prerequisites")
        lines.append(_df_to_markdown(df))
    return "\n".join(lines)
