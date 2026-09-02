
def list_closure_domain_labels() -> list[str]:
    return [
        "meta_review_domain",
        "lessons_learned_domain",
        "roadmap_domain",
        "governance_rehearsal_domain",
        "closure_dossier_domain",
        "recap_domain",
        "unresolved_items_domain",
        "maintenance_aftercare_domain",
        "quality_validation_domain",
        "unknown_closure_domain"
    ]

def list_closure_item_labels() -> list[str]:
    return [
        "closure_doc_item",
        "closure_report_item",
        "closure_datalake_item",
        "closure_script_item",
        "closure_test_item",
        "closure_generated_doc_item",
        "closure_safety_item",
        "closure_archival_item",
        "closure_delivery_item",
        "closure_acceptance_item",
        "closure_unknown_item"
    ]

def list_closure_status_labels() -> list[str]:
    return [
        "closure_ready_for_rehearsal",
        "closure_ready_with_warnings",
        "closure_missing",
        "closure_blocked_by_safety",
        "closure_needs_manual_review",
        "closure_unknown"
    ]

def list_roadmap_status_labels() -> list[str]:
    return [
        "roadmap_candidate",
        "roadmap_deferred",
        "roadmap_needs_research",
        "roadmap_blocked_by_safety",
        "roadmap_not_applicable",
        "roadmap_unknown"
    ]

def list_closure_risk_labels() -> list[str]:
    return [
        "closure_critical_risk",
        "closure_high_risk",
        "closure_medium_risk",
        "closure_low_risk",
        "closure_info",
        "closure_unknown_risk"
    ]

def validate_closure_domain_label(label: str) -> None:
    if label not in list_closure_domain_labels():
        raise ValueError(f"Invalid domain label: {label}")

def validate_closure_item_label(label: str) -> None:
    if label not in list_closure_item_labels():
        raise ValueError(f"Invalid item label: {label}")

def validate_closure_status(label: str) -> None:
    if label not in list_closure_status_labels():
        raise ValueError(f"Invalid closure status: {label}")

def validate_roadmap_status(label: str) -> None:
    if label not in list_roadmap_status_labels():
        raise ValueError(f"Invalid roadmap status: {label}")

def validate_closure_risk(label: str) -> None:
    if label not in list_closure_risk_labels():
        raise ValueError(f"Invalid closure risk: {label}")
