"""Phase 136: ML Artifact Governance Placeholders.

Catalogs future model artifact governance schemas, model card placeholders,
and audit trail structures without persisting models or writing to registries.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    ARTIFACT_GOVERNANCE_PLACEHOLDER_DOMAIN,
    RUNTIME_PLACEHOLDER_ONLY,
)


GOVERNANCE_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "placeholder_id": "future_model_artifact_manifest_placeholder",
        "title": "Model Artifact Manifest Placeholder",
        "description": "Schema defining model checkpoint hashes, architecture metadata, and training parameters.",
        "future_phase_target": 144,
        "details": "Ensures full reproducibility audit trails before any model artifact is saved.",
    },
    {
        "placeholder_id": "future_experiment_run_manifest_placeholder",
        "title": "Experiment Run Manifest Placeholder",
        "description": "Schema logging run UUID, deterministic seeds, Git commit, and environment snapshots.",
        "future_phase_target": 137,
        "details": "Ready for experiment registry integration in Phase 137.",
    },
    {
        "placeholder_id": "future_model_card_placeholder",
        "title": "Model Card Specification Placeholder",
        "description": "Standardized documentation of intended use, evaluation metrics, and safety boundaries.",
        "future_phase_target": 144,
        "details": "Mandatory governance component before model release.",
    },
    {
        "placeholder_id": "future_feature_snapshot_manifest_placeholder",
        "title": "Feature Snapshot Manifest Placeholder",
        "description": "Immutable catalog linking input feature versions and FeatureStore partition keys.",
        "future_phase_target": 137,
        "details": "Links FeatureStore schemas to experiment runs.",
    },
    {
        "placeholder_id": "future_calibration_report_placeholder",
        "title": "Calibration Report Placeholder",
        "description": "Schema for expected calibration error (ECE), Brier score, and reliability curves.",
        "future_phase_target": 141,
        "details": "Evaluates probability accuracy without executing trades.",
    },
    {
        "placeholder_id": "future_drift_monitoring_artifact_placeholder",
        "title": "Model Drift Monitoring Placeholder",
        "description": "Schema for Kolmogorov-Smirnov, PSI, and concept drift diagnostics.",
        "future_phase_target": 142,
        "details": "Monitors inference stability over time.",
    },
    {
        "placeholder_id": "future_explainability_artifact_placeholder",
        "title": "Explainability Artifact Placeholder",
        "description": "Schema for TreeSHAP, Integrated Gradients, and permutation feature importances.",
        "future_phase_target": 143,
        "details": "Ensures transparency of model internal decisions.",
    },
]


def build_ml_artifact_governance_placeholder_registry(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for artifact governance placeholders."""
    active = profile or get_gpu_ml_runtime_profile()

    rows: List[Dict[str, Any]] = []
    for g in GOVERNANCE_PLACEHOLDERS:
        rows.append(
            {
                "placeholder_id": g["placeholder_id"],
                "title": g["title"],
                "description": g["description"],
                "future_phase_target": g["future_phase_target"],
                "status_label": RUNTIME_PLACEHOLDER_ONLY,
                "artifact_persisted": False,
                "model_registry_written": False,
                "non_signal": True,
                "source_preserved": True,
                "official_approval": False,
                "production_ready": False,
                "broker_ready": False,
                "details": g["details"],
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_ml_artifact_governance_placeholders(df)
    summary["domain"] = ARTIFACT_GOVERNANCE_PLACEHOLDER_DOMAIN
    summary["active_profile"] = active.profile_name
    return df, summary


def summarize_ml_artifact_governance_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize artifact governance placeholders DataFrame."""
    return {
        "total_placeholders": len(df),
        "status_label": RUNTIME_PLACEHOLDER_ONLY,
        "zero_artifact_persisted": True,
        "zero_registry_written": True,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
