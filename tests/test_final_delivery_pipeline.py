# -*- coding: utf-8 -*-
"""Unit tests for Phase 160 Pipeline."""

from advanced_final_delivery.final_delivery_pipeline import FinalDeliveryPipeline


def test_final_delivery_pipeline_dry_run():
    pipeline = FinalDeliveryPipeline()
    df_status, summary = pipeline.build_final_delivery_status(save=False)
    assert not df_status.empty
    assert summary["current_phase"] == 160
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] is None
    assert summary["phase_160_completed"] is True
    assert summary["final_plan_closed"] is True
    assert summary["full_advanced_bot_final_delivery_completed"] is True
    assert summary["all_subsystems_ready"] is True
