import pytest
from local_knowledge_graph.graph_models import (
    build_graph_node_id,
    build_graph_edge_id,
    build_relationship_query_id,
    GraphNode,
    graph_node_to_dict,
    GraphExportManifest
)

def test_build_ids_deterministic():
    assert build_graph_node_id("type", "label", "path") == build_graph_node_id("type", "label", "path")
    assert build_graph_edge_id("n1", "n2", "type") == build_graph_edge_id("n1", "n2", "type")
    assert build_relationship_query_id("q1") == build_relationship_query_id("q1")

def test_graph_node_to_dict():
    node = GraphNode("1", "type", "label", "mod", "path", "title", "summary", {}, [])
    d = graph_node_to_dict(node)
    assert d["node_id"] == "1"

def test_graph_export_manifest():
    m = GraphExportManifest("1", "prof", "time", 1, 1, ["json"], True, [])
    assert m.local_only is True
