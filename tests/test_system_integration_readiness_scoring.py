# -*- coding: utf-8 -*-
"""Unit tests for Phase 158 Readiness Scoring."""

import pytest
import pandas as pd
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.system_integration_readiness_scoring import (
    classify_system_integration_readiness_score,
    calculate_system_integration_readiness_score,
    build_system_integration_readiness_score_report,
)


def test_classify_score():
    assert classify_system_integration_readiness_score(0.10) == "blocked"
    assert classify_system_integration_readiness_score(0.40) == "incomplete"
    assert classify_system_integration_readiness_score(0.60) == "integration_contract_ready_with_manual_review"
    assert classify_system_integration_readiness_score(0.90) == "full_system_integration_contract_ready_non_production"


def test_readiness_scoring_report():
    profile = get_default_full_system_integration_profile()
    df, summary = build_system_integration_readiness_score_report(profile)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
    assert "overall_score" in df.columns
    assert "meets_threshold" in df.columns

    assert summary["active_profile"] == profile.profile_name
    assert summary["readiness_score"] >= profile.min_readiness_score
    assert summary["meets_threshold"] is True
    assert summary["blocker_count"] == 0
    assert summary["non_signal"] is True
