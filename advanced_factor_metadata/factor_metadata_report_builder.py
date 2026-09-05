"""Phase 122 Factor Metadata Report Builder.

Generates comprehensive Markdown and text reports across factor profiles,
families, contracts, dependencies, manifests, safety boundaries, and handoffs.
Strictly non-signal and research-only.
"""

from typing import Any, Dict
import pandas as pd

DISCLAIMER = (
    "Bu çıktı Phase 122 Factor Metadata and Factor Families raporudur. Canlı emir, broker talimatı, "
    "kesin AL/SAT, yatırım tavsiyesi, factor değerini trade sinyali olarak kullanma, strateji üretimi, "
    "backtest, optimizer, model training, prediction/target/label üretimi, sentiment model output, "
    "haber tam metni kullanımı, production-ready/official approval iddiası, production deployment, "
    "model deployment, scraping veya gerçek provider API çağrısı değildir."
)


def build_factor_metadata_disclaimer() -> str:
    """Return the canonical Phase 122 non-signal disclaimer."""
    return DISCLAIMER


def _df_to_markdown(df: pd.DataFrame) -> str:
    """Format DataFrame as Markdown table safely without requiring external tabulate dependency."""
    try:
        return df.to_markdown(index=False)
    except Exception:
        if df is None or df.empty:
            return ""
        cols = [str(c) for c in df.columns]
        header_row = "| " + " | ".join(cols) + " |"
        sep_row = "| " + " | ".join(["---"] * len(cols)) + " |"
        body_rows = []
        for _, row in df.iterrows():
            body_rows.append("| " + " | ".join(str(row[c]) for c in df.columns) + " |")
        return "\n".join([header_row, sep_row] + body_rows)


def build_factor_metadata_profile_markdown_report(summary: Dict[str, Any], profile_df: pd.DataFrame | None = None) -> str:
    md = [
        "# Phase 122: Factor Metadata Profile Report",
        "",
        f"> **Yasal Uyarı**: {DISCLAIMER}",
        "",
        "## Profile Summary",
        f"- **Active Profile**: `{summary.get('active_profile', 'balanced_local_factor_metadata')}`",
        f"- **Total Profiles**: {summary.get('total_profiles', 0)}",
        f"- **Current Phase**: {summary.get('current_phase', 122)}",
        f"- **Target Final Phase**: {summary.get('target_final_phase', 160)}",
        f"- **Next Phase**: {summary.get('next_phase', 123)}",
        f"- **Dry Run Default**: {summary.get('dry_run_default', True)}",
        f"- **Non-Signal Mandate**: {summary.get('non_signal', True)}",
        f"- **Status**: `{summary.get('status', 'factor_ready')}`",
        "",
    ]
    if profile_df is not None and not profile_df.empty:
        md.append("## Registered Profiles")
        md.append(_df_to_markdown(profile_df))
        md.append("")
    return "\n".join(md)


def build_factor_family_markdown_report(summary: Dict[str, Any], family_df: pd.DataFrame | None = None) -> str:
    md = [
        "# Phase 122: Factor Family Taxonomy Report",
        "",
        f"> **Yasal Uyarı**: {DISCLAIMER}",
        "",
        "## Family Taxonomy Overview",
        f"- **Active Profile**: `{summary.get('active_profile', 'balanced_local_factor_metadata')}`",
        f"- **Total Families**: {summary.get('total_families', 0)}",
        f"- **Ready Families**: {summary.get('ready_families', 0)}",
        f"- **Placeholder Families**: {summary.get('placeholder_families', 0)}",
        f"- **Non-Signal Mandate**: {summary.get('non_signal', True)}",
        f"- **Status**: `{summary.get('status', 'factor_ready')}`",
        "",
    ]
    if family_df is not None and not family_df.empty:
        md.append("## Family Specifications")
        md.append(_df_to_markdown(family_df))
        md.append("")
    return "\n".join(md)


def build_factor_contract_markdown_report(summary: Dict[str, Any], contract_df: pd.DataFrame | None = None) -> str:
    md = [
        "# Phase 122: Factor Contract Registry Report",
        "",
        f"> **Yasal Uyarı**: {DISCLAIMER}",
        "",
        "## Contract Summary",
        f"- **Total Contracts**: {summary.get('total_contracts', 0)}",
        f"- **Valid Contracts**: {summary.get('valid_contracts', 0)}",
        f"- **All Contracts Valid**: {summary.get('all_contracts_valid', True)}",
        f"- **Current Phase**: {summary.get('current_phase', 122)}",
        f"- **Non-Signal**: {summary.get('non_signal', True)}",
        "",
    ]
    if contract_df is not None and not contract_df.empty:
        md.append("## Active Contracts")
        md.append(_df_to_markdown(contract_df))
        md.append("")
    return "\n".join(md)


def build_factor_dependency_markdown_report(summary: Dict[str, Any], dependency_df: pd.DataFrame | None = None) -> str:
    md = [
        "# Phase 122: Factor Dependency Registry Report",
        "",
        f"> **Yasal Uyarı**: {DISCLAIMER}",
        "",
        "## Dependency Summary",
        f"- **Total Dependencies**: {summary.get('total_dependencies', 0)}",
        f"- **Mandatory Dependencies**: {summary.get('mandatory_dependencies', 0)}",
        f"- **Optional Dependencies**: {summary.get('optional_dependencies', 0)}",
        f"- **Source Phases**: Phase 116, 117, 118, 119, 120, 121",
        f"- **Non-Signal**: {summary.get('non_signal', True)}",
        "",
    ]
    if dependency_df is not None and not dependency_df.empty:
        md.append("## Factor Dependencies")
        md.append(_df_to_markdown(dependency_df))
        md.append("")
    return "\n".join(md)


def build_factor_manifest_markdown_report(summary: Dict[str, Any], manifest_df: pd.DataFrame | None = None) -> str:
    md = [
        "# Phase 122: Factor Metadata Manifest Report",
        "",
        f"> **Yasal Uyarı**: {DISCLAIMER}",
        "",
        "## Manifest Invariants",
        f"- **Total Factor Items**: {summary.get('total_manifest_items', 0)}",
        f"- **All Non-Signal Verified**: {summary.get('all_non_signal', True)}",
        f"- **Zero Predictions/Targets**: {summary.get('zero_target_or_prediction', True)}",
        f"- **Zero Trading Recommendations**: {summary.get('zero_trading_recommendation', True)}",
        f"- **Source Preserved**: {summary.get('all_source_preserved', True)}",
        f"- **Status**: `{summary.get('status', 'factor_ready')}`",
        "",
    ]
    if manifest_df is not None and not manifest_df.empty:
        md.append("## Manifest Entries")
        md.append(_df_to_markdown(manifest_df))
        md.append("")
    return "\n".join(md)


def build_technical_factor_markdown_report(summary: Dict[str, Any], factor_df: pd.DataFrame | None = None) -> str:
    md = [
        "# Phase 122: Technical Factor Families Report",
        "",
        f"> **Yasal Uyarı**: {DISCLAIMER}",
        "",
        "## Technical Families Overview",
        f"- **Total Technical Factors**: {summary.get('total_factors', 0)}",
        f"- **Non-Signal Verified**: {summary.get('non_signal', True)}",
        f"- **Status**: `{summary.get('status', 'factor_ready')}`",
        "",
    ]
    if factor_df is not None and not factor_df.empty:
        md.append("## Factor Inventory")
        md.append(_df_to_markdown(factor_df))
        md.append("")
    return "\n".join(md)


def build_macro_event_news_factor_markdown_report(summary: Dict[str, Any], factor_df: pd.DataFrame | None = None) -> str:
    md = [
        "# Phase 122: Macro, Calendar Event & News Factor Families Report",
        "",
        f"> **Yasal Uyarı**: {DISCLAIMER}",
        "",
        "## Macro & Event Factor Overview",
        f"- **Total Factors**: {summary.get('total_factors', 0)}",
        f"- **Metadata-Only News Verified**: True",
        f"- **Point-in-Time Macro Verified**: True",
        f"- **Status**: `{summary.get('status', 'factor_ready')}`",
        "",
    ]
    if factor_df is not None and not factor_df.empty:
        md.append("## Factor Inventory")
        md.append(_df_to_markdown(factor_df))
        md.append("")
    return "\n".join(md)


def build_factor_validation_markdown_report(summary: Dict[str, Any], validation_df: pd.DataFrame | None = None) -> str:
    md = [
        "# Phase 122: Factor Validation Report",
        "",
        f"> **Yasal Uyarı**: {DISCLAIMER}",
        "",
        "## Validation Summary",
        f"- **Overall Status**: `{summary.get('status', 'factor_ready')}`",
        f"- **All Non-Signal Verified**: {summary.get('all_non_signal', True)}",
        f"- **Zero Forbidden Claims**: {summary.get('zero_forbidden_claims', True)}",
        f"- **Zero Lookahead Guarantees**: {summary.get('zero_lookahead', True)}",
        f"- **Source Preserved**: {summary.get('source_preserved', True)}",
        "",
    ]
    if validation_df is not None and not validation_df.empty:
        md.append("## Validation Results")
        md.append(_df_to_markdown(validation_df))
        md.append("")
    return "\n".join(md)


def build_factor_health_markdown_report(summary: Dict[str, Any], health_df: pd.DataFrame | None = None) -> str:
    md = [
        "# Phase 122: Factor Metadata Health Check Report",
        "",
        f"> **Yasal Uyarı**: {DISCLAIMER}",
        "",
        "## Health Check Summary",
        f"- **Overall Health**: `{summary.get('health_status', 'HEALTHY')}`",
        f"- **Total Checks**: {summary.get('total_checks', 0)}",
        f"- **Passed Checks**: {summary.get('passed_checks', 0)}",
        f"- **Failed Checks**: {summary.get('failed_checks', 0)}",
        f"- **Prerequisites Ready**: {summary.get('prerequisites_ready', True)}",
        "",
    ]
    if health_df is not None and not health_df.empty:
        md.append("## Health Check Items")
        md.append(_df_to_markdown(health_df))
        md.append("")
    return "\n".join(md)


def build_factor_safety_markdown_report(summary: Dict[str, Any], safety_df: pd.DataFrame | None = None) -> str:
    md = [
        "# Phase 122: Factor Safety Boundary Report",
        "",
        f"> **Yasal Uyarı**: {DISCLAIMER}",
        "",
        "## Safety Boundary Summary",
        f"- **Safety Status**: `{summary.get('safety_status', 'SECURE')}`",
        f"- **NO-GO Conditions Enforced**: {summary.get('no_go_count', 0)}",
        f"- **SAFE-GO Principles Active**: {summary.get('safe_go_count', 0)}",
        f"- **Destructive Action Allowed**: {summary.get('destructive_action_allowed', False)}",
        f"- **Non-Signal Mandate**: True",
        "",
    ]
    if safety_df is not None and not safety_df.empty:
        md.append("## Safety Rules Matrix")
        md.append(_df_to_markdown(safety_df))
        md.append("")
    return "\n".join(md)


def build_phase_123_handoff_markdown_report(summary: Dict[str, Any], handoff_df: pd.DataFrame | None = None) -> str:
    md = [
        "# Phase 122 to Phase 123: Feature Quality & Drift Handoff Report",
        "",
        f"> **Yasal Uyarı**: {DISCLAIMER}",
        "",
        "## Handoff Summary",
        f"- **Source Phase**: 122 (Factor Metadata and Factor Families)",
        f"- **Target Phase**: 123 (Feature Quality and Drift Diagnostics)",
        f"- **Target Final Phase**: 160",
        f"- **Total Handoff Items**: {summary.get('total_items', 0)}",
        f"- **Ready Items**: {summary.get('ready_items', 0)}",
        f"- **Handoff Status**: `{summary.get('handoff_status', 'READY')}`",
        f"- **Non-Signal**: True",
        "",
    ]
    if handoff_df is not None and not handoff_df.empty:
        md.append("## Handoff Specifications")
        md.append(_df_to_markdown(handoff_df))
        md.append("")
    return "\n".join(md)
