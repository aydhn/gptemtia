# -*- coding: utf-8 -*-
"""Unit tests for Phase 145: Advanced ML Acceptance Models."""

import pytest
from advanced_ml_acceptance.advanced_ml_acceptance_models import (
    AdvancedMlAcceptanceProfileItem,
    AdvancedMlComponentItem,
    AdvancedMlAcceptanceCheckpoint,
    AdvancedMlReadinessScore,
    AdvancedMlAcceptanceManifest,
)


def test_models_instantiation():
    p = AdvancedMlAcceptanceProfileItem(profile_name="test_p", description="test desc")
    assert p.current_phase == 145
    assert p.target_final_phase == 160
    assert p.next_phase == 146
    assert p.production_ready is False

    c = AdvancedMlComponentItem(
        component_id="CMP-01",
        component_name="comp1",
        phase_ref="Phase 136",
        primary_module="mod1",
        description="desc1",
    )
    assert c.contract_only is True
    assert c.non_production is True
    assert c.production_ready is False

    chk = AdvancedMlAcceptanceCheckpoint(
        checkpoint_id="CHK-01",
        component_name="comp1",
        expected_module="mod1",
        expected_scripts=["s1.py"],
        expected_tests=["t1.py"],
        expected_manifest="m.json",
        expected_validation_report="v.json",
        expected_safety_boundary="s.json",
        expected_handoff="h.py",
    )
    assert chk.production_ready is False
    assert chk.broker_ready is False

    score = AdvancedMlReadinessScore(
        score=0.85,
        classification="advanced_ml_contract_acceptance_ready_non_production",
        meets_threshold=True,
    )
    assert score.score == 0.85
    assert score.production_ready is False

    with pytest.raises(ValueError):
        AdvancedMlReadinessScore(score=1.5, classification="invalid", meets_threshold=True)

    with pytest.raises(ValueError):
        AdvancedMlReadinessScore(score=-0.1, classification="invalid", meets_threshold=True)
