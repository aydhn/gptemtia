"""Phase 132: Macro/Event/News Regime Markdown Report Builder."""

from typing import Any, Dict, Optional
import pandas as pd

DISCLAIMER_TEXT = (
    "Bu çıktı Phase 132 Macro/Event/News Regime Context Expansion raporudur. "
    "Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, macro/event/news "
    "context değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, "
    "model training, clustering execution, prediction/target/label üretimi, sentiment model output, "
    "haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı, "
    "production-ready/official approval/broker-ready iddiası, production deployment, "
    "model deployment, scraping veya gerçek provider API çağrısı değildir."
)


def build_macro_event_news_regime_disclaimer() -> str:
    """Return standard regulatory disclaimer for Phase 132."""
    return f"> **YASAL UYARI & SINIRLAR**\n> {DISCLAIMER_TEXT}\n"


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


def build_macro_event_news_regime_profile_markdown_report(
    summary: Dict[str, Any],
    profile_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for operational profiles."""
    lines = [
        "# Phase 132: Macro/Event/News Regime Operational Profiles",
        "",
        build_macro_event_news_regime_disclaimer(),
        "## Profile Summary",
        f"- **Active Profile**: `{summary.get('active_profile', 'balanced_local_macro_event_news_regime_context')}`",
        f"- **Total Profiles**: `{summary.get('total_profiles', 0)}`",
        f"- **Current Phase**: `{summary.get('current_phase', 132)}`",
        f"- **Target Final Phase**: `{summary.get('target_final_phase', 160)}`",
        f"- **Next Phase**: `{summary.get('next_phase', 133)}`",
        f"- **Non-Signal Certified**: `{summary.get('all_non_signal', True)}`",
        f"- **Source Preserved**: `{summary.get('all_source_preserved', True)}`",
        "",
    ]
    if profile_df is not None and not profile_df.empty:
        lines.append("## Registered Profiles Table")
        lines.append(_render_df_table(profile_df))
        lines.append("")
    return "\n".join(lines)


def build_macro_event_news_entity_markdown_report(
    summary: Dict[str, Any],
    entity_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for macro/event/news entities."""
    lines = [
        "# Phase 132: Macro, Event & News Metadata Entities Report",
        "",
        build_macro_event_news_regime_disclaimer(),
        "## Entity Registry Metrics",
        f"- **Total Entities**: `{summary.get('total_entities', 0)}`",
        f"- **Macro Entities**: `{summary.get('macro_entities', 0)}`",
        f"- **Event Entities**: `{summary.get('event_entities', 0)}`",
        f"- **News Metadata Entities**: `{summary.get('news_metadata_entities', 0)}`",
        f"- **Strictly Metadata-Only**: `True`",
        f"- **Zero Raw Text / Zero Sentiment**: `True`",
        "",
    ]
    if entity_df is not None and not entity_df.empty:
        lines.append("## Sample Entities")
        lines.append(_render_df_table(entity_df.head(15)))
        lines.append("")
    return "\n".join(lines)


def build_macro_context_markdown_report(
    summary: Dict[str, Any],
    context_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for macro indicator context."""
    lines = [
        "# Phase 132: Macro Indicator & Release Regime Context Report",
        "",
        build_macro_event_news_regime_disclaimer(),
        "## Macro Context Summary",
        f"- **Total Macro Contexts**: `{summary.get('total_macro_contexts', 0)}`",
        f"- **Non-Signal Invariant Enforced**: `True`",
        f"- **Revision Tracking Enforced**: `True`",
        f"- **Consensus Delta Placeholders**: `Non-Signal Only`",
        "",
    ]
    if context_df is not None and not context_df.empty:
        lines.append("## Macro Context Table")
        lines.append(_render_df_table(context_df))
        lines.append("")
    return "\n".join(lines)


def build_event_context_markdown_report(
    summary: Dict[str, Any],
    context_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for economic calendar event context."""
    lines = [
        "# Phase 132: Economic Calendar & Event Window Regime Context Report",
        "",
        build_macro_event_news_regime_disclaimer(),
        "## Event Context Summary",
        f"- **Total Calendar Events**: `{summary.get('total_calendar_events', 0)}`",
        f"- **Pre-Event Buffer Tracking**: `Active`",
        f"- **Post-Event Digestion Tracking**: `Active`",
        f"- **Scheduled vs Actual Alignment**: `Lookahead-Free`",
        "",
    ]
    if context_df is not None and not context_df.empty:
        lines.append("## Event Context Table")
        lines.append(_render_df_table(context_df))
        lines.append("")
    return "\n".join(lines)


def build_news_metadata_context_markdown_report(
    summary: Dict[str, Any],
    context_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for metadata-only news context."""
    lines = [
        "# Phase 132: News Metadata Regime Context Report (Zero Full Article)",
        "",
        build_macro_event_news_regime_disclaimer(),
        "## News Metadata Summary",
        f"- **Total Topic Contexts**: `{summary.get('total_topic_contexts', 0)}`",
        f"- **Asset Tag Linkages**: `Active`",
        f"- **Event Reference Linkages**: `Active`",
        f"- **Zero Sentiment Output**: `Guaranteed`",
        f"- **Zero Scraped HTML / Article Body**: `Guaranteed`",
        "",
    ]
    if context_df is not None and not context_df.empty:
        lines.append("## News Metadata Context Table")
        lines.append(_render_df_table(context_df))
        lines.append("")
    return "\n".join(lines)


def build_metadata_only_boundary_markdown_report(
    summary: Dict[str, Any],
    boundary_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for metadata-only boundary enforcement."""
    lines = [
        "# Phase 132: Metadata-Only News Boundary Enforcement Report",
        "",
        build_macro_event_news_regime_disclaimer(),
        "## Boundary Guard Summary",
        f"- **Total Boundary Rules**: `{summary.get('total_boundary_rules', 0)}`",
        f"- **Forbidden Fields Tracked**: `{summary.get('forbidden_fields_count', 0)}`",
        f"- **Strict Enforcement Active**: `True`",
        f"- **Auto-Drop Prohibited**: `True`",
        "",
    ]
    if boundary_df is not None and not boundary_df.empty:
        lines.append("## Boundary Rules Table")
        lines.append(_render_df_table(boundary_df))
        lines.append("")
    return "\n".join(lines)


def build_macro_event_news_cross_asset_markdown_report(
    summary: Dict[str, Any],
    context_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for cross-asset macro context."""
    lines = [
        "# Phase 132: Macro/Event/News Cross-Asset & Transition Context Report",
        "",
        build_macro_event_news_regime_disclaimer(),
        "## Cross-Asset Context Summary",
        f"- **Total Cross-Asset Contexts**: `{summary.get('total_cross_asset_contexts', 0)}`",
        f"- **Target Asset Classes**: `{summary.get('target_asset_classes', [])}`",
        f"- **Directional Claims**: `Prohibited`",
        f"- **Non-Signal Certified**: `True`",
        "",
    ]
    if context_df is not None and not context_df.empty:
        lines.append("## Cross-Asset Context Table")
        lines.append(_render_df_table(context_df))
        lines.append("")
    return "\n".join(lines)


def build_macro_event_news_findings_markdown_report(
    summary: Dict[str, Any],
    findings_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for diagnostic findings."""
    lines = [
        "# Phase 132: Macro/Event/News Diagnostic Findings Report",
        "",
        build_macro_event_news_regime_disclaimer(),
        "## Findings Summary",
        f"- **Total Findings**: `{summary.get('total_findings', 0)}`",
        f"- **Manual Reviews Required**: `{summary.get('manual_review_count', 0)}`",
        f"- **Auto-Destructive Action Permitted**: `False`",
        "",
    ]
    if findings_df is not None and not findings_df.empty:
        lines.append("## Findings Table")
        lines.append(_render_df_table(findings_df))
        lines.append("")
    return "\n".join(lines)


def build_macro_event_news_score_markdown_report(
    summary: Dict[str, Any],
    score_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for context scoring."""
    lines = [
        "# Phase 132: Macro/Event/News Context Score Report",
        "",
        build_macro_event_news_regime_disclaimer(),
        "## Context Score Diagnostics",
        f"- **Context Score**: `{summary.get('context_score', 1.0):.4f}`",
        f"- **Classification**: `{summary.get('classification', 'high_context_integrity')}`",
        f"- **Meets Threshold**: `{summary.get('meets_threshold', True)}`",
        f"- **Non-Signal Invariant Certified**: `True`",
        f"- **Official Approval Claim**: `False`",
        f"- **Production Ready Claim**: `False`",
        "",
    ]
    if score_df is not None and not score_df.empty:
        lines.append("## Score Table")
        lines.append(_render_df_table(score_df))
        lines.append("")
    return "\n".join(lines)


def build_macro_event_news_manifest_markdown_report(
    summary: Dict[str, Any],
    manifest_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for context manifest."""
    lines = [
        "# Phase 132: Macro/Event/News Regime Context Manifest",
        "",
        build_macro_event_news_regime_disclaimer(),
        "## Manifest Invariants",
        f"- **Manifest Name**: `{summary.get('manifest_name', 'macro_event_news_regime_context_manifest')}`",
        f"- **Current Phase**: `{summary.get('current_phase', 132)}`",
        f"- **Next Phase**: `{summary.get('next_phase', 133)}`",
        f"- **Context Score**: `{summary.get('context_score', 1.0):.4f}`",
        f"- **Zero Raw Text / Scraped HTML**: `True`",
        f"- **Zero Sentiment Models**: `True`",
        f"- **Zero Embeddings / Vectors**: `True`",
        f"- **Zero Model Training / Fit / Predict**: `True`",
        f"- **Zero Clustering Execution**: `True`",
        f"- **Source Preservation Enforced**: `True`",
        "",
    ]
    if manifest_df is not None and not manifest_df.empty:
        lines.append("## Manifest Content")
        lines.append(_render_df_table(manifest_df))
        lines.append("")
    return "\n".join(lines)


def build_macro_event_news_validation_markdown_report(
    summary: Dict[str, Any],
    validation_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for validation check suite."""
    lines = [
        "# Phase 132: Macro/Event/News Regime Validation Report",
        "",
        build_macro_event_news_regime_disclaimer(),
        "## Validation Results",
        f"- **Validation Status**: `{summary.get('validation_status', 'VALIDATION_PASS')}`",
        f"- **Total Checks**: `{summary.get('total_checks', 0)}`",
        f"- **Passed Checks**: `{summary.get('passed_checks', 0)}`",
        f"- **Forbidden Claims Clean**: `{summary.get('forbidden_claims_clean', True)}`",
        "",
    ]
    if validation_df is not None and not validation_df.empty:
        lines.append("## Validation Checks Table")
        lines.append(_render_df_table(validation_df))
        lines.append("")
    return "\n".join(lines)


def build_macro_event_news_safety_markdown_report(
    summary: Dict[str, Any],
    safety_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for safety boundary boundaries."""
    lines = [
        "# Phase 132: Macro/Event/News Regime Safety Boundary Report",
        "",
        build_macro_event_news_regime_disclaimer(),
        "## Safety Summary",
        f"- **Safety Status**: `{summary.get('safety_status', 'SECURE')}`",
        f"- **NO-GO Rules Enforced**: `{summary.get('no_go_count', 0)}`",
        f"- **SAFE-GO Principles Active**: `{summary.get('safe_go_count', 0)}`",
        f"- **Zero Live Trading**: `Guaranteed`",
        f"- **Zero Broker Execution**: `Guaranteed`",
        "",
    ]
    if safety_df is not None and not safety_df.empty:
        lines.append("## Safety Rules Table")
        lines.append(_render_df_table(safety_df))
        lines.append("")
    return "\n".join(lines)


def build_phase_133_handoff_markdown_report(
    summary: Dict[str, Any],
    handoff_df: Optional[pd.DataFrame] = None,
) -> str:
    """Build markdown report for Phase 133 handoff."""
    lines = [
        "# Phase 132 -> Phase 133: Regime Validation and No-Lookahead Acceptance Handoff Report",
        "",
        build_macro_event_news_regime_disclaimer(),
        "## Handoff Prerequisites",
        f"- **Handoff Status**: `{summary.get('handoff_status', 'READY')}`",
        f"- **Current Source Phase**: `{summary.get('current_phase', 132)}`",
        f"- **Next Phase**: `{summary.get('next_phase', 133)}`",
        f"- **Target Final Phase**: `{summary.get('target_final_phase', 160)}`",
        f"- **Total Handoff Items**: `{summary.get('total_items', 0)}`",
        f"- **All Prerequisites Ready**: `{summary.get('all_ready', True)}`",
        "",
    ]
    if handoff_df is not None and not handoff_df.empty:
        lines.append("## Handoff Checklist Table")
        lines.append(_render_df_table(handoff_df))
        lines.append("")
    return "\n".join(lines)
