import pandas as pd
from knowledge_base.kb_report_builder import build_kb_disclaimer, build_knowledge_index_markdown_report

def test_disclaimer():
    assert "DISCLAIMER" in build_kb_disclaimer()

def test_index_report():
    df = pd.DataFrame({"document_id": ["1"]})
    md = build_knowledge_index_markdown_report({"total": 1}, df, df)
    assert "DISCLAIMER" in md
