from typing import List

NODE_TYPE_LABELS = [
    "artifact_node",
    "model_card_node",
    "dataset_card_node",
    "experiment_card_node",
    "evidence_node",
    "policy_node",
    "control_node",
    "report_node",
    "scenario_node",
    "regression_node",
    "command_node",
    "module_node",
    "document_node",
    "symbol_node",
    "unknown_node"
]

EDGE_TYPE_LABELS = [
    "references_edge",
    "derived_from_edge",
    "validates_edge",
    "documents_edge",
    "evidences_edge",
    "controls_edge",
    "belongs_to_module_edge",
    "mentions_symbol_edge",
    "generated_by_edge",
    "depends_on_edge",
    "similar_to_edge",
    "summarizes_edge",
    "warns_about_edge",
    "unknown_edge"
]

GRAPH_STATUS_LABELS = [
    "graph_ready",
    "graph_ready_with_warnings",
    "graph_partial",
    "graph_blocked_by_safety",
    "graph_unknown"
]

QUERY_INTENT_LABELS = [
    "find_neighbors_query",
    "find_evidence_query",
    "find_cards_query",
    "find_reports_query",
    "find_scenarios_query",
    "find_controls_query",
    "find_symbols_query",
    "find_orphans_query",
    "find_gaps_query",
    "unknown_query"
]

RELATIONSHIP_STRENGTH_LABELS = [
    "strong_relationship",
    "medium_relationship",
    "weak_relationship",
    "inferred_relationship",
    "unknown_relationship"
]

def list_node_type_labels() -> List[str]:
    return NODE_TYPE_LABELS

def list_edge_type_labels() -> List[str]:
    return EDGE_TYPE_LABELS

def list_graph_status_labels() -> List[str]:
    return GRAPH_STATUS_LABELS

def list_query_intent_labels() -> List[str]:
    return QUERY_INTENT_LABELS

def list_relationship_strength_labels() -> List[str]:
    return RELATIONSHIP_STRENGTH_LABELS

def validate_node_type(label: str) -> None:
    if label not in NODE_TYPE_LABELS:
        raise ValueError(f"Invalid node type label: {label}")

def validate_edge_type(label: str) -> None:
    if label not in EDGE_TYPE_LABELS:
        raise ValueError(f"Invalid edge type label: {label}")

def validate_graph_status(label: str) -> None:
    if label not in GRAPH_STATUS_LABELS:
        raise ValueError(f"Invalid graph status label: {label}")

def validate_query_intent(label: str) -> None:
    if label not in QUERY_INTENT_LABELS:
        raise ValueError(f"Invalid query intent label: {label}")

def validate_relationship_strength(label: str) -> None:
    if label not in RELATIONSHIP_STRENGTH_LABELS:
        raise ValueError(f"Invalid relationship strength label: {label}")
