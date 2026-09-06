"""Test suite for Phase 135 Documentation Audit."""

from pathlib import Path
from advanced_regime_acceptance.regime_block_documentation import (
    build_regime_block_documentation_report,
    summarize_regime_block_documentation,
)


def test_documentation_report():
    root = Path(__file__).resolve().parent.parent
    df, summary = build_regime_block_documentation_report(root)
    assert not df.empty
    assert summary["total_docs"] >= 9
    assert summary["all_exist"] is True
    assert summary["non_signal"] is True

    s2 = summarize_regime_block_documentation(df)
    assert s2["all_exist"] is True
