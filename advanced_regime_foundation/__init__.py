"""Phase 126: Regime Classification and Market Behavior Foundation.

First phase of the Phase 126-135 Regime Classification and Market Behavior block.
Establishes market behavior taxonomy, regime state taxonomy, regime family contracts,
validation/quality dependencies, non-signal policies, and Phase 127 handoff.
"""

from advanced_regime_foundation.regime_foundation_config import (
    RegimeFoundationProfile,
    get_regime_foundation_profile,
    list_regime_foundation_profiles,
    validate_regime_foundation_profiles,
    get_default_regime_foundation_profile,
)
from advanced_regime_foundation.regime_foundation_labels import (
    list_regime_foundation_domain_labels,
    list_regime_family_labels,
    list_regime_status_labels,
    validate_regime_foundation_domain_label,
    validate_regime_family_label,
    validate_regime_status_label,
)
from advanced_regime_foundation.regime_foundation_models import (
    RegimeFoundationProfileItem,
    MarketBehaviorTaxonomyItem,
    RegimeStateTaxonomyItem,
    RegimeFamilyItem,
    RegimeInputFeatureContract,
    RegimeDependencyItem,
    RegimeStateOutputSchema,
    RegimeFoundationManifest,
)
from advanced_regime_foundation.regime_foundation_profile_registry import (
    build_regime_foundation_profile_registry,
)
from advanced_regime_foundation.regime_foundation_domain_registry import (
    build_regime_foundation_domain_registry,
)
from advanced_regime_foundation.market_behavior_taxonomy import (
    build_market_behavior_taxonomy_registry,
    summarize_market_behavior_taxonomy,
)
from advanced_regime_foundation.regime_state_taxonomy import (
    build_regime_state_taxonomy_registry,
    summarize_regime_state_taxonomy,
)
from advanced_regime_foundation.regime_family_registry import (
    build_regime_family_registry,
    summarize_regime_family_registry,
)
from advanced_regime_foundation.volatility_regime_families import (
    build_volatility_regime_family_registry,
    summarize_volatility_regime_families,
)
from advanced_regime_foundation.trend_regime_families import (
    build_trend_regime_family_registry,
    summarize_trend_regime_families,
)
from advanced_regime_foundation.range_regime_families import (
    build_range_regime_family_registry,
    summarize_range_regime_families,
)
from advanced_regime_foundation.liquidity_regime_placeholders import (
    build_liquidity_regime_placeholder_registry,
    summarize_liquidity_regime_placeholders,
)
from advanced_regime_foundation.macro_regime_context import (
    build_macro_regime_context_registry,
    summarize_macro_regime_context,
)
from advanced_regime_foundation.event_regime_context import (
    build_event_regime_context_registry,
    summarize_event_regime_context,
)
from advanced_regime_foundation.news_metadata_regime_context import (
    build_news_metadata_regime_context_registry,
    summarize_news_metadata_regime_context,
)
from advanced_regime_foundation.cross_asset_regime_context import (
    build_cross_asset_regime_context_registry,
    summarize_cross_asset_regime_context,
)
from advanced_regime_foundation.regime_input_feature_contracts import (
    build_regime_input_feature_contract_registry,
    validate_regime_input_feature_contract,
    summarize_regime_input_feature_contracts,
)
from advanced_regime_foundation.regime_factor_dependencies import (
    build_regime_factor_dependency_registry,
    summarize_regime_factor_dependencies,
)
from advanced_regime_foundation.regime_validation_dependencies import (
    build_regime_validation_dependency_registry,
    summarize_regime_validation_dependencies,
)
from advanced_regime_foundation.regime_quality_dependencies import (
    build_regime_quality_dependency_registry,
    summarize_regime_quality_dependencies,
)
from advanced_regime_foundation.regime_state_output_schema import (
    build_regime_state_output_schema_registry,
    validate_regime_state_output_schema,
    summarize_regime_state_output_schema,
)
from advanced_regime_foundation.regime_namespace_registry import (
    build_regime_namespace_registry,
    build_regime_state_name,
    validate_regime_state_name,
    summarize_regime_namespace_registry,
)
from advanced_regime_foundation.regime_non_signal_policies import (
    build_regime_non_signal_policy_registry,
    validate_regime_non_signal_text,
    summarize_regime_non_signal_policies,
)
from advanced_regime_foundation.regime_forbidden_claims import (
    build_regime_forbidden_claim_registry,
    validate_regime_forbidden_claims,
    summarize_regime_forbidden_claims,
)
from advanced_regime_foundation.regime_foundation_manifest import (
    build_regime_foundation_manifest,
    create_regime_foundation_manifest,
    summarize_regime_foundation_manifest,
)
from advanced_regime_foundation.regime_foundation_report_builder import (
    build_regime_foundation_profile_markdown_report,
    build_market_behavior_taxonomy_markdown_report,
    build_regime_state_taxonomy_markdown_report,
    build_regime_family_markdown_report,
    build_regime_context_markdown_report,
    build_regime_contract_dependency_markdown_report,
    build_regime_manifest_markdown_report,
    build_regime_health_markdown_report,
    build_regime_validation_markdown_report,
    build_regime_safety_markdown_report,
    build_phase_127_handoff_markdown_report,
    build_regime_foundation_disclaimer,
)
from advanced_regime_foundation.regime_foundation_safety_boundary import (
    build_regime_foundation_safety_boundary,
    build_regime_foundation_no_go_conditions,
    build_regime_foundation_safe_go_conditions,
    summarize_regime_foundation_safety_boundary,
)
from advanced_regime_foundation.regime_foundation_health import (
    build_regime_foundation_health_check,
    summarize_regime_foundation_health,
)
from advanced_regime_foundation.regime_foundation_validation import (
    validate_regime_foundation_profile_registry,
    validate_market_behavior_taxonomy,
    validate_regime_state_taxonomy,
    validate_regime_family_registry,
    validate_regime_foundation_manifest,
    validate_no_forbidden_regime_claims,
    build_regime_foundation_validation_report,
)
from advanced_regime_foundation.phase_127_handoff import (
    build_phase_127_regime_feature_matrix_handoff_report,
    summarize_phase_127_handoff,
)
from advanced_regime_foundation.regime_foundation_pipeline import (
    RegimeFoundationPipeline,
)

__all__ = [
    "RegimeFoundationProfile",
    "get_regime_foundation_profile",
    "list_regime_foundation_profiles",
    "validate_regime_foundation_profiles",
    "get_default_regime_foundation_profile",
    "list_regime_foundation_domain_labels",
    "list_regime_family_labels",
    "list_regime_status_labels",
    "validate_regime_foundation_domain_label",
    "validate_regime_family_label",
    "validate_regime_status_label",
    "RegimeFoundationProfileItem",
    "MarketBehaviorTaxonomyItem",
    "RegimeStateTaxonomyItem",
    "RegimeFamilyItem",
    "RegimeInputFeatureContract",
    "RegimeDependencyItem",
    "RegimeStateOutputSchema",
    "RegimeFoundationManifest",
    "build_regime_foundation_profile_registry",
    "build_regime_foundation_domain_registry",
    "build_market_behavior_taxonomy_registry",
    "summarize_market_behavior_taxonomy",
    "build_regime_state_taxonomy_registry",
    "summarize_regime_state_taxonomy",
    "build_regime_family_registry",
    "summarize_regime_family_registry",
    "build_volatility_regime_family_registry",
    "summarize_volatility_regime_families",
    "build_trend_regime_family_registry",
    "summarize_trend_regime_families",
    "build_range_regime_family_registry",
    "summarize_range_regime_families",
    "build_liquidity_regime_placeholder_registry",
    "summarize_liquidity_regime_placeholders",
    "build_macro_regime_context_registry",
    "summarize_macro_regime_context",
    "build_event_regime_context_registry",
    "summarize_event_regime_context",
    "build_news_metadata_regime_context_registry",
    "summarize_news_metadata_regime_context",
    "build_cross_asset_regime_context_registry",
    "summarize_cross_asset_regime_context",
    "build_regime_input_feature_contract_registry",
    "validate_regime_input_feature_contract",
    "summarize_regime_input_feature_contracts",
    "build_regime_factor_dependency_registry",
    "summarize_regime_factor_dependencies",
    "build_regime_validation_dependency_registry",
    "summarize_regime_validation_dependencies",
    "build_regime_quality_dependency_registry",
    "summarize_regime_quality_dependencies",
    "build_regime_state_output_schema_registry",
    "validate_regime_state_output_schema",
    "summarize_regime_state_output_schema",
    "build_regime_namespace_registry",
    "build_regime_state_name",
    "validate_regime_state_name",
    "summarize_regime_namespace_registry",
    "build_regime_non_signal_policy_registry",
    "validate_regime_non_signal_text",
    "summarize_regime_non_signal_policies",
    "build_regime_forbidden_claim_registry",
    "validate_regime_forbidden_claims",
    "summarize_regime_forbidden_claims",
    "build_regime_foundation_manifest",
    "create_regime_foundation_manifest",
    "summarize_regime_foundation_manifest",
    "build_regime_foundation_profile_markdown_report",
    "build_market_behavior_taxonomy_markdown_report",
    "build_regime_state_taxonomy_markdown_report",
    "build_regime_family_markdown_report",
    "build_regime_context_markdown_report",
    "build_regime_contract_dependency_markdown_report",
    "build_regime_manifest_markdown_report",
    "build_regime_health_markdown_report",
    "build_regime_validation_markdown_report",
    "build_regime_safety_markdown_report",
    "build_phase_127_handoff_markdown_report",
    "build_regime_foundation_disclaimer",
    "build_regime_foundation_safety_boundary",
    "build_regime_foundation_no_go_conditions",
    "build_regime_foundation_safe_go_conditions",
    "summarize_regime_foundation_safety_boundary",
    "build_regime_foundation_health_check",
    "summarize_regime_foundation_health",
    "validate_regime_foundation_profile_registry",
    "validate_market_behavior_taxonomy",
    "validate_regime_state_taxonomy",
    "validate_regime_family_registry",
    "validate_regime_foundation_manifest",
    "validate_no_forbidden_regime_claims",
    "build_regime_foundation_validation_report",
    "build_phase_127_regime_feature_matrix_handoff_report",
    "summarize_phase_127_handoff",
    "RegimeFoundationPipeline",
]
