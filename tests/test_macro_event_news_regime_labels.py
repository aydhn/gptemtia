"""Tests for Phase 132 Macro/Event/News Regime Labels."""

from advanced_macro_event_news_regime.macro_event_news_regime_labels import (
    list_macro_event_news_regime_domain_labels,
    list_macro_event_news_status_labels,
    list_macro_event_news_context_labels,
    validate_macro_event_news_regime_domain_label,
    validate_macro_event_news_status_label,
    validate_macro_event_news_context_label,
)


def test_labels_lists_not_empty():
    domains = list_macro_event_news_regime_domain_labels()
    statuses = list_macro_event_news_status_labels()
    contexts = list_macro_event_news_context_labels()

    assert len(domains) >= 35
    assert len(statuses) >= 6
    assert len(contexts) >= 10


def test_domain_label_validation():
    assert validate_macro_event_news_regime_domain_label("macro_entity_domain") is True
    assert validate_macro_event_news_regime_domain_label("event_entity_domain") is True
    assert validate_macro_event_news_regime_domain_label("news_metadata_entity_domain") is True
    assert validate_macro_event_news_regime_domain_label("metadata_only_news_boundary_domain") is True
    assert validate_macro_event_news_regime_domain_label("invalid_domain_xyz") is False


def test_status_label_validation():
    assert validate_macro_event_news_status_label("macro_event_news_context_ready") is True
    assert validate_macro_event_news_status_label("macro_event_news_context_blocked_by_safety") is True
    assert validate_macro_event_news_status_label("invalid_status_abc") is False


def test_context_label_validation():
    assert validate_macro_event_news_context_label("macro_inflation_context") is True
    assert validate_macro_event_news_context_label("calendar_event_context") is True
    assert validate_macro_event_news_context_label("news_topic_context") is True
    assert validate_macro_event_news_context_label("invalid_context_123") is False
