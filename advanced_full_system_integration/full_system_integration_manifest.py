# -*- coding: utf-8 -*-
"""Phase 158: Full-System Integration Master Manifest.

Defines the master manifest encapsulating full system completion and non-production invariants.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import FullSystemIntegrationManifest


def build_full_system_integration_manifest(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build full-system integration manifest DataFrame and summary."""
    manifest = FullSystemIntegrationManifest(
        manifest_id="MNF-158-FULL-SYSTEM-INTEGRATION-001",
        current_phase=158,
        target_final_phase=160,
        next_phase=159,
        full_system_integration_completed=True,
        non_signal=True,
        local_only=True,
        dry_run=True,
        non_production=True,
        research_only=True,
        production_ready=False,
        broker_ready=False,
        live_trading_ready=False,
        official_approval=False,
        system_executed=False,
        end_to_end_run_executed=False,
        live_trading_executed=False,
        broker_execution_executed=False,
        order_generation_executed=False,
        signal_generation_executed=False,
        model_training_executed=False,
        model_predict_executed=False,
        prediction_generated=False,
        target_label_generated=False,
        backtest_executed=False,
        benchmark_executed=False,
        portfolio_executed=False,
        risk_executed=False,
        scenario_executed=False,
        metric_calculated=False,
        optimizer_executed=False,
        artifact_persisted=False,
        model_registry_written=False,
        model_deployed=False,
        production_deployed=False,
        source_preserved=True,
        manual_review_required=True,
        phase_159_handoff_ready=True,
        contains_target_or_prediction=False,
        contains_trading_recommendation=False,
    )

    df = pd.DataFrame([manifest.__dict__])
    summary = {
        "manifest_id": manifest.manifest_id,
        "current_phase": manifest.current_phase,
        "target_final_phase": manifest.target_final_phase,
        "next_phase": manifest.next_phase,
        "full_system_integration_completed": manifest.full_system_integration_completed,
        "production_ready": manifest.production_ready,
        "broker_ready": manifest.broker_ready,
        "live_trading_ready": manifest.live_trading_ready,
        "phase_159_handoff_ready": manifest.phase_159_handoff_ready,
        "status": "full_system_integration_ready",
        "non_signal": True,
    }
    return df, summary
