from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_data_lineage.data_lineage_config import DataLineageProfile
from advanced_data_lineage.data_lineage_models import (
    LineageFinding,
    build_lineage_finding_id,
)


def create_lineage_finding(
    finding_type: str,
    dataset_type: str,
    provider_name: str,
    source_id: str,
    severity_label: str = "lineage_manual_review_required",
    status_label: str = "lineage_manual_review_required",
    message: str = "",
    recommendation: str = "",
    manual_review_required: bool = True,
) -> LineageFinding:
    f_id = build_lineage_finding_id(finding_type, dataset_type, provider_name)
    return LineageFinding(
        finding_id=f_id,
        finding_type=finding_type,
        dataset_type=dataset_type,
        provider_name=provider_name,
        source_id=source_id,
        severity_label=severity_label,
        status_label=status_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=manual_review_required,
    )


def lineage_finding_to_dict(finding: LineageFinding) -> Dict[str, Any]:
    return finding.to_dict()


DEFAULT_FINDINGS = [
    ("missing_quote_diagnostic", "dataset_fx_quote", "advanced_fx_providers_engine", "prov_src_fx_fixture_provider_fx_dry_run_fixture_source", "lineage_manual_review_required", "lineage_partial", "Quote record missing ask price", "Keep record in place; do not perform destructive auto-deletion", True),
    ("unmapped_futures_code", "dataset_commodity_spot", "advanced_commodity_providers_engine", "prov_src_commodity_fixture_provider_commodity_dry_run_fixture_source", "lineage_manual_review_required", "lineage_partial", "Futures contract symbol not found in continuous root dictionary", "Add dictionary alias to commodity normalization registry", True),
    ("vendor_license_verification", "dataset_provider_metadata", "licensed_vendor_provider_placeholder", "prov_src_licensed_provider_placeholder_source", "lineage_manual_review_required", "lineage_partial", "Vendor contract terms require periodic validation", "Verify license compliance before benchmark handoff", True),
]


def build_lineage_finding_registry(
    profile: DataLineageProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    findings: List[LineageFinding] = []
    for f_type, ds_type, provider, s_id, sev, stat, msg, rec, rev in DEFAULT_FINDINGS:
        findings.append(
            create_lineage_finding(
                finding_type=f_type,
                dataset_type=ds_type,
                provider_name=provider,
                source_id=s_id,
                severity_label=sev,
                status_label=stat,
                message=msg,
                recommendation=rec,
                manual_review_required=rev,
            )
        )
    df = pd.DataFrame.from_records([f.to_dict() for f in findings])
    summary = summarize_lineage_findings(df)
    return df, summary


def summarize_lineage_findings(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_lineage_findings": len(df),
        "finding_types": df["finding_type"].tolist() if "finding_type" in df.columns else [],
        "manual_review_count": int(df["manual_review_required"].sum()) if "manual_review_required" in df.columns else 0,
        "current_phase": 114,
        "target_final_phase": 160,
    }
