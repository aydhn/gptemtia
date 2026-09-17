# -*- coding: utf-8 -*-
"""Phase 138 Baseline ML Model Markdown Report Builder.

Generates markdown reports for all Phase 138 registries, contracts, stubs,
and safety boundaries with mandatory disclaimers.
"""

from typing import Any, Dict, Optional
import pandas as pd

BASELINE_ML_MODEL_REPORT_DISCLAIMER = (
    "Bu çıktı Phase 138 Baseline ML Model Contracts and Dry-Run Training Harness raporudur. "
    "Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, model contract/dry-run/readiness "
    "değerini trade sinyali veya production-ready/broker-ready onayı olarak kullanma, gerçek model training, "
    "model fit/predict/inference, dataset materialization, target/label/prediction üretimi, gerçek metric/performance "
    "claim, model artifact persistence, model registry write, strateji üretimi, backtest, optimizer, clustering, "
    "ensemble, calibration, sentiment model output, haber tam metni/article body/raw content/scraped HTML/"
    "embedding/vector kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir."
)


def build_baseline_ml_model_disclaimer() -> str:
    """Return the official Phase 138 legal disclaimer."""
    return f"> [!IMPORTANT]\n> **YASAL UYARI VE GÜVENLİK SINIRI:**\n> {BASELINE_ML_MODEL_REPORT_DISCLAIMER}\n"


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


def build_baseline_ml_model_profile_markdown_report(
    summary: Dict[str, Any],
    profile_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for profiles."""
    lines = [
        "# Phase 138: Baseline ML Model Profile Registry Report",
        "",
        build_baseline_ml_model_disclaimer(),
        "## Summary",
        f"- **Total Profiles:** {summary.get('total_profiles', 0)}",
        f"- **Enabled Profiles:** {summary.get('enabled_profiles', 0)}",
        f"- **All Dry-Run:** {summary.get('all_dry_run', True)}",
        f"- **Zero Real Training:** {summary.get('zero_real_training', True)}",
        f"- **Zero Prediction:** {summary.get('zero_prediction', True)}",
        f"- **Non-Signal Certified:** {summary.get('non_signal', True)}",
        "",
    ]
    if profile_df is not None and not profile_df.empty:
        lines.append("## Defined Profiles")
        lines.append(_df_to_markdown(profile_df))
        lines.append("")
    return "\n".join(lines)



def build_baseline_model_family_markdown_report(
    summary: Dict[str, Any],
    family_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for model families."""
    lines = [
        "# Phase 138: Baseline Model Family Registry Report",
        "",
        build_baseline_ml_model_disclaimer(),
        "## Summary",
        f"- **Total Model Families:** {summary.get('total_families', 0)}",
        f"- **All Contract Only:** {summary.get('all_contract_only', True)}",
        f"- **Zero Real Training:** {summary.get('zero_real_training', True)}",
        f"- **Zero Prediction:** {summary.get('zero_prediction', True)}",
        "",
    ]
    if family_df is not None and not family_df.empty:
        lines.append("## Registered Families")
        lines.append(_df_to_markdown(family_df))
        lines.append("")
    return "\n".join(lines)


def build_baseline_model_contract_markdown_report(
    summary: Dict[str, Any],
    contract_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for model contracts."""
    lines = [
        "# Phase 138: Baseline Model Contracts Registry Report",
        "",
        build_baseline_ml_model_disclaimer(),
        "## Summary",
        f"- **Total Contracts:** {summary.get('total_contracts', 0)}",
        f"- **All Real Training Blocked:** {summary.get('all_real_training_blocked', True)}",
        f"- **All Prediction Blocked:** {summary.get('all_prediction_blocked', True)}",
        f"- **All Target/Label Blocked:** {summary.get('all_target_label_blocked', True)}",
        f"- **All Artifact Blocked:** {summary.get('all_artifact_blocked', True)}",
        f"- **All Registry Write Blocked:** {summary.get('all_registry_write_blocked', True)}",
        "",
    ]
    if contract_df is not None and not contract_df.empty:
        lines.append("## Contracts Overview")
        lines.append(_df_to_markdown(contract_df))
        lines.append("")
    return "\n".join(lines)


def build_dry_run_training_harness_markdown_report(
    summary: Dict[str, Any],
    harness_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for dry-run harness contracts."""
    lines = [
        "# Phase 138: Dry-Run Training Harness Contracts Report",
        "",
        build_baseline_ml_model_disclaimer(),
        "## Summary",
        f"- **Total Harness Contracts:** {summary.get('total_harness_contracts', 0)}",
        f"- **All Real Training Blocked:** {summary.get('all_real_training_blocked', True)}",
        f"- **All Model Fit Blocked:** {summary.get('all_model_fit_blocked', True)}",
        f"- **All Prediction Blocked:** {summary.get('all_predict_blocked', True)}",
        "",
    ]
    if harness_df is not None and not harness_df.empty:
        lines.append("## Harness Specifications")
        lines.append(_df_to_markdown(harness_df))
        lines.append("")
    return "\n".join(lines)


def build_disabled_execution_markdown_report(
    summary: Dict[str, Any],
    disabled_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for disabled execution."""
    lines = [
        "# Phase 138: Disabled Execution Report",
        "",
        build_baseline_ml_model_disclaimer(),
        "## Summary",
        f"- **Real Training Executed:** {summary.get('real_training_executed', False)}",
        f"- **Model Fit Executed:** {summary.get('model_fit_executed', False)}",
        f"- **Model Predict Executed:** {summary.get('model_predict_executed', False)}",
        f"- **Target/Label Generated:** {summary.get('target_label_generated', False)}",
        f"- **Artifact Persisted:** {summary.get('artifact_persisted', False)}",
        f"- **Model Registry Written:** {summary.get('model_registry_written', False)}",
        "",
    ]
    if disabled_df is not None and not disabled_df.empty:
        lines.append("## Checks")
        lines.append(_df_to_markdown(disabled_df))
        lines.append("")
    return "\n".join(lines)


def build_baseline_metric_placeholder_markdown_report(
    summary: Dict[str, Any],
    metric_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for metric placeholders."""
    lines = [
        "# Phase 138: Baseline Metric Placeholders Report",
        "",
        build_baseline_ml_model_disclaimer(),
        "## Summary",
        f"- **Total Placeholders:** {summary.get('total_placeholders', 0)}",
        f"- **All Uncalculated:** {summary.get('all_uncalculated', True)}",
        f"- **Performance Claims Prohibited:** {summary.get('performance_claims_prohibited', True)}",
        "",
    ]
    if metric_df is not None and not metric_df.empty:
        lines.append("## Placeholders")
        lines.append(_df_to_markdown(metric_df))
        lines.append("")
    return "\n".join(lines)


def build_baseline_model_input_guard_markdown_report(
    summary: Dict[str, Any],
    guard_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for input guards."""
    lines = [
        "# Phase 138: Baseline Model Input Guards Report",
        "",
        build_baseline_ml_model_disclaimer(),
        "## Summary",
        f"- **Total Guards:** {summary.get('total_guards', 0)}",
        f"- **All Enforced:** {summary.get('all_enforced', True)}",
        f"- **Non-Signal Certified:** {summary.get('non_signal', True)}",
        "",
    ]
    if guard_df is not None and not guard_df.empty:
        lines.append("## Guards List")
        lines.append(_df_to_markdown(guard_df))
        lines.append("")
    return "\n".join(lines)


def build_baseline_model_findings_markdown_report(
    summary: Dict[str, Any],
    findings_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for findings."""
    lines = [
        "# Phase 138: Baseline Model Findings Registry Report",
        "",
        build_baseline_ml_model_disclaimer(),
        "## Summary",
        f"- **Total Findings:** {summary.get('total_findings', 0)}",
        f"- **Critical Blockers:** {summary.get('critical_blockers', 0)}",
        f"- **Clean Baseline Contracts:** {summary.get('clean_baseline_contracts', True)}",
        "",
    ]
    if findings_df is not None and not findings_df.empty:
        lines.append("## Findings")
        lines.append(_df_to_markdown(findings_df))
        lines.append("")
    return "\n".join(lines)


def build_baseline_model_readiness_score_markdown_report(
    summary: Dict[str, Any],
    score_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for readiness scores."""
    lines = [
        "# Phase 138: Baseline Model Readiness Score Report",
        "",
        build_baseline_ml_model_disclaimer(),
        "## Summary",
        f"- **Readiness Score:** {summary.get('readiness_score', 1.0)}",
        f"- **Score Tier:** {summary.get('score_tier', 'READY_FOR_LOCAL_DRY_RUN_HARNESS')}",
        f"- **Is Ready for Dry-Run:** {summary.get('is_ready_for_dry_run', True)}",
        f"- **Trade Signal Certified:** {summary.get('trade_signal_certified', False)}",
        f"- **Production Ready:** {summary.get('production_ready', False)}",
        "",
    ]
    if score_df is not None and not score_df.empty:
        lines.append("## Score Details")
        lines.append(_df_to_markdown(score_df))
        lines.append("")
    return "\n".join(lines)


def build_baseline_ml_model_manifest_markdown_report(
    summary: Dict[str, Any],
    manifest_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for manifest."""
    lines = [
        "# Phase 138: Baseline ML Model Manifest Report",
        "",
        build_baseline_ml_model_disclaimer(),
        "## Summary",
        f"- **Manifest Name:** {summary.get('manifest_name', 'baseline_ml_model_manifest')}",
        f"- **Current Phase:** {summary.get('current_phase', 138)}",
        f"- **Next Phase:** {summary.get('next_phase', 139)}",
        f"- **Target Final Phase:** {summary.get('target_final_phase', 160)}",
        f"- **Model Contracts:** {summary.get('model_contract_count', 10)}",
        f"- **Harness Contracts:** {summary.get('harness_contract_count', 5)}",
        f"- **Readiness Score:** {summary.get('readiness_score', 1.0)}",
        f"- **Zero Real Training:** {not summary.get('real_training_executed', False)}",
        f"- **Zero Prediction:** {not summary.get('model_predict_executed', False)}",
        "",
    ]
    if manifest_df is not None and not manifest_df.empty:
        lines.append("## Manifest Content")
        lines.append(_df_to_markdown(manifest_df))
        lines.append("")
    return "\n".join(lines)


def build_baseline_ml_model_validation_markdown_report(
    summary: Dict[str, Any],
    validation_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for validation."""
    lines = [
        "# Phase 138: Baseline ML Model Validation Report",
        "",
        build_baseline_ml_model_disclaimer(),
        "## Summary",
        f"- **Validation Status:** {summary.get('validation_status', 'VALIDATION_PASS')}",
        f"- **All Passed:** {summary.get('all_passed', True)}",
        f"- **Forbidden Claims Clean:** {summary.get('clean_of_forbidden_claims', True)}",
        "",
    ]
    if validation_df is not None and not validation_df.empty:
        lines.append("## Validation Results")
        lines.append(_df_to_markdown(validation_df))
        lines.append("")
    return "\n".join(lines)


def build_baseline_ml_model_safety_markdown_report(
    summary: Dict[str, Any],
    safety_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for safety boundary."""
    lines = [
        "# Phase 138: Baseline ML Model Safety Boundary Report",
        "",
        build_baseline_ml_model_disclaimer(),
        "## Summary",
        f"- **Safety Status:** {summary.get('safety_status', 'SECURE')}",
        f"- **NO-GO Conditions Enforced:** {summary.get('no_go_count', 24)}",
        f"- **SAFE-GO Conditions Active:** {summary.get('safe_go_count', 9)}",
        f"- **Zero Training Active:** True",
        f"- **Zero Live Trading:** True",
        "",
    ]
    if safety_df is not None and not safety_df.empty:
        lines.append("## Boundary Table")
        lines.append(_df_to_markdown(safety_df))
        lines.append("")
    return "\n".join(lines)


def build_phase_139_handoff_markdown_report(
    summary: Dict[str, Any],
    handoff_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for Phase 139 handoff."""
    lines = [
        "# Phase 138: Phase 139 GPU Training Harness and Resource Governance Handoff Report",
        "",
        build_baseline_ml_model_disclaimer(),
        "## Summary",
        f"- **Source Phase:** {summary.get('source_phase', 138)}",
        f"- **Next Phase:** {summary.get('next_phase', 139)}",
        f"- **Target Final Phase:** {summary.get('target_final_phase', 160)}",
        f"- **Handoff Status:** {summary.get('handoff_status', 'READY_FOR_PHASE_139')}",
        f"- **Prerequisites Count:** {summary.get('total_prerequisites', 11)}",
        f"- **All Prerequisites Satisfied:** {summary.get('all_satisfied', True)}",
        "",
    ]
    if handoff_df is not None and not handoff_df.empty:
        lines.append("## Handoff Checklist")
        lines.append(_df_to_markdown(handoff_df))
        lines.append("")
    return "\n".join(lines)

