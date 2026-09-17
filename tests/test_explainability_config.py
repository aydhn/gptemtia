# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Explainability Config."""

import pytest
from advanced_explainability_attribution.explainability_config import (
    get_explainability_profile,
    get_strict_explainability_profile,
    get_governance_focus_explainability_profile,
    list_explainability_profiles,
    validate_explainability_profiles,
)


def test_explainability_config_profiles():
    prof = get_explainability_profile()
    assert prof.current_phase == 143
    assert prof.target_final_phase == 160
    assert prof.next_phase == 144
    assert prof.dry_run_default is True
    assert prof.allow_live_trading is False
    assert prof.allow_explainability_calculation is False
    assert prof.allow_shap_execution is False
    assert prof.allow_lime_execution is False

    strict_prof = get_strict_explainability_profile()
    assert strict_prof.profile_name == "strict_non_executing_xai_safety"
    assert strict_prof.min_readiness_score == 0.50

    gov_prof = get_governance_focus_explainability_profile()
    assert gov_prof.profile_name == "dry_run_attribution_report_governance_focus"

    profiles = list_explainability_profiles()
    assert len(profiles) == 3
    assert validate_explainability_profiles() is True
