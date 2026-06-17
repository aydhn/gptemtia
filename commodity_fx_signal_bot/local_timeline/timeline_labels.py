"""
Controlled label sets for Local Timeline engine.
"""

EVENT_TYPE_LABELS = {
    "phase_event",
    "file_created_event",
    "file_modified_event",
    "report_generated_event",
    "datalake_artifact_event",
    "documentation_event",
    "command_script_event",
    "evidence_event",
    "metadata_card_event",
    "graph_event",
    "scenario_event",
    "regression_event",
    "quality_event",
    "safety_event",
    "backup_event",
    "packaging_event",
    "secrets_event",
    "unknown_event",
}

TIMELINE_SOURCE_LABELS = {
    "project_files_source",
    "reports_output_source",
    "data_lake_source",
    "docs_source",
    "generated_docs_source",
    "artifact_metadata_source",
    "evidence_governance_source",
    "local_knowledge_graph_source",
    "backup_recovery_source",
    "portable_packaging_source",
    "secrets_hygiene_source",
    "quality_gates_source",
    "scenario_regression_source",
    "unknown_source",
}

TEMPORAL_STATUS_LABELS = {
    "event_fresh",
    "event_warning_stale",
    "event_stale",
    "event_missing_timestamp",
    "event_unknown_time",
}

CHANGE_IMPACT_LABELS = {
    "high_change_attention",
    "medium_change_attention",
    "low_change_attention",
    "informational_change",
    "unknown_change_impact",
}

TIMELINE_QUERY_INTENT_LABELS = {
    "find_events_by_phase",
    "find_events_by_module",
    "find_events_by_artifact",
    "find_recent_changes",
    "find_stale_artifacts",
    "find_timeline_gaps",
    "find_phase_digest",
    "find_change_digest",
    "unknown_timeline_query",
}


def list_event_type_labels() -> list[str]:
    return sorted(list(EVENT_TYPE_LABELS))

def list_timeline_source_labels() -> list[str]:
    return sorted(list(TIMELINE_SOURCE_LABELS))

def list_temporal_status_labels() -> list[str]:
    return sorted(list(TEMPORAL_STATUS_LABELS))

def list_change_impact_labels() -> list[str]:
    return sorted(list(CHANGE_IMPACT_LABELS))

def list_timeline_query_intent_labels() -> list[str]:
    return sorted(list(TIMELINE_QUERY_INTENT_LABELS))


def validate_event_type(label: str) -> None:
    if label not in EVENT_TYPE_LABELS:
        raise ValueError(f"Invalid event type label: {label}")

def validate_timeline_source(label: str) -> None:
    if label not in TIMELINE_SOURCE_LABELS:
        raise ValueError(f"Invalid timeline source label: {label}")

def validate_temporal_status(label: str) -> None:
    if label not in TEMPORAL_STATUS_LABELS:
        raise ValueError(f"Invalid temporal status label: {label}")

def validate_change_impact(label: str) -> None:
    if label not in CHANGE_IMPACT_LABELS:
        raise ValueError(f"Invalid change impact label: {label}")

def validate_timeline_query_intent(label: str) -> None:
    if label not in TIMELINE_QUERY_INTENT_LABELS:
        raise ValueError(f"Invalid timeline query intent label: {label}")
