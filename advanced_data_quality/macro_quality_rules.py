from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_quality.data_quality_config import DataQualityProfile
from advanced_data_quality.data_quality_models import QualityFinding, build_quality_finding_id


def build_macro_quality_rule_set(profile: DataQualityProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rules = [
        {"rule_name": "macro_timeseries_integrity", "rule_domain": "macro_quality", "severity_label": "quality_high"},
        {"rule_name": "macro_release_metadata_integrity", "rule_domain": "macro_quality", "severity_label": "quality_medium"},
    ]
    df = pd.DataFrame.from_records(rules)
    return df, summarize_macro_quality_rules(df)


def check_macro_timeseries_quality(df: pd.DataFrame, provider_name: str = "") -> List[QualityFinding]:
    findings: List[QualityFinding] = []
    if df is None or len(df) == 0:
        return findings

    dataset_type = "dataset_macro_timeseries"
    required = ["indicator", "timestamp", "value", "unit", "region", "frequency"]
    for col in required:
        if col not in df.columns:
            findings.append(
                QualityFinding(
                    finding_id=build_quality_finding_id("rule_macro_ts_col", dataset_type, col),
                    rule_id="rule_macro_quality_macro_timeseries_sanity",
                    finding_type="finding_missing_required_field",
                    dataset_type=dataset_type,
                    provider_name=provider_name or "unknown_provider",
                    field_name=col,
                    severity_label="quality_high",
                    status_label="quality_fail",
                    message=f"Macro timeseries dataset is missing required field '{col}'.",
                    recommendation="Ensure indicator series schema is completed in Phase 113 Normalization.",
                    future_phase_owner="Phase 113",
                    manual_review_required=True,
                )
            )

    if "value" in df.columns:
        null_vals = df["value"].isna().sum()
        if null_vals > 0:
            findings.append(
                QualityFinding(
                    finding_id=build_quality_finding_id("rule_macro_val_null", dataset_type, "value"),
                    rule_id="rule_macro_quality_macro_timeseries_sanity",
                    finding_type="finding_missing_value",
                    dataset_type=dataset_type,
                    provider_name=provider_name or "unknown_provider",
                    field_name="value",
                    severity_label="quality_medium",
                    status_label="quality_pass_with_warnings",
                    message=f"Macro values contain {null_vals} missing observations.",
                    recommendation="Apply non-destructive forward-fill or missing imputation policy in Phase 113.",
                    future_phase_owner="Phase 113",
                    manual_review_required=True,
                )
            )
    return findings


def check_macro_release_metadata_quality(df: pd.DataFrame, provider_name: str = "") -> List[QualityFinding]:
    findings: List[QualityFinding] = []
    if df is None or len(df) == 0:
        return findings

    dataset_type = "dataset_macro_timeseries"
    if "revision_status" not in df.columns:
        findings.append(
            QualityFinding(
                finding_id=build_quality_finding_id("rule_macro_rev_status", dataset_type, "revision_status"),
                rule_id="rule_macro_quality_macro_release_metadata_sanity",
                finding_type="finding_provider_metadata_issue",
                dataset_type=dataset_type,
                provider_name=provider_name or "unknown_provider",
                field_name="revision_status",
                severity_label="quality_medium",
                status_label="quality_pass_with_warnings",
                message="Macro series lacks revision_status (preliminary, revised, final) metadata.",
                recommendation="Enforce revision policy attributes in Phase 113 Normalization.",
                future_phase_owner="Phase 113",
                manual_review_required=True,
            )
        )

    if "release_reference" not in df.columns:
        findings.append(
            QualityFinding(
                finding_id=build_quality_finding_id("rule_macro_rel_ref", dataset_type, "release_reference"),
                rule_id="rule_macro_quality_macro_release_metadata_sanity",
                finding_type="finding_provider_metadata_issue",
                dataset_type=dataset_type,
                provider_name=provider_name or "unknown_provider",
                field_name="release_reference",
                severity_label="quality_low",
                status_label="quality_pass_with_warnings",
                message="Macro series lacks explicit release_reference linkage.",
                recommendation="Link release events to calendar in Phase 113.",
                future_phase_owner="Phase 113",
                manual_review_required=False,
            )
        )

    return findings


def summarize_macro_quality_rules(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "rule_count": len(df),
        "rules": df["rule_name"].tolist() if "rule_name" in df.columns else [],
        "domain": "macro_quality",
    }
