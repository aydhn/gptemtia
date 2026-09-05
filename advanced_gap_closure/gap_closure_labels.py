DOMAIN_LABELS = [
    "gap_closure_profile_domain", "readiness_reconciliation_domain", "mvp_to_v2_closure_domain",
    "foundation_audit_domain", "dependency_closure_domain", "missing_functionality_domain",
    "implementation_backlog_domain", "phase_106_handoff_domain", "data_provider_requirement_domain",
    "no_scraping_boundary_domain", "provider_interface_readiness_domain", "data_quality_readiness_domain",
    "contract_handoff_domain", "functional_safety_domain", "functional_quality_domain", "unknown_gap_closure_domain"
]

STATUS_LABELS = [
    "gap_closed", "gap_partially_closed", "gap_open", "gap_blocked_by_safety",
    "gap_deferred_to_future_phase", "gap_needs_manual_review", "gap_unknown"
]

PRIORITY_LABELS = [
    "priority_critical", "priority_high", "priority_medium", "priority_low", "priority_info"
]

READINESS_LABELS = [
    "data_foundation_ready", "data_foundation_ready_with_warnings", "data_foundation_missing",
    "data_foundation_blocked_by_no_scraping_boundary", "data_foundation_needs_manual_review", "data_foundation_unknown"
]

RISK_LABELS = [
    "functional_gap_critical_risk", "functional_gap_high_risk", "functional_gap_medium_risk",
    "functional_gap_low_risk", "functional_gap_info", "functional_gap_unknown_risk"
]

def list_gap_closure_domain_labels(): return DOMAIN_LABELS
def list_gap_status_labels(): return STATUS_LABELS
def list_implementation_priority_labels(): return PRIORITY_LABELS
def list_data_foundation_readiness_labels(): return READINESS_LABELS
def list_functional_gap_risk_labels(): return RISK_LABELS

def validate_gap_closure_domain_label(label: str): assert label in DOMAIN_LABELS
def validate_gap_status(label: str): assert label in STATUS_LABELS
def validate_implementation_priority(label: str): assert label in PRIORITY_LABELS
def validate_data_foundation_readiness(label: str): assert label in READINESS_LABELS
def validate_functional_gap_risk_label(label: str): assert label in RISK_LABELS
