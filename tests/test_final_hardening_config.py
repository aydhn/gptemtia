# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Final Hardening Configuration."""

import pytest
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_final_hardening_profile,
    get_default_final_hardening_profile,
    list_final_hardening_profiles,
    validate_final_hardening_profiles,
    FINAL_HARDENING_PROFILES,
)


def test_default_profile():
    profile = get_default_final_hardening_profile()
    assert profile.profile_name == "balanced_local_final_hardening_contracts"
    assert profile.current_phase == 159
    assert profile.target_final_phase == 160
    assert profile.next_phase == 160
    assert profile.dry_run_default is True
    assert profile.local_only is True
    assert profile.non_production is True
    assert profile.research_only is True
    assert profile.allow_live_trading is False
    assert profile.allow_broker_integration is False
    assert profile.allow_signal_generation is False
    assert profile.allow_order_generation is False
    assert profile.allow_production_deployment is False
    assert profile.allow_model_training is False
    assert profile.allow_model_predict is False
    assert profile.allow_backtest_execution is False
    assert profile.allow_investment_advice is False
    assert profile.allow_web_scraping is False
    assert profile.allow_credential_output is False
    assert profile.allow_source_overwrite is False
    assert profile.allow_model_registry_write is False
    assert profile.allow_artifact_persistence is False


def test_list_and_get_profile():
    profiles = list_final_hardening_profiles()
    assert len(profiles) >= 3
    p = get_final_hardening_profile("strict_non_production_hardening_safety")
    assert p.profile_name == "strict_non_production_hardening_safety"

    with pytest.raises(KeyError):
        get_final_hardening_profile("non_existent_profile_phase_159")


def test_validate_profiles():
    assert validate_final_hardening_profiles() is True
