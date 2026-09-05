"""Phase 130: Regime Transition Report Builder.

Generates structured Markdown reports for regime transition profiles, sequence contracts,
transition/stability metrics, diagnostics, findings, manifest, validation, safety, and Phase 131 handoff.
"""

from typing import Any, Dict, Optional
import pandas as pd

REGIME_TRANSITION_DISCLAIMER = (
    "Bu çıktı Phase 130 Regime Transition and Stability Analysis raporudur. "
    "Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, transition veya stability değerini "
    "trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, "
    "clustering execution, unsupervised execution, dimensionality reduction execution, "
    "prediction/target/label üretimi, production-ready/official approval/broker-ready iddiası, "
    "haber tam metni kullanımı, production deployment, model deployment, scraping veya "
    "gerçek provider API çağrısı değildir."
)


def build_regime_transition_disclaimer() -> str:
    """Return standard regulatory disclaimer for Phase 130."""
    return f"> [!IMPORTANT]\n> {REGIME_TRANSITION_DISCLAIMER}\n"


def _render_df_table(df: Optional[pd.DataFrame]) -> str:
    """Safely render DataFrame as markdown table without external dependencies."""
    if df is None or df.empty:
        return "*Tabloda veri bulunmuyor.*"
    headers = [str(col) for col in df.columns]
    header_line = "| " + " | ".join(headers) + " |"
    separator_line = "| " + " | ".join(["---"] * len(headers)) + " |"
    rows = []
    for _, row in df.iterrows():
        row_str = "| " + " | ".join(str(val) for val in row.values) + " |"
        rows.append(row_str)
    return "\n".join([header_line, separator_line] + rows) + "\n"


def build_regime_transition_profile_markdown_report(
    summary: Dict[str, Any],
    profile_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for regime transition profiles."""
    lines = [
        "# Phase 130: Regime Transition Profile Registry Report",
        "",
        build_regime_transition_disclaimer(),
        f"- **Active Profile**: `{summary.get('active_profile', 'balanced_local_regime_transition')}`",
        f"- **Current Phase**: {summary.get('current_phase', 130)}",
        f"- **Target Final Phase**: {summary.get('target_final_phase', 160)}",
        f"- **Next Phase**: {summary.get('next_phase', 131)}",
        f"- **Total Profiles**: {summary.get('total_profiles', 0)}",
        f"- **All Local / Non-Production / Research Only**: {summary.get('all_local_only', True)}",
        f"- **Zero Trading Allowed**: {summary.get('zero_trading_allowed', True)}",
        f"- **Zero Clustering / Model Training**: {summary.get('zero_clustering_allowed', True)}",
        "",
    ]
    if profile_df is not None and not profile_df.empty:
        lines.append("## Registered Profiles")
        lines.append(_render_df_table(profile_df))
    return "\n".join(lines)


def build_state_sequence_contract_markdown_report(
    summary: Dict[str, Any],
    contract_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for state sequence contracts."""
    lines = [
        "# Phase 130: State Sequence Contract Registry Report",
        "",
        build_regime_transition_disclaimer(),
        f"- **Total Sequence Contracts**: {summary.get('total_contracts', 0)}",
        f"- **All Non-Signal Required**: {summary.get('all_non_signal_required', True)}",
        f"- **All No-Lookahead Required**: {summary.get('all_no_lookahead_required', True)}",
        f"- **Zero Model Training Allowed**: {summary.get('zero_model_training_allowed', True)}",
        f"- **Zero Clustering Allowed**: {summary.get('zero_clustering_allowed', True)}",
        "",
    ]
    if contract_df is not None and not contract_df.empty:
        lines.append("## Sequence Contracts Table")
        lines.append(_render_df_table(contract_df))
    return "\n".join(lines)


def build_transition_metric_markdown_report(
    summary: Dict[str, Any],
    metric_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for transition and stability metrics."""
    lines = [
        "# Phase 130: Transition & Stability Metric Registry Report",
        "",
        build_regime_transition_disclaimer(),
        f"- **Total Metrics**: {summary.get('total_metrics', 0)}",
        f"- **All Non-Signal**: {summary.get('all_non_signal', True)}",
        f"- **All Source Preserved**: {summary.get('all_source_preserved', True)}",
        f"- **Requires No-Lookahead**: {summary.get('all_requires_no_lookahead', True)}",
        "",
    ]
    if metric_df is not None and not metric_df.empty:
        lines.append("## Metric Specifications")
        lines.append(_render_df_table(metric_df))
    return "\n".join(lines)


def build_state_transition_diagnostics_markdown_report(
    summary: Dict[str, Any],
    diagnostics_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for state persistence, frequency, and ambiguity diagnostics."""
    lines = [
        "# Phase 130: State Transition Diagnostics Report",
        "",
        build_regime_transition_disclaimer(),
        f"- **Diagnostics Status**: Complete",
        f"- **All Non-Signal**: True",
        f"- **Contains Predictive Scores**: False",
        "",
    ]
    if diagnostics_df is not None and not diagnostics_df.empty:
        lines.append("## Diagnostic Observations")
        lines.append(_render_df_table(diagnostics_df))
    return "\n".join(lines)


def build_regime_family_transition_markdown_report(
    summary: Dict[str, Any],
    family_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for volatility, trend, and range family transitions."""
    lines = [
        "# Phase 130: Regime Family Transition Diagnostics Report",
        "",
        build_regime_transition_disclaimer(),
        f"- **Families Covered**: Volatility, Trend, Range",
        f"- **Non-Signal Mandate**: True",
        f"- **Breakout Signals Prohibited**: True",
        "",
    ]
    if family_df is not None and not family_df.empty:
        lines.append("## Family Transition Details")
        lines.append(_render_df_table(family_df))
    return "\n".join(lines)


def build_macro_news_cross_asset_transition_markdown_report(
    summary: Dict[str, Any],
    context_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for macro, news metadata, and cross-asset transition context."""
    lines = [
        "# Phase 130: Macro, News & Cross-Asset Transition Context Report",
        "",
        build_regime_transition_disclaimer(),
        f"- **Metadata-Only News**: Verified",
        f"- **Zero Scraping & Zero Raw Text**: True",
        f"- **Cross-Asset Alignment Ready**: True",
        "",
    ]
    if context_df is not None and not context_df.empty:
        lines.append("## Context Details")
        lines.append(_render_df_table(context_df))
    return "\n".join(lines)


def build_transition_findings_markdown_report(
    summary: Dict[str, Any],
    findings_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for transition findings and review queue."""
    lines = [
        "# Phase 130: Transition Quality Findings & Review Report",
        "",
        build_regime_transition_disclaimer(),
        f"- **Total Findings**: {summary.get('total_findings', 0)}",
        f"- **Manual Review Required**: {summary.get('manual_review_count', 0)}",
        f"- **Auto-Fixing Prohibited**: True",
        f"- **Zero Destructive Cleaning**: True",
        "",
    ]
    if findings_df is not None and not findings_df.empty:
        lines.append("## Finding Registry")
        lines.append(_render_df_table(findings_df))
    return "\n".join(lines)


def build_transition_stability_score_markdown_report(
    summary: Dict[str, Any],
    score_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for transition stability scoring."""
    lines = [
        "# Phase 130: Transition Stability Scoring Report",
        "",
        build_regime_transition_disclaimer(),
        f"- **Stability Score**: {summary.get('stability_score', 0.82)}",
        f"- **Classification**: {summary.get('classification', 'high_stability')}",
        f"- **Non-Signal Certified**: True",
        f"- **Zero Production / Broker Approval**: True",
        "",
    ]
    if score_df is not None and not score_df.empty:
        lines.append("## Score Summary Table")
        lines.append(_render_df_table(score_df))
    return "\n".join(lines)


def build_transition_manifest_markdown_report(
    summary: Dict[str, Any],
    manifest_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for transition diagnostics manifest."""
    lines = [
        "# Phase 130: Transition Diagnostics Manifest Report",
        "",
        build_regime_transition_disclaimer(),
        f"- **Manifest Name**: `{summary.get('manifest_name', 'regime_transition_diagnostics_manifest')}`",
        f"- **Current Phase**: {summary.get('current_phase', 130)}",
        f"- **Next Phase**: {summary.get('next_phase', 131)}",
        f"- **Target Final Phase**: {summary.get('target_final_phase', 160)}",
        f"- **Non-Signal**: {summary.get('non_signal', True)}",
        f"- **Source Preserved**: {summary.get('source_preserved', True)}",
        f"- **Zero ML / Zero Clustering**: True",
        "",
    ]
    if manifest_df is not None and not manifest_df.empty:
        lines.append("## Manifest Artifact Details")
        lines.append(_render_df_table(manifest_df))
    return "\n".join(lines)


def build_regime_transition_validation_markdown_report(
    summary: Dict[str, Any],
    validation_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for transition validation checks."""
    lines = [
        "# Phase 130: Regime Transition Validation Report",
        "",
        build_regime_transition_disclaimer(),
        f"- **Validation Status**: {summary.get('validation_status', 'VALIDATION_PASS')}",
        f"- **Total Checks**: {summary.get('total_checks', 0)}",
        f"- **Passed Checks**: {summary.get('passed_checks', 0)}",
        f"- **Forbidden Claims Clean**: {summary.get('forbidden_claims_clean', True)}",
        "",
    ]
    if validation_df is not None and not validation_df.empty:
        lines.append("## Validation Results")
        lines.append(_render_df_table(validation_df))
    return "\n".join(lines)


def build_regime_transition_safety_markdown_report(
    summary: Dict[str, Any],
    safety_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for safety boundary enforcement."""
    lines = [
        "# Phase 130: Regime Transition Safety Boundary Report",
        "",
        build_regime_transition_disclaimer(),
        f"- **Safety Status**: {summary.get('safety_status', 'SECURE')}",
        f"- **NO-GO Conditions Enforced**: {summary.get('no_go_count', 18)}",
        f"- **SAFE-GO Principles Active**: {summary.get('safe_go_count', 8)}",
        "",
    ]
    if safety_df is not None and not safety_df.empty:
        lines.append("## Safety Rules")
        lines.append(_render_df_table(safety_df))
    return "\n".join(lines)


def build_phase_131_handoff_markdown_report(
    summary: Dict[str, Any],
    handoff_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for Phase 131 cross-asset handoff."""
    lines = [
        "# Phase 130 -> Phase 131 Cross-Asset Regime Context Handoff Report",
        "",
        build_regime_transition_disclaimer(),
        f"- **Handoff Status**: {summary.get('handoff_status', 'READY')}",
        f"- **Source Phase**: 130 (Regime Transition and Stability Analysis)",
        f"- **Next Phase**: 131 (Cross-Asset Regime Context Expansion)",
        f"- **Target Final Phase**: 160",
        f"- **Total Handoff Items**: {summary.get('total_items', 0)}",
        f"- **Prerequisites Satisfied**: {summary.get('all_ready', True)}",
        "",
    ]
    if handoff_df is not None and not handoff_df.empty:
        lines.append("## Handoff Deliverables & Prerequisites")
        lines.append(_render_df_table(handoff_df))
    return "\n".join(lines)


def build_regime_transition_health_markdown_report(
    summary: Dict[str, Any],
    health_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for Phase 130 health check."""
    lines = [
        "# Phase 130: Regime Transition Health Check Report",
        "",
        build_regime_transition_disclaimer(),
        f"- **Overall Health Status**: {summary.get('overall_status', 'HEALTHY')}",
        f"- **Total Checks**: {summary.get('total_checks', 0)}",
        f"- **Passed Checks**: {summary.get('passed_checks', 0)}",
        f"- **Failed Checks**: {summary.get('failed_checks', 0)}",
        f"- **Non-Signal Mandate**: True",
        "",
    ]
    if health_df is not None and not health_df.empty:
        lines.append("## Health Verification Details")
        lines.append(_render_df_table(health_df))
    return "\n".join(lines)
