# -*- coding: utf-8 -*-
"""Phase 139 GPU Training Governance Markdown Report Builder."""

from typing import Any, Dict, Optional
import pandas as pd

DISCLAIMER_TEXT = (
    "> [!WARNING]\n"
    "> **YASAL UYARI VE GÜVENLİK SINIRI**:\n"
    "> Bu çıktı Phase 139 GPU-Accelerated Training Harness and Resource Governance raporudur. "
    "> Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, GPU/resource/harness/readiness "
    "> değerini trade sinyali veya production-ready/broker-ready onayı olarak kullanma, gerçek model "
    "> training, model fit/predict/inference, dataset materialization, target/label/prediction üretimi, "
    "> gerçek metric/performance claim, model artifact persistence, model registry write, strateji üretimi, "
    "> backtest, optimizer, clustering, ensemble, calibration, sentiment model output, haber tam metni/"
    "> article body/raw content/scraped HTML/embedding/vector kullanımı, production deployment, model "
    "> deployment, scraping veya gerçek provider API çağrısı değildir.\n"
)


def build_gpu_training_governance_disclaimer() -> str:
    """Return standard Phase 139 disclaimer."""
    return DISCLAIMER_TEXT


def _df_to_markdown(df: pd.DataFrame) -> str:
    """Format DataFrame as markdown table without requiring optional tabulate package."""
    try:
        return df.to_markdown(index=False)
    except Exception:
        if df.empty:
            return ""
        cols = list(df.columns)
        header = "| " + " | ".join(str(c) for c in cols) + " |"
        sep = "| " + " | ".join("---" for _ in cols) + " |"
        rows = []
        for _, row in df.iterrows():
            rows.append("| " + " | ".join(str(row[c]) for c in cols) + " |")
        return "\n".join([header, sep] + rows)


def build_gpu_training_governance_profile_markdown_report(
    summary: Dict[str, Any], profile_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for profile registry."""
    md = [
        "# Phase 139 GPU Training Governance Profile Registry Report",
        build_gpu_training_governance_disclaimer(),
        f"- **Active Profile**: {summary.get('active_profile', 'unknown')}",
        f"- **Total Profiles**: {summary.get('total_profiles', 0)}",
        f"- **Current Phase**: {summary.get('current_phase', 139)}",
        f"- **Next Phase**: {summary.get('next_phase', 140)}",
        f"- **All Dry-Run**: {summary.get('all_dry_run', True)}",
        f"- **Non-Signal Certified**: {summary.get('non_signal', True)}",
        "",
    ]
    if profile_df is not None and not profile_df.empty:
        md.append("## Profile Details")
        md.append(_df_to_markdown(profile_df))
    return "\n".join(md)


def build_gpu_training_resource_policy_markdown_report(
    summary: Dict[str, Any], policy_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for resource policies."""
    md = [
        "# Phase 139 GPU Training Resource Policies Report",
        build_gpu_training_governance_disclaimer(),
        f"- **Total Policies**: {summary.get('total_policies', 0)}",
        f"- **Contract Only Mode**: {summary.get('all_contract_only', True)}",
        f"- **Real Training Prohibited**: {summary.get('all_real_training_disabled', True)}",
        f"- **Manual Review Required**: {summary.get('all_manual_review_required', True)}",
        "",
    ]
    if policy_df is not None and not policy_df.empty:
        md.append("## Resource Policies")
        md.append(_df_to_markdown(policy_df))
    return "\n".join(md)


def build_gpu_training_harness_markdown_report(
    summary: Dict[str, Any], harness_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for harness contracts and stubs."""
    md = [
        "# Phase 139 GPU Training Harness Contracts Report",
        build_gpu_training_governance_disclaimer(),
        f"- **Total Stubs/Contracts**: {summary.get('total_stubs', 0)}",
        f"- **Dry-Run Mode**: {summary.get('all_dry_run', True)}",
        f"- **Execution Blocked By Policy**: {summary.get('all_blocked_by_policy', True)}",
        "",
    ]
    if harness_df is not None and not harness_df.empty:
        md.append("## Harness Stubs")
        md.append(_df_to_markdown(harness_df))
    return "\n".join(md)


def build_gpu_training_dry_run_guard_markdown_report(
    summary: Dict[str, Any], guard_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for dry-run guards."""
    md = [
        "# Phase 139 Dry-Run Resource Guards Report",
        build_gpu_training_governance_disclaimer(),
        f"- **Checks Passed**: {summary.get('all_passed', True)}",
        f"- **Total Checks**: {summary.get('total_checks', 0)}",
        f"- **Dry-Run Enforced**: {summary.get('all_dry_run', True)}",
        "",
    ]
    if guard_df is not None and not guard_df.empty:
        md.append("## Guard Checks")
        md.append(_df_to_markdown(guard_df))
    return "\n".join(md)


def build_gpu_training_disabled_execution_markdown_report(
    summary: Dict[str, Any], disabled_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for disabled execution verification."""
    md = [
        "# Phase 139 Disabled Execution Verification Report",
        build_gpu_training_governance_disclaimer(),
        f"- **Real Training Disabled**: {summary.get('real_training_executed', False) is False}",
        f"- **Prediction/Inference Disabled**: {summary.get('model_predict_executed', False) is False}",
        f"- **Target/Label Generation Disabled**: {summary.get('target_label_generated', False) is False}",
        f"- **Artifact Persistence Disabled**: {summary.get('artifact_persisted', False) is False}",
        f"- **Model Registry Write Disabled**: {summary.get('model_registry_written', False) is False}",
        "",
    ]
    if disabled_df is not None and not disabled_df.empty:
        md.append("## Verification Table")
        md.append(_df_to_markdown(disabled_df))
    return "\n".join(md)


def build_gpu_training_dependency_markdown_report(
    summary: Dict[str, Any], dependency_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for dependencies and input guards."""
    md = [
        "# Phase 139 Dependencies and Input Guards Report",
        build_gpu_training_governance_disclaimer(),
        f"- **Total Dependencies**: {summary.get('total_dependencies', 0)}",
        f"- **All Satisfied**: {summary.get('all_satisfied', True)}",
        "",
    ]
    if dependency_df is not None and not dependency_df.empty:
        md.append("## Dependency Table")
        md.append(_df_to_markdown(dependency_df))
    return "\n".join(md)


def build_gpu_training_audit_placeholder_markdown_report(
    summary: Dict[str, Any], audit_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for audit placeholders."""
    md = [
        "# Phase 139 Audit Placeholders Report",
        build_gpu_training_governance_disclaimer(),
        f"- **Total Placeholders**: {summary.get('total_placeholders', 0)}",
        f"- **Dry-Run Only**: {summary.get('all_dry_run', True)}",
        "",
    ]
    if audit_df is not None and not audit_df.empty:
        md.append("## Placeholders")
        md.append(_df_to_markdown(audit_df))
    return "\n".join(md)


def build_gpu_training_findings_markdown_report(
    summary: Dict[str, Any], findings_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for findings and manual review."""
    md = [
        "# Phase 139 GPU Training Governance Findings Report",
        build_gpu_training_governance_disclaimer(),
        f"- **Total Findings**: {summary.get('total_findings', 0)}",
        f"- **Manual Review Items**: {summary.get('manual_review_count', 0)}",
        f"- **Critical Severity Count**: {summary.get('critical_count', 0)}",
        "",
    ]
    if findings_df is not None and not findings_df.empty:
        md.append("## Findings Table")
        md.append(_df_to_markdown(findings_df))
    return "\n".join(md)


def build_gpu_training_readiness_score_markdown_report(
    summary: Dict[str, Any], score_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for readiness scoring."""
    md = [
        "# Phase 139 GPU Training Readiness Scoring Report",
        build_gpu_training_governance_disclaimer(),
        f"- **Readiness Score**: {summary.get('readiness_score', 1.0)}",
        f"- **Classification**: {summary.get('classification', 'READY_FOR_GPU_RESOURCE_GOVERNANCE_DRY_RUN')}",
        f"- **Meets Threshold**: {summary.get('meets_threshold', True)}",
        "- **Signal Approved**: False",
        "- **Production Approved**: False",
        "",
    ]
    if score_df is not None and not score_df.empty:
        md.append("## Scoring Metrics")
        md.append(_df_to_markdown(score_df))
    return "\n".join(md)


def build_gpu_training_governance_manifest_markdown_report(
    summary: Dict[str, Any], manifest_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for governance manifest."""
    md = [
        "# Phase 139 GPU Training Governance Manifest Report",
        build_gpu_training_governance_disclaimer(),
        f"- **Manifest Name**: {summary.get('manifest_name', 'gpu_training_governance_manifest')}",
        f"- **Current Phase**: {summary.get('current_phase', 139)}",
        f"- **Next Phase**: {summary.get('next_phase', 140)}",
        f"- **Target Final Phase**: {summary.get('target_final_phase', 160)}",
        f"- **Readiness Score**: {summary.get('readiness_score', 1.0)}",
        f"- **Real Training Executed**: {summary.get('real_training_executed', False)}",
        f"- **Artifact Persisted**: {summary.get('artifact_persisted', False)}",
        "",
    ]
    if manifest_df is not None and not manifest_df.empty:
        md.append("## Manifest Content")
        md.append(_df_to_markdown(manifest_df))
    return "\n".join(md)


def build_gpu_training_governance_validation_markdown_report(
    summary: Dict[str, Any], validation_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for validation check."""
    md = [
        "# Phase 139 GPU Training Governance Validation Report",
        build_gpu_training_governance_disclaimer(),
        f"- **Validation Status**: {summary.get('validation_status', 'VALIDATION_PASS')}",
        f"- **Total Checks**: {summary.get('total_checks', 0)}",
        f"- **Forbidden Claims Clean**: {summary.get('forbidden_claims_clean', True)}",
        "",
    ]
    if validation_df is not None and not validation_df.empty:
        md.append("## Validation Results")
        md.append(_df_to_markdown(validation_df))
    return "\n".join(md)


def build_gpu_training_governance_safety_markdown_report(
    summary: Dict[str, Any], safety_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for safety boundary."""
    md = [
        "# Phase 139 GPU Training Governance Safety Boundary Report",
        build_gpu_training_governance_disclaimer(),
        f"- **Safety Status**: {summary.get('safety_status', 'SECURE')}",
        f"- **NO-GO Conditions Enforced**: {summary.get('no_go_count', 24)}",
        f"- **SAFE-GO Conditions Active**: {summary.get('safe_go_count', 10)}",
        "",
    ]
    if safety_df is not None and not safety_df.empty:
        md.append("## Safety Rules")
        md.append(_df_to_markdown(safety_df))
    return "\n".join(md)


def build_phase_140_handoff_markdown_report(
    summary: Dict[str, Any], handoff_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for Phase 140 handoff."""
    md = [
        "# Phase 140 Ensemble Model Contracts Handoff Report",
        build_gpu_training_governance_disclaimer(),
        f"- **Source Phase**: {summary.get('source_phase', 139)}",
        f"- **Next Phase**: {summary.get('next_phase', 140)}",
        f"- **Target Final Phase**: {summary.get('target_final_phase', 160)}",
        f"- **Handoff Status**: {summary.get('handoff_status', 'READY_FOR_PHASE_140')}",
        f"- **Total Prerequisites**: {summary.get('total_prerequisites', 0)}",
        f"- **All Satisfied**: {summary.get('all_satisfied', True)}",
        "",
    ]
    if handoff_df is not None and not handoff_df.empty:
        md.append("## Handoff Prerequisites")
        md.append(_df_to_markdown(handoff_df))
    return "\n".join(md)
