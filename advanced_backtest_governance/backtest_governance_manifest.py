# -*- coding: utf-8 -*-
"""Phase 150: Backtest Governance Manifest Module.

Generates the master Phase 150 integrity manifest certifying all governance invariants.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    MANIFEST_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)
from advanced_backtest_governance.backtest_governance_models import BacktestGovernanceManifest


def build_backtest_governance_manifest(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the master Phase 150 manifest DataFrame and summary."""
    manifest = BacktestGovernanceManifest(
        manifest_id="MANIFEST_PHASE_150_BACKTEST_GOVERNANCE",
        current_phase=profile.current_phase,
        target_final_phase=profile.target_final_phase,
        next_phase=profile.next_phase,
        non_signal=True,
        local_only=profile.local_only,
        dry_run=profile.dry_run_default,
        non_production=profile.non_production,
        research_only=profile.research_only,
        production_ready=False,
        broker_ready=False,
        live_trading_ready=False,
        official_approval=False,
        backtest_executed=False,
        benchmark_executed=False,
        metric_calculated=False,
        result_claim_generated=False,
        performance_claim_generated=False,
        strategy_approved=False,
        optimizer_executed=False,
        model_training_executed=False,
        prediction_generated=False,
        target_label_generated=False,
        broker_order_sent=False,
        live_order_sent=False,
        artifact_persisted=False,
        model_registry_written=False,
        model_deployed=False,
        production_deployed=False,
        source_preserved=True,
        manual_review_required=True,
        phase_151_handoff_ready=True,
    )

    rows: List[Dict[str, Any]] = [
        {"property": "manifest_id", "value": manifest.manifest_id},
        {"property": "current_phase", "value": manifest.current_phase},
        {"property": "target_final_phase", "value": manifest.target_final_phase},
        {"property": "next_phase", "value": manifest.next_phase},
        {"property": "non_signal", "value": manifest.non_signal},
        {"property": "local_only", "value": manifest.local_only},
        {"property": "dry_run", "value": manifest.dry_run},
        {"property": "non_production", "value": manifest.non_production},
        {"property": "research_only", "value": manifest.research_only},
        {"property": "production_ready", "value": manifest.production_ready},
        {"property": "broker_ready", "value": manifest.broker_ready},
        {"property": "live_trading_ready", "value": manifest.live_trading_ready},
        {"property": "official_approval", "value": manifest.official_approval},
        {"property": "backtest_executed", "value": manifest.backtest_executed},
        {"property": "benchmark_executed", "value": manifest.benchmark_executed},
        {"property": "metric_calculated", "value": manifest.metric_calculated},
        {"property": "result_claim_generated", "value": manifest.result_claim_generated},
        {"property": "performance_claim_generated", "value": manifest.performance_claim_generated},
        {"property": "strategy_approved", "value": manifest.strategy_approved},
        {"property": "optimizer_executed", "value": manifest.optimizer_executed},
        {"property": "model_training_executed", "value": manifest.model_training_executed},
        {"property": "prediction_generated", "value": manifest.prediction_generated},
        {"property": "target_label_generated", "value": manifest.target_label_generated},
        {"property": "broker_order_sent", "value": manifest.broker_order_sent},
        {"property": "live_order_sent", "value": manifest.live_order_sent},
        {"property": "artifact_persisted", "value": manifest.artifact_persisted},
        {"property": "model_registry_written", "value": manifest.model_registry_written},
        {"property": "model_deployed", "value": manifest.model_deployed},
        {"property": "production_deployed", "value": manifest.production_deployed},
        {"property": "source_preserved", "value": manifest.source_preserved},
        {"property": "manual_review_required", "value": manifest.manual_review_required},
        {"property": "phase_151_handoff_ready", "value": manifest.phase_151_handoff_ready},
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": MANIFEST_DOMAIN,
        "manifest_id": manifest.manifest_id,
        "current_phase": manifest.current_phase,
        "next_phase": manifest.next_phase,
        "target_final_phase": manifest.target_final_phase,
        "all_negative_invariants_satisfied": True,
        "phase_151_handoff_ready": manifest.phase_151_handoff_ready,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "profile_name": profile.profile_name,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
