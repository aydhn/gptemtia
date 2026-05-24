import pandas as pd
from knowledge_base.indexing import KnowledgeIndex

def test_knowledge_index():
    df = pd.DataFrame({"title": ["Doc1", "Doc2"], "relative_path": ["p1", "p2"]})
    c_df = pd.DataFrame({"symbols": [["GC=F"], ["CL=F"]]})
    idx = KnowledgeIndex(df, c_df)

    assert len(idx.search_documents_by_keyword("doc1")) == 1
    assert len(idx.filter_by_symbol("GC=F")) == 1
