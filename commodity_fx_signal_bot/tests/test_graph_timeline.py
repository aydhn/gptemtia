import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from pathlib import Path
import pandas as pd
from local_timeline.graph_timeline import classify_graph_event, link_graph_events_to_nodes_edges

def test_classify_graph_event():
    assert classify_graph_event(Path("node_a.json"), Path(".")) == "node_update"
    assert classify_graph_event(Path("edge_a.json"), Path(".")) == "edge_update"
    assert classify_graph_event(Path("graph.json"), Path(".")) == "graph_structure_update"

def test_link_graph_events_to_nodes_edges():
    df = pd.DataFrame([{"relative_path": "a.json"}])
    mapped = link_graph_events_to_nodes_edges(Path("."), df)
    assert not mapped.empty
    assert mapped.iloc[0]['linked_element'] == "inferred_element"
