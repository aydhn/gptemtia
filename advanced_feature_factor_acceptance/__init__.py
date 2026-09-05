"""Phase 125 Advanced Feature/Factor Engine Acceptance Package.

Provides local/offline, dry-run compliant, non-signal end-to-end acceptance reporting,
gate evaluations, safety manifests, and Phase 126 regime classification handoffs.
"""

from advanced_feature_factor_acceptance.feature_factor_acceptance_config import (
    FeatureFactorAcceptanceProfile,
    get_feature_factor_acceptance_profile,
    list_feature_factor_acceptance_profiles,
    validate_feature_factor_acceptance_profiles,
    get_default_feature_factor_acceptance_profile,
)
from advanced_feature_factor_acceptance.feature_factor_acceptance_labels import (
    ACCEPTANCE_DOMAIN_LABELS,
    ACCEPTANCE_STATUS_LABELS,
    list_acceptance_domain_labels,
    list_acceptance_status_labels,
    validate_acceptance_domain_label,
    validate_acceptance_status_label,
)
from advanced_feature_factor_acceptance.feature_factor_acceptance_models import (
    FeatureFactorAcceptanceProfileItem,
    FeatureEngineBlockInventoryItem,
    FeatureEngineBlockDependencyItem,
    FeatureEngineAcceptanceGate,
    FeatureEngineAcceptanceScore,
    FeatureEngineManualReviewItem,
    FeatureEngineComplianceItem,
    FeatureEngineBlockStatusItem,
    Phase116125AcceptanceManifest,
)
from advanced_feature_factor_acceptance.feature_factor_acceptance_profile_registry import (
    build_feature_factor_acceptance_profile_registry,
    summarize_feature_factor_acceptance_profile_registry,
)
from advanced_feature_factor_acceptance.feature_factor_acceptance_domain_registry import (
    build_feature_factor_acceptance_domain_registry,
    summarize_feature_factor_acceptance_domain_registry,
)
from advanced_feature_factor_acceptance.feature_engine_block_inventory import (
    build_feature_engine_block_inventory_report,
    summarize_feature_engine_block_inventory,
)
from advanced_feature_factor_acceptance.feature_engine_block_dependencies import (
    build_feature_engine_block_dependency_report,
    summarize_feature_engine_block_dependencies,
)
from advanced_feature_factor_acceptance.feature_engine_block_acceptance_gates import (
    build_feature_engine_block_acceptance_gate_registry,
    validate_acceptance_gate,
    summarize_acceptance_gates,
)
from advanced_feature_factor_acceptance.feature_engine_block_acceptance_scoring import (
    calculate_feature_engine_block_acceptance_score,
    build_feature_engine_block_acceptance_score_report,
    classify_acceptance_score,
    summarize_acceptance_score,
)
from advanced_feature_factor_acceptance.feature_engine_block_manual_review import (
    build_feature_engine_block_manual_review_queue,
    summarize_feature_engine_block_manual_review_queue,
)
from advanced_feature_factor_acceptance.feature_engine_block_safety_boundary import (
    build_feature_engine_block_safety_boundary_report,
    build_feature_engine_block_no_go_conditions,
    build_feature_engine_block_safe_go_conditions,
    summarize_feature_engine_block_safety_boundary,
)
from advanced_feature_factor_acceptance.feature_engine_block_compliance import (
    build_feature_engine_block_non_signal_compliance_report,
    build_feature_engine_block_no_lookahead_compliance_report,
    build_feature_engine_block_forbidden_column_compliance_report,
    build_feature_engine_block_news_metadata_only_compliance_report,
    build_feature_engine_block_source_preservation_report,
    build_feature_engine_block_feature_store_readiness_report,
    summarize_feature_engine_block_compliance,
)
from advanced_feature_factor_acceptance.feature_engine_block_documentation import (
    build_feature_engine_block_documentation_report,
    summarize_feature_engine_block_documentation,
)
from advanced_feature_factor_acceptance.feature_engine_block_script_contracts import (
    build_feature_engine_block_script_contract_report,
    summarize_feature_engine_block_script_contracts,
)
from advanced_feature_factor_acceptance.feature_engine_block_test_contracts import (
    build_feature_engine_block_test_contract_report,
    summarize_feature_engine_block_test_contracts,
)
from advanced_feature_factor_acceptance.feature_engine_block_status import (
    build_feature_engine_block_status_report,
    summarize_feature_engine_block_status,
)
from advanced_feature_factor_acceptance.phase_116_125_acceptance_manifest import (
    build_phase_116_125_acceptance_manifest,
    create_phase_116_125_acceptance_manifest,
    summarize_phase_116_125_acceptance_manifest,
)
from advanced_feature_factor_acceptance.feature_factor_acceptance_health import (
    build_feature_factor_acceptance_health_check,
    summarize_feature_factor_acceptance_health,
)
from advanced_feature_factor_acceptance.feature_factor_acceptance_validation import (
    validate_feature_factor_acceptance_profile_registry,
    validate_feature_engine_block_inventory,
    validate_feature_engine_block_acceptance_gates,
    validate_phase_116_125_acceptance_manifest,
    validate_no_forbidden_acceptance_claims,
    build_feature_factor_acceptance_validation_report,
)
from advanced_feature_factor_acceptance.phase_126_handoff import (
    build_phase_126_regime_classification_handoff_report,
    summarize_phase_126_handoff,
)
from advanced_feature_factor_acceptance.feature_factor_acceptance_pipeline import (
    FeatureFactorAcceptancePipeline,
)
from advanced_feature_factor_acceptance.feature_factor_acceptance_report_builder import (
    build_feature_factor_acceptance_profile_markdown_report,
    build_feature_engine_inventory_markdown_report,
    build_feature_engine_dependency_markdown_report,
    build_acceptance_gate_markdown_report,
    build_acceptance_score_markdown_report,
    build_manual_review_markdown_report,
    build_compliance_markdown_report,
    build_contract_markdown_report,
    build_acceptance_manifest_markdown_report,
    build_health_markdown_report,
    build_validation_markdown_report,
    build_phase_126_handoff_markdown_report,
    build_feature_factor_acceptance_disclaimer,
)
