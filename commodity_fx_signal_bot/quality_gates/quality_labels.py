class ValueErrorLabel(Exception):
    pass

_QUALITY_CHECK_TYPE_LABELS = [
    "pytest_check",
    "import_validation_check",
    "static_safety_check",
    "repo_hygiene_check",
    "dependency_audit_check",
    "smoke_test_check",
    "output_contract_check",
    "documentation_coverage_check",
    "release_manifest_check",
    "unknown_quality_check",
]

_QUALITY_STATUS_LABELS = [
    "quality_passed",
    "quality_warning",
    "quality_failed",
    "quality_skipped",
    "quality_unknown",
]

_RELEASE_CANDIDATE_LABELS = [
    "rc_ready_offline",
    "rc_ready_with_warnings",
    "rc_blocked",
    "rc_incomplete",
    "rc_unknown",
]

_REPO_HYGIENE_LABELS = [
    "clean_repo_hygiene",
    "minor_repo_hygiene_warnings",
    "major_repo_hygiene_warnings",
    "repo_hygiene_failed",
    "repo_hygiene_unknown",
]

def list_quality_check_type_labels() -> list[str]:
    return _QUALITY_CHECK_TYPE_LABELS.copy()

def list_quality_status_labels() -> list[str]:
    return _QUALITY_STATUS_LABELS.copy()

def list_release_candidate_labels() -> list[str]:
    return _RELEASE_CANDIDATE_LABELS.copy()

def list_repo_hygiene_labels() -> list[str]:
    return _REPO_HYGIENE_LABELS.copy()

def validate_quality_check_type(label: str) -> None:
    if label not in _QUALITY_CHECK_TYPE_LABELS:
        raise ValueErrorLabel(f"Invalid quality check type label: {label}")

def validate_quality_status(label: str) -> None:
    if label not in _QUALITY_STATUS_LABELS:
        raise ValueErrorLabel(f"Invalid quality status label: {label}")

def validate_release_candidate_label(label: str) -> None:
    if label not in _RELEASE_CANDIDATE_LABELS:
        raise ValueErrorLabel(f"Invalid release candidate label: {label}")

def validate_repo_hygiene_label(label: str) -> None:
    if label not in _REPO_HYGIENE_LABELS:
        raise ValueErrorLabel(f"Invalid repo hygiene label: {label}")
