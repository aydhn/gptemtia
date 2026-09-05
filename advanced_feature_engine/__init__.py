"""Phase 116 — Advanced Indicator/Feature/Factor Engine Foundation.

Provides canonical feature contracts, indicator registry, feature schemas, factor schemas,
and non-signal feature computation layers for research and offline analytics.
"""

from advanced_feature_engine.feature_engine_config import (
    FeatureEngineProfile,
    get_feature_engine_profile,
    list_feature_engine_profiles,
    get_default_feature_engine_profile,
)

__all__ = [
    "FeatureEngineProfile",
    "get_feature_engine_profile",
    "list_feature_engine_profiles",
    "get_default_feature_engine_profile",
]
