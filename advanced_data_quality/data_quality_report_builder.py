from typing import Dict, Any, Optional
import pandas as pd


def build_data_quality_disclaimer() -> str:
    return (
        "Bu çıktı Phase 112 Data Quality Engine raporudur. "
        "Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, "
        "quality score’u trade sinyali olarak kullanma, provider official approval, "
        "production deployment, model deployment, scraping, haber tam metni toplama, "
        "telifli içerik kopyalama, external LLM/API çağrısı, gerçek provider API çağrısı "
        "zorunluluğu veya destructive auto-cleaning değildir."
    )


def _df_to_markdown(df: Optional[pd.DataFrame]) -> str:
    if df is None or df.empty:
        return ""
    try:
        return df.to_markdown(index=False)
    except Exception:
        cols = list(df.columns)
        header = "| " + " | ".join(str(c) for c in cols) + " |"
        sep = "| " + " | ".join("---" for _ in cols) + " |"
        rows = []
        for _, row in df.iterrows():
            rows.append("| " + " | ".join(str(row[c]) for c in cols) + " |")
        return "\n".join([header, sep] + rows)


def build_data_quality_profile_markdown_report(
    summary: Dict[str, Any],
    profile_df: Optional[pd.DataFrame] = None
) -> str:
    lines = [
        "# Data Quality Profile Registry Report",
        "",
        f"> {build_data_quality_disclaimer()}",
        "",
        "## Summary",
        f"- Total Profiles: {summary.get('total_profiles', 0)}",
        f"- Dry-Run Mode: {summary.get('dry_run_all', True)}",
        f"- Local Only: {summary.get('local_only_all', True)}",
        f"- Current Phase: {summary.get('current_phase', 112)}",
        f"- Target Final Phase: {summary.get('target_final_phase', 160)}",
        "",
    ]
    if profile_df is not None and not profile_df.empty:
        lines.append("## Registered Profiles")
        lines.append(_df_to_markdown(profile_df))
        lines.append("")
    return "\n".join(lines)


def build_quality_rule_registry_markdown_report(
    summary: Dict[str, Any],
    rules_df: Optional[pd.DataFrame] = None
) -> str:
    lines = [
        "# Quality Rule Registry Report",
        "",
        f"> {build_data_quality_disclaimer()}",
        "",
        "## Summary",
        f"- Total Rules: {summary.get('total_rules', 0)}",
        f"- Domains: {len(summary.get('domains', []))}",
        "",
    ]
    if rules_df is not None and not rules_df.empty:
        lines.append("## Rule Catalog")
        lines.append(_df_to_markdown(rules_df))
        lines.append("")
    return "\n".join(lines)


def build_quality_findings_markdown_report(
    summary: Dict[str, Any],
    findings_df: Optional[pd.DataFrame] = None
) -> str:
    lines = [
        "# Quality Findings Registry Report",
        "",
        f"> {build_data_quality_disclaimer()}",
        "",
        "## Summary",
        f"- Total Findings: {summary.get('total_findings', 0)}",
        f"- Critical: {summary.get('critical_count', 0)}",
        f"- High: {summary.get('high_count', 0)}",
        f"- Medium: {summary.get('medium_count', 0)}",
        f"- Low: {summary.get('low_count', 0)}",
        f"- Info: {summary.get('info_count', 0)}",
        "",
    ]
    if findings_df is not None and not findings_df.empty:
        lines.append("## Findings Table")
        lines.append(_df_to_markdown(findings_df))
        lines.append("")
    return "\n".join(lines)


def build_manual_review_queue_markdown_report(
    summary: Dict[str, Any],
    review_df: Optional[pd.DataFrame] = None
) -> str:
    lines = [
        "# Manual Review Queue Report",
        "",
        f"> {build_data_quality_disclaimer()}",
        "",
        "## Summary",
        f"- Total Review Items: {summary.get('total_review_items', 0)}",
        f"- Destructive Action Allowed: {summary.get('destructive_action_allowed_any', False)}",
        "",
        "> **Notice**: Destructive auto-cleaning is strictly forbidden. All items remain in this queue for human inspection or Phase 113 normalization.",
        "",
    ]
    if review_df is not None and not review_df.empty:
        lines.append("## Review Items")
        lines.append(_df_to_markdown(review_df))
        lines.append("")
    return "\n".join(lines)


def build_provider_quality_score_markdown_report(
    summary: Dict[str, Any],
    score_df: Optional[pd.DataFrame] = None
) -> str:
    lines = [
        "# Provider Quality Score Report",
        "",
        f"> {build_data_quality_disclaimer()}",
        "",
        "## Summary",
        f"- Total Providers Scored: {summary.get('total_providers_scored', 0)}",
        f"- Average Score: {summary.get('average_score', 0.0):.2f}",
        "",
        "> **Caution**: Quality score is strictly an internal research/diagnostic metric and NOT a trading signal or official certification.",
        "",
    ]
    if score_df is not None and not score_df.empty:
        lines.append("## Provider Scores")
        lines.append(_df_to_markdown(score_df))
        lines.append("")
    return "\n".join(lines)


def build_dataset_quality_score_markdown_report(
    summary: Dict[str, Any],
    score_df: Optional[pd.DataFrame] = None
) -> str:
    lines = [
        "# Dataset Quality Score Report",
        "",
        f"> {build_data_quality_disclaimer()}",
        "",
        "## Summary",
        f"- Total Datasets Scored: {summary.get('total_datasets_scored', 0)}",
        f"- Average Score: {summary.get('average_score', 0.0):.2f}",
        "",
    ]
    if score_df is not None and not score_df.empty:
        lines.append("## Dataset Scores")
        lines.append(_df_to_markdown(score_df))
        lines.append("")
    return "\n".join(lines)


def build_data_quality_health_markdown_report(
    summary: Dict[str, Any],
    health_df: Optional[pd.DataFrame] = None
) -> str:
    lines = [
        "# Data Quality Health Check Report",
        "",
        f"> {build_data_quality_disclaimer()}",
        "",
        "## Summary",
        f"- Total Checks: {summary.get('total_checks', 0)}",
        f"- Passing: {summary.get('passing_checks', 0)}",
        f"- Failing: {summary.get('failing_checks', 0)}",
        f"- Health Rate: {summary.get('health_rate', 0.0) * 100:.1f}%",
        "",
    ]
    if health_df is not None and not health_df.empty:
        lines.append("## Health Findings")
        lines.append(_df_to_markdown(health_df))
        lines.append("")
    return "\n".join(lines)


def build_data_quality_validation_markdown_report(
    summary: Dict[str, Any],
    val_df: Optional[pd.DataFrame] = None
) -> str:
    lines = [
        "# Data Quality Validation Report",
        "",
        f"> {build_data_quality_disclaimer()}",
        "",
        "## Summary",
        f"- Valid: {summary.get('valid', False)}",
        f"- Total Validations: {summary.get('total_validations', 0)}",
        f"- Current Phase: {summary.get('current_phase', 112)}",
        f"- Target Final Phase: {summary.get('target_final_phase', 160)}",
        "",
    ]
    if val_df is not None and not val_df.empty:
        lines.append("## Validation Results")
        lines.append(_df_to_markdown(val_df))
        lines.append("")
    return "\n".join(lines)


def build_data_quality_safety_markdown_report(
    summary: Dict[str, Any],
    safety_df: Optional[pd.DataFrame] = None
) -> str:
    lines = [
        "# Data Quality Safety Boundary Report",
        "",
        f"> {build_data_quality_disclaimer()}",
        "",
        "## Summary",
        f"- Total Conditions: {summary.get('total_conditions', 0)}",
        f"- No-Go Conditions: {summary.get('no_go_count', 0)}",
        f"- Safe-Go Conditions: {summary.get('safe_go_count', 0)}",
        "",
    ]
    if safety_df is not None and not safety_df.empty:
        lines.append("## Safety Boundary Rules")
        lines.append(_df_to_markdown(safety_df))
        lines.append("")
    return "\n".join(lines)


def build_phase_113_handoff_markdown_report(
    summary: Dict[str, Any],
    handoff_df: Optional[pd.DataFrame] = None
) -> str:
    lines = [
        "# Phase 113 Normalization Handoff Report",
        "",
        f"> {build_data_quality_disclaimer()}",
        "",
        "## Summary",
        f"- Target Phase: {summary.get('target_phase', 113)} ({summary.get('target_phase_name', '')})",
        f"- Total Areas: {summary.get('total_areas', 0)}",
        f"- Manual Review Items Required: {summary.get('manual_review_count', 0)}",
        "",
    ]
    if handoff_df is not None and not handoff_df.empty:
        lines.append("## Normalization Scope")
        lines.append(_df_to_markdown(handoff_df))
        lines.append("")
    return "\n".join(lines)
