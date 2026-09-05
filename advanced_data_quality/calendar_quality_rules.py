from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_quality.data_quality_config import DataQualityProfile
from advanced_data_quality.data_quality_models import QualityFinding, build_quality_finding_id


def build_calendar_quality_rule_set(profile: DataQualityProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rules = [
        {"rule_name": "calendar_event_schema", "rule_domain": "calendar_quality", "severity_label": "quality_high"},
        {"rule_name": "calendar_release_values", "rule_domain": "calendar_quality", "severity_label": "quality_medium"},
    ]
    df = pd.DataFrame.from_records(rules)
    return df, summarize_calendar_quality_rules(df)


def check_calendar_event_quality(df: pd.DataFrame, provider_name: str = "") -> List[QualityFinding]:
    findings: List[QualityFinding] = []
    if df is None or len(df) == 0:
        return findings

    dataset_type = "dataset_calendar_event"
    required = ["canonical_event", "scheduled_time", "region", "currency", "category", "importance"]
    for col in required:
        if col not in df.columns:
            findings.append(
                QualityFinding(
                    finding_id=build_quality_finding_id("rule_cal_col", dataset_type, col),
                    rule_id="rule_calendar_quality_calendar_event_sanity",
                    finding_type="finding_missing_required_field",
                    dataset_type=dataset_type,
                    provider_name=provider_name or "unknown_provider",
                    field_name=col,
                    severity_label="quality_high",
                    status_label="quality_fail",
                    message=f"Calendar event is missing required field '{col}'.",
                    recommendation="Populate canonical calendar event fields in Phase 113.",
                    future_phase_owner="Phase 113",
                    manual_review_required=True,
                )
            )

    if "scheduled_time" in df.columns:
        # Check timezone notice for Phase 113 handoff
        findings.append(
            QualityFinding(
                finding_id=build_quality_finding_id("rule_cal_tz_notice", dataset_type, "scheduled_time"),
                rule_id="rule_calendar_quality_calendar_event_sanity",
                finding_type="finding_timestamp_issue",
                dataset_type=dataset_type,
                provider_name=provider_name or "unknown_provider",
                field_name="scheduled_time",
                severity_label="quality_info",
                status_label="quality_pass",
                message="Scheduled times require canonical UTC alignment during Phase 113.",
                recommendation="Normalize timezone offsets to UTC in Phase 113.",
                future_phase_owner="Phase 113",
                manual_review_required=False,
            )
        )

    return findings


def check_release_event_quality(df: pd.DataFrame, provider_name: str = "") -> List[QualityFinding]:
    findings: List[QualityFinding] = []
    if df is None or len(df) == 0:
        return findings

    dataset_type = "dataset_release_event"
    required = ["actual", "forecast", "previous"]
    for col in required:
        if col not in df.columns:
            findings.append(
                QualityFinding(
                    finding_id=build_quality_finding_id("rule_rel_col", dataset_type, col),
                    rule_id="rule_calendar_quality_calendar_release_values_sanity",
                    finding_type="finding_missing_required_field",
                    dataset_type=dataset_type,
                    provider_name=provider_name or "unknown_provider",
                    field_name=col,
                    severity_label="quality_medium",
                    status_label="quality_pass_with_warnings",
                    message=f"Release event is missing field '{col}'.",
                    recommendation="Ensure actual/forecast/previous fields are structured in Phase 113.",
                    future_phase_owner="Phase 113",
                    manual_review_required=True,
                )
            )

    if "surprise_value" in df.columns:
        findings.append(
            QualityFinding(
                finding_id=build_quality_finding_id("rule_rel_surprise_notice", dataset_type, "surprise_value"),
                rule_id="rule_calendar_quality_calendar_release_values_sanity",
                finding_type="finding_manual_review_required",
                dataset_type=dataset_type,
                provider_name=provider_name or "unknown_provider",
                field_name="surprise_value",
                severity_label="quality_info",
                status_label="quality_pass",
                message="surprise_value is purely descriptive/research placeholder and NEVER a trading signal.",
                recommendation="Strictly preserve non-signal boundary.",
                future_phase_owner="Phase 113",
                manual_review_required=False,
            )
        )

    return findings


def summarize_calendar_quality_rules(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "rule_count": len(df),
        "rules": df["rule_name"].tolist() if "rule_name" in df.columns else [],
        "domain": "calendar_quality",
    }
