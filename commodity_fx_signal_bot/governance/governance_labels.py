# Artifact type labels
ARTIFACT_TYPE_LABELS = [
    "raw_data_artifact",
    "processed_data_artifact",
    "feature_artifact",
    "candidate_artifact",
    "backtest_artifact",
    "validation_artifact",
    "ml_artifact",
    "paper_artifact",
    "notification_artifact",
    "orchestration_artifact",
    "observability_artifact",
    "security_artifact",
    "research_report_artifact",
    "report_export_artifact",
    "portfolio_artifact",
    "regime_artifact",
    "synthetic_index_artifact",
    "factor_artifact",
    "meta_research_artifact",
    "experiment_artifact",
    "governance_artifact",
    "unknown_artifact"
]

# Lineage relation labels
LINEAGE_RELATION_LABELS = [
    "derived_from",
    "depends_on",
    "produced_by",
    "consumed_by",
    "validates",
    "compares_to",
    "summarizes",
    "exports",
    "tracks",
    "audits",
    "unknown_relation"
]

# Governance status labels
GOVERNANCE_STATUS_LABELS = [
    "governance_passed",
    "governance_warning",
    "governance_failed",
    "governance_incomplete",
    "governance_unknown"
]

# Audit event labels
AUDIT_EVENT_LABELS = [
    "artifact_created",
    "artifact_updated",
    "artifact_scanned",
    "fingerprint_created",
    "provenance_recorded",
    "lineage_recorded",
    "dependency_traced",
    "quality_checked",
    "governance_reported",
    "unknown_audit_event"
]

def list_artifact_type_labels() -> list[str]:
    return list(ARTIFACT_TYPE_LABELS)

def list_lineage_relation_labels() -> list[str]:
    return list(LINEAGE_RELATION_LABELS)

def list_governance_status_labels() -> list[str]:
    return list(GOVERNANCE_STATUS_LABELS)

def list_audit_event_labels() -> list[str]:
    return list(AUDIT_EVENT_LABELS)

def validate_artifact_type(label: str) -> None:
    if label not in ARTIFACT_TYPE_LABELS:
        raise ValueError(f"Invalid artifact type label: {label}")

def validate_lineage_relation(label: str) -> None:
    if label not in LINEAGE_RELATION_LABELS:
        raise ValueError(f"Invalid lineage relation label: {label}")

def validate_governance_status(label: str) -> None:
    if label not in GOVERNANCE_STATUS_LABELS:
        raise ValueError(f"Invalid governance status label: {label}")

def validate_audit_event_label(label: str) -> None:
    if label not in AUDIT_EVENT_LABELS:
        raise ValueError(f"Invalid audit event label: {label}")
