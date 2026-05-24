from typing import List

KNOWLEDGE_DOCUMENT_TYPE_LABELS = [
    "research_report_document",
    "report_export_document",
    "experiment_document",
    "governance_document",
    "planning_document",
    "meta_research_document",
    "factor_document",
    "portfolio_document",
    "regime_document",
    "synthetic_index_document",
    "paper_document",
    "validation_document",
    "ml_document",
    "observability_document",
    "security_document",
    "documentation_document",
    "phase_log_document",
    "unknown_document"
]

MEMORY_CARD_TYPE_LABELS = [
    "symbol_memory_card",
    "hypothesis_memory_card",
    "experiment_memory_card",
    "governance_memory_card",
    "planning_memory_card",
    "warning_memory_card",
    "finding_memory_card",
    "unknown_memory_card"
]

RETRIEVAL_METHOD_LABELS = [
    "keyword_retrieval",
    "tfidf_retrieval",
    "fuzzy_retrieval",
    "hybrid_retrieval",
    "manual_lookup",
    "unknown_retrieval"
]

DECISION_JOURNAL_STATUS_LABELS = [
    "decision_note",
    "research_observation",
    "hypothesis_note",
    "follow_up_needed",
    "resolved_note",
    "archived_note",
    "unknown_decision_status"
]

def list_knowledge_document_type_labels() -> List[str]:
    return KNOWLEDGE_DOCUMENT_TYPE_LABELS.copy()

def list_memory_card_type_labels() -> List[str]:
    return MEMORY_CARD_TYPE_LABELS.copy()

def list_retrieval_method_labels() -> List[str]:
    return RETRIEVAL_METHOD_LABELS.copy()

def list_decision_journal_status_labels() -> List[str]:
    return DECISION_JOURNAL_STATUS_LABELS.copy()

def validate_knowledge_document_type(label: str) -> None:
    if label not in KNOWLEDGE_DOCUMENT_TYPE_LABELS:
        raise ValueError(f"Invalid knowledge document type label: {label}")

def validate_memory_card_type(label: str) -> None:
    if label not in MEMORY_CARD_TYPE_LABELS:
        raise ValueError(f"Invalid memory card type label: {label}")

def validate_retrieval_method(label: str) -> None:
    if label not in RETRIEVAL_METHOD_LABELS:
        raise ValueError(f"Invalid retrieval method label: {label}")

def validate_decision_journal_status(label: str) -> None:
    if label not in DECISION_JOURNAL_STATUS_LABELS:
        raise ValueError(f"Invalid decision journal status label: {label}")
