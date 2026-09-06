"""Test suite for Phase 135 Test Contracts."""

from pathlib import Path
from advanced_regime_acceptance.regime_block_test_contracts import (
    build_regime_block_test_contract_report,
    summarize_regime_block_test_contracts,
)


def test_test_contracts():
    root = Path(__file__).resolve().parent.parent
    df, summary = build_regime_block_test_contract_report(root)
    assert not df.empty
    assert summary["total_test_suites_checked"] == 10
    # Note: Phase 135 manifest test will exist once written
    assert summary["non_signal"] is True

    s2 = summarize_regime_block_test_contracts(df)
    assert s2["total_test_suites"] == 10
