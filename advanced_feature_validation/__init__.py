"""Phase 121: Advanced Feature Validation and No-Lookahead Guard Layer.

Provides comprehensive feature validation, forbidden column enforcement,
no-lookahead guards, data quality integrity checks, and leakage detection.
Strictly non-signal, local/offline, research use only.
"""

from advanced_feature_validation.feature_validation_config import (
    FeatureValidationProfile,
    get_feature_validation_profile,
    list_feature_validation_profiles,
    get_default_feature_validation_profile,
    validate_feature_validation_profiles,
)

__version__ = "1.21.0"
__phase__ = 121
__target_final_phase__ = 160
__next_phase__ = 122

__all__ = [
    "FeatureValidationProfile",
    "get_feature_validation_profile",
    "list_feature_validation_profiles",
    "get_default_feature_validation_profile",
    "validate_feature_validation_profiles",
    "__version__",
    "__phase__",
    "__target_final_phase__",
    "__next_phase__",
]
