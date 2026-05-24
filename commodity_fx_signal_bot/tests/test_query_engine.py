import pandas as pd
from knowledge_base.query_engine import ResearchQueryEngine
from knowledge_base.kb_config import get_default_knowledge_base_profile

def test_query_engine():
    prof = get_default_knowledge_base_profile()
    df = pd.DataFrame()
    eng = ResearchQueryEngine(df, df, prof)
    ans, _ = eng.answer_with_sources("test")
    assert "Kanıt yetersiz" in ans
