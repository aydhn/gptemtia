# -*- coding: utf-8 -*-
"""
Phase 137 - Advanced ML Dataset Contracts and Experiment Registry
Markdown Report Builder.

Generates audit and governance markdown reports with mandatory disclaimers.
"""

from typing import Dict, Optional
import pandas as pd

DISCLAIMER_TEXT = (
    "> [!WARNING]\n"
    "> **YASAL UYARI VE GOVERNANCE BİLDİRİMİ (PHASE 137)**:\n"
    "> Bu çıktı Phase 137 Advanced ML Dataset Contracts and Experiment Registry raporudur.\n"
    "> Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, dataset/experiment/readiness "
    "> değerini trade sinyali veya production-ready/broker-ready onayı olarak kullanma, "
    "> dataset materialization, feature snapshot materialization, strateji üretimi, backtest, "
    "> optimizer, model training, model fit/predict/inference, clustering, ensemble, calibration, "
    "> prediction/target/label üretimi, sentiment model output, haber tam metni/article body/raw "
    "> content/scraped HTML/embedding/vector kullanımı, production deployment, model deployment, "
    "> scraping veya gerçek provider API çağrısı değildir.\n"
)


def build_advanced_ml_dataset_disclaimer() -> str:
    """Return standard disclaimer string."""
    return DISCLAIMER_TEXT


def build_advanced_ml_dataset_profile_markdown_report(
    summary: Dict,
    profile_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for dataset profiles."""
    lines = [
        "# Phase 137: Advanced ML Dataset Profiles Report",
        "",
        build_advanced_ml_dataset_disclaimer(),
        "",
        "## Summary",
        f"- **Total Profiles**: {summary.get('total_profiles', 0)}",
        f"- **Enabled Profiles**: {summary.get('enabled_profiles', 0)}",
        f"- **Non-Signal Certified**: {summary.get('non_signal', True)}",
        f"- **Current Phase**: {summary.get('current_phase', 137)}",
        f"- **Target Final Phase**: {summary.get('target_final_phase', 160)}",
        "",
    ]
    if profile_df is not None and not profile_df.empty:
        lines.append("## Profiles Table")
        lines.append(profile_df.to_markdown(index=False))
    return "\n".join(lines)


def build_ml_dataset_contract_markdown_report(
    summary: Dict,
    contract_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for dataset contracts."""
    lines = [
        "# Phase 137: ML Dataset Contracts Report",
        "",
        build_advanced_ml_dataset_disclaimer(),
        "",
        "## Summary",
        f"- **Total Contracts**: {summary.get('total_contracts', 0)}",
        f"- **Materialization Allowed**: {summary.get('materialization_allowed', False)}",
        f"- **Target/Label Generation Allowed**: {summary.get('target_label_allowed', False)}",
        f"- **Training Allowed**: {summary.get('training_allowed', False)}",
        f"- **Prediction Allowed**: {summary.get('prediction_allowed', False)}",
        f"- **Non-Signal Enforced**: {summary.get('non_signal', True)}",
        "",
    ]
    if contract_df is not None and not contract_df.empty:
        lines.append("## Contracts Table")
        lines.append(contract_df.to_markdown(index=False))
    return "\n".join(lines)


def build_ml_dataset_schema_markdown_report(
    summary: Dict,
    schema_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for dataset schemas."""
    lines = [
        "# Phase 137: ML Dataset Schema Policies Report",
        "",
        build_advanced_ml_dataset_disclaimer(),
        "",
        "## Summary",
        f"- **Total Schemas**: {summary.get('total_schemas', 0)}",
        f"- **Forbidden Columns Enforced**: {summary.get('forbidden_columns_enforced', True)}",
        f"- **Timestamp UTC Required**: {summary.get('timestamp_utc_required', True)}",
        "",
    ]
    if schema_df is not None and not schema_df.empty:
        lines.append("## Schema Definitions")
        lines.append(schema_df.to_markdown(index=False))
    return "\n".join(lines)


def build_ml_dataset_split_policy_markdown_report(
    summary: Dict,
    split_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for split policies."""
    lines = [
        "# Phase 137: ML Dataset Split Policies Report",
        "",
        build_advanced_ml_dataset_disclaimer(),
        "",
        "## Summary",
        f"- **Total Split Policies**: {summary.get('total_split_policies', 0)}",
        f"- **Split Execution Blocked**: {summary.get('split_execution_blocked', True)}",
        f"- **Purged Placeholder Active**: {summary.get('purged_placeholder_active', True)}",
        "",
    ]
    if split_df is not None and not split_df.empty:
        lines.append("## Split Policies Table")
        lines.append(split_df.to_markdown(index=False))
    return "\n".join(lines)


def build_ml_dataset_guard_markdown_report(
    summary: Dict,
    guard_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for dataset guards."""
    lines = [
        "# Phase 137: ML Dataset Safety Guards Report",
        "",
        build_advanced_ml_dataset_disclaimer(),
        "",
        "## Summary",
        f"- **Leakage Guards Active**: {summary.get('leakage_guards_active', True)}",
        f"- **No-Lookahead Guards Active**: {summary.get('no_lookahead_guards_active', True)}",
        f"- **Metadata-Only News Guards Active**: {summary.get('metadata_only_news_guards_active', True)}",
        f"- **Source Preservation Active**: {summary.get('source_preservation_active', True)}",
        "",
    ]
    if guard_df is not None and not guard_df.empty:
        lines.append("## Safety Guards Table")
        lines.append(guard_df.to_markdown(index=False))
    return "\n".join(lines)


def build_feature_snapshot_contract_markdown_report(
    summary: Dict,
    snapshot_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for feature snapshot contracts."""
    lines = [
        "# Phase 137: Feature Snapshot Contracts Report",
        "",
        build_advanced_ml_dataset_disclaimer(),
        "",
        "## Summary",
        f"- **Total Snapshot Contracts**: {summary.get('total_snapshot_contracts', 0)}",
        f"- **All Unmaterialized**: {summary.get('all_unmaterialized', True)}",
        f"- **Production Ready**: {summary.get('production_ready', False)}",
        "",
    ]
    if snapshot_df is not None and not snapshot_df.empty:
        lines.append("## Feature Snapshot Contracts Table")
        lines.append(snapshot_df.to_markdown(index=False))
    return "\n".join(lines)


def build_ml_experiment_registry_markdown_report(
    summary: Dict,
    experiment_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for experiment registry."""
    lines = [
        "# Phase 137: ML Experiment Registry Report",
        "",
        build_advanced_ml_dataset_disclaimer(),
        "",
        "## Summary",
        f"- **Total Experiments**: {summary.get('total_experiments', 0)}",
        f"- **Training Blocked**: {summary.get('training_blocked', True)}",
        f"- **Prediction Blocked**: {summary.get('prediction_blocked', True)}",
        f"- **Artifact Persistence Blocked**: {summary.get('artifact_persistence_blocked', True)}",
        "",
    ]
    if experiment_df is not None and not experiment_df.empty:
        lines.append("## Experiments Table")
        lines.append(experiment_df.to_markdown(index=False))
    return "\n".join(lines)


def build_ml_dataset_findings_markdown_report(
    summary: Dict,
    findings_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for findings."""
    lines = [
        "# Phase 137: ML Dataset Findings Report",
        "",
        build_advanced_ml_dataset_disclaimer(),
        "",
        "## Summary",
        f"- **Total Findings**: {summary.get('total_findings', 0)}",
        f"- **Critical Findings**: {summary.get('critical_findings', 0)}",
        f"- **Warning Findings**: {summary.get('warning_findings', 0)}",
        f"- **Auto-Fix Allowed**: {summary.get('auto_fix_allowed', False)}",
        "",
    ]
    if findings_df is not None and not findings_df.empty:
        lines.append("## Findings Table")
        lines.append(findings_df.to_markdown(index=False))
    return "\n".join(lines)


def build_ml_dataset_readiness_score_markdown_report(
    summary: Dict,
    score_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for readiness scoring."""
    lines = [
        "# Phase 137: ML Dataset Readiness Score Report",
        "",
        build_advanced_ml_dataset_disclaimer(),
        "",
        "## Summary",
        f"- **Readiness Score**: {summary.get('readiness_score', 1.0)}",
        f"- **Classification**: {summary.get('classification', 'READY_FOR_LOCAL_ML_CONTRACTS')}",
        f"- **Is Minimum Passed**: {summary.get('is_minimum_passed', True)}",
        f"- **Training Approved**: {summary.get('training_approved', False)}",
        f"- **Production Ready**: {summary.get('production_ready', False)}",
        "",
    ]
    if score_df is not None and not score_df.empty:
        lines.append("## Score Details")
        lines.append(score_df.to_markdown(index=False))
    return "\n".join(lines)


def build_advanced_ml_dataset_manifest_markdown_report(
    summary: Dict,
    manifest_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for manifest."""
    lines = [
        "# Phase 137: Advanced ML Dataset Manifest Report",
        "",
        build_advanced_ml_dataset_disclaimer(),
        "",
        "## Summary",
        f"- **Manifest Name**: {summary.get('manifest_name', 'advanced_ml_dataset_manifest')}",
        f"- **Current Phase**: {summary.get('current_phase', 137)}",
        f"- **Next Phase**: {summary.get('next_phase', 138)}",
        f"- **Target Final Phase**: {summary.get('target_final_phase', 160)}",
        f"- **Readiness Score**: {summary.get('readiness_score', 1.0)}",
        f"- **Status**: {summary.get('status', 'dataset_contract_placeholder_only')}",
        "",
    ]
    if manifest_df is not None and not manifest_df.empty:
        lines.append("## Manifest Details")
        lines.append(manifest_df.to_markdown(index=False))
    return "\n".join(lines)


def build_advanced_ml_dataset_validation_markdown_report(
    summary: Dict,
    validation_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for validation."""
    lines = [
        "# Phase 137: Advanced ML Dataset Validation Report",
        "",
        build_advanced_ml_dataset_disclaimer(),
        "",
        "## Summary",
        f"- **All Validations Passed**: {summary.get('all_passed', True)}",
        f"- **Total Checks**: {summary.get('total_checks', 0)}",
        f"- **Passed Checks**: {summary.get('passed_checks', 0)}",
        f"- **Forbidden Claims Clean**: {summary.get('forbidden_claims_clean', True)}",
        "",
    ]
    if validation_df is not None and not validation_df.empty:
        lines.append("## Validation Results Table")
        lines.append(validation_df.to_markdown(index=False))
    return "\n".join(lines)


def build_advanced_ml_dataset_safety_markdown_report(
    summary: Dict,
    safety_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for safety boundary."""
    lines = [
        "# Phase 137: Advanced ML Dataset Safety Boundary Report",
        "",
        build_advanced_ml_dataset_disclaimer(),
        "",
        "## Summary",
        f"- **Safety Status**: {summary.get('safety_status', 'SECURE')}",
        f"- **NO-GO Conditions Enforced**: {summary.get('no_go_count', 22)}",
        f"- **SAFE-GO Principles Active**: {summary.get('safe_go_count', 12)}",
        f"- **Live Trading Prohibited**: True",
        f"- **Model Training Blocked**: True",
        "",
    ]
    if safety_df is not None and not safety_df.empty:
        lines.append("## Safety Boundaries Table")
        lines.append(safety_df.to_markdown(index=False))
    return "\n".join(lines)


def build_phase_138_handoff_markdown_report(
    summary: Dict,
    handoff_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for Phase 138 handoff."""
    lines = [
        "# Phase 137 to Phase 138 Handoff Report",
        "",
        build_advanced_ml_dataset_disclaimer(),
        "",
        "## Summary",
        f"- **Handoff Status**: {summary.get('handoff_status', 'READY_FOR_PHASE_138')}",
        f"- **Source Phase**: {summary.get('source_phase', 137)}",
        f"- **Next Phase**: {summary.get('next_phase', 138)}",
        f"- **Target Final Phase**: {summary.get('target_final_phase', 160)}",
        f"- **Total Prerequisites**: {summary.get('total_prerequisites', 0)}",
        f"- **All Prerequisites Satisfied**: {summary.get('all_satisfied', True)}",
        "",
    ]
    if handoff_df is not None and not handoff_df.empty:
        lines.append("## Handoff Deliverables Table")
        lines.append(handoff_df.to_markdown(index=False))
    return "\n".join(lines)
