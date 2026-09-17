# -*- coding: utf-8 -*-
"""Phase 140: Ensemble Model Contracts & Candidate Model Registry Package."""

from advanced_ensemble_model_registry.ensemble_model_config import (
    EnsembleModelProfile,
    get_ensemble_model_profile,
    list_ensemble_model_profiles,
    validate_ensemble_model_profile,
)
from advanced_ensemble_model_registry.ensemble_model_labels import (
    ENSEMBLE_MODEL_DOMAINS,
    CANDIDATE_MODEL_STATUSES,
    ENSEMBLE_EXECUTION_LABELS,
    validate_ensemble_domain_label,
    validate_candidate_model_status_label,
    validate_ensemble_execution_label,
)
from advanced_ensemble_model_registry.ensemble_model_models import (
    EnsembleModelProfileItem,
    CandidateModelFamilyItem,
    CandidateModelContract,
    CandidateModelInputContract,
    CandidateModelOutputContract,
    CandidateModelEligibilityGate,
    CandidateCompatibilityMatrixItem,
    EnsembleStrategyContract,
    EnsemblePlaceholderItem,
    EnsembleFinding,
    EnsembleReadinessScore,
    EnsembleModelManifest,
    EnsembleManualReviewItem,
)
from advanced_ensemble_model_registry.ensemble_model_profile_registry import (
    build_ensemble_model_profile_registry,
    validate_ensemble_model_profile_registry,
    summarize_ensemble_model_profiles,
)
from advanced_ensemble_model_registry.ensemble_model_domain_registry import (
    build_ensemble_model_domain_registry,
    validate_ensemble_model_domain_registry,
    summarize_ensemble_model_domains,
)
from advanced_ensemble_model_registry.candidate_model_families import (
    build_candidate_model_families,
    validate_candidate_model_families,
    summarize_candidate_model_families,
)
from advanced_ensemble_model_registry.candidate_model_contracts import (
    build_candidate_model_contracts,
    validate_candidate_model_contracts,
    summarize_candidate_model_contracts,
)
from advanced_ensemble_model_registry.candidate_model_input_contracts import (
    build_candidate_model_input_contracts,
    validate_candidate_model_input_contracts,
    summarize_candidate_model_input_contracts,
)
from advanced_ensemble_model_registry.candidate_model_output_contracts import (
    build_candidate_model_output_contracts,
    validate_candidate_model_output_contracts,
    summarize_candidate_model_output_contracts,
)
from advanced_ensemble_model_registry.candidate_model_eligibility_gates import (
    build_candidate_model_eligibility_gates,
    validate_candidate_model_eligibility_gates,
    summarize_candidate_model_eligibility_gates,
)
from advanced_ensemble_model_registry.candidate_model_compatibility_matrix import (
    build_candidate_compatibility_matrix,
    validate_candidate_compatibility_matrix,
    summarize_candidate_compatibility_matrix,
)
from advanced_ensemble_model_registry.ensemble_strategy_contracts import (
    build_ensemble_strategy_contracts,
    validate_ensemble_strategy_contracts,
    summarize_ensemble_strategy_contracts,
)
from advanced_ensemble_model_registry.ensemble_voting_placeholders import (
    build_ensemble_voting_placeholders,
    validate_ensemble_voting_placeholders,
    summarize_ensemble_voting_placeholders,
)
from advanced_ensemble_model_registry.ensemble_blending_placeholders import (
    build_ensemble_blending_placeholders,
    validate_ensemble_blending_placeholders,
    summarize_ensemble_blending_placeholders,
)
from advanced_ensemble_model_registry.ensemble_stacking_placeholders import (
    build_ensemble_stacking_placeholders,
    validate_ensemble_stacking_placeholders,
    summarize_ensemble_stacking_placeholders,
)
from advanced_ensemble_model_registry.ensemble_weighting_policy_placeholders import (
    build_ensemble_weighting_policy_placeholders,
    validate_ensemble_weighting_policy_placeholders,
    summarize_ensemble_weighting_policy_placeholders,
)
from advanced_ensemble_model_registry.ensemble_meta_model_placeholders import (
    build_ensemble_meta_model_placeholders,
    validate_ensemble_meta_model_placeholders,
    summarize_ensemble_meta_model_placeholders,
)
from advanced_ensemble_model_registry.ensemble_selection_policies import (
    build_ensemble_selection_policies,
    validate_ensemble_selection_policies,
    summarize_ensemble_selection_policies,
)
from advanced_ensemble_model_registry.ensemble_input_contracts import (
    build_ensemble_input_contracts,
    validate_ensemble_input_contracts,
    summarize_ensemble_input_contracts,
)
from advanced_ensemble_model_registry.ensemble_output_contracts import (
    build_ensemble_output_contracts,
    validate_ensemble_output_contracts,
    summarize_ensemble_output_contracts,
)
from advanced_ensemble_model_registry.ensemble_execution_disabled import (
    build_ensemble_execution_disabled_report,
    validate_ensemble_execution_disabled_report,
    summarize_ensemble_execution_disabled_report,
)
from advanced_ensemble_model_registry.candidate_model_training_disabled import (
    build_candidate_model_training_disabled_report,
    validate_candidate_model_training_disabled_report,
    summarize_candidate_model_training_disabled_report,
)
from advanced_ensemble_model_registry.candidate_model_prediction_disabled import (
    build_candidate_model_prediction_disabled_report,
    validate_candidate_model_prediction_disabled_report,
    summarize_candidate_model_prediction_disabled_report,
)
from advanced_ensemble_model_registry.candidate_model_target_label_disabled import (
    build_candidate_model_target_label_disabled_report,
    validate_candidate_model_target_label_disabled_report,
    summarize_candidate_model_target_label_disabled_report,
)
from advanced_ensemble_model_registry.candidate_model_artifact_disabled import (
    build_candidate_model_artifact_disabled_report,
    validate_candidate_model_artifact_disabled_report,
    summarize_candidate_model_artifact_disabled_report,
)
from advanced_ensemble_model_registry.candidate_model_registry_write_disabled import (
    build_candidate_model_registry_write_disabled_report,
    validate_candidate_model_registry_write_disabled_report,
    summarize_candidate_model_registry_write_disabled_report,
)
from advanced_ensemble_model_registry.ensemble_metric_placeholders import (
    build_ensemble_metric_placeholders,
    validate_ensemble_metric_placeholders,
    summarize_ensemble_metric_placeholders,
)
from advanced_ensemble_model_registry.ensemble_evaluation_placeholders import (
    build_ensemble_evaluation_placeholders,
    validate_ensemble_evaluation_placeholders,
    summarize_ensemble_evaluation_placeholders,
)
from advanced_ensemble_model_registry.ensemble_validation_dependencies import (
    build_ensemble_validation_dependencies,
    validate_ensemble_validation_dependencies,
    summarize_ensemble_validation_dependencies,
)
from advanced_ensemble_model_registry.ensemble_quality_dependencies import (
    build_ensemble_quality_dependencies,
    validate_ensemble_quality_dependencies,
    summarize_ensemble_quality_dependencies,
)
from advanced_ensemble_model_registry.ensemble_lineage import (
    build_ensemble_lineage,
    validate_ensemble_lineage,
    summarize_ensemble_lineage,
)
from advanced_ensemble_model_registry.ensemble_experiment_linkage import (
    build_ensemble_experiment_linkage,
    validate_ensemble_experiment_linkage,
    summarize_ensemble_experiment_linkage,
)
from advanced_ensemble_model_registry.ensemble_no_lookahead_guards import (
    build_ensemble_no_lookahead_guards,
    validate_ensemble_no_lookahead_guards,
    summarize_ensemble_no_lookahead_guards,
)
from advanced_ensemble_model_registry.ensemble_metadata_only_news_guards import (
    build_ensemble_metadata_only_news_guards,
    validate_ensemble_metadata_only_news_guards,
    summarize_ensemble_metadata_only_news_guards,
)
from advanced_ensemble_model_registry.ensemble_source_preservation_guards import (
    build_ensemble_source_preservation_guards,
    validate_ensemble_source_preservation_guards,
    summarize_ensemble_source_preservation_guards,
)
from advanced_ensemble_model_registry.ensemble_forbidden_column_policies import (
    get_ensemble_forbidden_column_patterns,
    check_columns_against_ensemble_policy,
    summarize_ensemble_forbidden_column_policy,
)
from advanced_ensemble_model_registry.ensemble_candidate_audit_placeholders import (
    build_ensemble_candidate_audit_placeholders,
    validate_ensemble_candidate_audit_placeholders,
    summarize_ensemble_candidate_audit_placeholders,
)
from advanced_ensemble_model_registry.ensemble_manual_review import (
    build_ensemble_manual_review_queue,
    validate_ensemble_manual_review_queue,
    summarize_ensemble_manual_review_queue,
)
from advanced_ensemble_model_registry.ensemble_findings import (
    build_ensemble_findings,
    validate_ensemble_findings,
    summarize_ensemble_findings,
)
from advanced_ensemble_model_registry.ensemble_readiness_scoring import (
    calculate_ensemble_readiness_score,
    validate_ensemble_readiness_score,
    summarize_ensemble_readiness_score,
)
from advanced_ensemble_model_registry.ensemble_model_manifest import (
    build_ensemble_model_manifest,
    validate_ensemble_model_manifest,
    summarize_ensemble_model_manifest,
)
from advanced_ensemble_model_registry.ensemble_model_report_builder import (
    ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER,
    build_ensemble_model_text_report,
    build_ensemble_model_markdown_report,
)
from advanced_ensemble_model_registry.ensemble_model_health import (
    check_ensemble_model_health,
    validate_ensemble_model_health_report,
    summarize_ensemble_model_health_report,
)
from advanced_ensemble_model_registry.ensemble_model_validation import (
    build_ensemble_model_validation_report,
    validate_ensemble_model_validation_report,
    summarize_ensemble_model_validation_report,
)
from advanced_ensemble_model_registry.ensemble_model_safety_boundary import (
    enforce_ensemble_model_safety_boundary,
    assert_ensemble_model_safety_boundary,
    summarize_ensemble_model_safety_boundary,
)
from advanced_ensemble_model_registry.phase_141_handoff import (
    build_phase_141_handoff_report,
    validate_phase_141_handoff_report,
    summarize_phase_141_handoff_report,
)
from advanced_ensemble_model_registry.ensemble_model_pipeline import (
    run_ensemble_model_pipeline,
    validate_ensemble_model_pipeline_result,
    summarize_ensemble_model_pipeline_result,
)

__all__ = [
    "EnsembleModelProfile",
    "get_ensemble_model_profile",
    "list_ensemble_model_profiles",
    "validate_ensemble_model_profile",
    "ENSEMBLE_MODEL_DOMAINS",
    "CANDIDATE_MODEL_STATUSES",
    "ENSEMBLE_EXECUTION_LABELS",
    "validate_ensemble_domain_label",
    "validate_candidate_model_status_label",
    "validate_ensemble_execution_label",
    "EnsembleModelProfileItem",
    "CandidateModelFamilyItem",
    "CandidateModelContract",
    "CandidateModelInputContract",
    "CandidateModelOutputContract",
    "CandidateModelEligibilityGate",
    "CandidateCompatibilityMatrixItem",
    "EnsembleStrategyContract",
    "EnsemblePlaceholderItem",
    "EnsembleFinding",
    "EnsembleReadinessScore",
    "EnsembleModelManifest",
    "EnsembleManualReviewItem",
    "build_ensemble_model_profile_registry",
    "validate_ensemble_model_profile_registry",
    "summarize_ensemble_model_profiles",
    "build_ensemble_model_domain_registry",
    "validate_ensemble_model_domain_registry",
    "summarize_ensemble_model_domains",
    "build_candidate_model_families",
    "validate_candidate_model_families",
    "summarize_candidate_model_families",
    "build_candidate_model_contracts",
    "validate_candidate_model_contracts",
    "summarize_candidate_model_contracts",
    "build_candidate_model_input_contracts",
    "validate_candidate_model_input_contracts",
    "summarize_candidate_model_input_contracts",
    "build_candidate_model_output_contracts",
    "validate_candidate_model_output_contracts",
    "summarize_candidate_model_output_contracts",
    "build_candidate_model_eligibility_gates",
    "validate_candidate_model_eligibility_gates",
    "summarize_candidate_model_eligibility_gates",
    "build_candidate_compatibility_matrix",
    "validate_candidate_compatibility_matrix",
    "summarize_candidate_compatibility_matrix",
    "build_ensemble_strategy_contracts",
    "validate_ensemble_strategy_contracts",
    "summarize_ensemble_strategy_contracts",
    "build_ensemble_voting_placeholders",
    "validate_ensemble_voting_placeholders",
    "summarize_ensemble_voting_placeholders",
    "build_ensemble_blending_placeholders",
    "validate_ensemble_blending_placeholders",
    "summarize_ensemble_blending_placeholders",
    "build_ensemble_stacking_placeholders",
    "validate_ensemble_stacking_placeholders",
    "summarize_ensemble_stacking_placeholders",
    "build_ensemble_weighting_policy_placeholders",
    "validate_ensemble_weighting_policy_placeholders",
    "summarize_ensemble_weighting_policy_placeholders",
    "build_ensemble_meta_model_placeholders",
    "validate_ensemble_meta_model_placeholders",
    "summarize_ensemble_meta_model_placeholders",
    "build_ensemble_selection_policies",
    "validate_ensemble_selection_policies",
    "summarize_ensemble_selection_policies",
    "build_ensemble_input_contracts",
    "validate_ensemble_input_contracts",
    "summarize_ensemble_input_contracts",
    "build_ensemble_output_contracts",
    "validate_ensemble_output_contracts",
    "summarize_ensemble_output_contracts",
    "build_ensemble_execution_disabled_report",
    "validate_ensemble_execution_disabled_report",
    "summarize_ensemble_execution_disabled_report",
    "build_candidate_model_training_disabled_report",
    "validate_candidate_model_training_disabled_report",
    "summarize_candidate_model_training_disabled_report",
    "build_candidate_model_prediction_disabled_report",
    "validate_candidate_model_prediction_disabled_report",
    "summarize_candidate_model_prediction_disabled_report",
    "build_candidate_model_target_label_disabled_report",
    "validate_candidate_model_target_label_disabled_report",
    "summarize_candidate_model_target_label_disabled_report",
    "build_candidate_model_artifact_disabled_report",
    "validate_candidate_model_artifact_disabled_report",
    "summarize_candidate_model_artifact_disabled_report",
    "build_candidate_model_registry_write_disabled_report",
    "validate_candidate_model_registry_write_disabled_report",
    "summarize_candidate_model_registry_write_disabled_report",
    "build_ensemble_metric_placeholders",
    "validate_ensemble_metric_placeholders",
    "summarize_ensemble_metric_placeholders",
    "build_ensemble_evaluation_placeholders",
    "validate_ensemble_evaluation_placeholders",
    "summarize_ensemble_evaluation_placeholders",
    "build_ensemble_validation_dependencies",
    "validate_ensemble_validation_dependencies",
    "summarize_ensemble_validation_dependencies",
    "build_ensemble_quality_dependencies",
    "validate_ensemble_quality_dependencies",
    "summarize_ensemble_quality_dependencies",
    "build_ensemble_lineage",
    "validate_ensemble_lineage",
    "summarize_ensemble_lineage",
    "build_ensemble_experiment_linkage",
    "validate_ensemble_experiment_linkage",
    "summarize_ensemble_experiment_linkage",
    "build_ensemble_no_lookahead_guards",
    "validate_ensemble_no_lookahead_guards",
    "summarize_ensemble_no_lookahead_guards",
    "build_ensemble_metadata_only_news_guards",
    "validate_ensemble_metadata_only_news_guards",
    "summarize_ensemble_metadata_only_news_guards",
    "build_ensemble_source_preservation_guards",
    "validate_ensemble_source_preservation_guards",
    "summarize_ensemble_source_preservation_guards",
    "get_ensemble_forbidden_column_patterns",
    "check_columns_against_ensemble_policy",
    "summarize_ensemble_forbidden_column_policy",
    "build_ensemble_candidate_audit_placeholders",
    "validate_ensemble_candidate_audit_placeholders",
    "summarize_ensemble_candidate_audit_placeholders",
    "build_ensemble_manual_review_queue",
    "validate_ensemble_manual_review_queue",
    "summarize_ensemble_manual_review_queue",
    "build_ensemble_findings",
    "validate_ensemble_findings",
    "summarize_ensemble_findings",
    "calculate_ensemble_readiness_score",
    "validate_ensemble_readiness_score",
    "summarize_ensemble_readiness_score",
    "build_ensemble_model_manifest",
    "validate_ensemble_model_manifest",
    "summarize_ensemble_model_manifest",
    "ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER",
    "build_ensemble_model_text_report",
    "build_ensemble_model_markdown_report",
    "check_ensemble_model_health",
    "validate_ensemble_model_health_report",
    "summarize_ensemble_model_health_report",
    "build_ensemble_model_validation_report",
    "validate_ensemble_model_validation_report",
    "summarize_ensemble_model_validation_report",
    "enforce_ensemble_model_safety_boundary",
    "assert_ensemble_model_safety_boundary",
    "summarize_ensemble_model_safety_boundary",
    "build_phase_141_handoff_report",
    "validate_phase_141_handoff_report",
    "summarize_phase_141_handoff_report",
    "run_ensemble_model_pipeline",
    "validate_ensemble_model_pipeline_result",
    "summarize_ensemble_model_pipeline_result",
]
