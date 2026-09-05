from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_quality.data_quality_config import DataQualityProfile
from advanced_data_quality.data_quality_models import QualityFinding, build_quality_finding_id


def build_frequency_unit_consistency_rule_set(profile: DataQualityProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rules = [
        {
            "rule_name": "check_frequency_values",
            "rule_domain": "frequency_unit",
            "severity_label": "quality_medium",
            "description": "Frekans değerlerinin önceden tanımlanmış sözlükle (daily, monthly vb.) uyumu.",
        },
        {
            "rule_name": "check_unit_values",
            "rule_domain": "frequency_unit",
            "severity_label": "quality_medium",
            "description": "Birim değerlerinin (index, percent, usd_per_barrel vb.) sözlükle uyumu.",
        },
    ]
    df = pd.DataFrame.from_records(rules)
    return df, summarize_frequency_unit_rules(df)


def check_frequency_values(
    df: pd.DataFrame,
    frequency_field: str,
    allowed_values: List[str],
    dataset_type: str,
    provider_name: str = ""
) -> List[QualityFinding]:
    findings: List[QualityFinding] = []
    if df is None or len(df) == 0 or frequency_field not in df.columns:
        return findings

    allowed_set = {str(v).strip().lower() for v in allowed_values}
    unique_vals = [str(x).strip().lower() for x in df[frequency_field].dropna().unique()]
    invalid_vals = [v for v in unique_vals if v not in allowed_set]

    if invalid_vals:
        findings.append(
            QualityFinding(
                finding_id=build_quality_finding_id("rule_invalid_frequency", dataset_type, frequency_field),
                rule_id="rule_frequency_unit_frequency_vocabulary_check",
                finding_type="finding_frequency_unit_mismatch",
                dataset_type=dataset_type,
                provider_name=provider_name or "unknown_provider",
                field_name=frequency_field,
                severity_label="quality_medium",
                status_label="quality_pass_with_warnings",
                message=f"Found invalid frequency values: {invalid_vals}. Allowed: {allowed_values}",
                recommendation="Normalize frequency strings in Phase 113 Normalization Layer.",
                future_phase_owner="Phase 113",
                manual_review_required=True,
            )
        )
    return findings


def check_unit_values(
    df: pd.DataFrame,
    unit_field: str,
    allowed_values: List[str],
    dataset_type: str,
    provider_name: str = ""
) -> List[QualityFinding]:
    findings: List[QualityFinding] = []
    if df is None or len(df) == 0 or unit_field not in df.columns:
        return findings

    allowed_set = {str(v).strip().lower() for v in allowed_values}
    unique_vals = [str(x).strip().lower() for x in df[unit_field].dropna().unique()]
    invalid_vals = [v for v in unique_vals if v not in allowed_set]

    if invalid_vals:
        findings.append(
            QualityFinding(
                finding_id=build_quality_finding_id("rule_invalid_unit", dataset_type, unit_field),
                rule_id="rule_frequency_unit_unit_vocabulary_check",
                finding_type="finding_frequency_unit_mismatch",
                dataset_type=dataset_type,
                provider_name=provider_name or "unknown_provider",
                field_name=unit_field,
                severity_label="quality_medium",
                status_label="quality_pass_with_warnings",
                message=f"Found invalid unit values: {invalid_vals}. Allowed: {allowed_values}",
                recommendation="Normalize units to canonical forms in Phase 113.",
                future_phase_owner="Phase 113",
                manual_review_required=True,
            )
        )
    return findings


def summarize_frequency_unit_rules(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "rule_count": len(df),
        "rules": df["rule_name"].tolist() if "rule_name" in df.columns else [],
        "domain": "frequency_unit",
    }
