import pytest
from local_knowledge_graph.graph_labels import (
    list_node_type_labels,
    list_edge_type_labels,
    list_graph_status_labels,
    list_query_intent_labels,
    list_relationship_strength_labels,
    validate_node_type,
    validate_edge_type,
    validate_graph_status
)

def test_label_lists_not_empty():
    assert len(list_node_type_labels()) > 0
    assert len(list_edge_type_labels()) > 0
    assert len(list_graph_status_labels()) > 0
    assert len(list_query_intent_labels()) > 0
    assert len(list_relationship_strength_labels()) > 0

def test_validate_node_type():
    validate_node_type("artifact_node")
    with pytest.raises(ValueError):
        validate_node_type("invalid_node")

def test_validate_edge_type():
    validate_edge_type("references_edge")
    with pytest.raises(ValueError):
        validate_edge_type("invalid_edge")

def test_graph_status_not_production():
    assert "production_ready" not in list_graph_status_labels()
