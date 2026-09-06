"""Phase 133: Regime Validation and No-Lookahead Acceptance Configuration.

Defines profiles, safety switches, and acceptance thresholds.
Enforces local-only, research-only, non-signal operation with zero model execution.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class RegimeValidationAcceptanceProfile:
    """Configuration profile for Phase 133 Regime Validation Acceptance."""

    profile_name: str
    description: str
    current_phase: int = 133
    target_final_phase: int = 160
    next_phase: int = 134
    default_language: str = "tr"
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True

    # Absolute safety boundaries (strictly False)
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_real_order: bool = False
    allow_investment_advice: bool = False
    allow_acceptance_as_signal: bool = False
    allow_validation_as_signal: bool = False
    allow_directional_claim: bool = False
    allow_strategy_generation: bool = False
    allow_backtest_execution: bool = False
    allow_optimizer_execution: bool = False
    allow_model_training: bool = False
    allow_model_fit: bool = False
    allow_model_predict: bool = False
    allow_clustering_execution: bool = False
    allow_unsupervised_execution: bool = False
    allow_target_label_generation: bool = False
    allow_prediction_generation: bool = False
    allow_sentiment_model_output: bool = False
    allow_full_article_usage: bool = False
    allow_article_body_usage: bool = False
    allow_raw_content_usage: bool = False
    allow_scraped_html_usage: bool = False
    allow_embedding_generation: bool = False
    allow_vector_db: bool = False
    allow_official_approval_claim: bool = False
    allow_production_ready_claim: bool = False
    allow_broker_ready_claim: bool = False
    allow_model_deployment: bool = False
    allow_production_deployment: bool = False
    allow_web_scraping: bool = False
    allow_credential_output: bool = False
    allow_source_overwrite: bool = False
    allow_auto_destructive_cleaning: bool = False
    allow_file_deletion: bool = False
    allow_overwrite: bool = False
    allow_auto_imputation: bool = False
    allow_auto_feature_drop: bool = False

    # Acceptance verification switches
    enable_gates: bool = True
    enable_no_lookahead: bool = True
    enable_timestamp_order: bool = True
    enable_backward_asof: bool = True
    enable_forbidden_column: bool = True
    enable_metadata_only_news: bool = True
    enable_source_preservation: bool = True
    enable_non_signal: bool = True
    enable_component_acceptance: bool = True
    enable_dependency_acceptance: bool = True
    enable_findings: bool = True
    enable_manifest: bool = True
    enable_phase_134_handoff: bool = True

    # Scoring and report generation
    min_acceptance_score: float = 0.45
    save_reports: bool = True
    enabled: bool = True
    extra_metadata: Dict[str, Any] = field(default_factory=dict)


PROFILES: Dict[str, RegimeValidationAcceptanceProfile] = {
    "balanced_local_regime_validation_acceptance": RegimeValidationAcceptanceProfile(
        profile_name="balanced_local_regime_validation_acceptance",
        description="Standard balanced acceptance profile evaluating all Phase 126-132 regime outputs locally.",
        min_acceptance_score=0.45,
    ),
    "strict_no_lookahead_metadata_only_acceptance": RegimeValidationAcceptanceProfile(
        profile_name="strict_no_lookahead_metadata_only_acceptance",
        description="Strict profile placing maximal emphasis on backward-only asof join, no-lookahead, and news metadata purity.",
        min_acceptance_score=0.60,
    ),
    "dry_run_regime_acceptance_focus": RegimeValidationAcceptanceProfile(
        profile_name="dry_run_regime_acceptance_focus",
        description="Dry-run verification profile for zero file-write checks and fast synthetic acceptance testing.",
        dry_run_default=True,
        save_reports=False,
        min_acceptance_score=0.40,
    ),
}


def get_regime_validation_acceptance_profile(
    name: Optional[str] = None,
) -> RegimeValidationAcceptanceProfile:
    """Retrieve profile by name or return default balanced profile."""
    profile_key = name or "balanced_local_regime_validation_acceptance"
    if profile_key not in PROFILES:
        raise ValueError(f"Unknown Regime Validation Acceptance profile: {profile_key}. Available: {list(PROFILES.keys())}")
    return PROFILES[profile_key]


def list_regime_validation_acceptance_profiles(
    enabled_only: bool = True,
) -> List[RegimeValidationAcceptanceProfile]:
    """List configured validation acceptance profiles."""
    if enabled_only:
        return [p for p in PROFILES.values() if p.enabled]
    return list(PROFILES.values())


def validate_regime_validation_acceptance_profiles() -> bool:
    """Validate all configured profiles adhere to safety rules."""
    for name, p in PROFILES.items():
        if p.current_phase != 133:
            raise ValueError(f"Profile {name} has invalid current_phase: {p.current_phase}")
        if p.target_final_phase != 160:
            raise ValueError(f"Profile {name} has invalid target_final_phase: {p.target_final_phase}")
        if p.next_phase != 134:
            raise ValueError(f"Profile {name} has invalid next_phase: {p.next_phase}")
        if not (p.local_only and p.non_production and p.research_only):
            raise ValueError(f"Profile {name} must be local_only, non_production, and research_only")
        if (
            p.allow_live_trading
            or p.allow_broker_integration
            or p.allow_real_order
            or p.allow_investment_advice
            or p.allow_acceptance_as_signal
            or p.allow_validation_as_signal
            or p.allow_directional_claim
            or p.allow_strategy_generation
            or p.allow_backtest_execution
            or p.allow_optimizer_execution
            or p.allow_model_training
            or p.allow_model_fit
            or p.allow_model_predict
            or p.allow_clustering_execution
            or p.allow_unsupervised_execution
            or p.allow_target_label_generation
            or p.allow_prediction_generation
            or p.allow_sentiment_model_output
            or p.allow_full_article_usage
            or p.allow_article_body_usage
            or p.allow_raw_content_usage
            or p.allow_scraped_html_usage
            or p.allow_embedding_generation
            or p.allow_vector_db
            or p.allow_official_approval_claim
            or p.allow_production_ready_claim
            or p.allow_broker_ready_claim
            or p.allow_model_deployment
            or p.allow_production_deployment
            or p.allow_web_scraping
            or p.allow_credential_output
            or p.allow_source_overwrite
            or p.allow_auto_destructive_cleaning
            or p.allow_file_deletion
            or p.allow_overwrite
            or p.allow_auto_imputation
            or p.allow_auto_feature_drop
        ):
            raise ValueError(f"Profile {name} violates non-trading/non-destructive safety constraints!")
    return True


def get_default_regime_validation_acceptance_profile() -> RegimeValidationAcceptanceProfile:
    """Return default balanced regime validation acceptance profile."""
    return get_regime_validation_acceptance_profile("balanced_local_regime_validation_acceptance")
