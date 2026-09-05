"""Feature Validation Findings Registry.

Manages validation findings, severity classifications, and non-destructive issue reporting.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_feature_validation.feature_validation_config import (
    FeatureValidationProfile,
    get_default_feature_validation_profile,
)
from advanced_feature_validation.feature_validation_models import (
    FeatureValidationFinding,
    build_feature_validation_finding_id,
)


def create_feature_validation_finding(
    rule_id: str,
    finding_type: str,
    feature_or_matrix_name: str,
    severity_label: str = "validation_medium",
    status_label: str = "validation_manual_review_required",
    message: str = "",
    recommendation: str = "",
    manual_review_required: bool = True,
) -> FeatureValidationFinding:
    """Instantiate a structured, non-destructive validation finding."""
    finding_id = build_feature_validation_finding_id(rule_id, feature_or_matrix_name)
    return FeatureValidationFinding(
        finding_id=finding_id,
        rule_id=rule_id,
        finding_type=finding_type,
        feature_or_matrix_name=feature_or_matrix_name,
        severity_label=severity_label,
        status_label=status_label,
        message=message,
        recommendation=recommendation,
        destructive_action_allowed=False,
        manual_review_required=manual_review_required,
    )


def feature_validation_finding_to_dict(finding: FeatureValidationFinding) -> Dict[str, Any]:
    """Serialize finding object to dictionary."""
    return finding.to_dict()


def build_feature_validation_finding_registry(
    profile: FeatureValidationProfile | None = None,
    custom_findings: List[FeatureValidationFinding] | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary of validation findings."""
    active_profile = profile or get_default_feature_validation_profile()

    findings_list = custom_findings or [
        create_feature_validation_finding(
            rule_id="val_rule_matrix_warmup",
            finding_type="warmup_nan_notice",
            feature_or_matrix_name="sma_w200",
            severity_label="validation_info",
            status_label="validation_pass_with_warnings",
            message="Feature 'sma_w200' has expected warmup NaNs in initial 199 bars.",
            recommendation="Preserve warmup NaNs transparently; do not drop or forward fill.",
            manual_review_required=False,
        )
    ]

    records = [f.to_dict() for f in findings_list]
    df = pd.DataFrame(records)

    critical_count = sum(1 for f in findings_list if f.severity_label == "validation_critical")
    high_count = sum(1 for f in findings_list if f.severity_label == "validation_high")
    medium_count = sum(1 for f in findings_list if f.severity_label == "validation_medium")

    summary = {
        "active_profile": active_profile.name,
        "total_findings": len(records),
        "critical_count": critical_count,
        "high_count": high_count,
        "medium_count": medium_count,
        "manual_review_required_count": sum(1 for f in findings_list if f.manual_review_required),
        "destructive_action_allowed": False,
        "non_signal": True,
    }
    return df, summary


def summarize_feature_validation_findings(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize findings DataFrame."""
    return {
        "total_findings": len(df),
        "critical": int((df["severity_label"] == "validation_critical").sum()) if "severity_label" in df else 0,
        "high": int((df["severity_label"] == "validation_high").sum()) if "severity_label" in df else 0,
        "medium": int((df["severity_label"] == "validation_medium").sum()) if "severity_label" in df else 0,
        "manual_review_required_count": int(df["manual_review_required"].sum()) if "manual_review_required" in df else 0,
        "destructive_action_allowed": False,
    }


_GLOBAL_FINDINGS: List[FeatureValidationFinding] = []


def clear_findings() -> None:
    """Clear in-memory validation findings."""
    global _GLOBAL_FINDINGS
    _GLOBAL_FINDINGS.clear()


def get_all_findings() -> List[FeatureValidationFinding]:
    """Return all in-memory validation findings."""
    return list(_GLOBAL_FINDINGS)


def create_finding(
    rule_id: str,
    column_name: str,
    severity: str,
    finding_type: str,
    message: str = "",
    recommendation: str = "",
    manual_review_required: bool = True,
) -> FeatureValidationFinding:
    """Create and register a validation finding in the global findings store."""
    fid = f"FIND-{len(_GLOBAL_FINDINGS) + 1:03d}-{rule_id}"
    sev_label = severity.lower()
    if not sev_label.startswith("validation_"):
        sev_label = f"validation_{sev_label}"

    finding = FeatureValidationFinding(
        finding_id=fid,
        rule_id=rule_id,
        finding_type=finding_type,
        feature_or_matrix_name=column_name,
        severity_label=sev_label,
        status_label="validation_manual_review_required",
        message=message,
        recommendation=recommendation,
        destructive_action_allowed=False,
        manual_review_required=manual_review_required,
    )
    _GLOBAL_FINDINGS.append(finding)
    return finding


def get_findings_summary() -> Dict[str, Any]:
    """Return summary dictionary of all current findings."""
    total = len(_GLOBAL_FINDINGS)
    critical = sum(1 for f in _GLOBAL_FINDINGS if "critical" in f.severity_label.lower())
    high = sum(1 for f in _GLOBAL_FINDINGS if "high" in f.severity_label.lower())
    medium = sum(1 for f in _GLOBAL_FINDINGS if "medium" in f.severity_label.lower())
    low = sum(1 for f in _GLOBAL_FINDINGS if "low" in f.severity_label.lower() or "info" in f.severity_label.lower())

    return {
        "total_findings": total,
        "critical": critical,
        "high": high,
        "medium": medium,
        "low": low,
        "destructive_action_allowed": False,
        "current_phase": 121,
    }

