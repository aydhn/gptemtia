# -*- coding: utf-8 -*-
"""Phase 159: Release Candidate Manifest.

Builds the comprehensive Release Candidate Manifest formalizing phase completion,
non-execution guarantees, and Phase 160 handoff readiness.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    MANIFEST_DOMAIN,
    RELEASE_CANDIDATE_CONTRACT_READY,
)
from advanced_final_hardening.final_hardening_models import ReleaseCandidateManifest


def build_release_candidate_manifest(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build the release candidate manifest DataFrame and summary dictionary."""
    active_profile = profile or get_default_final_hardening_profile()

    manifest = ReleaseCandidateManifest(
        manifest_id="MNF-159-RELEASE-CANDIDATE-001",
        current_phase=active_profile.current_phase,
        target_final_phase=active_profile.target_final_phase,
        next_phase=active_profile.next_phase,
        final_hardening_completed=True,
        release_candidate_contract_ready=True,
        operator_runbook_contract_ready=True,
        domain=MANIFEST_DOMAIN,
        non_signal=True,
        local_only=True,
        dry_run=True,
        non_production=True,
        research_only=True,
        production_ready=False,
        broker_ready=False,
        live_trading_ready=False,
        official_approval=False,
        contains_target_or_prediction=False,
        contains_trading_recommendation=False,
        system_executed=False,
        end_to_end_run_executed=False,
        release_deployed=False,
        production_deployed=False,
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
        source_preserved=True,
        source_overwritten=False,
        destructive_action_executed=False,
        manual_review_required=True,
        phase_160_handoff_ready=True,
        status=RELEASE_CANDIDATE_CONTRACT_READY,
    )

    manifest_dict = manifest.__dict__.copy()
    df = pd.DataFrame([manifest_dict])

    summary = {
        "manifest_id": manifest.manifest_id,
        "current_phase": manifest.current_phase,
        "target_final_phase": manifest.target_final_phase,
        "next_phase": manifest.next_phase,
        "final_hardening_completed": manifest.final_hardening_completed,
        "release_candidate_contract_ready": manifest.release_candidate_contract_ready,
        "operator_runbook_contract_ready": manifest.operator_runbook_contract_ready,
        "production_ready": manifest.production_ready,
        "broker_ready": manifest.broker_ready,
        "live_trading_ready": manifest.live_trading_ready,
        "system_executed": manifest.system_executed,
        "phase_160_handoff_ready": manifest.phase_160_handoff_ready,
        "status": RELEASE_CANDIDATE_CONTRACT_READY,
    }
    return df, summary
