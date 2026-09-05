"""Phase 129: Market Behavior Diagnostics and Regime Quality Labels.

Defines standardized taxonomy domains, status labels, severity labels, and validators.
"""

from typing import List

# Master module and cycle constants
MARKET_BEHAVIOR_DIAGNOSTICS_MODULE_NAME = "advanced_market_behavior_diagnostics"
MARKET_BEHAVIOR_DIAGNOSTICS_CYCLE_NAME = "Phase 126-135: Regime Classification and Market Behavior"
PHASE_129_TARGET_FINAL_PHASE = 160

CORE_BEHAVIOR_QUALITY_LABELS = [
    "candidate_state_quality",
    "pseudo_state_quality",
    "candidate_state_coverage",
    "candidate_state_consistency",
    "candidate_state_ambiguity",
    "candidate_state_stability",
    "candidate_state_missingness",
    "candidate_state_namespace_quality",
    "regime_family_quality",
    "regime_family_coverage",
    "regime_family_consistency",
    "volatility_behavior_diagnostics",
    "trend_behavior_diagnostics",
    "range_behavior_diagnostics",
    "macro_event_behavior_diagnostics",
    "news_metadata_behavior_diagnostics",
    "cross_asset_behavior_diagnostics",
    "transition_readiness",
    "stability_readiness",
    "regime_quality_dependencies",
    "behavior_quality_findings",
    "manual_review_queue",
    "behavior_quality_scoring",
    "behavior_diagnostics_manifest",
]

FORBIDDEN_BEHAVIOR_CLAIMS = [
    "buy_signal",
    "sell_signal",
    "long_position",
    "short_position",
    "target_label",
    "future_prediction",
    "trading_recommendation",
    "official_approval",
    "production_ready",
    "broker_ready",
    "clustering_execution",
    "model_training",
]

SAFE_GO_BEHAVIOR_PRINCIPLES = [
    "diagnostics_only",
    "non_signal_mandate",
    "source_preservation",
    "zero_lookahead_guarantee",
    "news_metadata_boundary",
    "manual_review_governance",
]

# Master domain label taxonomy
MARKET_BEHAVIOR_DIAGNOSTICS_DOMAIN_LABELS: List[str] = [

    "market_behavior_diagnostics_profile_domain",
    "market_behavior_diagnostics_domain",
    "behavior_quality_metric_domain",
    "behavior_diagnostics_metric_domain",
    "behavior_threshold_domain",
    "candidate_state_quality_domain",
    "pseudo_state_quality_domain",
    "candidate_state_coverage_domain",
    "candidate_state_consistency_domain",
    "candidate_state_ambiguity_domain",
    "candidate_state_stability_domain",
    "candidate_state_missingness_domain",
    "candidate_state_namespace_domain",
    "regime_family_quality_domain",
    "regime_family_coverage_domain",
    "regime_family_consistency_domain",
    "volatility_behavior_domain",
    "trend_behavior_domain",
    "range_behavior_domain",
    "macro_event_behavior_domain",
    "news_metadata_behavior_domain",
    "cross_asset_behavior_domain",
    "transition_readiness_domain",
    "stability_readiness_domain",
    "regime_quality_dependency_domain",
    "behavior_quality_finding_domain",
    "manual_review_domain",
    "behavior_quality_score_domain",
    "behavior_diagnostics_manifest_domain",
    "health_domain",
    "validation_domain",
    "safety_domain",
    "phase_130_handoff_domain",
    "unknown_behavior_diagnostics_domain",
]

# Status labels
BEHAVIOR_QUALITY_STATUS_LABELS: List[str] = [
    "behavior_quality_ready",
    "behavior_quality_ready_with_warnings",
    "behavior_quality_placeholder_only",
    "behavior_quality_manual_review_required",
    "behavior_quality_blocked_by_safety",
    "behavior_quality_unknown",
]

# Severity labels
BEHAVIOR_QUALITY_SEVERITY_LABELS: List[str] = [
    "behavior_critical",
    "behavior_high",
    "behavior_medium",
    "behavior_low",
    "behavior_info",
]


def list_market_behavior_diagnostics_domain_labels() -> List[str]:
    """Return all valid market behavior diagnostics domain labels."""
    return list(MARKET_BEHAVIOR_DIAGNOSTICS_DOMAIN_LABELS)


def list_behavior_quality_status_labels() -> List[str]:
    """Return all valid behavior quality status labels."""
    return list(BEHAVIOR_QUALITY_STATUS_LABELS)


def list_behavior_quality_severity_labels() -> List[str]:
    """Return all valid behavior quality severity labels."""
    return list(BEHAVIOR_QUALITY_SEVERITY_LABELS)


def validate_market_behavior_diagnostics_domain_label(label: str) -> bool:
    """Validate whether label is a recognized market behavior diagnostics domain label."""
    if label not in MARKET_BEHAVIOR_DIAGNOSTICS_DOMAIN_LABELS:
        raise ValueError(
            f"Invalid market behavior diagnostics domain label: '{label}'. "
            f"Allowed: {MARKET_BEHAVIOR_DIAGNOSTICS_DOMAIN_LABELS}"
        )
    return True


def validate_behavior_quality_status_label(label: str) -> bool:
    """Validate whether label is a recognized behavior quality status label."""
    if label not in BEHAVIOR_QUALITY_STATUS_LABELS:
        raise ValueError(
            f"Invalid behavior quality status label: '{label}'. "
            f"Allowed: {BEHAVIOR_QUALITY_STATUS_LABELS}"
        )
    return True


def validate_behavior_quality_severity_label(label: str) -> bool:
    """Validate whether label is a recognized behavior quality severity label."""
    if label not in BEHAVIOR_QUALITY_SEVERITY_LABELS:
        raise ValueError(
            f"Invalid behavior quality severity label: '{label}'. "
            f"Allowed: {BEHAVIOR_QUALITY_SEVERITY_LABELS}"
        )
    return True
