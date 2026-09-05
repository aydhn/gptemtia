"""Tests for Macro Feature Fusion Contracts."""

from advanced_feature_fusion.macro_feature_fusion_contracts import (
    build_macro_feature_fusion_contract_registry,
    get_macro_timeseries_contracts,
    summarize_macro_feature_fusion_contracts,
)


def test_macro_contracts():
    df, summary = build_macro_feature_fusion_contract_registry()
    assert len(df) == 4
    assert summary["total_contracts"] == 4
    assert summary["non_signal_guaranteed"] is True


def test_macro_contracts_list():
    contracts = get_macro_timeseries_contracts()
    assert len(contracts) == 4
    assert any(c["contract_name"] == "macro_timeseries_context_contract" for c in contracts)
