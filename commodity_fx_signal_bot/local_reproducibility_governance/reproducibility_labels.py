"""Reproducibility labels."""
_DOMAIN_LABELS = [
    "reproducibility_dossier_domain",
    "environment_replay_domain",
    "deterministic_runbook_domain",
    "build_free_reproduction_domain",
    "reproducibility_evidence_domain",
    "reproducibility_integrity_domain",
    "reproducibility_drift_variance_domain",
    "reproducibility_manual_review_domain",
    "reproducibility_governance_domain",
    "reproducibility_boundary_domain",
    "quality_validation_domain",
    "unknown_reproducibility_domain",
]

_STATUS_LABELS = [
    "reproducibility_rehearsal_ready",
    "reproducibility_rehearsal_ready_with_warnings",
    "reproducibility_rehearsal_missing",
    "reproducibility_rehearsal_blocked_by_safety",
    "reproducibility_rehearsal_needs_manual_review",
    "reproducibility_rehearsal_unknown",
]

_ENV_REPLAY_LABELS = [
    "environment_replay_documented_only",
    "environment_replay_non_install",
    "environment_replay_manual_review_required",
    "environment_replay_blocked_by_boundary",
    "environment_replay_unknown",
]

_DETERMINISM_LABELS = [
    "deterministic_rehearsal_available",
    "deterministic_rehearsal_partial",
    "deterministic_rehearsal_manual_review",
    "deterministic_rehearsal_not_guaranteed",
    "deterministic_rehearsal_unknown",
]

_RISK_LABELS = [
    "reproducibility_critical_risk",
    "reproducibility_high_risk",
    "reproducibility_medium_risk",
    "reproducibility_low_risk",
    "reproducibility_info",
    "reproducibility_unknown_risk",
]

def list_reproducibility_domain_labels() -> list[str]:
    return _DOMAIN_LABELS.copy()

def list_reproducibility_status_labels() -> list[str]:
    return _STATUS_LABELS.copy()

def list_environment_replay_labels() -> list[str]:
    return _ENV_REPLAY_LABELS.copy()

def list_determinism_labels() -> list[str]:
    return _DETERMINISM_LABELS.copy()

def list_reproducibility_risk_labels() -> list[str]:
    return _RISK_LABELS.copy()

def validate_reproducibility_domain_label(label: str) -> None:
    if label not in _DOMAIN_LABELS:
        raise ValueError(f"Invalid domain label: {label}")

def validate_reproducibility_status(label: str) -> None:
    if label not in _STATUS_LABELS:
        raise ValueError(f"Invalid status label: {label}")

def validate_environment_replay_label(label: str) -> None:
    if label not in _ENV_REPLAY_LABELS:
        raise ValueError(f"Invalid replay label: {label}")

def validate_determinism_label(label: str) -> None:
    if label not in _DETERMINISM_LABELS:
        raise ValueError(f"Invalid determinism label: {label}")

def validate_reproducibility_risk(label: str) -> None:
    if label not in _RISK_LABELS:
        raise ValueError(f"Invalid risk label: {label}")
