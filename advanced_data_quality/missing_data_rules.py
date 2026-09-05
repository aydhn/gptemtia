from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_quality.data_quality_config import DataQualityProfile
from advanced_data_quality.data_quality_models import QualityFinding, build_quality_finding_id


def build_missing_data_rule_set(profile: DataQualityProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rules = [
        {
            "rule_name": "check_missing_required_fields",
            "rule_domain": "missing_data",
            "severity_label": "quality_high",
            "description": "Kritik veri alanlarının şema içinde eksik olması durumu.",
        },
        {
            "rule_name": "check_missing_values",
            "rule_domain": "missing_data",
            "severity_label": "quality_medium",
            "description": "Mevcut alanlar içinde null/NaN değerlerin bulunması.",
        },
    ]
    df = pd.DataFrame.from_records(rules)
    return df, summarize_missing_data_rules(df)


def check_missing_required_fields(
    df: pd.DataFrame,
    required_fields: List[str],
    dataset_type: str,
    provider_name: str = ""
) -> List[QualityFinding]:
    findings: List[QualityFinding] = []
    if df is None:
        return findings
    for col in required_fields:
        if col not in df.columns:
            findings.append(
                QualityFinding(
                    finding_id=build_quality_finding_id("rule_missing_data_field", dataset_type, col),
                    rule_id="rule_missing_data_missing_field_presence",
                    finding_type="finding_missing_required_field",
                    dataset_type=dataset_type,
                    provider_name=provider_name or "unknown_provider",
                    field_name=col,
                    severity_label="quality_high",
                    status_label="quality_fail",
                    message=f"Required field '{col}' is completely missing.",
                    recommendation=f"Define field mapping in Phase 113 for field '{col}'.",
                    future_phase_owner="Phase 113",
                    manual_review_required=True,
                )
            )
    return findings


def check_missing_values(
    df: pd.DataFrame,
    fields: List[str],
    dataset_type: str,
    provider_name: str = ""
) -> List[QualityFinding]:
    findings: List[QualityFinding] = []
    if df is None or len(df) == 0:
        return findings
    for col in fields:
        if col in df.columns:
            null_count = int(df[col].isna().sum())
            if null_count > 0:
                findings.append(
                    QualityFinding(
                        finding_id=build_quality_finding_id("rule_missing_data_value", dataset_type, col),
                        rule_id="rule_missing_data_missing_values_threshold",
                        finding_type="finding_missing_value",
                        dataset_type=dataset_type,
                        provider_name=provider_name or "unknown_provider",
                        field_name=col,
                        severity_label="quality_medium",
                        status_label="quality_pass_with_warnings",
                        message=f"Field '{col}' contains {null_count} null/missing values.",
                        recommendation=f"Impute or handle nulls non-destructively in Phase 113.",
                        future_phase_owner="Phase 113",
                        manual_review_required=True,
                    )
                )
    return findings


def summarize_missing_data_rules(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "rule_count": len(df),
        "rules": df["rule_name"].tolist() if "rule_name" in df.columns else [],
        "domain": "missing_data",
    }
