import pandas as pd
from knowledge_base.hybrid_retrieval import combine_retrieval_scores, rerank_retrieval_results

def test_combine_scores():
    df1 = pd.DataFrame({"chunk_id": ["1"], "tfidf_score": [0.8]})
    df2 = pd.DataFrame({"chunk_id": ["1"], "fuzzy_score": [0.6]})
    res = combine_retrieval_scores(df1, df2)
    assert not res.empty
    assert "hybrid_score" in res.columns

def test_rerank():
    df = pd.DataFrame({"hybrid_score": [0.5], "symbols": [["GC=F"]]})
    res = rerank_retrieval_results(df, "GC=F")
    assert res['final_score'].iloc[0] > 0.5
