import pytest
import pandas as pd
from pathlib import Path
from local_knowledge_graph.semantic_keyword_index import (
    build_local_semantic_keyword_index,
    tokenize_local_text,
    extract_top_keywords,
    search_keyword_index
)
from local_knowledge_graph.graph_config import get_local_knowledge_graph_profile

def test_semantic_keyword_index():
    profile = get_local_knowledge_graph_profile("balanced_local_graph")
    df = pd.DataFrame()

    k_df, sum_ = build_local_semantic_keyword_index(df, Path("."), profile)
    assert k_df is not None

    tokens = tokenize_local_text("test string")
    assert "test" in tokens

    tops = extract_top_keywords("test test string")
    assert len(tops) <= 20

    s_df, _ = search_keyword_index("query", df, profile)
    assert s_df is not None
