"""
Command Center configuration and profile management.
"""

from dataclasses import dataclass
from typing import List
from core.exceptions import ConfigError
from config.settings import settings


@dataclass(frozen=True)
class CommandCenterProfile:
    name: str
    description: str
    dry_run_default: bool = True
    require_safe_commands: bool = True
    allow_live_commands: bool = False
    allow_broker_commands: bool = False
    allow_deploy_commands: bool = False
    allow_background_daemons: bool = False
    max_suggested_commands: int = 50
    include_research_reports: bool = True
    include_portfolio_reports: bool = True
    include_regime_reports: bool = True
    include_synthetic_indices: bool = True
    include_factor_research: bool = True
    include_meta_research: bool = True
    include_experiments: bool = True
    include_governance: bool = True
    include_planning: bool = True
    include_knowledge_base: bool = True
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""


_PROFILES = {
    "balanced_offline_command_center": CommandCenterProfile(
        name="balanced_offline_command_center",
        description="Balanced profile for offline analyst command center.",
        dry_run_default=True,
        require_safe_commands=True,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        max_suggested_commands=50,
        include_research_reports=True,
        include_portfolio_reports=True,
        include_regime_reports=True,
        include_synthetic_indices=True,
        include_factor_research=True,
        include_meta_research=True,
        include_experiments=True,
        include_governance=True,
        include_planning=True,
        include_knowledge_base=True,
        min_quality_score=0.40,
        notes="Genel amaçlı offline analyst command center profili."
    ),
    "strict_safe_command_center": CommandCenterProfile(
        name="strict_safe_command_center",
        description="Strict safe profile for offline analyst command center.",
        dry_run_default=True,
        require_safe_commands=True,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        max_suggested_commands=30,
        include_research_reports=True,
        include_portfolio_reports=True,
        include_regime_reports=True,
        include_synthetic_indices=True,
        include_factor_research=True,
        include_meta_research=True,
        include_experiments=True,
        include_governance=True,
        include_planning=True,
        include_knowledge_base=True,
        min_quality_score=0.55,
        notes="Daha sıkı güvenli komut ve runbook kontrolü isteyen profil."
    ),
    "knowledge_assistant_command_center": CommandCenterProfile(
        name="knowledge_assistant_command_center",
        description="Profile emphasizing knowledge base and query flows.",
        dry_run_default=True,
        require_safe_commands=True,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        max_suggested_commands=50,
        include_research_reports=True,
        include_portfolio_reports=False,
        include_regime_reports=False,
        include_synthetic_indices=False,
        include_factor_research=False,
        include_meta_research=True,
        include_experiments=True,
        include_governance=True,
        include_planning=True,
        include_knowledge_base=True,
        min_quality_score=0.40,
        notes="Knowledge base, query, planning ve governance akışlarını öne çıkaran profil."
    ),
    "reporting_command_center": CommandCenterProfile(
        name="reporting_command_center",
        description="Profile emphasizing reporting and research queries.",
        dry_run_default=True,
        require_safe_commands=True,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        max_suggested_commands=50,
        include_research_reports=True,
        include_portfolio_reports=True,
        include_regime_reports=True,
        include_synthetic_indices=True,
        include_factor_research=True,
        include_meta_research=True,
        include_experiments=False,
        include_governance=False,
        include_planning=False,
        include_knowledge_base=True,
        min_quality_score=0.40,
        notes="Rapor üretimi ve araştırma sorgusu odaklı komut merkezi profili."
    ),
}


def get_command_center_profile(name: str) -> CommandCenterProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Unknown Command Center Profile: {name}")
    return _PROFILES[name]


def list_command_center_profiles(enabled_only: bool = True) -> List[CommandCenterProfile]:
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())


def validate_command_center_profiles() -> None:
    for name, profile in _PROFILES.items():
        if profile.max_suggested_commands <= 0:
            raise ConfigError(f"Profile {name} has max_suggested_commands <= 0")
        if not (0.0 <= profile.min_quality_score <= 1.0):
            raise ConfigError(f"Profile {name} has invalid min_quality_score")
        if not profile.dry_run_default:
            raise ConfigError(f"Profile {name} must have dry_run_default=True")
        if profile.allow_live_commands:
            raise ConfigError(f"Profile {name} must have allow_live_commands=False")
        if profile.allow_broker_commands:
            raise ConfigError(f"Profile {name} must have allow_broker_commands=False")
        if profile.allow_deploy_commands:
            raise ConfigError(f"Profile {name} must have allow_deploy_commands=False")
        if profile.allow_background_daemons:
            raise ConfigError(f"Profile {name} must have allow_background_daemons=False")

        flags = [
            profile.include_research_reports,
            profile.include_portfolio_reports,
            profile.include_regime_reports,
            profile.include_synthetic_indices,
            profile.include_factor_research,
            profile.include_meta_research,
            profile.include_experiments,
            profile.include_governance,
            profile.include_planning,
            profile.include_knowledge_base
        ]
        if not any(flags):
            raise ConfigError(f"Profile {name} must have at least one include flag set to True")


def get_default_command_center_profile() -> CommandCenterProfile:
    name = getattr(settings, "default_command_center_profile", "balanced_offline_command_center")
    return get_command_center_profile(name)
