import pytest
from local_knowledge_graph.graph_report_builder import (
    build_graph_disclaimer,
    build_graph_node_edge_registry_markdown_report,
    build_artifact_relationship_graph_markdown_report,
    build_semantic_index_markdown_report,
    build_relationship_query_markdown_report,
    build_graph_analysis_markdown_report,
    build_graph_quality_markdown_report,
    build_graph_status_markdown_report
)

def test_graph_report_builder():
    d = build_graph_disclaimer()
    assert "offline/local knowledge graph" in d

    assert build_graph_node_edge_registry_markdown_report({}) is not None
    assert build_artifact_relationship_graph_markdown_report({}) is not None
    assert build_semantic_index_markdown_report({}) is not None
    assert build_relationship_query_markdown_report({}) is not None
    assert build_graph_analysis_markdown_report({}) is not None
    assert build_graph_quality_markdown_report({}) is not None
    assert build_graph_status_markdown_report({}) is not None
