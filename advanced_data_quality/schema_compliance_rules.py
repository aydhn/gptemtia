from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_quality.data_quality_config import DataQualityProfile
from advanced_data_quality.data_quality_models import QualityFinding, build_quality_finding_id


def build_schema_compliance_rule_set(profile: DataQualityProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rules = [
        {
            "rule_name": "mandatory_columns_presence",
            "rule_domain": "schema_compliance",
            "severity_label": "quality_critical",
            "description": "Veri setinde tanımlanmış zorunlu şema alanlarının tam bulunması.",
            "action_on_failure": "manual_review_queue",
        },
        {
            "rule_name": "dataframe_not_empty",
            "rule_domain": "schema_compliance",
            "severity_label": "quality_high",
            "description": "Veri setinin en az bir kayıt içermesi kontrolü.",
            "action_on_failure": "manual_review_queue",
        },
    ]
    df = pd.DataFrame.from_records(rules)
    return df, summarize_schema_compliance_rules(df)


def check_schema_compliance(
    df: pd.DataFrame,
    required_fields: List[str],
    dataset_type: str,
    provider_name: str = ""
) -> List[QualityFinding]:
    findings: List[QualityFinding] = []
    if df is None or len(df) == 0:
        findings.append(
            QualityFinding(
                finding_id=build_quality_finding_id("rule_schema_compliance_empty", dataset_type, "rows"),
                rule_id="rule_schema_compliance_dataframe_not_empty",
                finding_type="finding_schema_mismatch",
                dataset_type=dataset_type,
                provider_name=provider_name or "unknown_provider",
                field_name="rows",
                severity_label="quality_high",
                status_label="quality_fail",
                message="DataFrame is completely empty (0 rows).",
                recommendation="Provide non-empty fixture or verify ingestion in Phase 113.",
                future_phase_owner="Phase 113",
                manual_review_required=True,
            )
        )
        return findings

    missing_cols = [f for f in required_fields if f not in df.columns]
    for col in missing_cols:
        findings.append(
            QualityFinding(
                finding_id=build_quality_finding_id("rule_schema_compliance_mandatory_cols", dataset_type, col),
                rule_id="rule_schema_compliance_mandatory_columns_presence",
                finding_type="finding_missing_required_field",
                dataset_type=dataset_type,
                provider_name=provider_name or "unknown_provider",
                field_name=col,
                severity_label="quality_critical",
                status_label="quality_fail",
                message=f"Mandatory schema field '{col}' is missing from DataFrame.",
                recommendation=f"Map or normalize '{col}' field during Phase 113 Normalization.",
                future_phase_owner="Phase 113",
                manual_review_required=True,
            )
        )
    return findings


def summarize_schema_compliance_rules(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "rule_count": len(df),
        "rules": df["rule_name"].tolist() if "rule_name" in df.columns else [],
        "domain": "schema_compliance",
    }
