import pandas as pd
from knowledge_base.workspace_summary import build_workspace_summary, build_workspace_status_table

def test_workspace_summary():
    df = pd.DataFrame({"text": ["warning"]})
    summ = build_workspace_summary(df, df)
    assert summ["warning_count"] == 1

def test_status_table():
    df = pd.DataFrame()
    table = build_workspace_status_table(df, df)
    assert len(table) == 4
