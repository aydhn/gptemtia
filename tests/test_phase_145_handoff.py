# -*- coding: utf-8 -*-
"""Unit tests for Phase 145 Handoff Specification."""

import pytest
from advanced_model_governance.model_governance_config import get_model_governance_profile
from advanced_model_governance.phase_145_handoff import (
    build_phase_145_advanced_ml_acceptance_handoff_report,
)


def test_phase_145_handoff_report():
    prof = get_model_governance_profile()
    df, summary = build_phase_145_advanced_ml_acceptance_handoff_report(prof)
    assert len(df) >= 7
    assert summary["current_phase"] == 144
    assert summary["next_phase"] == 145
    assert summary["target_final_phase"] == 160
    assert summary["handoff_status"] == "READY_FOR_PHASE_145"
    assert summary["all_satisfied"] is True
    assert summary["live_trading_prohibited"] is True
    assert summary["broker_execution_prohibited"] is True
    assert summary["investment_advice_prohibited"] is True
    assert summary["non_signal"] is True
