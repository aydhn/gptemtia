"""Phase 133: Advanced Regime Validation and No-Lookahead Acceptance Package.

Provides local-only, research-only validation gates, no-lookahead checks,
metadata-only news enforcement, non-signal guarantees, component acceptance (Phases 127-132),
findings registries, and Phase 134 handoffs.
"""

from advanced_regime_validation_acceptance.regime_validation_acceptance_config import (
    RegimeValidationAcceptanceProfile,
    get_regime_validation_acceptance_profile,
    get_default_regime_validation_acceptance_profile,
    list_regime_validation_acceptance_profiles,
    validate_regime_validation_acceptance_profiles,
)
from advanced_regime_validation_acceptance.regime_validation_acceptance_labels import (
    list_regime_validation_acceptance_domain_labels,
    list_regime_validation_acceptance_status_labels,
    list_regime_validation_acceptance_severity_labels,
    validate_regime_validation_acceptance_domain_label,
    validate_regime_validation_acceptance_status_label,
    validate_regime_validation_acceptance_severity_label,
)
from advanced_regime_validation_acceptance.regime_validation_acceptance_models import (
    RegimeValidationAcceptanceProfileItem,
    RegimeValidationGate,
    RegimeAcceptanceCheckItem,
    RegimeValidationFinding,
    RegimeAcceptanceScore,
    RegimeValidationAcceptanceManifest,
    RegimeAcceptanceManualReviewItem,
)
from advanced_regime_validation_acceptance.regime_validation_acceptance_profile_registry import (
    build_regime_validation_acceptance_profile_registry,
    summarize_regime_validation_acceptance_profiles,
)
from advanced_regime_validation_acceptance.regime_validation_acceptance_domain_registry import (
    build_regime_validation_acceptance_domain_registry,
    summarize_regime_validation_acceptance_domains,
)
from advanced_regime_validation_acceptance.regime_validation_gates import (
    build_regime_validation_gate_registry,
    validate_regime_validation_gate,
    summarize_regime_validation_gates,
)
from advanced_regime_validation_acceptance.regime_no_lookahead_acceptance import (
    build_regime_no_lookahead_acceptance_report,
    validate_no_future_join_records,
    validate_no_negative_shift_usage,
    summarize_regime_no_lookahead_acceptance,
)
from advanced_regime_validation_acceptance.regime_timestamp_order_acceptance import (
    build_regime_timestamp_order_acceptance_report,
    validate_timestamp_monotonicity,
    validate_context_timestamp_not_future,
    summarize_regime_timestamp_order_acceptance,
)
from advanced_regime_validation_acceptance.regime_backward_asof_acceptance import (
    build_regime_backward_asof_acceptance_report,
    validate_backward_asof_policy,
    summarize_regime_backward_asof_acceptance,
)
from advanced_regime_validation_acceptance.regime_forbidden_column_acceptance import (
    build_regime_forbidden_column_acceptance_report,
    validate_forbidden_regime_columns,
    summarize_regime_forbidden_column_acceptance,
)
from advanced_regime_validation_acceptance.regime_metadata_only_news_acceptance import (
    build_regime_metadata_only_news_acceptance_report,
    validate_metadata_only_news_acceptance,
    validate_no_forbidden_news_content,
    summarize_metadata_only_news_acceptance,
)
from advanced_regime_validation_acceptance.regime_source_preservation_acceptance import (
    build_regime_source_preservation_acceptance_report,
    validate_source_preservation_action,
    summarize_source_preservation_acceptance,
)
from advanced_regime_validation_acceptance.regime_non_signal_acceptance import (
    build_regime_non_signal_acceptance_report,
    validate_non_signal_text,
    summarize_non_signal_acceptance,
)
from advanced_regime_validation_acceptance.regime_target_label_prediction_absence import (
    build_regime_target_label_prediction_absence_report,
    validate_no_target_label_prediction_columns,
    validate_no_target_label_prediction_text,
    summarize_target_label_prediction_absence,
)
from advanced_regime_validation_acceptance.regime_model_execution_absence import (
    build_regime_model_execution_absence_report,
    validate_no_model_execution_flags,
    validate_no_model_execution_text,
    summarize_model_execution_absence,
)
from advanced_regime_validation_acceptance.regime_matrix_validation_acceptance import (
    build_regime_matrix_validation_acceptance_report,
    summarize_regime_matrix_validation_acceptance,
)
from advanced_regime_validation_acceptance.candidate_state_validation_acceptance import (
    build_candidate_state_validation_acceptance_report,
    summarize_candidate_state_validation_acceptance,
)
from advanced_regime_validation_acceptance.pseudo_state_validation_acceptance import (
    build_pseudo_state_validation_acceptance_report,
    summarize_pseudo_state_validation_acceptance,
)
from advanced_regime_validation_acceptance.transition_validation_acceptance import (
    build_transition_validation_acceptance_report,
    summarize_transition_validation_acceptance,
)
from advanced_regime_validation_acceptance.cross_asset_regime_validation_acceptance import (
    build_cross_asset_regime_validation_acceptance_report,
    summarize_cross_asset_regime_validation_acceptance,
)
from advanced_regime_validation_acceptance.macro_event_news_validation_acceptance import (
    build_macro_event_news_validation_acceptance_report,
    summarize_macro_event_news_validation_acceptance,
)
from advanced_regime_validation_acceptance.regime_validation_dependency_acceptance import (
    build_regime_validation_dependency_acceptance_report,
    summarize_regime_validation_dependency_acceptance,
)
from advanced_regime_validation_acceptance.regime_quality_dependency_acceptance import (
    build_regime_quality_dependency_acceptance_report,
    summarize_regime_quality_dependency_acceptance,
)
from advanced_regime_validation_acceptance.regime_validation_findings import (
    build_regime_validation_findings_registry,
    create_regime_validation_finding,
    summarize_regime_validation_findings,
)
from advanced_regime_validation_acceptance.regime_manual_review_acceptance import (
    build_regime_manual_review_acceptance_queue,
    summarize_regime_manual_review_acceptance_queue,
)
from advanced_regime_validation_acceptance.regime_acceptance_scoring import (
    calculate_regime_acceptance_score,
    build_regime_acceptance_score_report,
    classify_regime_acceptance_score,
    summarize_regime_acceptance_scores,
)
from advanced_regime_validation_acceptance.regime_validation_acceptance_manifest import (
    create_regime_validation_acceptance_manifest,
    build_regime_validation_acceptance_manifest,
    summarize_regime_validation_acceptance_manifest,
)
from advanced_regime_validation_acceptance.regime_validation_acceptance_health import (
    build_regime_validation_acceptance_health_check,
    summarize_regime_validation_acceptance_health,
)
from advanced_regime_validation_acceptance.regime_validation_acceptance_validation import (
    validate_regime_validation_acceptance_profile_registry,
    validate_regime_validation_gate_registry,
    validate_regime_validation_acceptance_manifest,
    validate_no_forbidden_regime_acceptance_claims,
    build_regime_validation_acceptance_validation_report,
)
from advanced_regime_validation_acceptance.regime_validation_acceptance_safety_boundary import (
    build_regime_validation_acceptance_safety_boundary,
    build_regime_validation_acceptance_no_go_conditions,
    build_regime_validation_acceptance_safe_go_conditions,
    summarize_regime_validation_acceptance_safety_boundary,
)
from advanced_regime_validation_acceptance.phase_134_handoff import (
    build_phase_134_regime_featurestore_integration_handoff_report,
    summarize_phase_134_handoff,
)
from advanced_regime_validation_acceptance.regime_validation_acceptance_pipeline import (
    RegimeValidationAcceptancePipeline,
)

__all__ = [
    "RegimeValidationAcceptanceProfile",
    "get_regime_validation_acceptance_profile",
    "get_default_regime_validation_acceptance_profile",
    "list_regime_validation_acceptance_profiles",
    "validate_regime_validation_acceptance_profiles",
    "list_regime_validation_acceptance_domain_labels",
    "list_regime_validation_acceptance_status_labels",
    "list_regime_validation_acceptance_severity_labels",
    "validate_regime_validation_acceptance_domain_label",
    "validate_regime_validation_acceptance_status_label",
    "validate_regime_validation_acceptance_severity_label",
    "RegimeValidationAcceptanceProfileItem",
    "RegimeValidationGate",
    "RegimeAcceptanceCheckItem",
    "RegimeValidationFinding",
    "RegimeAcceptanceScore",
    "RegimeValidationAcceptanceManifest",
    "RegimeAcceptanceManualReviewItem",
    "build_regime_validation_acceptance_profile_registry",
    "summarize_regime_validation_acceptance_profiles",
    "build_regime_validation_acceptance_domain_registry",
    "summarize_regime_validation_acceptance_domains",
    "build_regime_validation_gate_registry",
    "validate_regime_validation_gate",
    "summarize_regime_validation_gates",
    "build_regime_no_lookahead_acceptance_report",
    "validate_no_future_join_records",
    "validate_no_negative_shift_usage",
    "summarize_regime_no_lookahead_acceptance",
    "build_regime_timestamp_order_acceptance_report",
    "validate_timestamp_monotonicity",
    "validate_context_timestamp_not_future",
    "summarize_regime_timestamp_order_acceptance",
    "build_regime_backward_asof_acceptance_report",
    "validate_backward_asof_policy",
    "summarize_regime_backward_asof_acceptance",
    "build_regime_forbidden_column_acceptance_report",
    "validate_forbidden_regime_columns",
    "summarize_regime_forbidden_column_acceptance",
    "build_regime_metadata_only_news_acceptance_report",
    "validate_metadata_only_news_acceptance",
    "validate_no_forbidden_news_content",
    "summarize_metadata_only_news_acceptance",
    "build_regime_source_preservation_acceptance_report",
    "validate_source_preservation_action",
    "summarize_source_preservation_acceptance",
    "build_regime_non_signal_acceptance_report",
    "validate_non_signal_text",
    "summarize_non_signal_acceptance",
    "build_regime_target_label_prediction_absence_report",
    "validate_no_target_label_prediction_columns",
    "validate_no_target_label_prediction_text",
    "summarize_target_label_prediction_absence",
    "build_regime_model_execution_absence_report",
    "validate_no_model_execution_flags",
    "validate_no_model_execution_text",
    "summarize_model_execution_absence",
    "build_regime_matrix_validation_acceptance_report",
    "summarize_regime_matrix_validation_acceptance",
    "build_candidate_state_validation_acceptance_report",
    "summarize_candidate_state_validation_acceptance",
    "build_pseudo_state_validation_acceptance_report",
    "summarize_pseudo_state_validation_acceptance",
    "build_transition_validation_acceptance_report",
    "summarize_transition_validation_acceptance",
    "build_cross_asset_regime_validation_acceptance_report",
    "summarize_cross_asset_regime_validation_acceptance",
    "build_macro_event_news_validation_acceptance_report",
    "summarize_macro_event_news_validation_acceptance",
    "build_regime_validation_dependency_acceptance_report",
    "summarize_regime_validation_dependency_acceptance",
    "build_regime_quality_dependency_acceptance_report",
    "summarize_regime_quality_dependency_acceptance",
    "build_regime_validation_findings_registry",
    "create_regime_validation_finding",
    "summarize_regime_validation_findings",
    "build_regime_manual_review_acceptance_queue",
    "summarize_regime_manual_review_acceptance_queue",
    "calculate_regime_acceptance_score",
    "build_regime_acceptance_score_report",
    "classify_regime_acceptance_score",
    "summarize_regime_acceptance_scores",
    "create_regime_validation_acceptance_manifest",
    "build_regime_validation_acceptance_manifest",
    "summarize_regime_validation_acceptance_manifest",
    "build_regime_validation_acceptance_health_check",
    "summarize_regime_validation_acceptance_health",
    "validate_regime_validation_acceptance_profile_registry",
    "validate_regime_validation_gate_registry",
    "validate_regime_validation_acceptance_manifest",
    "validate_no_forbidden_regime_acceptance_claims",
    "build_regime_validation_acceptance_validation_report",
    "build_regime_validation_acceptance_safety_boundary",
    "build_regime_validation_acceptance_no_go_conditions",
    "build_regime_validation_acceptance_safe_go_conditions",
    "summarize_regime_validation_acceptance_safety_boundary",
    "build_phase_134_regime_featurestore_integration_handoff_report",
    "summarize_phase_134_handoff",
    "RegimeValidationAcceptancePipeline",
]
