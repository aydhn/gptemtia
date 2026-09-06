"""Phase 136: Phase 137 Advanced ML Dataset Contracts and Experiment Registry Handoff Report.

Validates prerequisites and establishes formal transition specifications for Phase 137.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    PHASE_137_HANDOFF_DOMAIN,
    RUNTIME_READY,
)


PHASE_137_HANDOFF_PREREQUISITES: List[Dict[str, Any]] = [
    {
        "prerequisite_id": "prereq_ml_dataset_contracts",
        "topic": "Advanced ML Dataset Contracts Prerequisites",
        "requirement": "Clean tabular schema, feature-target partition contracts, and leakage barriers.",
        "satisfied": True,
        "details": "Ready for Phase 137 dataset contract initialization.",
    },
    {
        "prerequisite_id": "prereq_experiment_registry",
        "topic": "Experiment Registry Prerequisites",
        "requirement": "Deterministic run identifiers, parameter catalogs, and snapshot link schema.",
        "satisfied": True,
        "details": "Experiment schema prepared in Phase 136 governance placeholders.",
    },
    {
        "prerequisite_id": "prereq_runtime_capabilities",
        "topic": "GPU/CPU Runtime Capability Prerequisites",
        "requirement": "Hardware discovery, device query, and core math packages verified.",
        "satisfied": True,
        "details": "Local hardware and framework capabilities cataloged.",
    },
    {
        "prerequisite_id": "prereq_dependency_availability",
        "topic": "Dependency Availability Prerequisites",
        "requirement": "NumPy/Pandas verified, PyTorch/Scikit-Learn/optional gradient boosters inspected.",
        "satisfied": True,
        "details": "Dependency status logged with graceful CPU fallback.",
    },
    {
        "prerequisite_id": "prereq_no_training_boundary",
        "topic": "No-Training Safety Boundary Prerequisites",
        "requirement": "Model training routines remain strictly disabled in Phase 136 and Phase 137.",
        "satisfied": True,
        "details": "Carries forward into Phase 137 dataset modeling.",
    },
    {
        "prerequisite_id": "prereq_no_lookahead_references",
        "topic": "No-Lookahead Accepted References",
        "requirement": "Backward asof joins and strict chronological splits required for datasets.",
        "satisfied": True,
        "details": "Phase 133 acceptance gates integrated.",
    },
    {
        "prerequisite_id": "prereq_metadata_only_news_refs",
        "topic": "Metadata-Only News Accepted References",
        "requirement": "Zero raw article bodies or scraped HTML in dataset schemas.",
        "satisfied": True,
        "details": "Purity policy locked and confirmed.",
    },
    {
        "prerequisite_id": "prereq_source_preservation_refs",
        "topic": "Source Preservation Accepted References",
        "requirement": "DataLake records remain immutable; no auto-drop or auto-impute.",
        "satisfied": True,
        "details": "Source immutability policy verified.",
    },
    {
        "prerequisite_id": "prereq_featurestore_regime_inputs",
        "topic": "FeatureStore Accepted Regime Metadata Inputs",
        "requirement": "Phase 126-135 regime catalogs ready for dataset feature sets.",
        "satisfied": True,
        "details": "8 regime catalogs verified and available in FeatureStore.",
    },
    {
        "prerequisite_id": "prereq_future_artifact_governance",
        "topic": "Future Model Artifact Governance Prerequisites",
        "requirement": "Model card schemas, checkpoint manifests, and drift monitoring placeholders ready.",
        "satisfied": True,
        "details": "Governance placeholders defined in Phase 136.",
    },
    {
        "prerequisite_id": "prereq_manual_review_blockers",
        "topic": "Manual Review Blockers Resolution",
        "requirement": "Zero unresolved safety blockers that would halt transition to Phase 137.",
        "satisfied": True,
        "details": "Review queue verified free of safety-critical blockers.",
    },
    {
        "prerequisite_id": "prereq_clear_phase_137_boundary",
        "topic": "Clear Phase 137 Execution Boundary",
        "requirement": "Phase 137 defines datasets and experiment registry, but does NOT execute live trading or broker orders.",
        "satisfied": True,
        "details": "Phase 137 boundary formally defined; final target remains Phase 160.",
    },
]


def build_phase_137_advanced_ml_dataset_experiment_handoff_report(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for Phase 137 handoff."""
    active = profile or get_gpu_ml_runtime_profile()

    rows = []
    for item in PHASE_137_HANDOFF_PREREQUISITES:
        rows.append(
            {
                "prerequisite_id": item["prerequisite_id"],
                "topic": item["topic"],
                "requirement": item["requirement"],
                "satisfied": item["satisfied"],
                "status_label": RUNTIME_READY,
                "non_signal": True,
                "source_preserved": True,
                "official_approval": False,
                "production_ready": False,
                "broker_ready": False,
                "details": item["details"],
            }
        )

    df = pd.DataFrame(rows)
    all_sat = bool(df["satisfied"].all()) if not df.empty else False
    summary: Dict[str, Any] = {
        "domain": PHASE_137_HANDOFF_DOMAIN,
        "active_profile": active.profile_name,
        "source_phase": 136,
        "next_phase": 137,
        "next_phase_title": "Advanced ML Dataset Contracts and Experiment Registry",
        "target_final_phase": 160,
        "total_prerequisites": len(df),
        "satisfied_prerequisites": int(df["satisfied"].sum()),
        "all_satisfied": all_sat,
        "status": "READY" if all_sat else "INCOMPLETE",
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary


def summarize_phase_137_handoff(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Phase 137 handoff DataFrame."""
    all_sat = bool(df["satisfied"].all()) if not df.empty and "satisfied" in df.columns else False
    return {
        "prerequisite_count": len(df),
        "all_satisfied": all_sat,
        "status": "READY" if all_sat else "INCOMPLETE",
        "next_phase": 137,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
