# -*- coding: utf-8 -*-
"""Phase 139 GPU Training Governance Domain Registry Builder."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_training_governance_labels import (
    GPU_TRAINING_GOVERNANCE_DOMAINS,
)


def build_gpu_training_governance_domain_registry(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build domain registry covering all Phase 139 GPU governance sub-domains."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    domain_descriptions = {
        "gpu_training_governance_profile_domain": "Governance profiles for offline GPU training harness",
        "gpu_training_governance_domain": "Root governance domain for Phase 139 ML harness",
        "resource_policy_domain": "GPU/CPU training resource budget and restriction policies",
        "device_selection_policy_domain": "Device preference and fallback rules without allocation",
        "memory_budget_policy_domain": "VRAM memory fraction caps and system reserved memory rules",
        "cpu_fallback_policy_domain": "Deterministic CPU fallback policies when GPU unavailable",
        "timeout_policy_domain": "Training loop execution timeout limits and watchdog rules",
        "batch_size_placeholder_domain": "Batch size placeholder schema for future ML iterations",
        "dataloader_placeholder_domain": "Dataloader placeholder contracts with zero dataset reading",
        "training_loop_stub_contract_domain": "Contracts defining stubbed execution and forbidden methods",
        "harness_interface_domain": "Interface contracts for resource checks, simulations, and validation",
        "harness_stub_domain": "Stub implementation returning blocked execution status and metadata",
        "dry_run_resource_check_domain": "Dry-run verification of compute and hardware constraints",
        "dry_run_device_selection_domain": "Simulated device selector returning safe device metadata",
        "dry_run_memory_guard_domain": "Pre-execution memory allocation guard against OOM",
        "dry_run_timeout_guard_domain": "Timeout guard ensuring no runaway loops occur",
        "dry_run_execution_block_domain": "Static and runtime keyword blocks preventing execution",
        "no_real_training_domain": "Explicit verification that real model training is disabled",
        "no_prediction_domain": "Explicit verification that model prediction/inference is disabled",
        "no_target_label_domain": "Explicit verification that target/label generation is disabled",
        "artifact_disabled_domain": "Explicit verification that model artifact writing is blocked",
        "model_registry_write_disabled_domain": "Explicit verification that registry writing is blocked",
        "dataset_dependency_domain": "Verification of Phase 137 dataset contract dependencies",
        "baseline_model_dependency_domain": "Verification of Phase 138 baseline model contract dependencies",
        "runtime_dependency_domain": "Verification of Phase 136 GPU/ML runtime capabilities",
        "featurestore_input_dependency_domain": "Verification of FeatureStore catalog integration",
        "no_lookahead_guard_domain": "Guard ensuring no future return or lookahead leakage",
        "metadata_only_news_guard_domain": "Guard rejecting raw text, embeddings, and sentiment output",
        "source_preservation_guard_domain": "Guard preventing destructive mutation and file deletion",
        "forbidden_column_policy_domain": "Forbidden column catalog (signals, targets, predictions)",
        "resource_audit_placeholder_domain": "Audit schema capturing simulated resource usage",
        "experiment_audit_placeholder_domain": "Audit schema capturing simulated experiment runs",
        "manual_review_domain": "Manual review items required prior to real execution phases",
        "finding_domain": "Audit findings and governance observations",
        "readiness_score_domain": "Readiness score report for Phase 139 governance layer",
        "manifest_domain": "Comprehensive Phase 139 governance manifest",
        "health_domain": "System health and prerequisite checks",
        "validation_domain": "Validation report verifying all constraints and contracts",
        "safety_domain": "NO-GO and SAFE-GO security boundary definitions",
        "phase_140_handoff_domain": "Handoff prerequisites to Phase 140 candidate model registry",
        "unknown_gpu_training_governance_domain": "Fallback domain for unclassified items",
    }

    rows = []
    for domain in GPU_TRAINING_GOVERNANCE_DOMAINS:
        rows.append(
            {
                "domain_name": domain,
                "description": domain_descriptions.get(domain, "Domain description"),
                "status": "gpu_governance_ready",
                "current_phase": 139,
                "target_final_phase": 160,
                "next_phase": 140,
                "dry_run_only": True,
                "non_signal": True,
                "real_training_allowed": False,
                "active_profile": active_profile.name,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "total_domains": len(df),
        "active_profile": active_profile.name,
        "all_ready": bool((df["status"] == "gpu_governance_ready").all()),
        "all_dry_run": bool((df["dry_run_only"] == True).all()),
        "current_phase": 139,
        "target_final_phase": 160,
        "next_phase": 140,
        "non_signal": True,
    }
    return df, summary


def summarize_gpu_training_governance_domains(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize GPU training governance domains DataFrame."""
    if df.empty:
        return {"total_domains": 0, "non_signal": True}
    return {
        "total_domains": len(df),
        "all_ready": bool((df["status"] == "gpu_governance_ready").all()) if "status" in df.columns else True,
        "non_signal": True,
    }
