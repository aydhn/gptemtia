"""Tests for Calendar Event Fusion Contracts."""

from advanced_feature_fusion.calendar_event_fusion_contracts import (
    build_calendar_event_fusion_contract_registry,
    get_calendar_event_contracts,
    summarize_calendar_event_fusion_contracts,
)


def test_calendar_contracts():
    df, summary = build_calendar_event_fusion_contract_registry()
    assert len(df) == 4
    assert summary["total_contracts"] == 4
    assert summary["non_signal_guaranteed"] is True


def test_calendar_contracts_list():
    contracts = get_calendar_event_contracts()
    assert len(contracts) == 4
    assert any(c["contract_name"] == "economic_calendar_event_context_contract" for c in contracts)
