# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Ensemble Metadata-Only News Guards."""

from advanced_ensemble_model_registry.ensemble_metadata_only_news_guards import (
    build_ensemble_metadata_only_news_guards,
    validate_ensemble_metadata_only_news_guards,
    summarize_ensemble_metadata_only_news_guards,
)


def test_ensemble_metadata_only_news_guards():
    guards = build_ensemble_metadata_only_news_guards()
    assert len(guards) == 4
    assert "article_body_prohibition_guard" in guards
    assert "embedding_vector_prohibition_guard" in guards
    assert validate_ensemble_metadata_only_news_guards(guards) is True

    summary = summarize_ensemble_metadata_only_news_guards(guards)
    assert summary["total_guards"] == 4
    assert summary["all_guards_enforced"] is True
    assert summary["raw_text_prohibited"] is True
    assert summary["embeddings_prohibited"] is True
