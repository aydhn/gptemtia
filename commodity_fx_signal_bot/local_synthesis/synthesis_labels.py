from typing import List

_phase_family_labels = [
    "core_research_family", "data_storage_family", "reporting_family",
    "safety_governance_family", "metadata_evidence_family", "graph_timeline_family",
    "consistency_readiness_family", "maintenance_archive_dr_family",
    "training_briefing_family", "synthesis_family", "unknown_family"
]

_index_item_labels = [
    "artifact_index_item", "report_index_item", "datalake_index_item",
    "docs_index_item", "script_index_item", "test_index_item",
    "command_index_item", "generated_doc_index_item", "unknown_index_item"
]

_synthesis_status_labels = [
    "synthesis_ready", "synthesis_ready_with_warnings", "synthesis_missing",
    "synthesis_blocked_by_safety", "synthesis_needs_manual_review", "synthesis_unknown"
]

_closure_checklist_labels = [
    "closure_item_done", "closure_item_warning", "closure_item_missing",
    "closure_item_blocked", "closure_item_not_applicable", "closure_item_unknown"
]

_synthesis_risk_labels = [
    "synthesis_critical_risk", "synthesis_high_risk", "synthesis_medium_risk",
    "synthesis_low_risk", "synthesis_info", "synthesis_unknown_risk"
]

def list_phase_family_labels() -> List[str]: return _phase_family_labels.copy()
def list_index_item_labels() -> List[str]: return _index_item_labels.copy()
def list_synthesis_status_labels() -> List[str]: return _synthesis_status_labels.copy()
def list_closure_checklist_labels() -> List[str]: return _closure_checklist_labels.copy()
def list_synthesis_risk_labels() -> List[str]: return _synthesis_risk_labels.copy()

def validate_phase_family_label(label: str) -> None:
    if label not in _phase_family_labels: raise ValueError(f"Invalid {label}")
def validate_index_item_label(label: str) -> None:
    if label not in _index_item_labels: raise ValueError(f"Invalid {label}")
def validate_synthesis_status(label: str) -> None:
    if label not in _synthesis_status_labels: raise ValueError(f"Invalid {label}")
def validate_closure_checklist_label(label: str) -> None:
    if label not in _closure_checklist_labels: raise ValueError(f"Invalid {label}")
def validate_synthesis_risk(label: str) -> None:
    if label not in _synthesis_risk_labels: raise ValueError(f"Invalid {label}")
