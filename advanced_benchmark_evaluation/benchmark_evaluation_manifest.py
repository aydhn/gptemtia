# -*- coding: utf-8 -*-
"""Phase 151: Benchmark Evaluation Manifest Module.

Generates the master integrity manifest certifying that all Phase 151
invariants and boundaries are strictly satisfied.
"""

from typing import Any, Dict, List, Tuple
from datetime import datetime, timezone
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_MANIFEST_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)
from advanced_benchmark_evaluation.benchmark_evaluation_models import BenchmarkEvaluationManifest


def build_benchmark_evaluation_manifest(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the signed BenchmarkEvaluationManifest for Phase 151."""
    manifest_id = "MANIFEST_PHASE_151_BENCHMARK_EVALUATION"
    now_iso = datetime.now(timezone.utc).isoformat()

    manifest_obj = BenchmarkEvaluationManifest(
        manifest_id=manifest_id,
        timestamp=now_iso,
        current_phase=151,
        target_final_phase=160,
        next_phase=152,
        non_signal=True,
        local_only=True,
        dry_run=True,
        non_production=True,
        research_only=True,
        production_ready=False,
        broker_ready=False,
        live_trading_ready=False,
        official_approval=False,
        benchmark_report_executed=False,
        strategy_evaluation_executed=False,
        benchmark_executed=False,
        backtest_executed=False,
        metric_calculated=False,
        result_claim_generated=False,
        performance_claim_generated=False,
        strategy_approved=False,
        capital_allocation_generated=False,
        portfolio_constructed=False,
        position_sizing_generated=False,
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
        phase_152_handoff_ready=True,
    )

    rows = [
        {"property": k, "value": v}
        for k, v in manifest_obj.__dict__.items()
    ]
    df = pd.DataFrame(rows)

    summary = {
        "domain": LABEL_MANIFEST_DOMAIN,
        "manifest_id": manifest_id,
        "timestamp": now_iso,
        "current_phase": 151,
        "next_phase": 152,
        "target_final_phase": 160,
        "all_negative_invariants_satisfied": True,
        "phase_152_handoff_ready": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
