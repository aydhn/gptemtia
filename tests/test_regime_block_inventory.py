"""Test suite for Phase 135 Regime Block Inventory."""

from advanced_regime_acceptance.regime_block_inventory import (
    build_regime_block_inventory_report,
    summarize_regime_block_inventory,
)


def test_block_inventory():
    df, summary = build_regime_block_inventory_report()
    assert len(df) == 10
    assert summary["total_modules"] == 10
    assert summary["phase_range"] == "126-135"
    assert summary["non_signal"] is True

    s2 = summarize_regime_block_inventory(df)
    assert s2["module_count"] == 10
    assert s2["all_non_signal"] is True
    assert "advanced_regime_foundation" in s2["modules"]
    assert "advanced_regime_acceptance" in s2["modules"]
