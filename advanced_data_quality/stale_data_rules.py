from typing import Tuple, Dict, Any, List
from datetime import datetime, timezone
import pandas as pd
from advanced_data_quality.data_quality_config import DataQualityProfile
from advanced_data_quality.data_quality_models import QualityFinding, build_quality_finding_id


def build_stale_data_rule_set(profile: DataQualityProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rules = [
        {
            "rule_name": "check_stale_timestamp",
            "rule_domain": "stale_data",
            "severity_label": "quality_medium",
            "description": "Veri setindeki en güncel zaman damgasının izin verilen yaş sınırını aşması kontrolü.",
        }
    ]
    df = pd.DataFrame.from_records(rules)
    return df, summarize_stale_data_rules(df)


def check_stale_timestamp(
    df: pd.DataFrame,
    timestamp_field: str,
    max_age_days: int,
    dataset_type: str,
    provider_name: str = ""
) -> List[QualityFinding]:
    findings: List[QualityFinding] = []
    if df is None or len(df) == 0 or timestamp_field not in df.columns:
        return findings

    try:
        ts_series = pd.to_datetime(df[timestamp_field], errors="coerce")
        valid_ts = ts_series.dropna()
        if len(valid_ts) == 0:
            return findings

        max_ts = valid_ts.max()
        # handle tz-aware vs tz-naive
        now = datetime.now(timezone.utc)
        if max_ts.tzinfo is None:
            now_compare = datetime.utcnow()
        else:
            now_compare = now

        age_days = (now_compare - max_ts).total_seconds() / 86400.0
        if age_days > max_age_days:
            findings.append(
                QualityFinding(
                    finding_id=build_quality_finding_id("rule_stale_data", dataset_type, timestamp_field),
                    rule_id="rule_stale_data_stale_timestamp_check",
                    finding_type="finding_stale_data",
                    dataset_type=dataset_type,
                    provider_name=provider_name or "unknown_provider",
                    field_name=timestamp_field,
                    severity_label="quality_medium",
                    status_label="quality_pass_with_warnings",
                    message=f"Latest timestamp is {age_days:.1f} days old (threshold: {max_age_days} days).",
                    recommendation="Review source update frequency and schedule refresh in Phase 113/114.",
                    future_phase_owner="Phase 113",
                    manual_review_required=True,
                )
            )
    except Exception as exc:
        findings.append(
            QualityFinding(
                finding_id=build_quality_finding_id("rule_stale_data_parse_err", dataset_type, timestamp_field),
                rule_id="rule_stale_data_stale_timestamp_check",
                finding_type="finding_timestamp_issue",
                dataset_type=dataset_type,
                provider_name=provider_name or "unknown_provider",
                field_name=timestamp_field,
                severity_label="quality_medium",
                status_label="quality_pass_with_warnings",
                message=f"Could not compute staleness: {exc}",
                recommendation="Normalize timestamp format in Phase 113.",
                future_phase_owner="Phase 113",
                manual_review_required=True,
            )
        )
    return findings


def summarize_stale_data_rules(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "rule_count": len(df),
        "rules": df["rule_name"].tolist() if "rule_name" in df.columns else [],
        "domain": "stale_data",
    }
