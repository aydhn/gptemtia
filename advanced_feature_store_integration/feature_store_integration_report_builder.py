"""Phase 124 Feature Store Integration Report Builder."""

from typing import Any, Dict, Optional
import pandas as pd

FEATURE_STORE_INTEGRATION_DISCLAIMER = (
    "Bu cikti Phase 124 Feature Store Integration Expansion raporudur. Canli emir, broker talimati, "
    "kesin AL/SAT, yatirim tavsiyesi, feature store kaydini trade sinyali olarak kullanma, strateji uretimi, "
    "backtest, optimizer, model training, prediction/target/label uretimi, production-ready/official approval/broker-ready "
    "iddiasi, otomatik feature silme/duzeltme, haber tam metni kullanimi, production deployment, model deployment, "
    "scraping veya gercek provider API cagrisi degildir."
)


def _df_to_markdown(df: pd.DataFrame) -> str:
    """Format DataFrame as markdown table without requiring optional tabulate."""
    if df is None or df.empty:
        return "_Empty table_"
    try:
        return df.to_markdown(index=False)
    except Exception:
        cols = [str(c) for c in df.columns]
        header = "| " + " | ".join(cols) + " |"
        sep = "| " + " | ".join(["---"] * len(cols)) + " |"
        rows = []
        for _, row in df.iterrows():
            rows.append("| " + " | ".join(str(row[c]) for c in df.columns) + " |")
        return "\n".join([header, sep] + rows)


def build_feature_store_integration_disclaimer() -> str:
    """Return standard disclaimer string."""
    return FEATURE_STORE_INTEGRATION_DISCLAIMER


def build_feature_store_integration_profile_markdown_report(summary: Dict[str, Any], profile_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Phase 124 Feature Store Integration Profile Report",
        "",
        f"> {FEATURE_STORE_INTEGRATION_DISCLAIMER}",
        "",
        "## Profile Summary",
        f"- Active Profile: `{summary.get('active_profile', 'unknown')}`",
        f"- Total Profiles: `{summary.get('total_profiles', 0)}`",
        f"- Current Phase: `{summary.get('current_phase', 124)}`",
        f"- Next Phase: `{summary.get('next_phase', 125)}`",
        f"- Target Final Phase: `{summary.get('target_final_phase', 160)}`",
        f"- Non-Signal Invariant: `{summary.get('non_signal', True)}`",
        f"- Source Preserved: `{summary.get('source_preserved', True)}`",
        "",
    ]
    if profile_df is not None and not profile_df.empty:
        lines.append("## Registered Profiles Table")
        lines.append(_df_to_markdown(profile_df))
        lines.append("")
    return "\n".join(lines)


def build_feature_store_contract_markdown_report(summary: Dict[str, Any], contract_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Phase 124 Feature Store Contracts Report",
        "",
        f"> {FEATURE_STORE_INTEGRATION_DISCLAIMER}",
        "",
        "## Contract Summary",
        f"- Total Contracts: `{summary.get('total_contracts', 0)}`",
        f"- All Non-Signal: `{summary.get('all_non_signal', True)}`",
        f"- All Source Preserved: `{summary.get('all_source_preserved', True)}`",
        f"- Validation Required: `{summary.get('all_validation_required', True)}`",
        "",
    ]
    if contract_df is not None and not contract_df.empty:
        lines.append("## Contracts Table")
        lines.append(_df_to_markdown(contract_df))
        lines.append("")
    return "\n".join(lines)


def build_feature_store_catalog_markdown_report(summary: Dict[str, Any], catalog_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Phase 124 Feature Store Catalogs Report",
        "",
        f"> {FEATURE_STORE_INTEGRATION_DISCLAIMER}",
        "",
        "## Catalog Summary",
        f"- Catalog Type: `{summary.get('catalog_type', 'catalog')}`",
        f"- Total Items: `{summary.get('total_items', summary.get('total_features', summary.get('total_factors', 0)))}`",
        f"- Non-Signal: `{summary.get('non_signal', True)}`",
        "",
    ]
    if catalog_df is not None and not catalog_df.empty:
        lines.append("## Catalog Table")
        lines.append(_df_to_markdown(catalog_df))
        lines.append("")
    return "\n".join(lines)


def build_feature_store_manifest_markdown_report(summary: Dict[str, Any], manifest_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Phase 124 Feature Store Metadata Manifest Report",
        "",
        f"> {FEATURE_STORE_INTEGRATION_DISCLAIMER}",
        "",
        "## Manifest Summary",
        f"- Store Name: `{summary.get('store_name', 'central_feature_store_v124')}`",
        f"- Total Features: `{summary.get('total_features', 0)}`",
        f"- Total Factors: `{summary.get('total_factors', 0)}`",
        f"- Total Entities: `{summary.get('total_entities', 0)}`",
        f"- Official Approval: `{summary.get('official_approval', False)}`",
        f"- Production Ready: `{summary.get('production_ready', False)}`",
        f"- Broker Ready: `{summary.get('broker_ready', False)}`",
        f"- Non-Signal: `{summary.get('non_signal', True)}`",
        "",
    ]
    if manifest_df is not None and not manifest_df.empty:
        lines.append("## Manifest Table")
        lines.append(_df_to_markdown(manifest_df))
        lines.append("")
    return "\n".join(lines)


def build_feature_store_policy_markdown_report(summary: Dict[str, Any], policy_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Phase 124 Feature Store Policies Report",
        "",
        f"> {FEATURE_STORE_INTEGRATION_DISCLAIMER}",
        "",
        "## Policy Summary",
        f"- Total Policies: `{summary.get('total_policies', 0)}`",
        f"- Non-Signal Enforced: `{summary.get('non_signal', True)}`",
        f"- Source Preservation Enforced: `{summary.get('source_preserved', True)}`",
        "",
    ]
    if policy_df is not None and not policy_df.empty:
        lines.append("## Policy Table")
        lines.append(_df_to_markdown(policy_df))
        lines.append("")
    return "\n".join(lines)


def build_feature_store_health_markdown_report(summary: Dict[str, Any], health_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Phase 124 Feature Store Integration Health Check Report",
        "",
        f"> {FEATURE_STORE_INTEGRATION_DISCLAIMER}",
        "",
        "## Health Summary",
        f"- Health Status: `{summary.get('status', 'HEALTHY')}`",
        f"- Total Checks: `{summary.get('total_checks', 0)}`",
        f"- Passed Checks: `{summary.get('passed_checks', 0)}`",
        f"- Failed Checks: `{summary.get('failed_checks', 0)}`",
        "",
    ]
    if health_df is not None and not health_df.empty:
        lines.append("## Health Checks Table")
        lines.append(_df_to_markdown(health_df))
        lines.append("")
    return "\n".join(lines)


def build_feature_store_validation_markdown_report(summary: Dict[str, Any], validation_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Phase 124 Feature Store Integration Validation Report",
        "",
        f"> {FEATURE_STORE_INTEGRATION_DISCLAIMER}",
        "",
        "## Validation Summary",
        f"- Validation Status: `{summary.get('status', 'VALIDATION_PASS')}`",
        f"- Total Rules Verified: `{summary.get('total_rules', 0)}`",
        f"- Forbidden Claims Detected: `{summary.get('forbidden_claims_detected', 0)}`",
        f"- Lookahead Violations: `{summary.get('lookahead_violations', 0)}`",
        f"- Destructive Cleaning Permitted: `{summary.get('destructive_cleaning_permitted', False)}`",
        "",
    ]
    if validation_df is not None and not validation_df.empty:
        lines.append("## Validation Table")
        lines.append(_df_to_markdown(validation_df))
        lines.append("")
    return "\n".join(lines)


def build_feature_store_safety_markdown_report(summary: Dict[str, Any], safety_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Phase 124 Feature Store Integration Safety Boundary Report",
        "",
        f"> {FEATURE_STORE_INTEGRATION_DISCLAIMER}",
        "",
        "## Safety Boundary Summary",
        f"- Safety Status: `{summary.get('safety_status', 'SECURE')}`",
        f"- Total NO-GO Conditions: `{summary.get('no_go_count', 0)}`",
        f"- Total SAFE-GO Conditions: `{summary.get('safe_go_count', 0)}`",
        f"- Non-Signal Guaranteed: `{summary.get('non_signal', True)}`",
        f"- Source Preservation Guaranteed: `{summary.get('source_preserved', True)}`",
        "",
    ]
    if safety_df is not None and not safety_df.empty:
        lines.append("## Safety Boundary Table")
        lines.append(_df_to_markdown(safety_df))
        lines.append("")
    return "\n".join(lines)


def build_phase_125_handoff_markdown_report(summary: Dict[str, Any], handoff_df: Optional[pd.DataFrame] = None) -> str:
    lines = [
        "# Phase 125 Feature/Factor Engine Acceptance Handoff Report",
        "",
        f"> {FEATURE_STORE_INTEGRATION_DISCLAIMER}",
        "",
        "## Handoff Summary",
        f"- Handoff Status: `{summary.get('handoff_status', 'READY')}`",
        f"- Source Phase: `{summary.get('source_phase', 124)}`",
        f"- Next Phase: `{summary.get('next_phase', 125)}`",
        f"- Target Final Phase: `{summary.get('target_final_phase', 160)}`",
        f"- Total Handoff Items: `{summary.get('total_items', 0)}`",
        f"- Ready Items: `{summary.get('ready_items', 0)}`",
        "",
    ]
    if handoff_df is not None and not handoff_df.empty:
        lines.append("## Handoff Items Table")
        lines.append(_df_to_markdown(handoff_df))
        lines.append("")
    return "\n".join(lines)
