# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Stress Testing Pipeline."""

from advanced_stress_testing.stress_testing_pipeline import (
    StressTestingPipeline,
)


def test_pipeline_dry_run():
    pipeline = StressTestingPipeline()
    status_df, summary = pipeline.build_stress_testing_status(save=False)
    assert not status_df.empty
    assert len(status_df) >= 8
    assert summary["current_phase"] == 148
    assert summary["next_phase"] == 149
    assert summary["target_final_phase"] == 160
    assert summary["all_components_ready"] is True
    assert summary["non_signal"] is True
