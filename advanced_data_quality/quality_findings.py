from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_quality.data_quality_config import DataQualityProfile
from advanced_data_quality.data_quality_models import (
    QualityFinding,
    build_quality_finding_id,
)


def create_quality_finding(
    rule_id: str,
    finding_type: str,
    dataset_type: str,
    provider_name: str,
    field_name: str = "",
    severity_label: str = "quality_medium",
    status_label: str = "quality_manual_review_required",
    message: str = "",
    recommendation: str = "",
    future_phase_owner: str = "Phase 113",
    manual_review_required: bool = True,
) -> QualityFinding:
    finding_id = build_quality_finding_id(rule_id, dataset_type, field_name)
    return QualityFinding(
        finding_id=finding_id,
        rule_id=rule_id,
        finding_type=finding_type,
        dataset_type=dataset_type,
        provider_name=provider_name or "unknown_provider",
        field_name=field_name,
        severity_label=severity_label,
        status_label=status_label,
        message=message,
        recommendation=recommendation,
        future_phase_owner=future_phase_owner,
        manual_review_required=manual_review_required,
    )


def quality_finding_to_dict(finding: QualityFinding) -> Dict[str, Any]:
    return finding.to_dict()


def build_quality_finding_registry(
    findings: List[QualityFinding],
    profile: DataQualityProfile
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    if not findings:
        df = pd.DataFrame(columns=[
            "finding_id", "rule_id", "finding_type", "dataset_type", "provider_name",
            "field_name", "severity_label", "status_label", "message",
            "recommendation", "future_phase_owner", "manual_review_required"
        ])
    else:
        records = [f.to_dict() for f in findings]
        df = pd.DataFrame.from_records(records)
    summary = summarize_quality_findings(df)
    return df, summary


def summarize_quality_findings(df: pd.DataFrame) -> Dict[str, Any]:
    if df is None or len(df) == 0:
        return {
            "total_findings": 0,
            "critical_count": 0,
            "high_count": 0,
            "medium_count": 0,
            "low_count": 0,
            "info_count": 0,
            "manual_review_required_count": 0,
            "current_phase": 112,
            "target_final_phase": 160,
        }

    sev_counts = df["severity_label"].value_counts().to_dict() if "severity_label" in df.columns else {}
    manual_rev = int(df["manual_review_required"].sum()) if "manual_review_required" in df.columns else 0

    return {
        "total_findings": len(df),
        "critical_count": sev_counts.get("quality_critical", 0),
        "high_count": sev_counts.get("quality_high", 0),
        "medium_count": sev_counts.get("quality_medium", 0),
        "low_count": sev_counts.get("quality_low", 0),
        "info_count": sev_counts.get("quality_info", 0),
        "manual_review_required_count": manual_rev,
        "dataset_types": sorted(list(df["dataset_type"].unique())) if "dataset_type" in df.columns else [],
        "providers": sorted(list(df["provider_name"].unique())) if "provider_name" in df.columns else [],
        "current_phase": 112,
        "target_final_phase": 160,
    }
