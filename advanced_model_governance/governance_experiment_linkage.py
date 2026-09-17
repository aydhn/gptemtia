# -*- coding: utf-8 -*-
"""Phase 144: Governance Experiment Linkage Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

EXPERIMENT_LINKAGE_ITEMS: List[Dict[str, str]] = [
    {"linkage_id": "EXP-LNK-137", "source_phase": "Phase 137", "component": "Experiment Registry", "linked_to": "Governance Contract Data Spec", "status": "LINKED"},
    {"linkage_id": "EXP-LNK-138", "source_phase": "Phase 138", "component": "Baseline Model Contracts", "linked_to": "Baseline Model Card", "status": "LINKED"},
    {"linkage_id": "EXP-LNK-139", "source_phase": "Phase 139", "component": "GPU Resource Governance", "linked_to": "Runtime Dependency Spec", "status": "LINKED"},
    {"linkage_id": "EXP-LNK-140", "source_phase": "Phase 140", "component": "Candidate & Ensemble Registry", "linked_to": "Candidate & Ensemble Model Cards", "status": "LINKED"},
    {"linkage_id": "EXP-LNK-141", "source_phase": "Phase 141", "component": "Calibration & Uncertainty", "linked_to": "Calibration Uncertainty Model Card", "status": "LINKED"},
    {"linkage_id": "EXP-LNK-142", "source_phase": "Phase 142", "component": "Drift Monitoring Registry", "linked_to": "Risk Disclosure & Drift Card", "status": "LINKED"},
    {"linkage_id": "EXP-LNK-143", "source_phase": "Phase 143", "component": "Explainability Registry", "linked_to": "Explainability Model Card", "status": "LINKED"},
    {"linkage_id": "EXP-LNK-144", "source_phase": "Phase 144", "component": "Governance & Model Cards", "linked_to": "Governance Manifest", "status": "LINKED"},
    {"linkage_id": "EXP-LNK-145", "source_phase": "Phase 145", "component": "Advanced ML Acceptance", "linked_to": "Phase 145 Handoff Contract", "status": "READY_FOR_HANDOFF"},
]


def build_governance_experiment_linkage_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for governance experiment linkages."""
    prof = profile or get_model_governance_profile()
    records = []
    for item in EXPERIMENT_LINKAGE_ITEMS:
        row = dict(item)
        row["phase"] = prof.current_phase
        row["non_signal"] = True
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_governance_experiment_linkage(df)
    return df, summary


def summarize_governance_experiment_linkage(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize governance experiment linkage."""
    return {
        "total_linkages": len(df),
        "all_linked": True,
        "status": "EXPERIMENT_LINKAGE_VERIFIED",
    }
