# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Report Builder Module.

Provides markdown formatting functions and formal legal disclaimers for all Phase 149 reports.
"""

from typing import Any, Dict, Optional
import pandas as pd


MONTE_CARLO_REPORT_DISCLAIMER = (
    "Bu çıktı Phase 149 Monte Carlo Robustness and Parameter Stability raporudur. "
    "Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, "
    "Monte-Carlo/readiness/robustness/parameter-stability değerini trade sinyali veya "
    "production-ready/broker-ready/onay olarak kullanma, gerçek Monte Carlo execution, "
    "bootstrap, resampling, parameter optimization, parameter sweep, optimizer, "
    "gerçek model training, model fit/predict/inference, dataset materialization, "
    "target/label/prediction üretimi, gerçek VaR/ES/distribution/robustness metric hesaplama, "
    "performans garantisi, model deployment, model registry write, model artifact persistence, "
    "scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı "
    "veya gerçek provider API çağrısı değildir."
)


def build_monte_carlo_disclaimer() -> str:
    """Return the standardized Phase 149 legal disclaimer."""
    return MONTE_CARLO_REPORT_DISCLAIMER


def _df_to_markdown(df: Optional[pd.DataFrame]) -> str:
    """Helper formatting DataFrame as markdown table."""
    if df is None or df.empty:
        return "_No tabular records available._"
    try:
        return df.to_markdown(index=False)
    except Exception:
        return df.to_string(index=False)


def build_monte_carlo_profile_markdown_report(summary: Dict[str, Any], profile_df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 149: Monte Carlo Profile Registry Report\n\n"
        f"> **Disclaimer**: {MONTE_CARLO_REPORT_DISCLAIMER}\n\n"
        f"- **Domain**: `{summary.get('domain')}`\n"
        f"- **Active Profile**: `{summary.get('active_profile')}`\n"
        f"- **Total Profiles**: `{summary.get('total_profiles')}`\n"
        f"- **All Local Only**: `{summary.get('all_local_only')}`\n"
        f"- **All Zero Execution**: `{summary.get('all_zero_execution')}`\n"
        f"- **Status**: `{summary.get('status')}`\n\n"
        f"## Registered Profiles\n\n{_df_to_markdown(profile_df)}\n"
    )


def build_monte_carlo_contract_markdown_report(summary: Dict[str, Any], df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 149: Monte Carlo Robustness Contracts Report\n\n"
        f"> **Disclaimer**: {MONTE_CARLO_REPORT_DISCLAIMER}\n\n"
        f"- **Total Contracts**: `{summary.get('total_contracts')}`\n"
        f"- **All Contracts Valid**: `{summary.get('all_contracts_valid')}`\n"
        f"- **All Executions Blocked**: `{summary.get('all_executions_blocked')}`\n"
        f"- **Status**: `{summary.get('status')}`\n\n"
        f"## Contracts Matrix\n\n{_df_to_markdown(df)}\n"
    )


def build_bootstrap_contract_markdown_report(summary: Dict[str, Any], df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 149: Bootstrap Simulation Contracts Report\n\n"
        f"> **Disclaimer**: {MONTE_CARLO_REPORT_DISCLAIMER}\n\n"
        f"- **Total Methods**: `{summary.get('total_methods')}`\n"
        f"- **All Unexecuted**: `{summary.get('all_unexecuted')}`\n"
        f"- **Status**: `{summary.get('status')}`\n\n"
        f"## Bootstrap Specifications\n\n{_df_to_markdown(df)}\n"
    )


def build_resampling_placeholder_markdown_report(summary: Dict[str, Any], df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 149: Resampling and Perturbation Placeholders Report\n\n"
        f"> **Disclaimer**: {MONTE_CARLO_REPORT_DISCLAIMER}\n\n"
        f"- **Total Contracts**: `{summary.get('total_contracts', summary.get('total_placeholders', 0))}`\n"
        f"- **All Unexecuted**: `{summary.get('all_unexecuted')}`\n"
        f"- **Status**: `{summary.get('status')}`\n\n"
        f"## Resampling Specifications\n\n{_df_to_markdown(df)}\n"
    )


def build_parameter_stability_markdown_report(summary: Dict[str, Any], df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 149: Parameter Stability and Sensitivity Contracts Report\n\n"
        f"> **Disclaimer**: {MONTE_CARLO_REPORT_DISCLAIMER}\n\n"
        f"- **Total Contracts**: `{summary.get('total_contracts')}`\n"
        f"- **All Valid**: `{summary.get('all_valid')}`\n"
        f"- **Optimizations Disabled**: `{summary.get('all_optimizations_disabled')}`\n"
        f"- **Status**: `{summary.get('status')}`\n\n"
        f"## Parameter Stability Matrix\n\n{_df_to_markdown(df)}\n"
    )


def build_robustness_placeholder_markdown_report(summary: Dict[str, Any], df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 149: Robustness Envelope Placeholders Report\n\n"
        f"> **Disclaimer**: {MONTE_CARLO_REPORT_DISCLAIMER}\n\n"
        f"- **Total Bounds**: `{summary.get('total_envelope_bounds', 0)}`\n"
        f"- **All Uncalculated**: `{summary.get('all_uncalculated')}`\n"
        f"- **Status**: `{summary.get('status')}`\n\n"
        f"## Envelope Bounds\n\n{_df_to_markdown(df)}\n"
    )


def build_monte_carlo_metric_placeholder_markdown_report(summary: Dict[str, Any], df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 149: Monte Carlo Metric Placeholders Report\n\n"
        f"> **Disclaimer**: {MONTE_CARLO_REPORT_DISCLAIMER}\n\n"
        f"- **Total Metrics**: `{summary.get('total_metric_placeholders', 0)}`\n"
        f"- **All Uncalculated**: `{summary.get('all_uncalculated')}`\n"
        f"- **Status**: `{summary.get('status')}`\n\n"
        f"## Metric Formulas\n\n{_df_to_markdown(df)}\n"
    )


def build_monte_carlo_dependency_markdown_report(summary: Dict[str, Any], df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 149: Monte Carlo Dependencies Report\n\n"
        f"> **Disclaimer**: {MONTE_CARLO_REPORT_DISCLAIMER}\n\n"
        f"- **Total Dependencies**: `{summary.get('total_dependencies', 0)}`\n"
        f"- **All Satisfied**: `{summary.get('all_satisfied')}`\n"
        f"- **Status**: `{summary.get('status')}`\n\n"
        f"## Dependency Matrix\n\n{_df_to_markdown(df)}\n"
    )


def build_monte_carlo_guard_markdown_report(summary: Dict[str, Any], df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 149: Monte Carlo Bias & Lookahead Guards Report\n\n"
        f"> **Disclaimer**: {MONTE_CARLO_REPORT_DISCLAIMER}\n\n"
        f"- **Total Guards**: `{summary.get('total_guards', 0)}`\n"
        f"- **All Active**: `{summary.get('all_active')}`\n"
        f"- **Status**: `{summary.get('status')}`\n\n"
        f"## Active Guards\n\n{_df_to_markdown(df)}\n"
    )


def build_monte_carlo_disabled_execution_markdown_report(summary: Dict[str, Any], df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 149: Disabled Execution Audit Report\n\n"
        f"> **Disclaimer**: {MONTE_CARLO_REPORT_DISCLAIMER}\n\n"
        f"- **Total Capabilities**: `{summary.get('total_capabilities', 0)}`\n"
        f"- **All Executions Blocked**: `{summary.get('all_executions_blocked')}`\n"
        f"- **Status**: `{summary.get('status')}`\n\n"
        f"## Disabled Execution Policies\n\n{_df_to_markdown(df)}\n"
    )


def build_monte_carlo_findings_markdown_report(summary: Dict[str, Any], df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 149: Monte Carlo Findings Report\n\n"
        f"> **Disclaimer**: {MONTE_CARLO_REPORT_DISCLAIMER}\n\n"
        f"- **Total Findings**: `{summary.get('total_findings', 0)}`\n"
        f"- **Critical Findings**: `{summary.get('critical_count', 0)}`\n"
        f"- **High Findings**: `{summary.get('high_count', 0)}`\n"
        f"- **Manual Review Required**: `{summary.get('manual_review_count', 0)}`\n"
        f"- **Status**: `{summary.get('status')}`\n\n"
        f"## Findings Register\n\n{_df_to_markdown(df)}\n"
    )


def build_monte_carlo_readiness_score_markdown_report(summary: Dict[str, Any], df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 149: Monte Carlo Readiness Score Report\n\n"
        f"> **Disclaimer**: {MONTE_CARLO_REPORT_DISCLAIMER}\n\n"
        f"- **Readiness Score**: `{summary.get('score')}`\n"
        f"- **Classification**: `{summary.get('classification')}`\n"
        f"- **Meets Threshold**: `{summary.get('meets_threshold')}`\n"
        f"- **Manual Review Required**: `{summary.get('manual_review_required')}`\n"
        f"- **Status**: `{summary.get('status')}`\n\n"
        f"## Score Details\n\n{_df_to_markdown(df)}\n"
    )


def build_monte_carlo_manifest_markdown_report(summary: Dict[str, Any], df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 149: Master Monte Carlo Robustness Manifest\n\n"
        f"> **Disclaimer**: {MONTE_CARLO_REPORT_DISCLAIMER}\n\n"
        f"- **Manifest ID**: `{summary.get('manifest_id')}`\n"
        f"- **Current Phase**: `{summary.get('current_phase')}`\n"
        f"- **Next Phase**: `{summary.get('next_phase')}`\n"
        f"- **Target Final Phase**: `{summary.get('target_final_phase')}`\n"
        f"- **All Negative Invariants Satisfied**: `{summary.get('all_negative_invariants_satisfied')}`\n"
        f"- **Phase 150 Handoff Ready**: `{summary.get('phase_150_handoff_ready')}`\n"
        f"- **Status**: `{summary.get('status')}`\n\n"
        f"## Invariants Certification\n\n{_df_to_markdown(df)}\n"
    )


def build_monte_carlo_validation_markdown_report(summary: Dict[str, Any], df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 149: Monte Carlo Validation Report\n\n"
        f"> **Disclaimer**: {MONTE_CARLO_REPORT_DISCLAIMER}\n\n"
        f"- **Validation Status**: `{summary.get('validation_status')}`\n"
        f"- **Total Checks**: `{summary.get('total_checks')}`\n"
        f"- **All Passed**: `{summary.get('all_passed')}`\n"
        f"- **Status**: `{summary.get('status')}`\n\n"
        f"## Validation Checks\n\n{_df_to_markdown(df)}\n"
    )


def build_monte_carlo_safety_markdown_report(summary: Dict[str, Any], df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 149: Monte Carlo Safety Boundary Report\n\n"
        f"> **Disclaimer**: {MONTE_CARLO_REPORT_DISCLAIMER}\n\n"
        f"- **Safety Status**: `{summary.get('safety_status')}`\n"
        f"- **NO-GO Rules Enforced**: `{summary.get('no_go_count')}`\n"
        f"- **SAFE-GO Principles Active**: `{summary.get('safe_go_count')}`\n"
        f"- **Status**: `{summary.get('status')}`\n\n"
        f"## Safety Invariants\n\n{_df_to_markdown(df)}\n"
    )


def build_phase_150_handoff_markdown_report(summary: Dict[str, Any], df: Optional[pd.DataFrame] = None) -> str:
    return (
        f"# Phase 149 -> Phase 150 Handoff Report\n\n"
        f"> **Disclaimer**: {MONTE_CARLO_REPORT_DISCLAIMER}\n\n"
        f"- **Source Phase**: `{summary.get('source_phase', 149)}`\n"
        f"- **Next Phase**: `{summary.get('next_phase', 150)}`\n"
        f"- **Next Phase Name**: `{summary.get('next_phase_name')}`\n"
        f"- **Target Final Phase**: `{summary.get('target_final_phase', 160)}`\n"
        f"- **Total Prerequisites**: `{summary.get('total_prerequisites')}`\n"
        f"- **All Prerequisites Satisfied**: `{summary.get('all_prerequisites_satisfied')}`\n"
        f"- **Handoff Status**: `{summary.get('handoff_status')}`\n\n"
        f"## Handoff Items\n\n{_df_to_markdown(df)}\n"
    )
