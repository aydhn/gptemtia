# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Ensemble No-Lookahead Guards."""

from advanced_ensemble_model_registry.ensemble_no_lookahead_guards import (
    build_ensemble_no_lookahead_guards,
    validate_ensemble_no_lookahead_guards,
    summarize_ensemble_no_lookahead_guards,
)


def test_ensemble_no_lookahead_guards():
    guards = build_ensemble_no_lookahead_guards()
    assert len(guards) == 4
    assert "candidate_input_temporal_guard" in guards
    assert "ensemble_weight_temporal_guard" in guards
    assert validate_ensemble_no_lookahead_guards(guards) is True

    summary = summarize_ensemble_no_lookahead_guards(guards)
    assert summary["total_guards"] == 4
    assert summary["all_guards_enforced"] is True
    assert summary["zero_leakage_guaranteed"] is True
