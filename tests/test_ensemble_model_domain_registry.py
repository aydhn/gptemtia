# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Ensemble Model Domain Registry."""

from advanced_ensemble_model_registry.ensemble_model_domain_registry import (
    build_ensemble_model_domain_registry,
    validate_ensemble_model_domain_registry,
    summarize_ensemble_model_domains,
)


def test_build_ensemble_model_domain_registry():
    df, summary = build_ensemble_model_domain_registry()
    assert not df.empty
    assert len(df) == 47
    assert summary["total_domains"] == 47
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True
    assert summary["execution_blocked"] is True


def test_validate_ensemble_model_domain_registry():
    df, summary = build_ensemble_model_domain_registry()
    assert validate_ensemble_model_domain_registry(df, summary) is True
