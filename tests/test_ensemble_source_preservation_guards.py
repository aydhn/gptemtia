# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Ensemble Source Preservation Guards."""

from advanced_ensemble_model_registry.ensemble_source_preservation_guards import (
    build_ensemble_source_preservation_guards,
    validate_ensemble_source_preservation_guards,
    summarize_ensemble_source_preservation_guards,
)


def test_ensemble_source_preservation_guards():
    guards = build_ensemble_source_preservation_guards()
    assert len(guards) == 3
    assert "source_immutability_guard" in guards
    assert validate_ensemble_source_preservation_guards(guards) is True

    summary = summarize_ensemble_source_preservation_guards(guards)
    assert summary["total_guards"] == 3
    assert summary["all_guards_enforced"] is True
    assert summary["raw_sources_preserved"] is True
    assert summary["destructive_mutations_blocked"] is True
