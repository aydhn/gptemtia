# -*- coding: utf-8 -*-
"""Unit tests for Phase 139 handoff."""

import pytest
import pandas as pd
from advanced_baseline_ml_models.phase_139_handoff import (
    PHASE_139_PREREQUISITES,
    build_phase_139_gpu_training_harness_resource_governance_handoff_report,
    summarize_phase_139_handoff,
)


def test_build_phase_139_handoff_report():
    df, summary = build_phase_139_gpu_training_harness_resource_governance_handoff_report()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(PHASE_139_PREREQUISITES)
    assert len(df) == 12
    assert summary["source_phase"] == 138
    assert summary["next_phase"] == 139
    assert summary["target_final_phase"] == 160
    assert summary["total_prerequisites"] == 12
    assert summary["all_satisfied"] is True
    assert summary["handoff_status"] == "READY_FOR_PHASE_139"
    assert summary["non_signal"] is True
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
    assert (df["status"].isin(["READY", "ENFORCED"])).all()


def test_summarize_phase_139_handoff_empty():
    empty_df = pd.DataFrame(columns=[
        "prerequisite", "status", "details", "source_phase",
        "next_phase", "target_final_phase", "non_signal",
        "production_ready", "broker_ready"
    ])
    summary = summarize_phase_139_handoff(empty_df)
    assert summary["total_prerequisites"] == 0
    assert summary["all_satisfied"] is True
    assert summary["handoff_status"] == "READY_FOR_PHASE_139"
