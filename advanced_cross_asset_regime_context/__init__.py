"""Phase 131: Cross-Asset Regime Context Expansion Package.

Exports core configuration, labels, models, registries, contracts, guards,
pipeline, health, validation, safety boundary, and Phase 132 handoff components.
"""

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    CROSS_ASSET_REGIME_PROFILES,
    get_cross_asset_regime_profile,
    list_cross_asset_regime_profiles,
    validate_cross_asset_regime_profiles,
    get_default_cross_asset_regime_profile,
)
from advanced_cross_asset_regime_context.cross_asset_regime_labels import (
    CROSS_ASSET_REGIME_DOMAIN_LABELS,
    CROSS_ASSET_REGIME_STATUS_LABELS,
    CROSS_ASSET_RELATIONSHIP_LABELS,
    list_cross_asset_regime_domain_labels,
    list_cross_asset_regime_status_labels,
    list_cross_asset_relationship_labels,
    validate_cross_asset_regime_domain_label,
    validate_cross_asset_regime_status_label,
    validate_cross_asset_relationship_label,
)
from advanced_cross_asset_regime_context.cross_asset_regime_models import (
    CrossAssetRegimeProfileItem,
    CrossAssetRegimeEntity,
    CrossAssetRegimePair,
    CrossAssetRelationshipTaxonomyItem,
    CrossAssetContextContract,
    CrossAssetContextFinding,
    CrossAssetContextScore,
    CrossAssetRegimeManifest,
    CrossAssetManualReviewItem,
)
from advanced_cross_asset_regime_context.cross_asset_regime_pipeline import (
    CrossAssetRegimePipeline,
)
from advanced_cross_asset_regime_context.phase_132_handoff import (
    build_phase_132_macro_event_news_regime_context_handoff_report,
    summarize_phase_132_handoff,
)

__all__ = [
    "CrossAssetRegimeProfile",
    "CROSS_ASSET_REGIME_PROFILES",
    "get_cross_asset_regime_profile",
    "list_cross_asset_regime_profiles",
    "validate_cross_asset_regime_profiles",
    "get_default_cross_asset_regime_profile",
    "CROSS_ASSET_REGIME_DOMAIN_LABELS",
    "CROSS_ASSET_REGIME_STATUS_LABELS",
    "CROSS_ASSET_RELATIONSHIP_LABELS",
    "list_cross_asset_regime_domain_labels",
    "list_cross_asset_regime_status_labels",
    "list_cross_asset_relationship_labels",
    "validate_cross_asset_regime_domain_label",
    "validate_cross_asset_regime_status_label",
    "validate_cross_asset_relationship_label",
    "CrossAssetRegimeProfileItem",
    "CrossAssetRegimeEntity",
    "CrossAssetRegimePair",
    "CrossAssetRelationshipTaxonomyItem",
    "CrossAssetContextContract",
    "CrossAssetContextFinding",
    "CrossAssetContextScore",
    "CrossAssetRegimeManifest",
    "CrossAssetManualReviewItem",
    "CrossAssetRegimePipeline",
    "build_phase_132_macro_event_news_regime_context_handoff_report",
    "summarize_phase_132_handoff",
]
