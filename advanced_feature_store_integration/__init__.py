"""Phase 124 Advanced Feature Store Integration Package.

Provides local/offline, validation-aware, quality/drift metadata storage
in a non-signal feature store layer.
"""

from advanced_feature_store_integration.feature_store_integration_config import (
    FeatureStoreIntegrationProfile,
    get_feature_store_integration_profile,
    list_feature_store_integration_profiles,
    validate_feature_store_integration_profiles,
    get_default_feature_store_integration_profile,
)
from advanced_feature_store_integration.feature_store_integration_labels import (
    FEATURE_STORE_INTEGRATION_DOMAIN_LABELS,
    FEATURE_STORE_STATUS_LABELS,
    FEATURE_STORE_ENTITY_TYPE_LABELS,
    list_feature_store_integration_domain_labels,
    list_feature_store_status_labels,
    list_feature_store_entity_type_labels,
    validate_feature_store_integration_domain_label,
    validate_feature_store_status_label,
    validate_feature_store_entity_type_label,
)
from advanced_feature_store_integration.feature_store_integration_models import (
    FeatureStoreIntegrationProfileItem,
    FeatureStoreContract,
    FeatureStoreEntity,
    FeatureStoreFeatureRecord,
    FeatureStoreFactorRecord,
    FeatureStoreSchemaRecord,
    FeatureStoreLineageReference,
    FeatureStoreValidationStatus,
    FeatureStoreQualityScoreRecord,
    FeatureStoreDriftScoreRecord,
    FeatureStoreManualReviewBlocker,
    FeatureStoreMetadataManifest,
)
from advanced_feature_store_integration.feature_store_integration_profile_registry import (
    build_feature_store_integration_profile_registry,
    summarize_feature_store_integration_profile_registry,
)
from advanced_feature_store_integration.feature_store_integration_domain_registry import (
    build_feature_store_integration_domain_registry,
    summarize_feature_store_integration_domain_registry,
)
from advanced_feature_store_integration.feature_store_contract_registry import (
    build_feature_store_contract_registry,
    summarize_feature_store_contract_registry,
)
from advanced_feature_store_integration.feature_store_entity_registry import (
    build_feature_store_entity_registry,
    summarize_feature_store_entity_registry,
)
from advanced_feature_store_integration.feature_store_feature_registry import (
    build_feature_store_feature_registry,
    summarize_feature_store_feature_registry,
)
from advanced_feature_store_integration.feature_store_factor_registry import (
    build_feature_store_factor_registry,
    summarize_feature_store_factor_registry,
)
from advanced_feature_store_integration.feature_store_namespace_registry import (
    build_feature_store_namespace_registry,
    build_store_feature_key,
    validate_store_feature_key,
    summarize_feature_store_namespace_registry,
)
from advanced_feature_store_integration.feature_store_schema_registry import (
    build_feature_store_schema_registry,
    validate_feature_store_schema,
    summarize_feature_store_schema_registry,
)
from advanced_feature_store_integration.feature_store_version_policies import (
    build_feature_store_version_policy_registry,
    validate_store_version_policy,
    summarize_feature_store_version_policies,
)
from advanced_feature_store_integration.feature_store_partition_policies import (
    build_feature_store_partition_policy_registry,
    summarize_feature_store_partition_policies,
)
from advanced_feature_store_integration.feature_store_lineage_references import (
    build_feature_store_lineage_reference_registry,
    summarize_feature_store_lineage_references,
)
from advanced_feature_store_integration.feature_store_validation_status import (
    build_feature_store_validation_status_registry,
    summarize_feature_store_validation_status,
)
from advanced_feature_store_integration.feature_store_quality_scores import (
    build_feature_store_quality_score_registry,
    summarize_feature_store_quality_scores,
)
from advanced_feature_store_integration.feature_store_drift_scores import (
    build_feature_store_drift_score_registry,
    summarize_feature_store_drift_scores,
)
from advanced_feature_store_integration.feature_store_manual_review_blockers import (
    build_feature_store_manual_review_blocker_registry,
    summarize_feature_store_manual_review_blockers,
)
from advanced_feature_store_integration.feature_store_metadata_manifest import (
    create_feature_store_metadata_manifest,
    build_feature_store_metadata_manifest,
    summarize_feature_store_metadata_manifest,
)
from advanced_feature_store_integration.feature_store_read_contracts import (
    build_feature_store_read_contract_registry,
    validate_feature_store_read_request,
    summarize_feature_store_read_contracts,
)
from advanced_feature_store_integration.feature_store_write_contracts import (
    build_feature_store_write_contract_registry,
    validate_feature_store_write_request,
    summarize_feature_store_write_contracts,
)
from advanced_feature_store_integration.feature_store_query_contracts import (
    build_feature_store_query_contract_registry,
    validate_feature_store_query_request,
    summarize_feature_store_query_contracts,
)
from advanced_feature_store_integration.feature_store_non_signal_policies import (
    build_feature_store_non_signal_policy_registry,
    validate_feature_store_non_signal_text,
    summarize_feature_store_non_signal_policies,
)
from advanced_feature_store_integration.feature_store_forbidden_column_policies import (
    build_feature_store_forbidden_column_policy_registry,
    validate_feature_store_forbidden_columns,
    summarize_feature_store_forbidden_column_policies,
)
from advanced_feature_store_integration.feature_store_source_preservation_policies import (
    build_feature_store_source_preservation_policy_registry,
    validate_source_preservation_policy,
    summarize_feature_store_source_preservation_policies,
)
from advanced_feature_store_integration.feature_store_catalog_reports import (
    build_feature_store_feature_catalog_report,
    build_feature_store_factor_catalog_report,
    build_feature_store_quality_drift_catalog_report,
    build_feature_store_validation_catalog_report,
    summarize_feature_store_catalog_report,
)
from advanced_feature_store_integration.feature_store_integration_report_builder import (
    build_feature_store_integration_disclaimer,
    build_feature_store_integration_profile_markdown_report,
    build_feature_store_contract_markdown_report,
    build_feature_store_catalog_markdown_report,
    build_feature_store_manifest_markdown_report,
    build_feature_store_policy_markdown_report,
    build_feature_store_health_markdown_report,
    build_feature_store_validation_markdown_report,
    build_feature_store_safety_markdown_report,
    build_phase_125_handoff_markdown_report,
)
from advanced_feature_store_integration.feature_store_integration_pipeline import (
    FeatureStoreIntegrationPipeline,
)
from advanced_feature_store_integration.feature_store_integration_health import (
    build_feature_store_integration_health_check,
    summarize_feature_store_integration_health,
)
from advanced_feature_store_integration.feature_store_integration_validation import (
    build_feature_store_integration_validation_report,
    validate_no_forbidden_feature_store_claims,
)
from advanced_feature_store_integration.feature_store_integration_safety_boundary import (
    build_feature_store_integration_safety_boundary,
    build_feature_store_integration_no_go_conditions,
    build_feature_store_integration_safe_go_conditions,
    summarize_feature_store_integration_safety_boundary,
)
from advanced_feature_store_integration.phase_125_handoff import (
    HANDOFF_ITEMS,
    build_phase_125_feature_factor_engine_acceptance_handoff_report,
    summarize_phase_125_handoff,
)

__version__ = "124.0.0"
CURRENT_PHASE = 124
TARGET_FINAL_PHASE = 160
NEXT_PHASE = 125
NON_SIGNAL_INVARIANT = True
