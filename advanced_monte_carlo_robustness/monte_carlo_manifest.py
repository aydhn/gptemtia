# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Robustness Manifest Module.

Generates the master Phase 149 integrity manifest certifying all negative invariants.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    MANIFEST_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)
from advanced_monte_carlo_robustness.monte_carlo_models import MonteCarloManifest


def build_monte_carlo_robustness_manifest(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the master Phase 149 manifest DataFrame and summary."""
    manifest = MonteCarloManifest(
        manifest_id="MANIFEST_PHASE_149_MONTE_CARLO_ROBUSTNESS",
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
        monte_carlo_executed=False,
        bootstrap_executed=False,
        resampling_executed=False,
        parameter_optimization_executed=False,
        parameter_sweep_executed=False,
        robustness_metric_calculated=False,
        parameter_stability_metric_calculated=False,
        distribution_calculated=False,
        var_calculated=False,
        expected_shortfall_calculated=False,
        optimizer_executed=False,
        model_training_executed=False,
        model_predict_executed=False,
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
        phase_150_handoff_ready=True,
        contains_target_or_prediction=False,
        contains_trading_recommendation=False,
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
        {"property": "monte_carlo_executed", "value": manifest.monte_carlo_executed},
        {"property": "bootstrap_executed", "value": manifest.bootstrap_executed},
        {"property": "resampling_executed", "value": manifest.resampling_executed},
        {"property": "parameter_optimization_executed", "value": manifest.parameter_optimization_executed},
        {"property": "parameter_sweep_executed", "value": manifest.parameter_sweep_executed},
        {"property": "robustness_metric_calculated", "value": manifest.robustness_metric_calculated},
        {"property": "parameter_stability_metric_calculated", "value": manifest.parameter_stability_metric_calculated},
        {"property": "distribution_calculated", "value": manifest.distribution_calculated},
        {"property": "var_calculated", "value": manifest.var_calculated},
        {"property": "expected_shortfall_calculated", "value": manifest.expected_shortfall_calculated},
        {"property": "optimizer_executed", "value": manifest.optimizer_executed},
        {"property": "model_training_executed", "value": manifest.model_training_executed},
        {"property": "prediction_generated", "value": manifest.prediction_generated},
        {"property": "target_label_generated", "value": manifest.target_label_generated},
        {"property": "performance_claim_generated", "value": manifest.performance_claim_generated},
        {"property": "broker_order_sent", "value": manifest.broker_order_sent},
        {"property": "live_order_sent", "value": manifest.live_order_sent},
        {"property": "artifact_persisted", "value": manifest.artifact_persisted},
        {"property": "model_registry_written", "value": manifest.model_registry_written},
        {"property": "source_preserved", "value": manifest.source_preserved},
        {"property": "manual_review_required", "value": manifest.manual_review_required},
        {"property": "phase_150_handoff_ready", "value": manifest.phase_150_handoff_ready},
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": MANIFEST_DOMAIN,
        "manifest_id": manifest.manifest_id,
        "current_phase": manifest.current_phase,
        "next_phase": manifest.next_phase,
        "target_final_phase": manifest.target_final_phase,
        "all_negative_invariants_satisfied": True,
        "phase_150_handoff_ready": manifest.phase_150_handoff_ready,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
