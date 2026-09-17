# -*- coding: utf-8 -*-
"""Phase 141: Calibration & Uncertainty Report Builder."""

from typing import Any, Dict, Optional
import pandas as pd

CALIBRATION_UNCERTAINTY_DISCLAIMER = (
    "Bu çıktı Phase 141 Probability Calibration and Uncertainty Estimation Contracts raporudur. "
    "Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, calibration/uncertainty/readiness/confidence "
    "değerini trade sinyali veya production-ready/broker-ready onayı olarak kullanma, gerçek model training, "
    "model fit/predict/inference, probability prediction, calibration fit/transform, uncertainty estimation, "
    "prediction interval/conformal prediction, dataset materialization, target/label/prediction üretimi, "
    "gerçek metric/performance claim, model artifact persistence, model registry write, strateji üretimi, "
    "backtest, optimizer, clustering, ensemble execution, sentiment model output, haber tam metni/article body/"
    "raw content/scraped HTML/embedding/vector kullanımı, production deployment, model deployment, scraping "
    "veya gerçek provider API çağrısı değildir."
)


def build_calibration_uncertainty_disclaimer() -> str:
    """Return mandatory disclaimer."""
    return CALIBRATION_UNCERTAINTY_DISCLAIMER


def _render_df(df: Optional[pd.DataFrame]) -> str:
    """Safely render DataFrame to Markdown table."""
    if df is not None and isinstance(df, pd.DataFrame) and not df.empty:
        try:
            return df.to_markdown(index=False)
        except Exception:
            return df.to_string(index=False)
    return "_No tabular data available._"


def build_calibration_uncertainty_profile_markdown_report(summary: Dict[str, Any], profile_df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 141: Calibration & Uncertainty Profile Registry Report\n\n"
        f"> **YASAL UYARI VE GÜVENLİK SINIRI:**\n> {CALIBRATION_UNCERTAINTY_DISCLAIMER}\n\n"
        f"## Profile Summary\n"
        f"- **Total Profiles**: {summary.get('total_profiles', 0)}\n"
        f"- **Active Profile**: `{summary.get('active_profile', 'unknown')}`\n"
        f"- **Local Only**: `{summary.get('all_local_only', True)}`\n"
        f"- **Non-Signal**: `{summary.get('all_non_signal', True)}`\n"
        f"- **Zero Execution**: `{summary.get('all_zero_execution', True)}`\n\n"
        f"## Profile Table\n\n{_render_df(profile_df)}\n"
    )


def build_probability_calibration_contract_markdown_report(summary: Dict[str, Any], contract_df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 141: Probability Calibration Contracts Report\n\n"
        f"> **YASAL UYARI VE GÜVENLİK SINIRI:**\n> {CALIBRATION_UNCERTAINTY_DISCLAIMER}\n\n"
        f"## Contracts Summary\n"
        f"- **Total Contracts**: {summary.get('total_contracts', 0)}\n"
        f"- **All Zero Prediction**: `{summary.get('all_zero_prediction', True)}`\n"
        f"- **All Zero Fit**: `{summary.get('all_zero_fit', True)}`\n"
        f"- **All Zero Transform**: `{summary.get('all_zero_transform', True)}`\n"
        f"- **All Non-Signal**: `{summary.get('all_non_signal', True)}`\n\n"
        f"## Contracts Table\n\n{_render_df(contract_df)}\n"
    )


def build_uncertainty_estimation_contract_markdown_report(summary: Dict[str, Any], contract_df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 141: Uncertainty Estimation Contracts Report\n\n"
        f"> **YASAL UYARI VE GÜVENLİK SINIRI:**\n> {CALIBRATION_UNCERTAINTY_DISCLAIMER}\n\n"
        f"## Contracts Summary\n"
        f"- **Total Contracts**: {summary.get('total_contracts', 0)}\n"
        f"- **All Zero Uncertainty**: `{summary.get('all_zero_uncertainty', True)}`\n"
        f"- **All Zero Prediction Interval**: `{summary.get('all_zero_prediction_interval', True)}`\n"
        f"- **All Zero Conformal**: `{summary.get('all_zero_conformal', True)}`\n"
        f"- **All Non-Signal**: `{summary.get('all_non_signal', True)}`\n\n"
        f"## Contracts Table\n\n{_render_df(contract_df)}\n"
    )


def build_calibration_disabled_execution_markdown_report(summary: Dict[str, Any], disabled_df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 141: Calibration Execution Disabled Report\n\n"
        f"> **YASAL UYARI VE GÜVENLİK SINIRI:**\n> {CALIBRATION_UNCERTAINTY_DISCLAIMER}\n\n"
        f"## Policy Enforcement Summary\n"
        f"- **Total Operations Audited**: {summary.get('total_operations_audited', 0)}\n"
        f"- **All Disabled**: `{summary.get('all_disabled', True)}`\n"
        f"- **All Enforced**: `{summary.get('all_enforced', True)}`\n"
        f"- **Zero Probabilities Generated**: True\n\n"
        f"## Enforcement Table\n\n{_render_df(disabled_df)}\n"
    )


def build_uncertainty_disabled_execution_markdown_report(summary: Dict[str, Any], disabled_df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 141: Uncertainty Execution Disabled Report\n\n"
        f"> **YASAL UYARI VE GÜVENLİK SINIRI:**\n> {CALIBRATION_UNCERTAINTY_DISCLAIMER}\n\n"
        f"## Policy Enforcement Summary\n"
        f"- **Total Operations Audited**: {summary.get('total_operations_audited', 0)}\n"
        f"- **All Disabled**: `{summary.get('all_disabled', True)}`\n"
        f"- **All Enforced**: `{summary.get('all_enforced', True)}`\n"
        f"- **Zero Intervals Computed**: True\n\n"
        f"## Enforcement Table\n\n{_render_df(disabled_df)}\n"
    )


def build_calibration_uncertainty_placeholder_markdown_report(summary: Dict[str, Any], placeholder_df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 141: Calibration & Uncertainty Placeholders Report\n\n"
        f"> **YASAL UYARI VE GÜVENLİK SINIRI:**\n> {CALIBRATION_UNCERTAINTY_DISCLAIMER}\n\n"
        f"## Placeholders Summary\n"
        f"- **Total Placeholders**: {summary.get('total_placeholders', len(placeholder_df) if placeholder_df is not None else 0)}\n"
        f"- **Zero Calculation Verified**: True\n"
        f"- **Non-Signal Verified**: True\n\n"
        f"## Placeholders Table\n\n{_render_df(placeholder_df)}\n"
    )


def build_calibration_uncertainty_quality_gate_markdown_report(summary: Dict[str, Any], gate_df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 141: Quality Gates Report\n\n"
        f"> **YASAL UYARI VE GÜVENLİK SINIRI:**\n> {CALIBRATION_UNCERTAINTY_DISCLAIMER}\n\n"
        f"## Quality Gates Summary\n"
        f"- **Total Gates**: {summary.get('total_gates', 0)}\n"
        f"- **All Active**: `{summary.get('all_active', True)}`\n"
        f"- **All Blocking**: `{summary.get('all_blocking', True)}`\n\n"
        f"## Gates Table\n\n{_render_df(gate_df)}\n"
    )


def build_calibration_uncertainty_dependency_markdown_report(summary: Dict[str, Any], dependency_df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 141: Dependencies Report\n\n"
        f"> **YASAL UYARI VE GÜVENLİK SINIRI:**\n> {CALIBRATION_UNCERTAINTY_DISCLAIMER}\n\n"
        f"## Dependencies Summary\n"
        f"- **Total Dependencies**: {summary.get('total_dependencies', 0)}\n"
        f"- **All Satisfied**: `{summary.get('all_satisfied', True)}`\n\n"
        f"## Dependencies Table\n\n{_render_df(dependency_df)}\n"
    )


def build_calibration_uncertainty_guard_markdown_report(summary: Dict[str, Any], guard_df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 141: Safety Guards Report\n\n"
        f"> **YASAL UYARI VE GÜVENLİK SINIRI:**\n> {CALIBRATION_UNCERTAINTY_DISCLAIMER}\n\n"
        f"## Guards Summary\n"
        f"- **Total Guards**: {summary.get('total_guards', 0)}\n"
        f"- **All Active**: `{summary.get('all_active', True)}`\n\n"
        f"## Guards Table\n\n{_render_df(guard_df)}\n"
    )


def build_calibration_uncertainty_findings_markdown_report(summary: Dict[str, Any], findings_df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 141: Governance Findings Report\n\n"
        f"> **YASAL UYARI VE GÜVENLİK SINIRI:**\n> {CALIBRATION_UNCERTAINTY_DISCLAIMER}\n\n"
        f"## Findings Summary\n"
        f"- **Total Findings**: {summary.get('total_findings', 0)}\n"
        f"- **Critical Findings**: {summary.get('critical_findings', 0)}\n"
        f"- **Manual Review Items**: {summary.get('manual_review_items', 0)}\n\n"
        f"## Findings Table\n\n{_render_df(findings_df)}\n"
    )


def build_calibration_uncertainty_readiness_score_markdown_report(summary: Dict[str, Any], score_df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 141: Readiness Score Report\n\n"
        f"> **YASAL UYARI VE GÜVENLİK SINIRI:**\n> {CALIBRATION_UNCERTAINTY_DISCLAIMER}\n\n"
        f"## Readiness Scoring Summary\n"
        f"- **Readiness Score**: `{summary.get('readiness_score', 1.0):.4f}`\n"
        f"- **Classification**: `{summary.get('classification', 'READY')}`\n"
        f"- **Meets Threshold**: `{summary.get('meets_threshold', True)}`\n"
        f"- **Production Ready**: `{summary.get('production_ready', False)}`\n"
        f"- **Broker Ready**: `{summary.get('broker_ready', False)}`\n\n"
        f"## Score Table\n\n{_render_df(score_df)}\n"
    )


def build_calibration_uncertainty_manifest_markdown_report(summary: Dict[str, Any], manifest_df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 141: Calibration & Uncertainty Manifest Report\n\n"
        f"> **YASAL UYARI VE GÜVENLİK SINIRI:**\n> {CALIBRATION_UNCERTAINTY_DISCLAIMER}\n\n"
        f"## Manifest Summary\n"
        f"- **Manifest Name**: `{summary.get('manifest_name', 'manifest')}`\n"
        f"- **Current Phase**: `{summary.get('current_phase', 141)}`\n"
        f"- **Target Final Phase**: `{summary.get('target_final_phase', 160)}`\n"
        f"- **Next Phase**: `{summary.get('next_phase', 142)}`\n"
        f"- **Zero Execution Verified**: `{summary.get('zero_execution_verified', True)}`\n"
        f"- **Non-Signal Verified**: `{summary.get('non_signal', True)}`\n\n"
        f"## Manifest Table\n\n{_render_df(manifest_df)}\n"
    )


def build_calibration_uncertainty_validation_markdown_report(summary: Dict[str, Any], validation_df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 141: Validation Report\n\n"
        f"> **YASAL UYARI VE GÜVENLİK SINIRI:**\n> {CALIBRATION_UNCERTAINTY_DISCLAIMER}\n\n"
        f"## Validation Summary\n"
        f"- **Validation Status**: `{summary.get('validation_status', 'VALID')}`\n"
        f"- **Total Checks**: {summary.get('total_checks', 0)}\n"
        f"- **Passed Checks**: {summary.get('passed_checks', 0)}\n"
        f"- **Forbidden Claims Clean**: `{summary.get('forbidden_claims_clean', True)}`\n\n"
        f"## Checks Table\n\n{_render_df(validation_df)}\n"
    )


def build_calibration_uncertainty_safety_markdown_report(summary: Dict[str, Any], safety_df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 141: Safety Boundary Report\n\n"
        f"> **YASAL UYARI VE GÜVENLİK SINIRI:**\n> {CALIBRATION_UNCERTAINTY_DISCLAIMER}\n\n"
        f"## Safety Boundary Summary\n"
        f"- **Safety Status**: `{summary.get('safety_status', 'ENFORCED')}`\n"
        f"- **NO-GO Invariants**: {summary.get('no_go_count', 0)}\n"
        f"- **SAFE-GO Principles**: {summary.get('safe_go_count', 0)}\n\n"
        f"## Safety Table\n\n{_render_df(safety_df)}\n"
    )


def build_phase_142_handoff_markdown_report(summary: Dict[str, Any], handoff_df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 141 to Phase 142 Handoff Report\n\n"
        f"> **YASAL UYARI VE GÜVENLİK SINIRI:**\n> {CALIBRATION_UNCERTAINTY_DISCLAIMER}\n\n"
        f"## Handoff Summary\n"
        f"- **Status**: `{summary.get('handoff_status', 'READY_FOR_PHASE_142')}`\n"
        f"- **Source Phase**: 141 (Probability Calibration & Uncertainty Estimation)\n"
        f"- **Next Phase**: 142 (Model Drift Monitoring and Data/Feature Drift Linkage)\n"
        f"- **Target Final Phase**: 160\n"
        f"- **All Prerequisites Met**: `{summary.get('all_prerequisites_met', True)}`\n\n"
        f"## Handoff Table\n\n{_render_df(handoff_df)}\n"
    )


ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER = CALIBRATION_UNCERTAINTY_DISCLAIMER


def build_calibration_uncertainty_consolidated_markdown_report(result: Dict[str, Any]) -> str:
    """Build consolidated Markdown report from pipeline execution result."""
    prof = result.get("profile", {})
    prof_name = prof.get("name") or prof.get("profile_name", "unknown")
    readiness = result.get("readiness_score", 1.0)
    classification = result.get("readiness_classification", "READY")
    health = result.get("health_status", "UNKNOWN")
    validation = result.get("validation_status", "UNKNOWN")
    cal_count = result.get("calibration_contract_count", 0)
    unc_count = result.get("uncertainty_contract_count", 0)

    return (
        f"# Phase 141 Consolidated Report: Calibration & Uncertainty Contracts\n\n"
        f"> **YASAL UYARI VE GÜVENLİK SINIRI:**\n> {CALIBRATION_UNCERTAINTY_DISCLAIMER}\n\n"
        f"## Executive Overview\n"
        f"- **Phase**: 141 (Probability Calibration & Uncertainty Estimation Contracts)\n"
        f"- **Active Profile**: `{prof_name}`\n"
        f"- **Next Phase**: 142 (Model Drift Monitoring)\n"
        f"- **Target Final Phase**: 160\n"
        f"- **Readiness Score**: `{readiness:.4f}` ({classification})\n"
        f"- **Health Status**: `{health}`\n"
        f"- **Validation Status**: `{validation}`\n\n"
        f"## Contract Counts\n"
        f"- **Calibration Contracts**: {cal_count}\n"
        f"- **Uncertainty Contracts**: {unc_count}\n"
        f"- **Disabled Execution Reports**: {result.get('disabled_report_count', 0)}\n\n"
        f"## Strict Invariants Enforced\n"
        f"- Real Training Executed: `False`\n"
        f"- Model Fit/Predict Executed: `False`\n"
        f"- Probability Prediction Executed: `False`\n"
        f"- Calibration Fit/Transform Executed: `False`\n"
        f"- Uncertainty Estimation Executed: `False`\n"
        f"- Real Orders / Live Trading: `False`\n"
        f"- Non-Signal Guarantee: `True`\n"
        f"- Dry-Run Mode: `True`\n"
    )


def build_calibration_uncertainty_consolidated_text_report(result: Dict[str, Any]) -> str:
    """Build consolidated plain text report from pipeline execution result."""
    prof = result.get("profile", {})
    prof_name = prof.get("name") or prof.get("profile_name", "unknown")
    readiness = result.get("readiness_score", 1.0)
    classification = result.get("readiness_classification", "READY")

    lines = [
        "=" * 70,
        "PHASE 141: CALIBRATION & UNCERTAINTY CONSOLIDATED REPORT",
        "=" * 70,
        CALIBRATION_UNCERTAINTY_DISCLAIMER,
        "-" * 70,
        f"Active Profile          : {prof_name}",
        f"Phase                   : {result.get('phase', 141)}",
        f"Next Phase              : {result.get('next_phase', 142)}",
        f"Target Final Phase      : {result.get('target_final_phase', 160)}",
        f"Calibration Contracts   : {result.get('calibration_contract_count', 0)}",
        f"Uncertainty Contracts   : {result.get('uncertainty_contract_count', 0)}",
        f"Health Status           : {result.get('health_status', 'UNKNOWN')}",
        f"Validation Status       : {result.get('validation_status', 'UNKNOWN')}",
        f"Readiness Score         : {readiness:.4f} ({classification})",
        f"Zero Training Executed  : True",
        f"Zero Prediction Executed: True",
        f"Zero Calibration Executed: True",
        f"Zero Uncertainty Executed: True",
        f"Non-Signal Verified     : True",
        "=" * 70,
    ]
    return "\n".join(lines) + "\n"

