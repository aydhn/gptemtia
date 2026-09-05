"""Phase 128: Regime Rule-Free Report Builder.

Builds formatted Markdown reports for Phase 128 registries, contracts, schemas, and handoffs,
enforcing the standard non-signal disclaimer without external tabulate dependencies.
"""

from typing import Dict, Optional
import pandas as pd

PHASE_128_DISCLAIMER = (
    "> [!WARNING]\n"
    "> **YASAL UYARI VE NON-SIGNAL PREP BEYANI**\n"
    "> Bu çıktı Phase 128 Regime Rule-Free Labeling Contracts and Unsupervised Prep raporudur. "
    "Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, candidate state veya pseudo-state değerini "
    "trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, clustering execution, "
    "unsupervised execution, dimensionality reduction execution, prediction/target/label üretimi, "
    "production-ready/official approval/broker-ready iddiası, haber tam metni kullanımı, production deployment, "
    "model deployment, scraping veya gerçek provider API çağrısı değildir."
)


def build_regime_rule_free_disclaimer() -> str:
    """Return the canonical Phase 128 disclaimer."""
    return PHASE_128_DISCLAIMER


def _df_to_markdown_simple(df: pd.DataFrame) -> str:
    """Format DataFrame as a clean Markdown table without external dependencies."""
    if df is None or df.empty:
        return "_Tabloda veri bulunmuyor._\n"
    headers = [str(col) for col in df.columns]
    header_line = "| " + " | ".join(headers) + " |"
    separator_line = "| " + " | ".join(["---"] * len(headers)) + " |"
    rows = []
    for _, row in df.iterrows():
        row_str = "| " + " | ".join(str(val) for val in row.values) + " |"
        rows.append(row_str)
    return "\n".join([header_line, separator_line] + rows) + "\n"


def build_regime_rule_free_profile_markdown_report(summary: Dict, profile_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Phase 128: Regime Rule-Free Profile Registry Report",
        "",
        build_regime_rule_free_disclaimer(),
        "",
        "## Summary",
        f"- **Active Profile**: `{summary.get('active_profile')}`",
        f"- **Total Profiles**: `{summary.get('total_profiles')}`",
        f"- **Current Phase**: `{summary.get('current_phase')}`",
        f"- **Next Phase**: `{summary.get('next_phase')}`",
        f"- **Target Final Phase**: `{summary.get('target_final_phase')}`",
        f"- **Non-Signal Invariant**: `{summary.get('all_non_signal')}`",
        f"- **Clustering Execution Disallowed**: `{summary.get('all_clustering_disallowed')}`",
        f"- **Model Training Disallowed**: `{summary.get('all_model_training_disallowed')}`",
        "",
    ]
    if profile_df is not None and not profile_df.empty:
        lines.append("## Registered Profiles")
        lines.append(_df_to_markdown_simple(profile_df))
        lines.append("")
    return "\n".join(lines)


def build_rule_free_labeling_contract_markdown_report(summary: Dict, contract_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Phase 128: Rule-Free Labeling Contracts Report",
        "",
        build_regime_rule_free_disclaimer(),
        "",
        "## Contract Summary",
        f"- **Total Contracts**: `{summary.get('total_contracts')}`",
        f"- **Status**: `{summary.get('contracts_status')}`",
        f"- **All Non-Signal**: `{summary.get('all_non_signal')}`",
        f"- **Target/Label Forbidden**: `{summary.get('all_target_forbidden')}`",
        f"- **Prediction Forbidden**: `{summary.get('all_prediction_forbidden')}`",
        f"- **Clustering Forbidden**: `{summary.get('all_clustering_forbidden')}`",
        f"- **Model Training Forbidden**: `{summary.get('all_training_forbidden')}`",
        "",
    ]
    if contract_df is not None and not contract_df.empty:
        lines.append("## Contract Registry Details")
        lines.append(_df_to_markdown_simple(contract_df))
        lines.append("")
    return "\n".join(lines)


def build_candidate_state_schema_markdown_report(summary: Dict, schema_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Phase 128: Candidate State Schema Report",
        "",
        build_regime_rule_free_disclaimer(),
        "",
        "## Schema Summary",
        f"- **Total Fields**: `{summary.get('total_schema_fields')}`",
        f"- **Mandatory Fields**: `{summary.get('mandatory_fields_count')}`",
        f"- **All Non-Signal**: `{summary.get('all_non_signal')}`",
        f"- **All Not Target/Prediction**: `{summary.get('all_not_target_or_prediction')}`",
        f"- **Forbidden Terms Guarded**: `{summary.get('forbidden_terms_guarded')}`",
        "",
    ]
    if schema_df is not None and not schema_df.empty:
        lines.append("## Schema Definitions")
        lines.append(_df_to_markdown_simple(schema_df))
        lines.append("")
    return "\n".join(lines)


def build_unsupervised_prep_contract_markdown_report(summary: Dict, prep_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Phase 128: Unsupervised Preparation Contracts Report",
        "",
        build_regime_rule_free_disclaimer(),
        "",
        "## Prep Summary",
        f"- **Total Prep Contracts**: `{summary.get('total_prep_contracts')}`",
        f"- **All Non-Signal**: `{summary.get('all_non_signal')}`",
        f"- **No Model Training**: `{summary.get('all_no_training')}`",
        f"- **No Clustering**: `{summary.get('all_no_clustering')}`",
        f"- **Prep Status**: `{summary.get('prep_status')}`",
        "",
    ]
    if prep_df is not None and not prep_df.empty:
        lines.append("## Registered Prep Contracts")
        lines.append(_df_to_markdown_simple(prep_df))
        lines.append("")
    return "\n".join(lines)


def build_algorithm_placeholder_markdown_report(summary: Dict, algo_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Phase 128: Algorithm & Metric Placeholders Report",
        "",
        build_regime_rule_free_disclaimer(),
        "",
        "## Placeholder Summary",
        f"- **Total Placeholders**: `{summary.get('total_algorithm_placeholders', summary.get('total_distance_metrics', 0))}`",
        f"- **Placeholders Only**: `{summary.get('all_placeholders_only', True)}`",
        f"- **Execution Forbidden**: `{summary.get('all_execution_forbidden', True)}`",
        f"- **Non-Signal**: `{summary.get('all_non_signal', True)}`",
        "",
    ]
    if algo_df is not None and not algo_df.empty:
        lines.append("## Placeholder Details")
        lines.append(_df_to_markdown_simple(algo_df))
        lines.append("")
    return "\n".join(lines)


def build_candidate_state_metadata_markdown_report(summary: Dict, metadata_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Phase 128: Candidate State Metadata Report",
        "",
        build_regime_rule_free_disclaimer(),
        "",
        "## Metadata Summary",
        f"- **Total Records**: `{summary.get('total_candidate_metadata_records')}`",
        f"- **All Non-Signal**: `{summary.get('all_non_signal')}`",
        f"- **Phase 129 Ready**: `{summary.get('all_phase_129_ready')}`",
        "",
    ]
    if metadata_df is not None and not metadata_df.empty:
        lines.append("## Metadata Registry")
        lines.append(_df_to_markdown_simple(metadata_df))
        lines.append("")
    return "\n".join(lines)


def build_candidate_state_integrity_markdown_report(summary: Dict, manifest_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Phase 128: Candidate State Integrity Manifest Report",
        "",
        build_regime_rule_free_disclaimer(),
        "",
        "## Governance Manifest",
        f"- **Manifest Status**: `{summary.get('manifest_status')}`",
        f"- **Valid**: `{summary.get('is_valid')}`",
        f"- **Current Phase**: `{summary.get('current_phase')}`",
        f"- **Next Phase**: `{summary.get('next_phase')}`",
        f"- **Target Final Phase**: `{summary.get('target_final_phase')}`",
        f"- **Non-Signal Certified**: `{summary.get('non_signal')}`",
        f"- **Source Preserved**: `{summary.get('source_preserved')}`",
        f"- **Zero-Execution Guaranteed**: `{summary.get('zero_execution_guaranteed')}`",
        "",
    ]
    if manifest_df is not None and not manifest_df.empty:
        lines.append("## Manifest Attributes")
        lines.append(_df_to_markdown_simple(manifest_df))
        lines.append("")
    return "\n".join(lines)


def build_regime_rule_free_validation_markdown_report(summary: Dict, validation_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Phase 128: Regime Rule-Free Validation Report",
        "",
        build_regime_rule_free_disclaimer(),
        "",
        "## Validation Summary",
        f"- **Validation Status**: `{summary.get('validation_status', 'VALIDATION_PASS')}`",
        f"- **Total Checks**: `{summary.get('total_checks', 0)}`",
        f"- **Passed Checks**: `{summary.get('passed_checks', 0)}`",
        f"- **Forbidden Claims Clean**: `{summary.get('forbidden_claims_clean', True)}`",
        f"- **Zero Execution Clean**: `{summary.get('zero_execution_clean', True)}`",
        "",
    ]
    if validation_df is not None and not validation_df.empty:
        lines.append("## Validation Check Details")
        lines.append(_df_to_markdown_simple(validation_df))
        lines.append("")
    return "\n".join(lines)


def build_regime_rule_free_safety_markdown_report(summary: Dict, safety_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Phase 128: Regime Rule-Free Safety Boundary Report",
        "",
        build_regime_rule_free_disclaimer(),
        "",
        "## Safety Boundary Summary",
        f"- **Safety Status**: `{summary.get('safety_status', 'SECURE')}`",
        f"- **Total NO-GO Rules**: `{summary.get('no_go_count', 16)}`",
        f"- **Total SAFE-GO Principles**: `{summary.get('safe_go_count', 8)}`",
        f"- **Live Trading Prohibited**: `True`",
        f"- **Clustering Execution Prohibited**: `True`",
        "",
    ]
    if safety_df is not None and not safety_df.empty:
        lines.append("## Safety Boundary Rules")
        lines.append(_df_to_markdown_simple(safety_df))
        lines.append("")
    return "\n".join(lines)


def build_phase_129_handoff_markdown_report(summary: Dict, handoff_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Phase 128 to Phase 129 Handoff Report: Market Behavior Diagnostics and Regime Quality",
        "",
        build_regime_rule_free_disclaimer(),
        "",
        "## Handoff Overview",
        f"- **Source Phase**: `{summary.get('source_phase', 128)}`",
        f"- **Next Phase**: `{summary.get('next_phase', 129)}`",
        f"- **Target Final Phase**: `{summary.get('target_final_phase', 160)}`",
        f"- **Handoff Status**: `{summary.get('handoff_status', 'READY')}`",
        f"- **Total Deliverables**: `{summary.get('total_items', 0)}`",
        f"- **All Items Verified**: `{summary.get('all_verified', True)}`",
        "",
    ]
    if handoff_df is not None and not handoff_df.empty:
        lines.append("## Handoff Deliverables")
        lines.append(_df_to_markdown_simple(handoff_df))
        lines.append("")
    return "\n".join(lines)
