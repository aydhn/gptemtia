import pandas as pd
from knowledge_base.findings_digest import extract_recent_findings, extract_important_warnings

def test_extract_findings():
    df = pd.DataFrame({"text": ["warning something", "normal text"]})
    f_df = extract_recent_findings(pd.DataFrame(), df)
    assert len(f_df) == 1

def test_extract_warnings():
    df = pd.DataFrame({"text": ["warning!"]})
    w_df = extract_important_warnings(df)
    assert len(w_df) == 1
