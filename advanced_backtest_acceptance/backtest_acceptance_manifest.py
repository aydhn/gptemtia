# -*- coding: utf-8 -*-
"""Phase 152: Backtest Acceptance Manifest."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_backtest_acceptance.backtest_acceptance_config import (
    BacktestAcceptanceProfile,
    get_backtest_acceptance_profile,
)
from advanced_backtest_acceptance.backtest_acceptance_labels import (
    MANIFEST_DOMAIN,
    ACCEPTANCE_READY,
)
from advanced_backtest_acceptance.backtest_acceptance_models import (
    BacktestAcceptanceManifest,
)


def build_backtest_acceptance_manifest(
    profile: Optional[BacktestAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the master acceptance manifest for Phase 152."""
    active = profile or get_backtest_acceptance_profile()

    manifest = BacktestAcceptanceManifest(
        manifest_name="backtest_acceptance_manifest",
        manifest_id="MNF-152-001",
        current_phase=active.current_phase,
        target_final_phase=active.target_final_phase,
        next_phase=active.next_phase,
        component_count=7,
        accepted_component_count=7,
        blocker_count=0,
        warning_count=8,
        gap_count=0,
        finding_count=1,
        manual_review_count=7,
        readiness_score=1.0,
        manual_review_required=True,
        backtest_block_completed=True,
        non_signal=True,
        source_preserved=True,
        local_only=True,
        dry_run=True,
        non_production=True,
        research_only=True,
        official_approval=False,
        production_ready=False,
        broker_ready=False,
        live_trading_ready=False,
        production_approved=False,
        broker_ready_approved=False,
        live_trading_approved=False,
        contains_target_or_prediction=False,
        contains_trading_recommendation=False,
        contains_full_article_text=False,
        contains_article_body=False,
        contains_raw_content=False,
        contains_scraped_html=False,
        contains_embedding=False,
        contains_vector=False,
        backtest_executed=False,
        benchmark_executed=False,
        metric_calculated=False,
        result_claim_generated=False,
        performance_claim_generated=False,
        strategy_approved=False,
        capital_allocation_generated=False,
        portfolio_constructed=False,
        position_sizing_generated=False,
        optimizer_executed=False,
        model_training_executed=False,
        model_fit_executed=False,
        model_predict_executed=False,
        model_inference_executed=False,
        prediction_generated=False,
        target_label_generated=False,
        broker_order_sent=False,
        live_order_sent=False,
        artifact_persisted=False,
        model_registry_written=False,
        model_deployed=False,
        production_deployed=False,
        phase_153_handoff_ready=True,
    )

    records = [{
        "manifest_name": manifest.manifest_name,
        "manifest_id": manifest.manifest_id,
        "current_phase": manifest.current_phase,
        "target_final_phase": manifest.target_final_phase,
        "next_phase": manifest.next_phase,
        "component_count": manifest.component_count,
        "accepted_component_count": manifest.accepted_component_count,
        "blocker_count": manifest.blocker_count,
        "warning_count": manifest.warning_count,
        "gap_count": manifest.gap_count,
        "finding_count": manifest.finding_count,
        "manual_review_count": manifest.manual_review_count,
        "readiness_score": manifest.readiness_score,
        "manual_review_required": manifest.manual_review_required,
        "backtest_block_completed": manifest.backtest_block_completed,
        "non_signal": manifest.non_signal,
        "source_preserved": manifest.source_preserved,
        "local_only": manifest.local_only,
        "dry_run": manifest.dry_run,
        "non_production": manifest.non_production,
        "research_only": manifest.research_only,
        "official_approval": manifest.official_approval,
        "production_ready": manifest.production_ready,
        "broker_ready": manifest.broker_ready,
        "live_trading_ready": manifest.live_trading_ready,
        "backtest_executed": manifest.backtest_executed,
        "benchmark_executed": manifest.benchmark_executed,
        "metric_calculated": manifest.metric_calculated,
        "result_claim_generated": manifest.result_claim_generated,
        "performance_claim_generated": manifest.performance_claim_generated,
        "strategy_approved": manifest.strategy_approved,
        "capital_allocation_generated": manifest.capital_allocation_generated,
        "portfolio_constructed": manifest.portfolio_constructed,
        "position_sizing_generated": manifest.position_sizing_generated,
        "optimizer_executed": manifest.optimizer_executed,
        "model_training_executed": manifest.model_training_executed,
        "prediction_generated": manifest.prediction_generated,
        "target_label_generated": manifest.target_label_generated,
        "broker_order_sent": manifest.broker_order_sent,
        "live_order_sent": manifest.live_order_sent,
        "artifact_persisted": manifest.artifact_persisted,
        "model_registry_written": manifest.model_registry_written,
        "model_deployed": manifest.model_deployed,
        "production_deployed": manifest.production_deployed,
        "phase_153_handoff_ready": manifest.phase_153_handoff_ready,
        "status": ACCEPTANCE_READY,
    }]

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": MANIFEST_DOMAIN,
        "active_profile": active.profile_name,
        "manifest_id": manifest.manifest_id,
        "backtest_block_completed": manifest.backtest_block_completed,
        "readiness_score": manifest.readiness_score,
        "phase_153_handoff_ready": manifest.phase_153_handoff_ready,
        "non_signal": True,
        "status": "ACCEPTED",
    }
    return df, summary
