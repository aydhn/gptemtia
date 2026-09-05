"""Phase 120 Macro/Calendar/News Feature Fusion Package."""

from advanced_feature_fusion.fusion_feature_config import (
    FusionFeatureProfile,
    get_fusion_feature_profile,
    list_fusion_feature_profiles,
    get_default_fusion_feature_profile,
)
from advanced_feature_fusion.fusion_feature_profile_registry import (
    get_fusion_feature_profiles_summary,
)
from advanced_feature_fusion.fusion_feature_domain_registry import (
    get_fusion_feature_domains_summary,
)
from advanced_feature_fusion.fusion_asof_join_policies import (
    safe_fusion_asof_join_backward,
)
from advanced_feature_fusion.no_lookahead_fusion_guard import (
    validate_no_future_fusion_join,
    validate_no_forbidden_fusion_columns,
    validate_no_full_article_columns,
    validate_no_negative_shift_usage,
)
from advanced_feature_fusion.fusion_feature_matrix import (
    build_fusion_feature_matrix,
)
from advanced_feature_fusion.fusion_feature_pipeline import (
    run_fusion_feature_pipeline,
)
from advanced_feature_fusion.fusion_feature_health import (
    check_fusion_feature_health,
)

__version__ = "1.0.0"

__all__ = [
    "FusionFeatureProfile",
    "get_fusion_feature_profile",
    "list_fusion_feature_profiles",
    "get_default_fusion_feature_profile",
    "get_fusion_feature_profiles_summary",
    "get_fusion_feature_domains_summary",
    "safe_fusion_asof_join_backward",
    "validate_no_future_fusion_join",
    "validate_no_forbidden_fusion_columns",
    "validate_no_full_article_columns",
    "validate_no_negative_shift_usage",
    "build_fusion_feature_matrix",
    "run_fusion_feature_pipeline",
    "check_fusion_feature_health",
]
