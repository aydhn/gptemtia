import pandas as pd

from governance.lineage_graph import build_artifact_lineage_graph


def test_build_graph():
    inv_df = pd.DataFrame([
        {"artifact_id": "a1", "artifact_type": "raw_data_artifact", "file_name": "r.csv", "relative_path": "raw/r.csv", "size_bytes": 10},
        {"artifact_id": "a2", "artifact_type": "processed_data_artifact", "file_name": "p.csv", "relative_path": "processed/p.csv", "size_bytes": 10}
    ])

    # no provenance, just infer
    g, meta = build_artifact_lineage_graph(inv_df)

    assert len(g.nodes) == 2
    assert len(g.edges) == 1 # inferred raw -> processed

    ndf = g.to_node_dataframe()
    edf = g.to_edge_dataframe()

    assert not ndf.empty
    assert not edf.empty

    adj = g.build_adjacency()
    # node_a1 -> node_a2
    assert "node_a2" in adj["node_a1"]

    assert "node_a2" in g.get_downstream_nodes("node_a1")
    assert "node_a1" in g.get_upstream_nodes("node_a2")

    cycles = g.detect_cycles()
    assert not cycles["has_cycles"]
