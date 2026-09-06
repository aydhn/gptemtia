"""Test suite for Phase 135 Script Contracts."""

from pathlib import Path
from advanced_regime_acceptance.regime_block_script_contracts import (
    build_regime_block_script_contract_report,
    summarize_regime_block_script_contracts,
)


def test_script_contracts():
    root = Path(__file__).resolve().parent.parent
    df, summary = build_regime_block_script_contract_report(root)
    assert not df.empty
    assert summary["total_scripts_checked"] == 20
    assert summary["all_present"] is True
    assert summary["non_signal"] is True

    s2 = summarize_regime_block_script_contracts(df)
    assert s2["all_present"] is True
