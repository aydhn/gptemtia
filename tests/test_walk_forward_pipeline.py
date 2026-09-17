# -*- coding: utf-8 -*-
"""Unit tests for Phase 147: Walk-Forward Validation Pipeline."""

from advanced_walk_forward_validation.walk_forward_pipeline import (
    WalkForwardValidationPipeline,
)


def test_pipeline_execution():
    pipeline = WalkForwardValidationPipeline()
    status_df, summary = pipeline.build_walk_forward_status(save=False)
    assert not status_df.empty
    assert len(status_df) >= 8
    assert summary["phase"] == 147
    assert summary["next_phase"] == 148
    assert summary["target_final_phase"] == 160
    assert summary["readiness_score"] >= 0.80
    assert summary["validation_status"] == "PASS"
    assert summary["health_status"] == "HEALTHY"
    assert summary["safety_status"] == "SECURE"
    assert summary["phase_148_handoff_ready"] is True
    assert summary["live_trading"] is False
    assert summary["broker_execution"] is False
    assert summary["walk_forward_executed"] is False
    assert summary["benchmark_executed"] is False
    assert summary["metric_calculated"] is False
    assert summary["non_signal"] is True
