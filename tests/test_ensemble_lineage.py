# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Ensemble Lineage."""

from advanced_ensemble_model_registry.ensemble_lineage import (
    build_ensemble_lineage,
    validate_ensemble_lineage,
    summarize_ensemble_lineage,
)


def test_ensemble_lineage():
    lineage = build_ensemble_lineage()
    assert lineage["phase"] == 140
    assert lineage["next_phase"] == 141
    assert len(lineage["stages"]) == 6
    assert validate_ensemble_lineage(lineage) is True

    summary = summarize_ensemble_lineage(lineage)
    assert summary["total_stages"] == 6
    assert summary["is_valid"] is True
    assert summary["non_signal"] is True
