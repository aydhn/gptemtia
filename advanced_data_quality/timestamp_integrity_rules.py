from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_quality.data_quality_config import DataQualityProfile
from advanced_data_quality.data_quality_models import QualityFinding, build_quality_finding_id


def build_timestamp_integrity_rule_set(profile: DataQualityProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rules = [
        {
            "rule_name": "timestamp_parseability",
            "rule_domain": "timestamp_integrity",
            "severity_label": "quality_high",
            "description": "Zaman damgası alanının tarih-saat nesnesine dönüştürülebilir olması.",
        },
        {
            "rule_name": "timestamp_ordering",
            "rule_domain": "timestamp_integrity",
            "severity_label": "quality_medium",
            "description": "Zaman damgalarının zaman serisi akışında monoton artan sırada olması.",
        },
    ]
    df = pd.DataFrame.from_records(rules)
    return df, summarize_timestamp_integrity_rules(df)


def check_timestamp_parseability(
    df: pd.DataFrame,
    timestamp_field: str,
    dataset_type: str,
    provider_name: str = ""
) -> List[QualityFinding]:
    findings: List[QualityFinding] = []
    if df is None or len(df) == 0:
        return findings

    if timestamp_field not in df.columns:
        findings.append(
            QualityFinding(
                finding_id=build_quality_finding_id("rule_ts_missing", dataset_type, timestamp_field),
                rule_id="rule_timestamp_integrity_timestamp_parseability",
                finding_type="finding_timestamp_issue",
                dataset_type=dataset_type,
                provider_name=provider_name or "unknown_provider",
                field_name=timestamp_field,
                severity_label="quality_high",
                status_label="quality_fail",
                message=f"Timestamp field '{timestamp_field}' is not present in DataFrame.",
                recommendation=f"Include '{timestamp_field}' in dataset schema during Phase 113.",
                future_phase_owner="Phase 113",
                manual_review_required=True,
            )
        )
        return findings

    parsed = pd.to_datetime(df[timestamp_field], errors="coerce")
    unparseable_count = int(parsed.isna().sum() - df[timestamp_field].isna().sum())
    if unparseable_count > 0:
        findings.append(
            QualityFinding(
                finding_id=build_quality_finding_id("rule_ts_unparseable", dataset_type, timestamp_field),
                rule_id="rule_timestamp_integrity_timestamp_parseability",
                finding_type="finding_timestamp_issue",
                dataset_type=dataset_type,
                provider_name=provider_name or "unknown_provider",
                field_name=timestamp_field,
                severity_label="quality_high",
                status_label="quality_fail",
                message=f"Timestamp field '{timestamp_field}' has {unparseable_count} invalid/unparseable values.",
                recommendation=f"Standardize date formats in Phase 113 Normalization Layer.",
                future_phase_owner="Phase 113",
                manual_review_required=True,
            )
        )
    return findings


def check_timestamp_ordering(
    df: pd.DataFrame,
    timestamp_field: str,
    key_fields: List[str],
    dataset_type: str,
    provider_name: str = ""
) -> List[QualityFinding]:
    findings: List[QualityFinding] = []
    if df is None or len(df) <= 1 or timestamp_field not in df.columns:
        return findings

    try:
        # Check ordering per series if key_fields provided, else globally
        group_cols = [k for k in key_fields if k in df.columns]
        if group_cols:
            grouped = df.groupby(group_cols)
            for name, group in grouped:
                ts = pd.to_datetime(group[timestamp_field], errors="coerce").dropna()
                if not ts.is_monotonic_increasing:
                    findings.append(
                        QualityFinding(
                            finding_id=build_quality_finding_id("rule_ts_not_monotonic", dataset_type, f"{name}_{timestamp_field}"),
                            rule_id="rule_timestamp_integrity_timestamp_ordering",
                            finding_type="finding_timestamp_issue",
                            dataset_type=dataset_type,
                            provider_name=provider_name or "unknown_provider",
                            field_name=timestamp_field,
                            severity_label="quality_medium",
                            status_label="quality_pass_with_warnings",
                            message=f"Series '{name}' timestamps are not strictly monotonically increasing.",
                            recommendation="Sort by timestamp canonically in Phase 113.",
                            future_phase_owner="Phase 113",
                            manual_review_required=True,
                        )
                    )
                    break
        else:
            ts = pd.to_datetime(df[timestamp_field], errors="coerce").dropna()
            if not ts.is_monotonic_increasing:
                findings.append(
                    QualityFinding(
                        finding_id=build_quality_finding_id("rule_ts_global_not_monotonic", dataset_type, timestamp_field),
                        rule_id="rule_timestamp_integrity_timestamp_ordering",
                        finding_type="finding_timestamp_issue",
                        dataset_type=dataset_type,
                        provider_name=provider_name or "unknown_provider",
                        field_name=timestamp_field,
                        severity_label="quality_medium",
                        status_label="quality_pass_with_warnings",
                        message=f"Global timestamps in '{timestamp_field}' are not monotonically sorted.",
                        recommendation="Sort by timestamp canonically in Phase 113.",
                        future_phase_owner="Phase 113",
                        manual_review_required=True,
                    )
                )
    except Exception:
        pass
    return findings


def summarize_timestamp_integrity_rules(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "rule_count": len(df),
        "rules": df["rule_name"].tolist() if "rule_name" in df.columns else [],
        "domain": "timestamp_integrity",
    }
