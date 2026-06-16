import pytest
import pandas as pd
from pathlib import Path
from local_knowledge_graph.graph_export import (
    build_graph_export_manifest,
    export_graph_to_json,
    export_graph_to_csv,
    export_graph_to_graphml_if_available
)
from local_knowledge_graph.graph_config import get_local_knowledge_graph_profile

def test_graph_export(tmp_path):
    profile = get_local_knowledge_graph_profile("balanced_local_graph")
    df = pd.DataFrame()

    m = build_graph_export_manifest(df, df, profile)
    assert m is not None

    j_p = export_graph_to_json(df, df, tmp_path / "t.json")
    assert j_p.exists()

    c_p1, c_p2 = export_graph_to_csv(df, df, tmp_path)
    assert c_p1 is not None
    assert c_p2 is not None

    g_p, _ = export_graph_to_graphml_if_available(df, df, tmp_path / "t.graphml")
    assert g_p is None # default behavior
