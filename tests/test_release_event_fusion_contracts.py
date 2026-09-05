"""Tests for Release Event Fusion Contracts."""

from advanced_feature_fusion.release_event_fusion_contracts import (
    build_release_event_fusion_contract_registry,
    get_release_event_contracts,
    summarize_release_event_fusion_contracts,
)


def test_release_contracts():
    df, summary = build_release_event_fusion_contract_registry()
    assert len(df) == 4
    assert summary["total_contracts"] == 4
    assert summary["non_signal_guaranteed"] is True


def test_release_contracts_list():
    contracts = get_release_event_contracts()
    assert len(contracts) == 4
    assert any(c["contract_name"] == "release_actual_forecast_previous_context_contract" for c in contracts)
