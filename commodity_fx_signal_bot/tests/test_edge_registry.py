import pytest
import pandas as pd
from pathlib import Path
from local_knowledge_graph.edge_registry import (
    build_edges_from_path_relationships,
    build_edges_from_metadata_lineage,
    build_edges_from_evidence_mappings,
    build_edges_from_symbol_mentions,
    deduplicate_edges
)
from local_knowledge_graph.graph_config import get_local_knowledge_graph_profile

def test_edge_generation():
    profile = get_local_knowledge_graph_profile("balanced_local_graph")
    df = pd.DataFrame()

    e1, _ = build_edges_from_path_relationships(df, profile)
    assert e1 is not None

    e2, _ = build_edges_from_metadata_lineage(df, Path("."), profile)
    assert e2 is not None

    e3, _ = build_edges_from_evidence_mappings(df, Path("."), profile)
    assert e3 is not None

    e4, _ = build_edges_from_symbol_mentions(df, Path("."), profile)
    assert e4 is not None

def test_deduplicate_edges():
    df = pd.DataFrame([{"source_node_id":"A", "target_node_id":"B", "edge_type":"type1"},
                       {"source_node_id":"A", "target_node_id":"B", "edge_type":"type1"}])
    dedup = deduplicate_edges(df)
    assert len(dedup) == 1
