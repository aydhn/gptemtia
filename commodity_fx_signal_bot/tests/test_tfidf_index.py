import pytest
import pandas as pd
from pathlib import Path
from local_knowledge_graph.tfidf_index import (
    build_local_tfidf_index,
    build_tfidf_index_manifest,
    search_tfidf_index
)
from local_knowledge_graph.graph_config import get_local_knowledge_graph_profile

def test_tfidf_index():
    profile = get_local_knowledge_graph_profile("balanced_local_graph")
    df = pd.DataFrame()

    index, sum_ = build_local_tfidf_index(df, Path("."), profile)
    assert index is not None

    m = build_tfidf_index_manifest(index, profile)
    assert m is not None

    s_df, _ = search_tfidf_index("query", index, profile)
    assert s_df is not None
