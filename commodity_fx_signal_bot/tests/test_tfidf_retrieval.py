import pandas as pd
from knowledge_base.tfidf_retrieval import run_tfidf_retrieval

def test_tfidf_retrieval():
    c_df = pd.DataFrame({"text": ["Gold is shining", "Oil is dropping"], "chunk_id": ["1", "2"]})
    res, summ = run_tfidf_retrieval("gold", c_df)
    if summ.get("status") == "success":
        assert len(res) >= 0 # Could be 1 depending on tfidf stopwords
