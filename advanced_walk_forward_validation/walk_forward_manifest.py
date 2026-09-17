# -*- coding: utf-8 -*-
"""Phase 147: Walk-Forward Validation Manifest.

Master manifest compiling all metadata, negative invariants, and boundaries for Phase 147.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile
from advanced_walk_forward_validation.walk_forward_models import WalkForwardValidationManifest


def build_walk_forward_validation_manifest(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for the master walk-forward manifest."""
    manifest = WalkForwardValidationManifest(
        manifest_id=f"manifest_phase_147_{profile.profile_name}",
        current_phase=147,
        target_final_phase=160,
        next_phase=148,
        non_signal=True,
        local_only=True,
        dry_run=True,
        non_production=True,
        research_only=True,
        production_ready=False,
        broker_ready=False,
        live_trading_ready=False,
        official_approval=False,
        walk_forward_executed=False,
        oos_benchmark_executed=False,
        benchmark_metric_calculated=False,
        validation_metric_calculated=False,
        optimizer_executed=False,
        stress_test_executed=False,
        monte_carlo_executed=False,
        model_training_executed=False,
        prediction_generated=False,
        target_label_generated=False,
        performance_claim_generated=False,
        broker_order_sent=False,
        live_order_sent=False,
        artifact_persisted=False,
        model_registry_written=False,
        model_deployed=False,
        production_deployed=False,
        source_preserved=True,
        manual_review_required=True,
        phase_148_handoff_ready=True,
    )

    rows = [
        {
            "manifest_id": manifest.manifest_id,
            "current_phase": manifest.current_phase,
            "target_final_phase": manifest.target_final_phase,
            "next_phase": manifest.next_phase,
            "non_signal": manifest.non_signal,
            "local_only": manifest.local_only,
            "dry_run": manifest.dry_run,
            "non_production": manifest.non_production,
            "research_only": manifest.research_only,
            "production_ready": manifest.production_ready,
            "broker_ready": manifest.broker_ready,
            "live_trading_ready": manifest.live_trading_ready,
            "official_approval": manifest.official_approval,
            "walk_forward_executed": manifest.walk_forward_executed,
            "oos_benchmark_executed": manifest.oos_benchmark_executed,
            "benchmark_metric_calculated": manifest.benchmark_metric_calculated,
            "validation_metric_calculated": manifest.validation_metric_calculated,
            "optimizer_executed": manifest.optimizer_executed,
            "stress_test_executed": manifest.stress_test_executed,
            "monte_carlo_executed": manifest.monte_carlo_executed,
            "model_training_executed": manifest.model_training_executed,
            "prediction_generated": manifest.prediction_generated,
            "target_label_generated": manifest.target_label_generated,
            "performance_claim_generated": manifest.performance_claim_generated,
            "broker_order_sent": manifest.broker_order_sent,
            "live_order_sent": manifest.live_order_sent,
            "artifact_persisted": manifest.artifact_persisted,
            "model_registry_written": manifest.model_registry_written,
            "model_deployed": manifest.model_deployed,
            "production_deployed": manifest.production_deployed,
            "source_preserved": manifest.source_preserved,
            "manual_review_required": manifest.manual_review_required,
            "phase_148_handoff_ready": manifest.phase_148_handoff_ready,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "manifest_id": manifest.manifest_id,
        "current_phase": manifest.current_phase,
        "target_final_phase": manifest.target_final_phase,
        "next_phase": manifest.next_phase,
        "walk_forward_executed": False,
        "oos_benchmark_executed": False,
        "benchmark_metric_calculated": False,
        "validation_metric_calculated": False,
        "live_trading_ready": False,
        "broker_ready": False,
        "production_ready": False,
        "phase_148_handoff_ready": True,
        "non_signal": True,
    }
    return df, summary


# Backward compatibility alias
build_walk_forward_manifest = build_walk_forward_validation_manifest
