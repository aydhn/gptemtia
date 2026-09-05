from pathlib import Path
from advanced_feature_factor_acceptance.feature_engine_block_documentation import (
    build_feature_engine_block_documentation_report,
    summarize_feature_engine_block_documentation,
)

def test_feature_engine_block_documentation():
    root = Path(__file__).resolve().parent.parent
    df, summary = build_feature_engine_block_documentation_report(project_root=root)
    assert not df.empty
    assert summary["total_docs_checked"] == 9
    assert summary["all_present"] is True
    assert summary["non_signal"] is True

    s = summarize_feature_engine_block_documentation(df)
    assert s["total_docs"] == 9
    assert s["all_present"] is True
