"""Phase 123 Feature Quality and Drift Models.

Defines immutable dataclasses for quality metrics, drift metrics, thresholds,
findings, scores, and manifests. Enforces non-signal, non-production, and non-destructive invariants.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass(frozen=True)
class FeatureQualityDriftProfileItem:
    profile_name: str
    description: str
    current_phase: int = 123
    target_final_phase: int = 160
    next_phase: int = 124
    non_signal: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False
    notes: str = ""

    def __post_init__(self):
        if not (0 <= self.current_phase <= 160):
            raise ValueError("Phase must be between 0 and 160")
        if not self.non_signal:
            raise ValueError("Must remain non-signal")
        if self.official_approval or self.production_ready or self.broker_ready:
            raise ValueError("Cannot claim approval, production, or broker readiness")


@dataclass(frozen=True)
class FeatureQualityMetric:
    metric_id: str
    metric_name: str
    domain: str
    description: str
    metric_type: str
    severity: str
    default_threshold: float = 0.0
    non_signal: bool = True
    destructive_action_allowed: bool = False

    def __post_init__(self):
        if not self.non_signal or self.destructive_action_allowed:
            raise ValueError("Violates non-signal or non-destructive invariant")


@dataclass(frozen=True)
class FeatureDriftMetric:
    metric_id: str
    metric_name: str
    domain: str
    description: str
    drift_type: str
    severity: str
    default_threshold: float = 0.0
    non_signal: bool = True
    destructive_action_allowed: bool = False

    def __post_init__(self):
        if not self.non_signal or self.destructive_action_allowed:
            raise ValueError("Violates non-signal or non-destructive invariant")


@dataclass(frozen=True)
class FeatureQualityThreshold:
    threshold_id: str
    metric_id: str
    warning_threshold: float
    critical_threshold: float
    unit: str = "ratio"
    non_signal: bool = True
    auto_drop_allowed: bool = False
    auto_fix_allowed: bool = False

    def __post_init__(self):
        if self.auto_drop_allowed or self.auto_fix_allowed or not self.non_signal:
            raise ValueError("Thresholds must not allow automated dropping or fixing")


@dataclass(frozen=True)
class FeatureDriftThreshold:
    threshold_id: str
    metric_id: str
    warning_threshold: float
    critical_threshold: float
    unit: str = "delta"
    non_signal: bool = True
    auto_drop_allowed: bool = False
    auto_fix_allowed: bool = False

    def __post_init__(self):
        if self.auto_drop_allowed or self.auto_fix_allowed or not self.non_signal:
            raise ValueError("Thresholds must not allow automated dropping or fixing")


@dataclass(frozen=True)
class FeatureQualityFinding:
    finding_id: str
    domain: str
    severity: str
    feature_column: str
    issue_description: str
    recommended_action: str
    manual_review_required: bool = True
    destructive_action_allowed: bool = False
    non_signal: bool = True

    def __post_init__(self):
        if self.destructive_action_allowed or not self.non_signal:
            raise ValueError("Findings must not permit destructive actions or signals")


@dataclass(frozen=True)
class FeatureDriftFinding:
    finding_id: str
    domain: str
    severity: str
    feature_column: str
    drift_description: str
    recommended_action: str
    manual_review_required: bool = True
    destructive_action_allowed: bool = False
    non_signal: bool = True

    def __post_init__(self):
        if self.destructive_action_allowed or not self.non_signal:
            raise ValueError("Findings must not permit destructive actions or signals")


@dataclass(frozen=True)
class FeatureQualityScore:
    profile_name: str
    overall_quality_score: float
    missingness_score: float
    infinite_value_score: float
    zero_variance_score: float
    duplicate_score: float
    namespace_score: float
    non_signal: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False

    def __post_init__(self):
        for s in [
            self.overall_quality_score,
            self.missingness_score,
            self.infinite_value_score,
            self.zero_variance_score,
            self.duplicate_score,
            self.namespace_score,
        ]:
            if not (0.0 <= s <= 1.0):
                raise ValueError(f"Score {s} must be within [0, 1]")
        if not self.non_signal or self.official_approval or self.production_ready or self.broker_ready:
            raise ValueError("Scores are diagnostic only and cannot imply production or broker approval")


@dataclass(frozen=True)
class FeatureDriftScore:
    profile_name: str
    overall_stability_score: float
    mean_stability_score: float
    std_stability_score: float
    distribution_shift_score: float
    non_signal: bool = True
    official_approval: bool = False
    production_ready: bool = False
    broker_ready: bool = False

    def __post_init__(self):
        for s in [
            self.overall_stability_score,
            self.mean_stability_score,
            self.std_stability_score,
            self.distribution_shift_score,
        ]:
            if not (0.0 <= s <= 1.0):
                raise ValueError(f"Score {s} must be within [0, 1]")
        if not self.non_signal or self.official_approval or self.production_ready or self.broker_ready:
            raise ValueError("Scores are diagnostic only and cannot imply production or broker approval")


@dataclass(frozen=True)
class FeatureQualityDriftManifest:
    manifest_id: str
    matrix_or_factor_name: str
    source_phase_refs: List[int] = field(default_factory=lambda: [116, 117, 118, 119, 120, 121, 122])
    feature_count: int = 0
    factor_family_count: int = 10
    missingness_warning_count: int = 0
    infinite_value_count: int = 0
    all_nan_count: int = 0
    zero_variance_count: int = 0
    duplicate_warning_count: int = 0
    drift_warning_count: int = 0
    manual_review_count: int = 0
    non_signal: bool = True
    official_approval: bool = False
    production_ready: bool = False
    source_preserved: bool = True
    auto_fix_allowed: bool = False
    auto_drop_allowed: bool = False

    def __post_init__(self):
        if not self.non_signal or self.official_approval or self.production_ready:
            raise ValueError("Manifest violates non-signal/non-approval invariant")
        if not self.source_preserved or self.auto_fix_allowed or self.auto_drop_allowed:
            raise ValueError("Manifest violates source preservation invariant")
