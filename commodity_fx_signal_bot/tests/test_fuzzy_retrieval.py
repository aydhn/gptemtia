import pandas as pd
from knowledge_base.fuzzy_retrieval import run_fuzzy_retrieval, calculate_simple_fuzzy_score

def test_fuzzy_score():
    score = calculate_simple_fuzzy_score("hello world", "hello beautiful world")
    assert score > 0.0

def test_fuzzy_retrieval():
    c_df = pd.DataFrame({"text": ["hello world", "goodbye"], "chunk_id": ["1", "2"]})
    res, summ = run_fuzzy_retrieval("hello", c_df)
    assert summ["status"] == "success"
    assert len(res) == 1
