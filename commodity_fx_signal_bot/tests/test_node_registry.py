import pytest
from pathlib import Path
from local_knowledge_graph.node_registry import (
    build_nodes_from_artifact_metadata,
    build_nodes_from_evidence_governance,
    build_nodes_from_docs,
    build_symbol_nodes,
    build_module_nodes
)
from local_knowledge_graph.graph_config import get_local_knowledge_graph_profile

def test_node_generation():
    profile = get_local_knowledge_graph_profile("balanced_local_graph")
    df_meta, _ = build_nodes_from_artifact_metadata(Path("."), profile)
    assert df_meta is not None

    df_ev, _ = build_nodes_from_evidence_governance(Path("."), profile)
    assert df_ev is not None

    df_docs, _ = build_nodes_from_docs(Path("."), profile)
    assert not df_docs.empty

    df_sym = build_symbol_nodes(profile)
    assert not df_sym.empty

    df_mod = build_module_nodes(profile)
    assert not df_mod.empty
