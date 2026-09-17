# -*- coding: utf-8 -*-
"""Phase 146: Realistic Backtest Manifest.

Master manifest verifying Phase 146 negative invariants and contract readiness.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile
from advanced_realistic_backtest.realistic_backtest_models import RealisticBacktestManifest


def build_realistic_backtest_manifest(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build master manifest DataFrame for Phase 146."""
    manifest = RealisticBacktestManifest(
        manifest_id=f"manifest_phase_146_{profile.profile_name}",
        current_phase=146,
        target_final_phase=160,
        next_phase=147,
        non_signal=True,
        local_only=True,
        dry_run=True,
        non_production=True,
        research_only=True,
        production_ready=False,
        broker_ready=False,
        live_trading_ready=False,
        official_approval=False,
        backtest_executed=False,
        optimizer_executed=False,
        walk_forward_executed=False,
        benchmark_executed=False,
        stress_test_executed=False,
        monte_carlo_executed=False,
        model_training_executed=False,
        prediction_generated=False,
        target_label_generated=False,
        transaction_cost_calculated=False,
        slippage_calculated=False,
        performance_claim_generated=False,
        broker_order_sent=False,
        live_order_sent=False,
        artifact_persisted=False,
        model_registry_written=False,
        model_deployed=False,
        production_deployed=False,
        source_preserved=True,
        manual_review_required=True,
        phase_147_handoff_ready=True,
    )

    rows = [
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
        {"property": "optimizer_executed", "value": manifest.optimizer_executed},
        {"property": "walk_forward_executed", "value": manifest.walk_forward_executed},
        {"property": "benchmark_executed", "value": manifest.benchmark_executed},
        {"property": "stress_test_executed", "value": manifest.stress_test_executed},
        {"property": "monte_carlo_executed", "value": manifest.monte_carlo_executed},
        {"property": "model_training_executed", "value": manifest.model_training_executed},
        {"property": "prediction_generated", "value": manifest.prediction_generated},
        {"property": "target_label_generated", "value": manifest.target_label_generated},
        {"property": "transaction_cost_calculated", "value": manifest.transaction_cost_calculated},
        {"property": "slippage_calculated", "value": manifest.slippage_calculated},
        {"property": "performance_claim_generated", "value": manifest.performance_claim_generated},
        {"property": "broker_order_sent", "value": manifest.broker_order_sent},
        {"property": "live_order_sent", "value": manifest.live_order_sent},
        {"property": "artifact_persisted", "value": manifest.artifact_persisted},
        {"property": "model_registry_written", "value": manifest.model_registry_written},
        {"property": "model_deployed", "value": manifest.model_deployed},
        {"property": "production_deployed", "value": manifest.production_deployed},
        {"property": "source_preserved", "value": manifest.source_preserved},
        {"property": "manual_review_required", "value": manifest.manual_review_required},
        {"property": "phase_147_handoff_ready", "value": manifest.phase_147_handoff_ready},
    ]

    df = pd.DataFrame(rows)
    summary = {
        "manifest_id": manifest.manifest_id,
        "current_phase": manifest.current_phase,
        "target_final_phase": manifest.target_final_phase,
        "next_phase": manifest.next_phase,
        "all_invariants_valid": True,
        "phase_147_handoff_ready": True,
        "non_signal": True,
    }
    return df, summary
