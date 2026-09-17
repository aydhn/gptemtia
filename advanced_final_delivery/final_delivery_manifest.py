# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Manifest.

Builds and summarizes the master manifest declaring the official completion of Phase 160
and the closure of the 160-phase plan under strict local/offline research constraints.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_MANIFEST_DOMAIN,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)
from advanced_final_delivery.final_delivery_models import FinalDeliveryManifest


def build_final_delivery_manifest(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build the master final delivery manifest DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    m = FinalDeliveryManifest(
        current_phase=active_profile.current_phase,
        target_final_phase=active_profile.target_final_phase,
        next_phase=active_profile.next_phase,
    )

    rows = [{
        "manifest_id": m.manifest_id,
        "current_phase": m.current_phase,
        "target_final_phase": m.target_final_phase,
        "next_phase": m.next_phase,
        "phase_160_completed": m.phase_160_completed,
        "full_advanced_bot_final_delivery_completed": m.full_advanced_bot_final_delivery_completed,
        "final_delivery_contract_ready": m.final_delivery_contract_ready,
        "final_manifest_ready": m.final_manifest_ready,
        "final_operator_handover_ready": m.final_operator_handover_ready,
        "final_safety_summary_ready": m.final_safety_summary_ready,
        "final_manual_review_summary_ready": m.final_manual_review_summary_ready,
        "non_signal": m.non_signal,
        "local_only": m.local_only,
        "dry_run": m.dry_run,
        "non_production": m.non_production,
        "research_only": m.research_only,
        "production_ready": m.production_ready,
        "broker_ready": m.broker_ready,
        "live_trading_ready": m.live_trading_ready,
        "official_approval": m.official_approval,
        "system_executed": m.system_executed,
        "end_to_end_run_executed": m.end_to_end_run_executed,
        "release_deployed": m.release_deployed,
        "production_deployed": m.production_deployed,
        "live_trading_executed": m.live_trading_executed,
        "broker_execution_executed": m.broker_execution_executed,
        "order_generation_executed": m.order_generation_executed,
        "signal_generation_executed": m.signal_generation_executed,
        "model_training_executed": m.model_training_executed,
        "prediction_generated": m.prediction_generated,
        "target_label_generated": m.target_label_generated,
        "backtest_executed": m.backtest_executed,
        "benchmark_executed": m.benchmark_executed,
        "portfolio_executed": m.portfolio_executed,
        "risk_executed": m.risk_executed,
        "scenario_executed": m.scenario_executed,
        "metric_calculated": m.metric_calculated,
        "optimizer_executed": m.optimizer_executed,
        "artifact_persisted": m.artifact_persisted,
        "model_registry_written": m.model_registry_written,
        "model_deployed": m.model_deployed,
        "source_preserved": m.source_preserved,
        "destructive_action_executed": m.destructive_action_executed,
        "manual_review_required": m.manual_review_required,
        "final_plan_closed": m.final_plan_closed,
        "domain": FINAL_MANIFEST_DOMAIN,
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }]

    df = pd.DataFrame(rows)
    summary = {
        "manifest_id": m.manifest_id,
        "active_profile": active_profile.profile_name,
        "current_phase": m.current_phase,
        "target_final_phase": m.target_final_phase,
        "next_phase": m.next_phase,
        "phase_160_completed": m.phase_160_completed,
        "full_advanced_bot_final_delivery_completed": m.full_advanced_bot_final_delivery_completed,
        "final_delivery_contract_ready": m.final_delivery_contract_ready,
        "final_manifest_ready": m.final_manifest_ready,
        "final_operator_handover_ready": m.final_operator_handover_ready,
        "final_safety_summary_ready": m.final_safety_summary_ready,
        "final_manual_review_summary_ready": m.final_manual_review_summary_ready,
        "final_plan_closed": m.final_plan_closed,
        "production_ready": False,
        "broker_ready": False,
        "live_trading_ready": False,
        "official_approval": False,
        "system_executed": False,
        "release_deployed": False,
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
