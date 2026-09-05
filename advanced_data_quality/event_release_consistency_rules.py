from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_quality.data_quality_config import DataQualityProfile
from advanced_data_quality.data_quality_models import QualityFinding, build_quality_finding_id


def build_event_release_consistency_rule_contract(profile: DataQualityProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rules = [
        {"rule_name": "release_timing_consistency", "rule_domain": "event_release_consistency", "severity_label": "quality_medium"},
        {"rule_name": "revision_status_presence", "rule_domain": "event_release_consistency", "severity_label": "quality_medium"},
        {"rule_name": "surprise_calculation_notice", "rule_domain": "event_release_consistency", "severity_label": "quality_info"},
    ]
    df = pd.DataFrame.from_records(rules)
    return df, summarize_event_release_consistency_rules(df)


def check_event_release_consistency(df: pd.DataFrame, provider_name: str = "") -> List[QualityFinding]:
    findings: List[QualityFinding] = []
    if df is None or len(df) == 0:
        return findings

    dataset_type = "dataset_release_event"

    # 1. Scheduled vs actual release timing
    if "scheduled_time" in df.columns and "actual_release_time" in df.columns:
        valid_times = df.dropna(subset=["scheduled_time", "actual_release_time"])
        try:
            sched = pd.to_datetime(valid_times["scheduled_time"], errors="coerce")
            act = pd.to_datetime(valid_times["actual_release_time"], errors="coerce")
            early_releases = valid_times[act < sched]
            if len(early_releases) > 0:
                findings.append(
                    QualityFinding(
                        finding_id=build_quality_finding_id("rule_event_early_release", dataset_type, "actual_release_time"),
                        rule_id="rule_event_release_consistency_event_release_timing",
                        finding_type="finding_event_release_inconsistency",
                        dataset_type=dataset_type,
                        provider_name=provider_name or "unknown_provider",
                        field_name="actual_release_time",
                        severity_label="quality_medium",
                        status_label="quality_pass_with_warnings",
                        message=f"Found {len(early_releases)} events released earlier than scheduled_time.",
                        recommendation="Review early release timestamps; defer embargo policies to Phase 113.",
                        future_phase_owner="Phase 113",
                        manual_review_required=True,
                    )
                )
        except Exception:
            pass

    # 2. Revised previous requires revision_status
    if "revised_previous" in df.columns and "revision_status" not in df.columns:
        findings.append(
            QualityFinding(
                finding_id=build_quality_finding_id("rule_event_rev_missing_status", dataset_type, "revised_previous"),
                rule_id="rule_event_release_consistency_event_release_timing",
                finding_type="finding_event_release_inconsistency",
                dataset_type=dataset_type,
                provider_name=provider_name or "unknown_provider",
                field_name="revised_previous",
                severity_label="quality_medium",
                status_label="quality_pass_with_warnings",
                message="Dataset has revised_previous values but lacks revision_status column.",
                recommendation="Enrich revision tracking flags in Phase 113.",
                future_phase_owner="Phase 113",
                manual_review_required=True,
            )
        )

    # 3. Surprise calculation notice
    if "surprise_value" in df.columns:
        findings.append(
            QualityFinding(
                finding_id=build_quality_finding_id("rule_event_surprise_contract", dataset_type, "surprise_value"),
                rule_id="rule_event_release_consistency_event_release_timing",
                finding_type="finding_manual_review_required",
                dataset_type=dataset_type,
                provider_name=provider_name or "unknown_provider",
                field_name="surprise_value",
                severity_label="quality_info",
                status_label="quality_pass",
                message="Surprise formula is placeholder (actual - forecast). Not a trading signal.",
                recommendation="Maintain non-signal documentation throughout pipeline.",
                future_phase_owner="Phase 113",
                manual_review_required=False,
            )
        )

    return findings


def summarize_event_release_consistency_rules(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "rule_count": len(df),
        "rules": df["rule_name"].tolist() if "rule_name" in df.columns else [],
        "domain": "event_release_consistency",
    }
