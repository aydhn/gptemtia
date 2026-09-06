"""Tests for Phase 132 Macro/Event/News Regime Context Contracts."""

from advanced_macro_event_news_regime.macro_event_news_regime_context_contracts import (
    build_macro_event_news_regime_context_contract_registry,
    validate_macro_event_news_context_contract,
    summarize_macro_event_news_context_contracts,
)


def test_build_macro_event_news_context_contracts():
    df, summary = build_macro_event_news_regime_context_contract_registry()
    assert not df.empty
    assert len(df) >= 3
    assert "contract_name" in df.columns
    assert "context_type" in df.columns
    assert summary["all_require_no_lookahead"] is True
    assert summary["all_require_metadata_only"] is True
    assert summary["all_non_signal"] is True


def test_validate_macro_event_news_context_contract():
    valid_contract = {
        "contract_name": "test_contract",
        "context_type": "macro_indicator_context",
        "entity_type": "macro_indicator",
        "timestamp_policy_ref": "policy_backward",
        "asof_policy_ref": "asof_backward",
        "validation_dependency_ref": "val_dep_1",
        "quality_dependency_ref": "qual_dep_1",
        "source_phase_refs": ["Phase 120"],
        "metadata_only_news_required": True,
        "no_lookahead_required": True,
        "non_signal_required": True,
    }
    res_valid = validate_macro_event_news_context_contract(valid_contract)
    assert res_valid["valid"] is True
    assert res_valid["contract_status"] == "PASS"

    invalid_contract = dict(valid_contract)
    invalid_contract["metadata_only_news_required"] = False
    res_invalid = validate_macro_event_news_context_contract(invalid_contract)
    assert res_invalid["valid"] is False


def test_summarize_macro_event_news_context_contracts():
    df, _ = build_macro_event_news_regime_context_contract_registry()
    summary = summarize_macro_event_news_context_contracts(df)
    assert summary["total_contracts"] >= 3
    assert summary["all_no_lookahead"] is True
    assert summary["all_metadata_only"] is True
    assert summary["all_non_signal"] is True
