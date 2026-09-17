# -*- coding: utf-8 -*-
"""Unit tests for Phase 158 to Phase 159 Handoff."""

import pytest
import pandas as pd
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.phase_159_handoff import (
    build_phase_159_final_hardening_operator_runbook_release_candidate_handoff_report,
    summarize_phase_159_handoff,
)


def test_phase_159_handoff():
    profile = get_default_full_system_integration_profile()
    df, summary = build_phase_159_final_hardening_operator_runbook_release_candidate_handoff_report(profile)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 12
    assert "prerequisite_id" in df.columns
    assert "prerequisite_item" in df.columns
    assert "is_satisfied" in df.columns

    assert summary["current_phase"] == 158
    assert summary["next_phase"] == 159
    assert summary["target_final_phase"] == 160
    assert summary["total_prerequisites"] == 12
    assert summary["satisfied_prerequisites"] == 12
    assert summary["all_satisfied"] is True
    assert summary["handoff_ready"] is True
    assert summary["status"] == "ACCEPTED"
    assert summary["non_signal"] is True
