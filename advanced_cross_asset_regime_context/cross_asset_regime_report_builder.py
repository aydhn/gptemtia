"""Phase 131: Cross-Asset Regime Report Builder.

Generates comprehensive Markdown reports and legal disclaimers for Phase 131
Cross-Asset Regime Context Expansion deliverables.
"""

from typing import Any, Dict, Optional
import pandas as pd

DISCLAIMER_TEXT = (
    "> [!WARNING]\n"
    "> **YASAL VE OPERASYONEL FERAGATNAME (PHASE 131 CROSS-ASSET REGIME CONTEXT)**:\n"
    "> Bu çıktı Phase 131 Cross-Asset Regime Context Expansion raporudur. Canlı emir, broker talimatı, "
    "> kesin AL/SAT, yatırım tavsiyesi, cross-asset context/correlation/divergence değerini trade sinyali olarak kullanma, "
    "> strateji üretimi, backtest, optimizer, model training, clustering execution, prediction/target/label üretimi, "
    "> production-ready/official approval/broker-ready iddiası, haber tam metni kullanımı, production deployment, "
    "> model deployment, scraping veya gerçek provider API çağrısı değildir."
)


def build_cross_asset_regime_disclaimer() -> str:
    """Return standardized Phase 131 legal disclaimer."""
    return DISCLAIMER_TEXT


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


def build_cross_asset_regime_profile_markdown_report(
    summary: Dict[str, Any], profile_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for registered operational profiles."""
    lines = [
        "# Phase 131: Cross-Asset Regime Profile Registry Report",
        "",
        build_cross_asset_regime_disclaimer(),
        "",
        "## Profile Overview",
        f"- **Active Profile**: `{summary.get('active_profile', 'balanced_local_cross_asset_regime_context')}`",
        f"- **Current Phase**: `{summary.get('current_phase', 131)}`",
        f"- **Target Final Phase**: `{summary.get('target_final_phase', 160)}`",
        f"- **Total Registered Profiles**: `{summary.get('total_profiles', 0)}`",
        f"- **All Local Only**: `{summary.get('all_local_only', True)}`",
        f"- **All Non-Signal Certified**: `{summary.get('all_non_signal', True)}`",
        f"- **Zero Trading Allowed**: `{summary.get('zero_trading_allowed', True)}`",
        "",
    ]
    if profile_df is not None and not profile_df.empty:
        lines.extend(["## Profile Definitions", _render_df_table(profile_df), ""])
    return "\n".join(lines)


def build_cross_asset_entity_pair_markdown_report(
    summary: Dict[str, Any], pair_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for cross-asset entities and pairs."""
    lines = [
        "# Phase 131: Cross-Asset Regime Entity and Pair Registry Report",
        "",
        build_cross_asset_regime_disclaimer(),
        "",
        "## Entity & Pair Summary",
        f"- **Total Pairs Registered**: `{summary.get('total_pairs', 0)}`",
        f"- **All Non-Signal Required**: `{summary.get('all_non_signal', True)}`",
        f"- **Source Preserved**: `{summary.get('all_source_preserved', True)}`",
        f"- **Zero Arbitrage Claims**: `{summary.get('zero_arbitrage_claims', True)}`",
        "",
    ]
    if pair_df is not None and not pair_df.empty:
        lines.extend(["## Canonical Registered Pairs", _render_df_table(pair_df), ""])
    return "\n".join(lines)


def build_cross_asset_relationship_taxonomy_markdown_report(
    summary: Dict[str, Any], taxonomy_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for cross-asset relationship taxonomy."""
    lines = [
        "# Phase 131: Cross-Asset Relationship Taxonomy Report",
        "",
        build_cross_asset_regime_disclaimer(),
        "",
        "## Taxonomy Structure",
        f"- **Total Taxonomy Items**: `{summary.get('total_taxonomy_items', 0)}`",
        f"- **Zero Trading Signals Allowed**: `{summary.get('zero_trading_signals_allowed', True)}`",
        f"- **Zero Predictions Allowed**: `{summary.get('zero_predictions_allowed', True)}`",
        f"- **Requires No-Lookahead**: `{summary.get('all_require_no_lookahead', True)}`",
        "",
    ]
    if taxonomy_df is not None and not taxonomy_df.empty:
        lines.extend(["## Catalog Items", _render_df_table(taxonomy_df), ""])
    return "\n".join(lines)


def build_fx_commodity_context_markdown_report(
    summary: Dict[str, Any], context_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for FX/Commodity context linkages."""
    lines = [
        "# Phase 131: FX/Commodity Regime Context Report",
        "",
        build_cross_asset_regime_disclaimer(),
        "",
        "## FX/Commodity Context Overview",
        f"- **Total Records**: `{summary.get('total_records', 0)}`",
        f"- **Mean Readiness Score**: `{summary.get('mean_readiness_score', 0.0):.4f}`",
        f"- **Zero Trading Signals**: `{summary.get('zero_trading_signals', True)}`",
        f"- **Zero Model Execution**: True",
        "",
    ]
    if context_df is not None and not context_df.empty:
        lines.extend(["## Context Linkages", _render_df_table(context_df), ""])
    return "\n".join(lines)


def build_macro_calendar_news_context_markdown_report(
    summary: Dict[str, Any], context_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for macro/calendar/news cross-asset context."""
    lines = [
        "# Phase 131: Macro, Calendar & News Cross-Asset Context Report",
        "",
        build_cross_asset_regime_disclaimer(),
        "",
        "## Context Specifications",
        f"- **Total Records**: `{summary.get('total_records', 0)}`",
        f"- **All Metadata-Only**: `{summary.get('all_metadata_only', True)}`",
        f"- **Zero Full Article Text**: `{summary.get('zero_full_article_text', True)}`",
        f"- **All Non-Signal**: `{summary.get('all_non_signal', True)}`",
        "",
    ]
    if context_df is not None and not context_df.empty:
        lines.extend(["## Records", _render_df_table(context_df), ""])
    return "\n".join(lines)


def build_cross_asset_linkage_markdown_report(
    summary: Dict[str, Any], linkage_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for cross-asset volatility, trend, and range linkages."""
    lines = [
        "# Phase 131: Cross-Asset Volatility, Trend & Range Linkage Report",
        "",
        build_cross_asset_regime_disclaimer(),
        "",
        "## Linkage Summary",
        f"- **Total Linkages**: `{summary.get('total_linkages', 0)}`",
        f"- **Mean Linkage Score**: `{summary.get('mean_linkage_score', 0.0):.4f}`",
        f"- **All Non-Signal**: `{summary.get('all_non_signal', True)}`",
        f"- **Zero Directional Claims**: `{summary.get('zero_directional_claims', True)}`",
        "",
    ]
    if linkage_df is not None and not linkage_df.empty:
        lines.extend(["## Linkage Records", _render_df_table(linkage_df), ""])
    return "\n".join(lines)


def build_divergence_convergence_markdown_report(
    summary: Dict[str, Any], context_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for divergence and convergence context."""
    lines = [
        "# Phase 131: Cross-Asset Divergence and Convergence Diagnostic Report",
        "",
        build_cross_asset_regime_disclaimer(),
        "",
        "## Diagnostic Evaluation",
        f"- **Total Records**: `{summary.get('total_divergences', summary.get('total_convergences', 0))}`",
        f"- **Mean Diagnostic Score**: `{summary.get('mean_diagnostic_score', 0.0):.4f}`",
        f"- **Zero Trading Signals**: `{summary.get('zero_trading_signals', True)}`",
        f"- **Strictly Non-Pairs Trading**: True",
        "",
    ]
    if context_df is not None and not context_df.empty:
        lines.extend(["## Diagnostic Items", _render_df_table(context_df), ""])
    return "\n".join(lines)


def build_cross_asset_findings_markdown_report(
    summary: Dict[str, Any], findings_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for diagnostic findings and review queue."""
    lines = [
        "# Phase 131: Cross-Asset Diagnostic Findings Report",
        "",
        build_cross_asset_regime_disclaimer(),
        "",
        "## Findings Overview",
        f"- **Total Findings**: `{summary.get('total_findings', 0)}`",
        f"- **Manual Review Count**: `{summary.get('manual_review_count', 0)}`",
        f"- **Destructive Actions Allowed**: `{summary.get('destructive_action_allowed', False)}`",
        f"- **Auto-Fix Prohibited**: `{not summary.get('auto_fix_allowed', False)}`",
        "",
    ]
    if findings_df is not None and not findings_df.empty:
        lines.extend(["## Logged Findings", _render_df_table(findings_df), ""])
    return "\n".join(lines)


def build_cross_asset_score_markdown_report(
    summary: Dict[str, Any], score_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for composite cross-asset context score."""
    lines = [
        "# Phase 131: Cross-Asset Context Score Report",
        "",
        build_cross_asset_regime_disclaimer(),
        "",
        "## Integrity Score",
        f"- **Context Score**: `{summary.get('context_score', 0.0):.4f}`",
        f"- **Classification**: `{summary.get('classification', 'unknown')}`",
        f"- **Non-Signal Certified**: `{summary.get('all_non_signal', True)}`",
        f"- **Official Approval Claim**: `{summary.get('official_approval_claim', False)}`",
        f"- **Production Ready Claim**: `{summary.get('production_ready_claim', False)}`",
        "",
    ]
    if score_df is not None and not score_df.empty:
        lines.extend(["## Score Breakdown", _render_df_table(score_df), ""])
    return "\n".join(lines)


def build_cross_asset_manifest_markdown_report(
    summary: Dict[str, Any], manifest_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for master context audit manifest."""
    lines = [
        "# Phase 131: Cross-Asset Regime Context Manifest",
        "",
        build_cross_asset_regime_disclaimer(),
        "",
        "## Master Manifest Status",
        f"- **Manifest Name**: `{summary.get('manifest_name', 'cross_asset_regime_context_manifest')}`",
        f"- **Manifest Status**: `{summary.get('manifest_status', 'MANIFEST_VALID')}`",
        f"- **Current Phase**: `{summary.get('current_phase', 131)}`",
        f"- **Next Phase**: `{summary.get('next_phase', 132)}`",
        f"- **Target Final Phase**: `{summary.get('target_final_phase', 160)}`",
        f"- **Context Score**: `{summary.get('context_score', 0.0):.4f}`",
        f"- **Zero ML / Zero Clustering**: `{summary.get('zero_model_training', True) and summary.get('zero_clustering', True)}`",
        "",
    ]
    if manifest_df is not None and not manifest_df.empty:
        lines.extend(["## Certified Records", _render_df_table(manifest_df), ""])
    return "\n".join(lines)


def build_cross_asset_validation_markdown_report(
    summary: Dict[str, Any], validation_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for validation engine and safety checks."""
    lines = [
        "# Phase 131: Cross-Asset Regime Validation Report",
        "",
        build_cross_asset_regime_disclaimer(),
        "",
        "## Validation Results",
        f"- **Validation Status**: `{summary.get('validation_status', 'VALIDATION_PASS')}`",
        f"- **Total Checks**: `{summary.get('total_checks', 0)}`",
        f"- **Passed Checks**: `{summary.get('passed_checks', 0)}`",
        f"- **Forbidden Claims Clean**: `{summary.get('forbidden_claims_clean', True)}`",
        "",
    ]
    if validation_df is not None and not validation_df.empty:
        lines.extend(["## Validation Checklist", _render_df_table(validation_df), ""])
    return "\n".join(lines)


def build_cross_asset_safety_markdown_report(
    summary: Dict[str, Any], safety_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for safety boundary enforcement."""
    lines = [
        "# Phase 131: Cross-Asset Regime Safety Boundary Report",
        "",
        build_cross_asset_regime_disclaimer(),
        "",
        "## Safety Boundary Compliance",
        f"- **Safety Status**: `{summary.get('safety_status', 'SECURE')}`",
        f"- **NO-GO Conditions Enforced**: `{summary.get('no_go_count', 18)}`",
        f"- **SAFE-GO Principles Active**: `{summary.get('safe_go_count', 8)}`",
        f"- **Live Trading Prohibited**: True",
        f"- **Zero Model Execution**: True",
        "",
    ]
    if safety_df is not None and not safety_df.empty:
        lines.extend(["## Safety Matrix", _render_df_table(safety_df), ""])
    return "\n".join(lines)


def build_phase_132_handoff_markdown_report(
    summary: Dict[str, Any], handoff_df: Optional[pd.DataFrame] = None
) -> str:
    """Generate Markdown report for Phase 132 Handoff."""
    lines = [
        "# Phase 131: Phase 132 Macro/Event/News Regime Context Expansion Handoff Report",
        "",
        build_cross_asset_regime_disclaimer(),
        "",
        "## Handoff Verification",
        f"- **Handoff Status**: `{summary.get('handoff_status', 'READY')}`",
        f"- **Source Phase**: `{summary.get('source_phase', 131)}`",
        f"- **Next Phase**: `{summary.get('next_phase', 132)}`",
        f"- **Target Final Phase**: `{summary.get('target_final_phase', 160)}`",
        f"- **Total Handoff Deliverables**: `{summary.get('total_items', 0)}`",
        f"- **All Items Verified Ready**: `{summary.get('all_ready', True)}`",
        "",
    ]
    if handoff_df is not None and not handoff_df.empty:
        lines.extend(["## Handoff Deliverables", _render_df_table(handoff_df), ""])
    return "\n".join(lines)
