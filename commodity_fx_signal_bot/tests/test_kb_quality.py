import pandas as pd
from knowledge_base.kb_quality import check_for_sensitive_data_in_kb, check_for_forbidden_trade_terms_in_kb

def test_sensitive_data():
    df = pd.DataFrame({"text": ["Here is my API_KEY"]})
    res = check_for_sensitive_data_in_kb(df=df)
    assert res["found"] is True

def test_forbidden_terms():
    df = pd.DataFrame({"text": ["Should I AL now?"]})
    res = check_for_forbidden_trade_terms_in_kb(df=df)
    assert res["found"] is True
