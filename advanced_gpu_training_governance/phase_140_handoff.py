# -*- coding: utf-8 -*-
"""Phase 140 Handoff: Ensemble Model Contracts and Candidate Model Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)

PHASE_140_PREREQUISITES: List[Dict[str, str]] = [
    {
        "prerequisite": "gpu_resource_governance_prerequisite",
        "details": "Phase 139 GPU resource policies, memory caps, and timeout guards are established.",
        "status": "READY",
    },
    {
        "prerequisite": "device_selection_and_cpu_fallback_prerequisite",
        "details": "Deterministic device selection and CPU fallback policies are active.",
        "status": "READY",
    },
    {
        "prerequisite": "training_loop_stub_contracts_prerequisite",
        "details": "Harness stub contracts preventing fit/train/backward execution are verified.",
        "status": "READY",
    },
    {
        "prerequisite": "disabled_execution_reports_prerequisite",
        "details": "Zero real training, zero prediction, zero target/label reports are certified.",
        "status": "READY",
    },
    {
        "prerequisite": "baseline_model_contracts_prerequisite",
        "details": "Phase 138 baseline model contracts are accessible for ensemble stacking contracts.",
        "status": "READY",
    },
    {
        "prerequisite": "dataset_contracts_prerequisite",
        "details": "Phase 137 dataset contracts and splitting rules are established.",
        "status": "READY",
    },
    {
        "prerequisite": "resource_audit_placeholders_prerequisite",
        "details": "Structured resource audit schema is prepared for candidate registration logs.",
        "status": "READY",
    },
    {
        "prerequisite": "experiment_audit_placeholders_prerequisite",
        "details": "Simulated experiment audit schema is prepared for ensemble tracking.",
        "status": "READY",
    },
    {
        "prerequisite": "no_lookahead_guards_prerequisite",
        "details": "Temporal leakage guards are enforced across all model inputs.",
        "status": "ENFORCED",
    },
    {
        "prerequisite": "metadata_only_news_guards_prerequisite",
        "details": "Raw news text, embeddings, and sentiment output are strictly excluded.",
        "status": "ENFORCED",
    },
    {
        "prerequisite": "source_preservation_guards_prerequisite",
        "details": "Filesystem and source table preservation guards are active.",
        "status": "ENFORCED",
    },
    {
        "prerequisite": "candidate_registry_boundary_prerequisite",
        "details": "Phase 140 will establish ensemble and candidate model registry contracts with zero live execution.",
        "status": "ENFORCED",
    },
]


def build_phase_140_ensemble_candidate_model_registry_handoff_report(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Phase 140 handoff report DataFrame and summary."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    rows = []
    for item in PHASE_140_PREREQUISITES:
        rows.append(
            {
                "prerequisite": item["prerequisite"],
                "status": item["status"],
                "details": item["details"],
                "source_phase": 139,
                "next_phase": 140,
                "target_final_phase": 160,
                "non_signal": True,
                "production_ready": False,
                "broker_ready": False,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_phase_140_handoff(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_phase_140_handoff(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Phase 140 handoff report DataFrame."""
    if df.empty:
        return {
            "total_prerequisites": 0,
            "all_satisfied": True,
            "handoff_status": "READY_FOR_PHASE_140",
            "non_signal": True,
        }
    all_ready = bool((df["status"].isin(["READY", "ENFORCED"])).all())
    return {
        "source_phase": 139,
        "next_phase": 140,
        "target_final_phase": 160,
        "total_prerequisites": len(df),
        "all_satisfied": all_ready,
        "handoff_status": "READY_FOR_PHASE_140" if all_ready else "BLOCKED",
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
