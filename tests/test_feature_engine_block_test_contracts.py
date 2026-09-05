from pathlib import Path
from advanced_feature_factor_acceptance.feature_engine_block_test_contracts import (
    build_feature_engine_block_test_contract_report,
    summarize_feature_engine_block_test_contracts,
)

def test_feature_engine_block_test_contracts():
    root = Path(__file__).resolve().parent.parent
    df, summary = build_feature_engine_block_test_contract_report(project_root=root)
    assert not df.empty
    assert summary["all_present"] is True
    assert summary["missing_test_suites"] == 0
    assert summary["non_signal"] is True

    s = summarize_feature_engine_block_test_contracts(df)
    assert s["all_present"] is True
    assert s["non_signal"] is True
