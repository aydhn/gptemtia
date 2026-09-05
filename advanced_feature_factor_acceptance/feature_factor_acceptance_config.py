"""Phase 125: Feature/Factor Engine Acceptance Configuration.

Provides profile management, phase constraints, non-signal guarantees,
and security gates for end-to-end feature block acceptance.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class FeatureFactorAcceptanceProfile:
    """Configuration profile for Phase 125 feature/factor acceptance."""
    profile_name: str
    description: str
    current_phase: int = 125
    target_final_phase: int = 160
    next_phase: int = 126
    default_language: str = "tr"
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_real_order: bool = False
    allow_investment_advice: bool = False
    allow_acceptance_as_signal: bool = False
    allow_directional_claim: bool = False
    allow_strategy_generation: bool = False
    allow_backtest_execution: bool = False
    allow_optimizer_execution: bool = False
    allow_model_training: bool = False
    allow_target_label_generation: bool = False
    allow_prediction_generation: bool = False
    allow_full_article_usage: bool = False
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
    enable_inventory: bool = True
    enable_dependency_report: bool = True
    enable_acceptance_gates: bool = True
    enable_compliance_reports: bool = True
    enable_contract_reports: bool = True
    enable_manifest: bool = True
    enable_phase_126_handoff: bool = True
    min_score: float = 0.45
    save_reports: bool = True
    enabled: bool = True


PROFILES: Dict[str, FeatureFactorAcceptanceProfile] = {
    "balanced_local_feature_factor_acceptance": FeatureFactorAcceptanceProfile(
        profile_name="balanced_local_feature_factor_acceptance",
        description="Dengeli yerel feature/faktör motoru uçtan uca kabul ve yönetişim profili.",
        current_phase=125,
        target_final_phase=160,
        next_phase=126,
        min_score=0.45,
    ),
    "strict_non_signal_acceptance_safety": FeatureFactorAcceptanceProfile(
        profile_name="strict_non_signal_acceptance_safety",
        description="Sıkı non-signal, no-lookahead ve kaynak koruma odaklı kabul güvenlik profili.",
        current_phase=125,
        target_final_phase=160,
        next_phase=126,
        min_score=0.60,
    ),
    "dry_run_acceptance_manifest_focus": FeatureFactorAcceptanceProfile(
        profile_name="dry_run_acceptance_manifest_focus",
        description="Dry-run uyumlu, manifest ve Phase 126 rejim devri odaklı kabul profili.",
        current_phase=125,
        target_final_phase=160,
        next_phase=126,
        min_score=0.40,
    ),
}


def get_feature_factor_acceptance_profile(name: str) -> FeatureFactorAcceptanceProfile:
    """Retrieve a feature/factor acceptance profile by name."""
    if name not in PROFILES:
        raise KeyError(f"Unknown feature factor acceptance profile: {name}")
    return PROFILES[name]


def list_feature_factor_acceptance_profiles(enabled_only: bool = True) -> List[FeatureFactorAcceptanceProfile]:
    """List available acceptance profiles."""
    if enabled_only:
        return [p for p in PROFILES.values() if p.enabled]
    return list(PROFILES.values())


def validate_feature_factor_acceptance_profiles() -> bool:
    """Validate all profiles conform to non-signal, offline, safety invariants."""
    for p in PROFILES.values():
        if p.current_phase != 125:
            raise ValueError(f"Profile {p.profile_name} has invalid current_phase: {p.current_phase}")
        if p.target_final_phase != 160:
            raise ValueError(f"Profile {p.profile_name} has invalid target_final_phase: {p.target_final_phase}")
        if p.next_phase != 126:
            raise ValueError(f"Profile {p.profile_name} has invalid next_phase: {p.next_phase}")
        if not p.local_only or not p.non_production or not p.research_only:
            raise ValueError(f"Profile {p.profile_name} violates local/offline invariants.")
        if p.allow_live_trading or p.allow_broker_integration or p.allow_real_order:
            raise ValueError(f"Profile {p.profile_name} permits live trading or broker integration.")
        if p.allow_investment_advice or p.allow_acceptance_as_signal or p.allow_directional_claim:
            raise ValueError(f"Profile {p.profile_name} permits signal/advice/directional claims.")
        if p.allow_strategy_generation or p.allow_backtest_execution or p.allow_optimizer_execution:
            raise ValueError(f"Profile {p.profile_name} permits strategy/backtest/optimizer.")
        if p.allow_model_training or p.allow_target_label_generation or p.allow_prediction_generation:
            raise ValueError(f"Profile {p.profile_name} permits model training/target/prediction.")
        if p.allow_official_approval_claim or p.allow_production_ready_claim or p.allow_broker_ready_claim:
            raise ValueError(f"Profile {p.profile_name} permits official approval or production readiness claims.")
        if p.allow_model_deployment or p.allow_production_deployment:
            raise ValueError(f"Profile {p.profile_name} permits deployment.")
        if p.allow_web_scraping or p.allow_credential_output or p.allow_full_article_usage:
            raise ValueError(f"Profile {p.profile_name} permits scraping, credentials, or full article usage.")
        if p.allow_source_overwrite or p.allow_auto_destructive_cleaning or p.allow_file_deletion:
            raise ValueError(f"Profile {p.profile_name} permits destructive actions.")
        if p.allow_auto_imputation or p.allow_auto_feature_drop:
            raise ValueError(f"Profile {p.profile_name} permits auto-imputation or auto-feature-drop.")
    return True


def get_default_feature_factor_acceptance_profile() -> FeatureFactorAcceptanceProfile:
    """Get default profile for Phase 125."""
    validate_feature_factor_acceptance_profiles()
    return PROFILES["balanced_local_feature_factor_acceptance"]
