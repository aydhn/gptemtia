"""
ML Integration Profile Definitions
"""

from dataclasses import dataclass
from typing import Dict, List


class ConfigError(Exception):
    pass


@dataclass(frozen=True)
class MLIntegrationProfile:
    name: str
    description: str
    min_confidence_score: float = 0.45
    max_uncertainty_score: float = 0.70
    max_leakage_risk_score: float = 0.20
    min_model_quality_score: float = 0.50
    min_dataset_quality_score: float = 0.50
    support_weight: float = 0.10
    conflict_penalty_weight: float = 0.10
    uncertainty_penalty_weight: float = 0.05
    enable_signal_scoring: bool = True
    enable_decision_scoring: bool = True
    enable_strategy_scoring: bool = True
    enable_risk_precheck: bool = False
    block_on_high_leakage_risk: bool = True
    block_on_model_quality_fail: bool = True
    allow_uncertain_context_as_neutral: bool = True
    enabled: bool = True
    notes: str = ""


# Default built-in profiles
_BUILTIN_PROFILES: Dict[str, MLIntegrationProfile] = {
    "balanced_ml_context_integration": MLIntegrationProfile(
        name="balanced_ml_context_integration",
        description="Balanced ML Context Integration Profile",
        min_confidence_score=0.45,
        max_uncertainty_score=0.70,
        support_weight=0.10,
        conflict_penalty_weight=0.10,
        uncertainty_penalty_weight=0.05,
        enable_signal_scoring=True,
        enable_decision_scoring=True,
        enable_strategy_scoring=True,
        enable_risk_precheck=False,
        notes="ML context'i aday skorlarına düşük ağırlıklı ve güvenli bağlam olarak dahil eden profil.",
    ),
    "conservative_ml_context_integration": MLIntegrationProfile(
        name="conservative_ml_context_integration",
        description="Conservative ML Context Integration Profile",
        min_confidence_score=0.60,
        max_uncertainty_score=0.50,
        max_leakage_risk_score=0.10,
        min_model_quality_score=0.65,
        min_dataset_quality_score=0.65,
        support_weight=0.05,
        conflict_penalty_weight=0.15,
        uncertainty_penalty_weight=0.10,
        block_on_high_leakage_risk=True,
        block_on_model_quality_fail=True,
        notes="Daha sıkı kalite ve daha düşük ML ağırlığı kullanan profil.",
    ),
    "research_only_ml_context_integration": MLIntegrationProfile(
        name="research_only_ml_context_integration",
        description="Research Only ML Context Integration Profile",
        support_weight=0.0,
        conflict_penalty_weight=0.0,
        uncertainty_penalty_weight=0.0,
        enable_signal_scoring=False,
        enable_decision_scoring=False,
        enable_strategy_scoring=False,
        enable_risk_precheck=False,
        notes="Sadece alignment ve araştırma raporu üretir; skorlamaya etki etmez.",
    ),
    "model_conflict_focused_integration": MLIntegrationProfile(
        name="model_conflict_focused_integration",
        description="Model Conflict Focused ML Integration Profile",
        support_weight=0.05,
        conflict_penalty_weight=0.20,
        uncertainty_penalty_weight=0.10,
        notes="ML context özellikle mevcut adaylarla çelişkiyi ölçmek için kullanılır.",
    )
}


def get_ml_integration_profile(name: str) -> MLIntegrationProfile:
    """Retrieve an ML Integration profile by name."""
    if name not in _BUILTIN_PROFILES:
        raise ConfigError(f"Unknown ML Integration profile: {name}")
    return _BUILTIN_PROFILES[name]


def list_ml_integration_profiles(enabled_only: bool = True) -> List[MLIntegrationProfile]:
    """List all available ML Integration profiles."""
    profiles = list(_BUILTIN_PROFILES.values())
    if enabled_only:
        return [p for p in profiles if p.enabled]
    return profiles


def validate_ml_integration_profiles() -> None:
    """Validate all registered profiles."""
    for profile in _BUILTIN_PROFILES.values():
        thresholds = [
            profile.min_confidence_score,
            profile.max_uncertainty_score,
            profile.max_leakage_risk_score,
            profile.min_model_quality_score,
            profile.min_dataset_quality_score,
        ]
        weights = [
            profile.support_weight,
            profile.conflict_penalty_weight,
            profile.uncertainty_penalty_weight,
        ]
        for t in thresholds:
            if not (0.0 <= t <= 1.0):
                raise ConfigError(f"Thresholds must be between 0 and 1 in profile {profile.name}")
        for w in weights:
            if not (0.0 <= w <= 1.0):
                raise ConfigError(f"Weights must be between 0 and 1 in profile {profile.name}")


def get_default_ml_integration_profile() -> MLIntegrationProfile:
    """Get the default profile defined in settings, or fallback to balanced."""
    from config.settings import Settings
    s = Settings()
    profile_name = s.default_ml_integration_profile
    try:
        return get_ml_integration_profile(profile_name)
    except ConfigError:
        return _BUILTIN_PROFILES["balanced_ml_context_integration"]
