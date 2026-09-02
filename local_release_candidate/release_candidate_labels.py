
def list_release_candidate_domain_labels() -> list[str]:
    return [
        "release_candidate_rehearsal_domain",
        "frozen_baseline_domain",
        "baseline_inventory_domain",
        "baseline_hash_manifest_domain",
        "baseline_reproducibility_domain",
        "final_acceptance_domain",
        "operator_signoff_domain",
        "v1_release_dossier_domain",
        "release_notes_domain",
        "known_limitations_domain",
        "handoff_domain",
        "recap_domain",
        "quality_validation_domain",
        "unknown_release_candidate_domain"
    ]

def list_release_candidate_status_labels() -> list[str]:
    return [
        "release_candidate_ready_for_rehearsal",
        "release_candidate_ready_with_warnings",
        "release_candidate_missing",
        "release_candidate_blocked_by_safety",
        "release_candidate_needs_manual_review",
        "release_candidate_unknown"
    ]

def list_baseline_status_labels() -> list[str]:
    return [
        "baseline_rehearsal_available",
        "baseline_rehearsal_partial",
        "baseline_rehearsal_missing",
        "baseline_rehearsal_drift_warning",
        "baseline_rehearsal_unknown"
    ]

def list_acceptance_status_labels() -> list[str]:
    return [
        "acceptance_rehearsal_pass",
        "acceptance_rehearsal_warn",
        "acceptance_rehearsal_fail",
        "acceptance_rehearsal_blocked_by_safety",
        "acceptance_rehearsal_not_applicable",
        "acceptance_rehearsal_unknown"
    ]

def list_release_candidate_risk_labels() -> list[str]:
    return [
        "release_candidate_critical_risk",
        "release_candidate_high_risk",
        "release_candidate_medium_risk",
        "release_candidate_low_risk",
        "release_candidate_info",
        "release_candidate_unknown_risk"
    ]

def validate_release_candidate_domain_label(label: str) -> None:
    if label not in list_release_candidate_domain_labels():
        raise ValueError(f"Invalid label {label}")

def validate_release_candidate_status(label: str) -> None:
    if label not in list_release_candidate_status_labels():
        raise ValueError(f"Invalid label {label}")

def validate_baseline_status(label: str) -> None:
    if label not in list_baseline_status_labels():
        raise ValueError(f"Invalid label {label}")

def validate_acceptance_status(label: str) -> None:
    if label not in list_acceptance_status_labels():
        raise ValueError(f"Invalid label {label}")

def validate_release_candidate_risk(label: str) -> None:
    if label not in list_release_candidate_risk_labels():
        raise ValueError(f"Invalid label {label}")
