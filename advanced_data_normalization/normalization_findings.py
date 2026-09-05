from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_normalization.data_normalization_config import DataNormalizationProfile
from advanced_data_normalization.data_normalization_models import (
    NormalizationFinding,
    build_normalization_finding_id,
)


def create_normalization_finding(
    rule_id: str,
    dataset_type: str,
    source_field: str,
    original_value_repr: str = "",
    normalized_value_repr: str = "",
    status_label: str = "normalization_manual_review_required",
    severity_label: str = "normalization_medium",
    message: str = "",
    manual_review_required: bool = True,
) -> NormalizationFinding:
    return NormalizationFinding(
        finding_id=build_normalization_finding_id(rule_id, dataset_type, source_field),
        rule_id=rule_id,
        dataset_type=dataset_type,
        source_field=source_field,
        original_value_repr=original_value_repr,
        normalized_value_repr=normalized_value_repr,
        status_label=status_label,
        severity_label=severity_label,
        message=message,
        manual_review_required=manual_review_required,
    )


def normalization_finding_to_dict(finding: NormalizationFinding) -> Dict[str, Any]:
    return finding.to_dict()


def build_normalization_finding_registry(
    findings: List[NormalizationFinding],
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records = [f.to_dict() for f in findings]
    df = pd.DataFrame.from_records(records)
    summary = summarize_normalization_findings(df)
    return df, summary


def summarize_normalization_findings(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_findings": len(df),
        "manual_review_required_count": int(df["manual_review_required"].sum()) if "manual_review_required" in df.columns else 0,
        "applied_count": len(df[df["status_label"] == "normalization_applied"]) if "status_label" in df.columns else 0,
        "severities": df["severity_label"].value_counts().to_dict() if "severity_label" in df.columns else {},
        "current_phase": 113,
        "target_final_phase": 160,
    }
