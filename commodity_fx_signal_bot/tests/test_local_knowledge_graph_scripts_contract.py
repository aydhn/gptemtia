import pytest
import importlib

def test_local_knowledge_graph_scripts_importable():
    scripts = [
        "scripts.run_graph_node_edge_registry",
        "scripts.run_artifact_relationship_graph",
        "scripts.run_semantic_index_report",
        "scripts.run_relationship_query",
        "scripts.run_graph_analysis_report",
        "scripts.run_graph_quality_report",
        "scripts.run_graph_status"
    ]

    for script in scripts:
        try:
            importlib.import_module(script)
        except Exception as e:
            pytest.fail(f"Could not import {script}: {e}")
