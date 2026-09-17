# -*- coding: utf-8 -*-
"""Phase 147: Walk-Forward Validation and Out-of-Sample Benchmarking Package.

Provides local, offline, non-executing validation contracts, split contracts,
benchmark baselines, metric placeholders, and Phase 148 handoff report.
"""

from advanced_walk_forward_validation.walk_forward_config import (
    WalkForwardProfile,
    get_walk_forward_profile,
    get_default_walk_forward_profile,
    list_walk_forward_profiles,
    validate_walk_forward_profiles,
)
from advanced_walk_forward_validation.walk_forward_labels import (
    DOMAIN_LABELS,
    STATUS_LABELS,
    EXECUTION_LABELS,
)
from advanced_walk_forward_validation.walk_forward_models import (
    WalkForwardProfileItem,
    WalkForwardValidationContract,
    SplitContract,
    BenchmarkContract,
    BenchmarkPlaceholder,
    ValidationMetricPlaceholder,
    ValidationGuardItem,
    ValidationDisabledExecutionItem,
    WalkForwardFinding,
    WalkForwardReadinessScore,
    WalkForwardValidationManifest,
    WalkForwardManualReviewItem,
)
from advanced_walk_forward_validation.walk_forward_pipeline import (
    WalkForwardValidationPipeline,
)

__version__ = "1.147.0"
__all__ = [
    "WalkForwardProfile",
    "get_walk_forward_profile",
    "get_default_walk_forward_profile",
    "list_walk_forward_profiles",
    "validate_walk_forward_profiles",
    "DOMAIN_LABELS",
    "STATUS_LABELS",
    "EXECUTION_LABELS",
    "WalkForwardProfileItem",
    "WalkForwardValidationContract",
    "SplitContract",
    "BenchmarkContract",
    "BenchmarkPlaceholder",
    "ValidationMetricPlaceholder",
    "ValidationGuardItem",
    "ValidationDisabledExecutionItem",
    "WalkForwardFinding",
    "WalkForwardReadinessScore",
    "WalkForwardValidationManifest",
    "WalkForwardManualReviewItem",
    "WalkForwardValidationPipeline",
]
