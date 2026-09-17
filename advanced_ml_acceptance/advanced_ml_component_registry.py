# -*- coding: utf-8 -*-
"""Phase 145: Advanced ML Component Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    AdvancedMlAcceptanceProfile,
    get_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_acceptance_labels import (
    COMPONENT_REGISTRY_DOMAIN,
    ACCEPTANCE_READY,
)

COMPONENTS: List[Dict[str, Any]] = [
    {
        "component_id": "CMP-136",
        "component_name": "phase_136_gpu_ml_runtime_foundation",
        "phase_ref": "Phase 136",
        "phase_number": 136,
        "primary_module": "advanced_gpu_ml_runtime",
        "description": "GPU acceleration and advanced ML runtime foundation, local hardware discovery, and ML experiment safety contracts.",
    },
    {
        "component_id": "CMP-137",
        "component_name": "phase_137_ml_dataset_contracts_experiment_registry",
        "phase_ref": "Phase 137",
        "phase_number": 137,
        "primary_module": "advanced_ml_dataset_registry",
        "description": "Advanced ML dataset contracts, feature snapshot schemas, no-lookahead guards, and experiment registry.",
    },
    {
        "component_id": "CMP-138",
        "component_name": "phase_138_baseline_ml_model_contracts_dry_run_harness",
        "phase_ref": "Phase 138",
        "phase_number": 138,
        "primary_module": "advanced_baseline_ml_models",
        "description": "Baseline ML model contracts, model family catalog, and dry-run training harness interfaces.",
    },
    {
        "component_id": "CMP-139",
        "component_name": "phase_139_gpu_training_harness_resource_governance",
        "phase_ref": "Phase 139",
        "phase_number": 139,
        "primary_module": "advanced_gpu_training_governance",
        "description": "GPU-accelerated training harness interfaces, resource governance, memory budget policies, and timeout guards.",
    },
    {
        "component_id": "CMP-140",
        "component_name": "phase_140_ensemble_model_contracts_candidate_registry",
        "phase_ref": "Phase 140",
        "phase_number": 140,
        "primary_module": "advanced_ensemble_model_registry",
        "description": "Ensemble model contracts, candidate model registry, strategy schemas, and eligibility gates.",
    },
    {
        "component_id": "CMP-141",
        "component_name": "phase_141_probability_calibration_uncertainty_contracts",
        "phase_ref": "Phase 141",
        "phase_number": 141,
        "primary_module": "advanced_calibration_uncertainty",
        "description": "Probability calibration contracts, uncertainty estimation placeholders, and confidence interval bounds.",
    },
    {
        "component_id": "CMP-142",
        "component_name": "phase_142_model_drift_monitoring_feature_drift_linkage",
        "phase_ref": "Phase 142",
        "phase_number": 142,
        "primary_module": "advanced_model_drift_monitoring",
        "description": "Model drift monitoring contracts, data/feature drift linkage, and reference window policies.",
    },
    {
        "component_id": "CMP-143",
        "component_name": "phase_143_explainability_feature_attribution_reports",
        "phase_ref": "Phase 143",
        "phase_number": 143,
        "primary_module": "advanced_explainability_attribution",
        "description": "Explainability and feature attribution report contracts, global/local explanation schemas (SHAP/LIME placeholders).",
    },
    {
        "component_id": "CMP-144",
        "component_name": "phase_144_model_governance_model_cards_audit_trail",
        "phase_ref": "Phase 144",
        "phase_number": 144,
        "primary_module": "advanced_model_governance",
        "description": "Model governance, model cards, audit trail placeholders, risk register, and approval boundaries.",
    },
    {
        "component_id": "CMP-145",
        "component_name": "phase_145_advanced_ml_acceptance_report",
        "phase_ref": "Phase 145",
        "phase_number": 145,
        "primary_module": "advanced_ml_acceptance",
        "description": "Consolidated Advanced ML acceptance report, component checkpoints, readiness scoring, and Phase 146 handoff.",
    },
]


def build_advanced_ml_component_registry(
    profile: Optional[AdvancedMlAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for advanced ML block components."""
    active = profile or get_advanced_ml_acceptance_profile()

    records = []
    for c in COMPONENTS:
        row = dict(c)
        row["current_phase"] = active.current_phase
        row["target_final_phase"] = active.target_final_phase
        row["next_phase"] = active.next_phase
        row["status"] = ACCEPTANCE_READY
        row["contract_only"] = True
        row["non_production"] = True
        row["production_ready"] = False
        row["broker_ready"] = False
        row["signal_ready"] = False
        row["non_signal"] = True
        records.append(row)

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": COMPONENT_REGISTRY_DOMAIN,
        "active_profile": active.profile_name,
        "current_phase": active.current_phase,
        "target_final_phase": active.target_final_phase,
        "next_phase": active.next_phase,
        "total_components": len(df),
        "non_signal": True,
        "status": "READY",
    }
    return df, summary


def summarize_advanced_ml_components(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize components DataFrame."""
    return {
        "component_count": len(df),
        "components": df["component_name"].tolist() if not df.empty and "component_name" in df.columns else [],
        "all_contract_only": bool(df["contract_only"].all()) if not df.empty and "contract_only" in df.columns else True,
        "non_signal": True,
    }
