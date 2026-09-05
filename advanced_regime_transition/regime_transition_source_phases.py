"""Phase 130: Regime Transition Source Phases.

Catalogs upstream source phase lineage and dependencies that feed the Phase 130
Regime Transition and Stability Analysis layer.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_transition.regime_transition_config import (
    RegimeTransitionProfile,
    get_default_regime_transition_profile,
)

SOURCE_PHASES: List[Dict[str, Any]] = [
    {
        "source_phase": 121,
        "phase_name": "Phase 121 Feature Validation and Guardrails",
        "provided_artifacts": "no_lookahead_validation, timestamp_order, numeric_sanity",
        "dependency_type": "validation_gate",
        "status": "active_dependency",
    },
    {
        "source_phase": 123,
        "phase_name": "Phase 123 Feature Quality and Drift Diagnostics",
        "provided_artifacts": "missingness_metrics, drift_scores, quality_findings",
        "dependency_type": "quality_gate",
        "status": "active_dependency",
    },
    {
        "source_phase": 124,
        "phase_name": "Phase 124 Feature Store Integration Expansion",
        "provided_artifacts": "feature_metadata_catalogs, entity_registries",
        "dependency_type": "metadata_catalog",
        "status": "active_dependency",
    },
    {
        "source_phase": 126,
        "phase_name": "Phase 126 Regime Classification Foundation",
        "provided_artifacts": "regime_taxonomies, regime_family_registries",
        "dependency_type": "domain_foundation",
        "status": "active_dependency",
    },
    {
        "source_phase": 127,
        "phase_name": "Phase 127 Regime Feature Matrix and State Datasets",
        "provided_artifacts": "matrix_contracts, state_dataset_contracts",
        "dependency_type": "dataset_contract",
        "status": "active_dependency",
    },
    {
        "source_phase": 128,
        "phase_name": "Phase 128 Regime Rule-Free Labeling Contracts",
        "provided_artifacts": "candidate_states, pseudo_states_contracts",
        "dependency_type": "candidate_state_schema",
        "status": "active_dependency",
    },
    {
        "source_phase": 129,
        "phase_name": "Phase 129 Market Behavior Diagnostics and Regime Quality",
        "provided_artifacts": "behavior_diagnostics, candidate_quality_scores, handoff",
        "dependency_type": "behavior_diagnostics",
        "status": "active_dependency",
    },
]


def build_regime_transition_source_phase_registry(
    profile: Optional[RegimeTransitionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build source phase registry dataframe and summary."""
    if profile is None:
        profile = get_default_regime_transition_profile()

    df = pd.DataFrame(SOURCE_PHASES)
    summary = summarize_regime_transition_source_phases(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_regime_transition_source_phases(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize source phase registry."""
    return {
        "total_source_phases": len(df),
        "source_phase_numbers": df["source_phase"].tolist() if not df.empty else [],
        "all_active": bool((df["status"] == "active_dependency").all()) if not df.empty else True,
        "all_source_preserved": True,
        "all_read_only": True,
        "non_signal": True,
    }

