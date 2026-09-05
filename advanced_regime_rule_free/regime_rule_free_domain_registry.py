"""Phase 128: Regime Rule-Free Domain Registry.

Registers and maps all functional domain areas for Phase 128.
"""

from typing import Dict, Tuple
import pandas as pd

from advanced_regime_rule_free.regime_rule_free_config import (
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)

PHASE_128_DOMAINS = [
    {
        "domain_id": "rule_free_labeling_contracts",
        "domain_name": "Rule-Free Labeling Contracts",
        "domain_category": "labeling_contracts",
        "description": "Candidate state annotation preparation contracts without supervised target labels.",
        "non_signal": True,
        "is_executable": False,
    },
    {
        "domain_id": "candidate_state_assignment_policies",
        "domain_name": "Candidate State Assignment Policies",
        "domain_category": "assignment_policies",
        "description": "Contextual assignment policies without algorithmic execution or trade signals.",
        "non_signal": True,
        "is_executable": False,
    },
    {
        "domain_id": "candidate_state_schema",
        "domain_name": "Candidate State Schema",
        "domain_category": "schema",
        "description": "Standard schema for candidate state records strictly prohibiting trade/target words.",
        "non_signal": True,
        "is_executable": False,
    },
    {
        "domain_id": "pseudo_state_schema",
        "domain_name": "Pseudo-State Schema",
        "domain_category": "schema",
        "description": "Schema contracts for non-signal pseudo-state preparation.",
        "non_signal": True,
        "is_executable": False,
    },
    {
        "domain_id": "unsupervised_prep_contracts",
        "domain_name": "Unsupervised Preparation Contracts",
        "domain_category": "unsupervised_prep",
        "description": "Readiness contracts for future unsupervised regime discovery without model fitting.",
        "non_signal": True,
        "is_executable": False,
    },
    {
        "domain_id": "clustering_input_contracts",
        "domain_name": "Clustering Input Contracts",
        "domain_category": "clustering_inputs",
        "description": "Matrix schema specifications for clustering without actual clustering execution.",
        "non_signal": True,
        "is_executable": False,
    },
    {
        "domain_id": "clustering_algorithm_placeholders",
        "domain_name": "Clustering Algorithm Placeholders",
        "domain_category": "algorithm_placeholders",
        "description": "Non-executable metadata placeholders for KMeans, DBSCAN, GMM, HDBSCAN, SOM.",
        "non_signal": True,
        "is_executable": False,
    },
    {
        "domain_id": "distance_metric_placeholders",
        "domain_name": "Distance Metric Placeholders",
        "domain_category": "distance_metrics",
        "description": "Metadata placeholders for Euclidean, Cosine, Manhattan, Correlation distance, DTW.",
        "non_signal": True,
        "is_executable": False,
    },
    {
        "domain_id": "normalization_scaling_prep",
        "domain_name": "Normalization and Scaling Prep",
        "domain_category": "normalization_scaling",
        "description": "Preparation contracts for min-max, z-score, robust normalization and scaling.",
        "non_signal": True,
        "is_executable": False,
    },
    {
        "domain_id": "dimensionality_reduction_placeholders",
        "domain_name": "Dimensionality Reduction Placeholders",
        "domain_category": "dimensionality_reduction",
        "description": "Metadata placeholders for PCA, UMAP, t-SNE without vector/embedding generation.",
        "non_signal": True,
        "is_executable": False,
    },
    {
        "domain_id": "candidate_feature_sets",
        "domain_name": "Candidate Feature Sets",
        "domain_category": "features",
        "description": "Feature sets mapped from Phase 127 matrix inputs, Phase 122 factor families, Phase 123 quality.",
        "non_signal": True,
        "is_executable": False,
    },
    {
        "domain_id": "candidate_state_context_metadata",
        "domain_name": "Candidate State Context and Metadata",
        "domain_category": "context_metadata",
        "description": "Context and metadata records for candidate state families.",
        "non_signal": True,
        "is_executable": False,
    },
    {
        "domain_id": "candidate_state_namespace",
        "domain_name": "Candidate State Namespace",
        "domain_category": "namespace",
        "description": "Naming conventions enforcing candidate_state_ prefix and lowercase snake_case.",
        "non_signal": True,
        "is_executable": False,
    },
    {
        "domain_id": "candidate_state_integrity_manifest",
        "domain_name": "Candidate State Integrity Manifest",
        "domain_category": "integrity",
        "description": "Master governance manifest verifying zero lookahead, zero clustering, zero trading.",
        "non_signal": True,
        "is_executable": False,
    },
    {
        "domain_id": "no_lookahead_guard",
        "domain_name": "No-Lookahead Guard",
        "domain_category": "temporal_guard",
        "description": "Verification preventing future joins, negative shift usage, and lead functions.",
        "non_signal": True,
        "is_executable": False,
    },
    {
        "domain_id": "timestamp_policy",
        "domain_name": "Timestamp Policy",
        "domain_category": "temporal_policy",
        "description": "UTC timestamp validation and ordering rules context_ts <= base_ts.",
        "non_signal": True,
        "is_executable": False,
    },
    {
        "domain_id": "quality_validation_dependencies",
        "domain_name": "Quality and Validation Dependencies",
        "domain_category": "dependencies",
        "description": "Linkages to Phase 123 quality/drift scores and Phase 121 no-lookahead validations.",
        "non_signal": True,
        "is_executable": False,
    },
    {
        "domain_id": "candidate_state_manual_review",
        "domain_name": "Candidate State Manual Review",
        "domain_category": "governance",
        "description": "Offline manual review queue for candidate state contracts and ambiguity items.",
        "non_signal": True,
        "is_executable": False,
    },
    {
        "domain_id": "non_signal_forbidden_claim_policies",
        "domain_name": "Non-Signal and Forbidden Claim Policies",
        "domain_category": "policies",
        "description": "Strict policies prohibiting trade recommendations, buy/sell claims, or directional certainty.",
        "non_signal": True,
        "is_executable": False,
    },
    {
        "domain_id": "source_preservation_policies",
        "domain_name": "Source Preservation Policies",
        "domain_category": "policies",
        "description": "Policies strictly forbidding file deletion, source overwriting, and in-place dataframe mutation.",
        "non_signal": True,
        "is_executable": False,
    },
    {
        "domain_id": "phase_129_handoff",
        "domain_name": "Phase 129 Market Behavior Diagnostics Handoff",
        "domain_category": "handoff",
        "description": "Preconditions and readiness deliverables for Phase 129 Market Behavior Diagnostics.",
        "non_signal": True,
        "is_executable": False,
    },
]


def build_regime_rule_free_domain_registry(
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary metadata for Phase 128 domains."""
    active_profile = profile or get_default_regime_rule_free_profile()

    df = pd.DataFrame(PHASE_128_DOMAINS)
    df["current_phase"] = active_profile.current_phase
    df["next_phase"] = active_profile.next_phase
    df["target_final_phase"] = active_profile.target_final_phase

    summary = {
        "active_profile": active_profile.profile_name,
        "total_domains": len(df),
        "current_phase": active_profile.current_phase,
        "next_phase": active_profile.next_phase,
        "target_final_phase": active_profile.target_final_phase,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_non_executable": bool((~df["is_executable"]).all()) if not df.empty else True,
    }

    return df, summary
