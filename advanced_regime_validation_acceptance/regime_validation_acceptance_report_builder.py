"""Phase 133: Regime Validation Acceptance Markdown and Text Report Builder.

Formats human-readable and audit-compliant markdown reports with mandatory disclaimers.
Uses zero external dependencies (no tabulate requirement).
"""

from typing import Any, Dict, Optional
import pandas as pd


def build_regime_validation_acceptance_disclaimer() -> str:
    """Return standard non-signal legal disclaimer for Phase 133."""
    return (
        "> [!IMPORTANT]\n"
        "> **Phase 133 Regime Validation Acceptance Disclaimer**:\n"
        "> Bu çıktı Phase 133 Regime Validation and No-Lookahead Acceptance raporudur. "
        "> Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, validation/acceptance score’u trade sinyali olarak kullanma, "
        "> strateji üretimi, backtest, optimizer, model training, clustering execution, prediction/target/label üretimi, "
        "> sentiment model output, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı, "
        "> production-ready/official approval/broker-ready iddiası, production deployment, model deployment, scraping "
        "> veya gerçek provider API çağrısı değildir."
    )


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
    return "\n".join([header_line, separator_line] + rows)


def build_regime_validation_acceptance_profile_markdown_report(
    summary: Dict[str, Any], profile_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for profile registry."""
    lines = [
        "# Phase 133: Regime Validation Acceptance Profile Registry Report",
        "",
        build_regime_validation_acceptance_disclaimer(),
        "",
        "## Profile Overview",
        f"- **Active Profile**: `{summary.get('active_profile', 'balanced_local_regime_validation_acceptance')}`",
        f"- **Current Phase**: `{summary.get('current_phase', 133)}`",
        f"- **Target Final Phase**: `{summary.get('target_final_phase', 160)}`",
        f"- **Next Phase**: `{summary.get('next_phase', 134)}`",
        f"- **Total Profiles**: `{summary.get('total_profiles', 0)}`",
        f"- **Non-Signal Certified**: `{summary.get('all_non_signal', True)}`",
        f"- **Zero Model Training**: `{summary.get('zero_model_training', True)}`",
        "",
    ]
    if profile_df is not None and not profile_df.empty:
        lines.append("## Registered Profiles")
        lines.append(_render_df_table(profile_df))
    return "\n".join(lines)


def build_regime_validation_gate_markdown_report(
    summary: Dict[str, Any], gate_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for validation gates."""
    lines = [
        "# Phase 133: Regime Validation Gates Report",
        "",
        build_regime_validation_acceptance_disclaimer(),
        "",
        "## Gates Summary",
        f"- **Total Gates**: `{summary.get('total_gates', 19)}`",
        f"- **Passed Gates**: `{summary.get('passed_gates', 19)}`",
        f"- **Failed Gates**: `{summary.get('failed_gates', 0)}`",
        f"- **All Gates Passed**: `{summary.get('all_passed', True)}`",
        "",
    ]
    if gate_df is not None and not gate_df.empty:
        lines.append("## Gate Evaluation Details")
        cols = [c for c in ["gate_id", "gate_name", "status", "passed", "description"] if c in gate_df.columns]
        lines.append(_render_df_table(gate_df[cols]))
    return "\n".join(lines)


def build_no_lookahead_acceptance_markdown_report(
    summary: Dict[str, Any], report_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for no-lookahead acceptance."""
    lines = [
        "# Phase 133: Regime No-Lookahead Acceptance Report",
        "",
        build_regime_validation_acceptance_disclaimer(),
        "",
        "## No-Lookahead Summary",
        f"- **Total Checks**: `{summary.get('total_checks', 0)}`",
        f"- **Passed Checks**: `{summary.get('passed_checks', 0)}`",
        f"- **Lookahead Clean**: `{summary.get('lookahead_clean', True)}`",
        "",
    ]
    if report_df is not None and not report_df.empty:
        lines.append("## Checks Evaluated")
        lines.append(_render_df_table(report_df))
    return "\n".join(lines)


def build_metadata_only_news_acceptance_markdown_report(
    summary: Dict[str, Any], report_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for metadata-only news acceptance."""
    lines = [
        "# Phase 133: Regime Metadata-Only News Acceptance Report",
        "",
        build_regime_validation_acceptance_disclaimer(),
        "",
        "## News Metadata Boundary Summary",
        f"- **Total Checks**: `{summary.get('total_checks', 0)}`",
        f"- **Metadata Only Pure**: `{summary.get('metadata_only_pure', True)}`",
        "- **Article Body / Scraped HTML**: Strictly Excluded",
        "- **Sentiment Output / Embeddings**: Strictly Excluded",
        "",
    ]
    if report_df is not None and not report_df.empty:
        lines.append("## News Acceptance Checks")
        lines.append(_render_df_table(report_df))
    return "\n".join(lines)


def build_component_acceptance_markdown_report(
    summary: Dict[str, Any], report_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for regime component acceptance."""
    lines = [
        "# Phase 133: Regime Component Acceptance Report (Phases 127-132)",
        "",
        build_regime_validation_acceptance_disclaimer(),
        "",
        "## Components Evaluated",
        f"- **Component**: `{summary.get('component', 'regime_components')}`",
        f"- **Total Checks**: `{summary.get('total_checks', 0)}`",
        f"- **Passed Checks**: `{summary.get('passed_checks', 0)}`",
        f"- **All Passed**: `{summary.get('all_passed', True)}`",
        "",
    ]
    if report_df is not None and not report_df.empty:
        lines.append("## Check Details")
        lines.append(_render_df_table(report_df))
    return "\n".join(lines)


def build_dependency_acceptance_markdown_report(
    summary: Dict[str, Any], report_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for upstream validation/quality dependencies."""
    lines = [
        "# Phase 133: Regime Dependency Acceptance Report",
        "",
        build_regime_validation_acceptance_disclaimer(),
        "",
        "## Dependency Overview",
        f"- **Total Dependencies**: `{summary.get('total_dependencies', 0)}`",
        f"- **Satisfied Dependencies**: `{summary.get('satisfied_dependencies', 0)}`",
        f"- **All Satisfied**: `{summary.get('all_satisfied', True)}`",
        "",
    ]
    if report_df is not None and not report_df.empty:
        lines.append("## Upstream Dependency Status")
        lines.append(_render_df_table(report_df))
    return "\n".join(lines)


def build_regime_validation_findings_markdown_report(
    summary: Dict[str, Any], findings_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for diagnostic findings."""
    lines = [
        "# Phase 133: Regime Validation Findings Report",
        "",
        build_regime_validation_acceptance_disclaimer(),
        "",
        "## Findings Summary",
        f"- **Total Findings**: `{summary.get('total_findings', 0)}`",
        f"- **Critical Blockers**: `{summary.get('critical_blockers', 0)}`",
        f"- **Manual Review Required**: `{summary.get('manual_review_required_count', 0)}`",
        f"- **Destructive Remediation Allowed**: `{summary.get('destructive_action_allowed', False)}`",
        "",
    ]
    if findings_df is not None and not findings_df.empty:
        lines.append("## Findings Registry")
        lines.append(_render_df_table(findings_df))
    return "\n".join(lines)


def build_regime_acceptance_score_markdown_report(
    summary: Dict[str, Any], score_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for acceptance scoring."""
    lines = [
        "# Phase 133: Regime Acceptance Score Report",
        "",
        build_regime_validation_acceptance_disclaimer(),
        "",
        "## Acceptance Score",
        f"- **Overall Score**: `{summary.get('overall_score', 1.0)}`",
        f"- **Score Tier**: `{summary.get('score_tier', 'high_acceptance_integrity')}`",
        f"- **Status**: `{summary.get('passed', True)}`",
        "- **Trading Signal**: FALSE (NEVER A TRADE RECOMMENDATION)",
        "",
    ]
    if score_df is not None and not score_df.empty:
        lines.append("## Scoring Metrics")
        lines.append(_render_df_table(score_df))
    return "\n".join(lines)


def build_regime_validation_acceptance_manifest_markdown_report(
    summary: Dict[str, Any], manifest_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for the official acceptance manifest."""
    lines = [
        "# Phase 133: Regime Validation Acceptance Manifest",
        "",
        build_regime_validation_acceptance_disclaimer(),
        "",
        "## Manifest Summary",
        f"- **Manifest Name**: `{summary.get('manifest_name', 'regime_validation_acceptance_manifest')}`",
        f"- **Current Phase**: `{summary.get('current_phase', 133)}`",
        f"- **Next Phase**: `{summary.get('next_phase', 134)}`",
        f"- **Acceptance Score**: `{summary.get('acceptance_score', 1.0)}`",
        f"- **Manifest Valid**: `{summary.get('manifest_valid', True)}`",
        "",
    ]
    if manifest_df is not None and not manifest_df.empty:
        lines.append("## Manifest Fields")
        lines.append(_render_df_table(manifest_df))
    return "\n".join(lines)


def build_regime_validation_acceptance_validation_markdown_report(
    summary: Dict[str, Any], validation_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for subsystem validation."""
    lines = [
        "# Phase 133: Regime Validation Acceptance Integrity Report",
        "",
        build_regime_validation_acceptance_disclaimer(),
        "",
        "## Validation Status",
        f"- **Status**: `{summary.get('status', 'VALIDATION_PASS')}`",
        f"- **Total Checks**: `{summary.get('total_checks', 0)}`",
        f"- **Passed Checks**: `{summary.get('passed_checks', 0)}`",
        f"- **Forbidden Claims Clean**: `{summary.get('forbidden_claims_clean', True)}`",
        "",
    ]
    if validation_df is not None and not validation_df.empty:
        lines.append("## Check Details")
        lines.append(_render_df_table(validation_df))
    return "\n".join(lines)


def build_regime_validation_acceptance_safety_markdown_report(
    summary: Dict[str, Any], safety_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for safety boundary conditions."""
    lines = [
        "# Phase 133: Regime Validation Acceptance Safety Boundary Report",
        "",
        build_regime_validation_acceptance_disclaimer(),
        "",
        "## Safety Boundary",
        f"- **Safety Status**: `{summary.get('safety_status', 'SECURE')}`",
        f"- **NO-GO Conditions Enforced**: `{summary.get('no_go_count', 19)}`",
        f"- **SAFE-GO Principles Active**: `{summary.get('safe_go_count', 12)}`",
        "- **Live Trading Allowed**: `False`",
        "- **Model Execution Allowed**: `False`",
        "",
    ]
    if safety_df is not None and not safety_df.empty:
        lines.append("## Conditions Registry")
        lines.append(_render_df_table(safety_df))
    return "\n".join(lines)


def build_phase_134_handoff_markdown_report(
    summary: Dict[str, Any], handoff_df: Optional[pd.DataFrame] = None
) -> str:
    """Build markdown report for Phase 134 handoff."""
    lines = [
        "# Phase 133 -> Phase 134 Handoff Report: Regime FeatureStore Integration",
        "",
        build_regime_validation_acceptance_disclaimer(),
        "",
        "## Handoff Overview",
        f"- **Handoff Status**: `{summary.get('handoff_status', 'READY')}`",
        f"- **Current Phase**: `{summary.get('current_phase', 133)}`",
        f"- **Next Phase**: `{summary.get('next_phase', 134)}`",
        f"- **Target Final Phase**: `{summary.get('target_final_phase', 160)}`",
        f"- **Total Handoff Items**: `{summary.get('total_items', 0)}`",
        f"- **All Items Ready**: `{summary.get('all_ready', True)}`",
        "",
    ]
    if handoff_df is not None and not handoff_df.empty:
        lines.append("## Handoff Deliverables")
        lines.append(_render_df_table(handoff_df))
    return "\n".join(lines)
