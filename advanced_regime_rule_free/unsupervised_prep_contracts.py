"""Phase 128: Unsupervised Preparation Contracts.

Defines readiness contracts for future unsupervised exploration without model execution or clustering.
"""

from typing import Dict, Tuple
import pandas as pd

from advanced_regime_rule_free.regime_rule_free_config import (
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)
from advanced_regime_rule_free.regime_rule_free_models import UnsupervisedPrepContract

UNSUPERVISED_PREP_CONTRACTS = [
    UnsupervisedPrepContract(
        contract_name="unsupervised_matrix_readiness_contract",
        prep_category="matrix_readiness",
        description="Verifies that Phase 127 regime feature matrix satisfies completeness, schema, and alignment prerequisites.",
    ),
    UnsupervisedPrepContract(
        contract_name="candidate_state_feature_selection_placeholder_contract",
        prep_category="feature_selection",
        description="Defines criteria for non-signal candidate feature subsetting for future clustering pipelines.",
    ),
    UnsupervisedPrepContract(
        contract_name="unsupervised_normalization_prep_contract",
        prep_category="normalization_prep",
        description="Specifies scaling parameters (min-max, robust, z-score) required prior to distance computations.",
    ),
    UnsupervisedPrepContract(
        contract_name="unsupervised_distance_metric_prep_contract",
        prep_category="metric_prep",
        description="Specifies geometry and metric requirements (Euclidean, Cosine, Correlation) for candidate state distances.",
    ),
    UnsupervisedPrepContract(
        contract_name="unsupervised_cluster_validation_prep_contract",
        prep_category="cluster_validation_prep",
        description="Defines statistical validation placeholders (silhouette, Davies-Bouldin) for future cluster diagnostics.",
    ),
    UnsupervisedPrepContract(
        contract_name="unsupervised_manual_review_prep_contract",
        prep_category="manual_review_prep",
        description="Specifies governance protocols for manual inspection of unsupervised partition boundaries.",
    ),
]


def build_unsupervised_prep_contract_registry(
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary metadata for unsupervised prep contracts."""
    active_profile = profile or get_default_regime_rule_free_profile()

    rows = []
    for c in UNSUPERVISED_PREP_CONTRACTS:
        row = c.__dict__.copy()
        row["current_phase"] = active_profile.current_phase
        row["next_phase"] = active_profile.next_phase
        row["target_final_phase"] = active_profile.target_final_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_unsupervised_prep_contracts(df)
    return df, summary


def validate_unsupervised_prep_contract(contract: dict) -> dict:
    """Validate that unsupervised prep contract enforces zero-execution boundaries."""
    violations = []
    name = contract.get("contract_name", "unknown")

    if contract.get("fit_transform_allowed", True):
        violations.append("fit_transform_allowed must be False")
    if contract.get("model_training_allowed", True):
        violations.append("model_training_allowed must be False")
    if contract.get("clustering_allowed", True):
        violations.append("clustering_allowed must be False")
    if contract.get("dimensionality_reduction_allowed", True):
        violations.append("dimensionality_reduction_allowed must be False")
    if not contract.get("non_signal", False):
        violations.append("non_signal must be True")

    return {
        "contract_name": name,
        "is_valid": len(violations) == 0,
        "violations": violations,
    }


def summarize_unsupervised_prep_contracts(df: pd.DataFrame) -> Dict:
    """Summarize unsupervised preparation contracts."""
    total = len(df)
    all_non_signal = bool(df["non_signal"].all()) if not df.empty else True
    all_no_training = bool((~df["model_training_allowed"]).all()) if not df.empty else True
    all_no_clustering = bool((~df["clustering_allowed"]).all()) if not df.empty else True

    return {
        "total_prep_contracts": total,
        "all_non_signal": all_non_signal,
        "all_no_training": all_no_training,
        "all_no_clustering": all_no_clustering,
        "prep_status": "VALID" if all_non_signal and all_no_training and all_no_clustering else "INVALID",
    }
