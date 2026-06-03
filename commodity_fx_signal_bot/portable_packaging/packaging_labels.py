from typing import List

def list_packaging_artifact_labels() -> List[str]:
    return [
        "source_artifact",
        "config_artifact",
        "docs_artifact",
        "tests_artifact",
        "reports_manifest_artifact",
        "data_manifest_artifact",
        "requirements_artifact",
        "environment_snapshot_artifact",
        "setup_guide_artifact",
        "archive_manifest_artifact",
        "unknown_artifact"
    ]

def list_install_verification_labels() -> List[str]:
    return [
        "install_check_passed",
        "install_check_warning",
        "install_check_failed",
        "install_check_skipped",
        "install_check_unknown"
    ]

def list_packaging_safety_labels() -> List[str]:
    return [
        "packaging_safe_manifest_only",
        "packaging_safe_local_only",
        "packaging_review_required",
        "packaging_blocked_secret_risk",
        "packaging_blocked_publish_risk",
        "packaging_blocked_deploy_risk",
        "packaging_blocked_live_risk",
        "packaging_unknown_safety"
    ]

def list_environment_drift_labels() -> List[str]:
    return [
        "environment_match",
        "environment_minor_drift",
        "environment_major_drift",
        "environment_missing_snapshot",
        "environment_unknown_drift"
    ]

def validate_packaging_artifact_label(label: str) -> None:
    if label not in list_packaging_artifact_labels():
        raise ValueError(f"Invalid artifact label: {label}")

def validate_install_verification_label(label: str) -> None:
    if label not in list_install_verification_labels():
        raise ValueError(f"Invalid install verification label: {label}")

def validate_packaging_safety_label(label: str) -> None:
    if label not in list_packaging_safety_labels():
        raise ValueError(f"Invalid safety label: {label}")

def validate_environment_drift_label(label: str) -> None:
    if label not in list_environment_drift_labels():
        raise ValueError(f"Invalid environment drift label: {label}")
