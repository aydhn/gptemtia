from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_quality.data_quality_config import DataQualityProfile
from advanced_data_quality.data_quality_models import QualityFinding, build_quality_finding_id


def build_duplicate_data_rule_set(profile: DataQualityProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rules = [
        {
            "rule_name": "check_duplicate_records",
            "rule_domain": "duplicate_data",
            "severity_label": "quality_medium",
            "description": "Verilen birincil anahtar sütunları üzerinde mükerrer satırların tespiti.",
        }
    ]
    df = pd.DataFrame.from_records(rules)
    return df, summarize_duplicate_data_rules(df)


def check_duplicate_records(
    df: pd.DataFrame,
    key_fields: List[str],
    dataset_type: str,
    provider_name: str = ""
) -> List[QualityFinding]:
    findings: List[QualityFinding] = []
    if df is None or len(df) == 0:
        return findings

    available_keys = [k for k in key_fields if k in df.columns]
    if not available_keys:
        return findings

    dup_mask = df.duplicated(subset=available_keys, keep=False)
    dup_count = int(dup_mask.sum())
    if dup_count > 0:
        key_str = "+".join(available_keys)
        findings.append(
            QualityFinding(
                finding_id=build_quality_finding_id("rule_duplicate_records", dataset_type, key_str),
                rule_id="rule_duplicate_data_duplicate_record_keys",
                finding_type="finding_duplicate_record",
                dataset_type=dataset_type,
                provider_name=provider_name or "unknown_provider",
                field_name=key_str,
                severity_label="quality_medium",
                status_label="quality_pass_with_warnings",
                message=f"Found {dup_count} duplicate rows on keys [{key_str}].",
                recommendation=f"Deduplicate non-destructively during Phase 113 Normalization.",
                future_phase_owner="Phase 113",
                manual_review_required=True,
            )
        )
    return findings


def summarize_duplicate_data_rules(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "rule_count": len(df),
        "rules": df["rule_name"].tolist() if "rule_name" in df.columns else [],
        "domain": "duplicate_data",
    }
