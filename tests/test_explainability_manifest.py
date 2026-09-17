# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Explainability Manifest."""

import pytest
from advanced_explainability_attribution.explainability_manifest import (
    build_explainability_manifest,
    summarize_explainability_manifest,
)


def test_explainability_manifest():
    manifest = build_explainability_manifest()
    assert manifest.current_phase == 143
    assert manifest.next_phase == 144
    assert manifest.target_final_phase == 160
    assert manifest.non_signal is True
    assert manifest.dry_run is True
    assert manifest.real_training_executed is False
    assert manifest.shap_executed is False
    assert manifest.lime_executed is False
    assert manifest.pdp_executed is False
    assert manifest.ice_executed is False
    assert manifest.surrogate_model_executed is False
    assert manifest.counterfactual_generated is False
    assert manifest.explanation_model_action_generated is False

    summary = summarize_explainability_manifest(manifest)
    assert summary["all_invariants_preserved"] is True
    assert summary["current_phase"] == 143
    assert summary["next_phase"] == 144
