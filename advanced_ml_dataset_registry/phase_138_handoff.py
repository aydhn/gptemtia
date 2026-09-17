# -*- coding: utf-8 -*-
"""
Phase 137 - Advanced ML Dataset Contracts and Experiment Registry
Phase 138 Handoff Specification.

Outlines all contract, split, guard, and experiment prerequisites delivered
to Phase 138 (Baseline ML Model Contracts and Dry-Run Training Harness).
"""

from typing import Dict, List, Optional, Tuple
import pandas as pd

from advanced_ml_dataset_registry.advanced_ml_dataset_config import (
    AdvancedMlDatasetProfile,
    get_default_advanced_ml_dataset_profile,
)

HANDOFF_PREREQUISITES = [
    {
        "prerequisite_key": "dataset_contracts_established",
        "category": "contract_layer",
        "description": "All 9 ML dataset contracts established with source references and schema requirements",
        "status": "SATISFIED",
        "is_ready": True,
        "non_signal": True,
    },
    {
        "prerequisite_key": "feature_snapshot_contracts_established",
        "category": "contract_layer",
        "description": "Feature snapshot contracts prepared with strict unmaterialized invariant",
        "status": "SATISFIED",
        "is_ready": True,
        "non_signal": True,
    },
    {
        "prerequisite_key": "experiment_registry_metadata_ready",
        "category": "governance_layer",
        "description": "Experiment registry, templates, permissions, and run-plan placeholders defined",
        "status": "SATISFIED",
        "is_ready": True,
        "non_signal": True,
    },
    {
        "prerequisite_key": "time_series_split_policies_defined",
        "category": "split_layer",
        "description": "Chronological, expanding, rolling, and purged split placeholders established without execution",
        "status": "SATISFIED",
        "is_ready": True,
        "non_signal": True,
    },
    {
        "prerequisite_key": "leakage_no_lookahead_guards_enforced",
        "category": "safety_layer",
        "description": "Data leakage and no-lookahead guards active, blocking shift(-1) and future joins",
        "status": "SATISFIED",
        "is_ready": True,
        "non_signal": True,
    },
    {
        "prerequisite_key": "metadata_only_news_guards_enforced",
        "category": "safety_layer",
        "description": "Metadata-only news guards enforced, strictly blocking full text and raw HTML",
        "status": "SATISFIED",
        "is_ready": True,
        "non_signal": True,
    },
    {
        "prerequisite_key": "source_preservation_guards_enforced",
        "category": "safety_layer",
        "description": "Immutability verified; no file deletion, overwrite, or destructive cleaning permitted",
        "status": "SATISFIED",
        "is_ready": True,
        "non_signal": True,
    },
    {
        "prerequisite_key": "target_label_governance_established",
        "category": "governance_layer",
        "description": "Target/label disabled contracts verified, ensuring zero forward return signals",
        "status": "SATISFIED",
        "is_ready": True,
        "non_signal": True,
    },
    {
        "prerequisite_key": "model_family_placeholders_cataloged",
        "category": "metadata_layer",
        "description": "10 baseline model families cataloged as unexecuted metadata placeholders",
        "status": "SATISFIED",
        "is_ready": True,
        "non_signal": True,
    },
    {
        "prerequisite_key": "metric_placeholders_cataloged",
        "category": "metadata_layer",
        "description": "7 metric evaluation families cataloged without premature calculation",
        "status": "SATISFIED",
        "is_ready": True,
        "non_signal": True,
    },
    {
        "prerequisite_key": "artifact_governance_disabled_contracts",
        "category": "storage_layer",
        "description": "Model weights persistence and model registry writes strictly prohibited",
        "status": "SATISFIED",
        "is_ready": True,
        "non_signal": True,
    },
    {
        "prerequisite_key": "manual_review_queue_operational",
        "category": "governance_layer",
        "description": "Audit findings and manual review items operational for dry-run verification",
        "status": "SATISFIED",
        "is_ready": True,
        "non_signal": True,
    },
    {
        "prerequisite_key": "phase_138_dry_run_training_boundary",
        "category": "scope_boundary",
        "description": "Phase 138 may introduce dry-run training harness contracts, but must block live trading and broker execution",
        "status": "SATISFIED",
        "is_ready": True,
        "non_signal": True,
    },
]


def build_phase_138_baseline_ml_model_contracts_handoff_report(
    profile: Optional[AdvancedMlDatasetProfile] = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary for Phase 138 handoff."""
    p = profile or get_default_advanced_ml_dataset_profile()
    df = pd.DataFrame(HANDOFF_PREREQUISITES)
    summary = summarize_phase_138_handoff(df)
    return df, summary


def summarize_phase_138_handoff(df: pd.DataFrame) -> Dict:
    """Summarize Phase 138 handoff DataFrame."""
    total = len(df)
    satisfied = int((df["status"] == "SATISFIED").sum()) if "status" in df.columns else 0
    all_ready = (total == satisfied) and total > 0

    return {
        "handoff_status": "READY_FOR_PHASE_138" if all_ready else "PENDING_PREREQUISITES",
        "source_phase": 137,
        "next_phase": 138,
        "target_final_phase": 160,
        "total_prerequisites": total,
        "satisfied_prerequisites": satisfied,
        "all_satisfied": all_ready,
        "live_trading_prohibited": True,
        "broker_integration_blocked": True,
        "non_signal": True,
    }
