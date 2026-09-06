"""Phase 134: Regime FeatureStore Report Builder.

Builds formatted Markdown reports and tables with mandatory non-signal disclaimers.
Zero external dependency table formatting (no tabulate requirement).
"""

from typing import Any, Dict, Optional
import pandas as pd

DISCLAIMER_TEXT = (
    "> [!NOTE]\n"
    "> **Yasal ve Operasyonel Sınır**: Bu çıktı Phase 134 Regime FeatureStore Integration raporudur. "
    "Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, FeatureStore’daki rejim kaydını "
    "trade sinyali olarak kullanma, validation/store readiness değerini production-ready/official approval/broker-ready "
    "olarak sunma, strateji üretimi, backtest, optimizer, model training, clustering execution, "
    "prediction/target/label üretimi, sentiment model output, haber tam metni/article body/raw content/"
    "scraped HTML/embedding/vector kullanımı, production deployment, model deployment, scraping veya "
    "gerçek provider API çağrısı değildir."
)


def build_regime_featurestore_disclaimer() -> str:
    """Return canonical disclaimer block."""
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
    return "\n".join([header_line, separator_line] + rows)


def build_regime_featurestore_profile_markdown_report(
    summary: Dict[str, Any],
    profile_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for profile registry."""
    table_md = _render_df_table(profile_df)
    return (
        f"# Phase 134: Regime FeatureStore Profile Registry Report\n\n"
        f"{DISCLAIMER_TEXT}\n\n"
        f"- **Active Profile**: `{summary.get('active_profile')}`\n"
        f"- **Total Profiles**: `{summary.get('total_profiles', 0)}`\n"
        f"- **Current Phase**: `{summary.get('current_phase', 134)}`\n"
        f"- **Target Final Phase**: `{summary.get('target_final_phase', 160)}`\n"
        f"- **Status**: `{summary.get('status', 'regime_store_ready')}`\n\n"
        f"## Registered Profiles\n\n"
        f"{table_md}\n"
    )


def build_regime_featurestore_contract_markdown_report(
    summary: Dict[str, Any],
    contract_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for FeatureStore contract registry."""
    table_md = _render_df_table(contract_df)
    return (
        f"# Phase 134: Regime FeatureStore Contract Registry Report\n\n"
        f"{DISCLAIMER_TEXT}\n\n"
        f"- **Total Contracts**: `{summary.get('total_contracts', 0)}`\n"
        f"- **All Non-Signal Required**: `{summary.get('all_non_signal_required', True)}`\n"
        f"- **All Source Preservation Required**: `{summary.get('all_source_preservation_required', True)}`\n"
        f"- **Production Ready**: `{summary.get('production_ready', False)}`\n\n"
        f"## Canonical Contracts\n\n"
        f"{table_md}\n"
    )


def build_regime_featurestore_schema_markdown_report(
    summary: Dict[str, Any],
    schema_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for FeatureStore schema specifications."""
    table_md = _render_df_table(schema_df)
    return (
        f"# Phase 134: Regime FeatureStore Schema Registry Report\n\n"
        f"{DISCLAIMER_TEXT}\n\n"
        f"- **Total Schema Fields**: `{summary.get('total_fields', 0)}`\n"
        f"- **Forbidden Columns Monitored**: `{summary.get('forbidden_columns_count', 0)}`\n"
        f"- **Non-Signal Certified**: `{summary.get('non_signal', True)}`\n\n"
        f"## Minimum Schema Specification\n\n"
        f"{table_md}\n"
    )


def build_regime_component_store_catalog_markdown_report(
    summary: Dict[str, Any],
    catalog_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for component store catalogs."""
    table_md = _render_df_table(catalog_df)
    return (
        f"# Phase 134: Component Store Catalog Report\n\n"
        f"{DISCLAIMER_TEXT}\n\n"
        f"- **Catalog Domain**: `{summary.get('domain', 'unknown')}`\n"
        f"- **Total Items**: `{summary.get('total_items', 0)}`\n"
        f"- **All Non-Signal**: `{summary.get('all_non_signal', True)}`\n"
        f"- **Source Preserved**: `{summary.get('all_source_preserved', True)}`\n\n"
        f"## Catalog Items\n\n"
        f"{table_md}\n"
    )


def build_regime_accepted_reference_markdown_report(
    summary: Dict[str, Any],
    reference_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for accepted reference registries."""
    table_md = _render_df_table(reference_df)
    return (
        f"# Phase 134: Regime Accepted Reference Registry Report\n\n"
        f"{DISCLAIMER_TEXT}\n\n"
        f"- **Reference Type**: `{summary.get('reference_type', 'all')}`\n"
        f"- **Total References**: `{summary.get('total_references', 0)}`\n"
        f"- **Status**: `{summary.get('status', 'regime_store_ready')}`\n\n"
        f"## Reference Entries\n\n"
        f"{table_md}\n"
    )


def build_regime_dependency_store_markdown_report(
    summary: Dict[str, Any],
    dependency_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for dependency stores."""
    table_md = _render_df_table(dependency_df)
    return (
        f"# Phase 134: Regime Dependency Store Report\n\n"
        f"{DISCLAIMER_TEXT}\n\n"
        f"- **Domain**: `{summary.get('domain', 'unknown')}`\n"
        f"- **Total Dependencies**: `{summary.get('total_dependencies', 0)}`\n"
        f"- **All Satisfied**: `{summary.get('all_satisfied', True)}`\n\n"
        f"## Dependency Entries\n\n"
        f"{table_md}\n"
    )


def build_regime_featurestore_policy_markdown_report(
    summary: Dict[str, Any],
    policy_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for FeatureStore governance policies."""
    table_md = _render_df_table(policy_df)
    return (
        f"# Phase 134: Regime FeatureStore Policy Report\n\n"
        f"{DISCLAIMER_TEXT}\n\n"
        f"- **Policy Domain**: `{summary.get('domain', 'unknown')}`\n"
        f"- **Status**: `{summary.get('status', 'regime_store_ready')}`\n\n"
        f"## Policy Rules\n\n"
        f"{table_md}\n"
    )


def build_regime_featurestore_manifest_markdown_report(
    summary: Dict[str, Any],
    manifest_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for the master FeatureStore metadata manifest."""
    table_md = _render_df_table(manifest_df)
    return (
        f"# Phase 134: Regime FeatureStore Metadata Manifest Report\n\n"
        f"{DISCLAIMER_TEXT}\n\n"
        f"- **Manifest Name**: `{summary.get('manifest_name')}`\n"
        f"- **Readiness Score**: `{summary.get('readiness_score', 1.0)}`\n"
        f"- **Current Phase**: `{summary.get('current_phase', 134)}`\n"
        f"- **Next Phase**: `{summary.get('next_phase', 135)}`\n"
        f"- **Manifest Valid**: `{summary.get('manifest_valid', True)}`\n\n"
        f"## Manifest Attributes\n\n"
        f"{table_md}\n"
    )


def build_regime_featurestore_validation_markdown_report(
    summary: Dict[str, Any],
    validation_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for FeatureStore validation checks."""
    table_md = _render_df_table(validation_df)
    return (
        f"# Phase 134: Regime FeatureStore Validation Report\n\n"
        f"{DISCLAIMER_TEXT}\n\n"
        f"- **Validation Status**: `{summary.get('status', 'VALIDATION_PASS')}`\n"
        f"- **Total Checks**: `{summary.get('total_checks', 0)}`\n"
        f"- **Failed Checks**: `{summary.get('failed_checks', 0)}`\n"
        f"- **Non-Signal Invariant Maintained**: `{summary.get('non_signal', True)}`\n\n"
        f"## Validation Items\n\n"
        f"{table_md}\n"
    )


def build_regime_featurestore_safety_markdown_report(
    summary: Dict[str, Any],
    safety_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for safety boundaries."""
    table_md = _render_df_table(safety_df)
    return (
        f"# Phase 134: Regime FeatureStore Safety Boundary Report\n\n"
        f"{DISCLAIMER_TEXT}\n\n"
        f"- **Safety Status**: `{summary.get('safety_status', 'SECURE')}`\n"
        f"- **NO-GO Conditions**: `{summary.get('no_go_count', 0)}`\n"
        f"- **SAFE-GO Conditions**: `{summary.get('safe_go_count', 0)}`\n\n"
        f"## Boundary Rules\n\n"
        f"{table_md}\n"
    )


def build_phase_135_handoff_markdown_report(
    summary: Dict[str, Any],
    handoff_df: Optional[pd.DataFrame] = None,
) -> str:
    """Generate Markdown report for Phase 135 handoff prerequisites."""
    table_md = _render_df_table(handoff_df)
    return (
        f"# Phase 134 to Phase 135 Handoff Report\n\n"
        f"{DISCLAIMER_TEXT}\n\n"
        f"- **Handoff Target**: `Phase 135: Regime Classification Acceptance Report`\n"
        f"- **Handoff Status**: `{summary.get('handoff_status', 'READY')}`\n"
        f"- **Prerequisites Count**: `{summary.get('total_prerequisites', 0)}`\n"
        f"- **All Prerequisites Satisfied**: `{summary.get('all_satisfied', True)}`\n\n"
        f"## Handoff Prerequisites\n\n"
        f"{table_md}\n"
    )
