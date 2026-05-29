from dataclasses import dataclass

@dataclass(frozen=True)
class AnalystUXProfile:
    name: str
    description: str
    language: str = "tr"
    allow_live_commands: bool = False
    allow_broker_commands: bool = False
    allow_deploy_commands: bool = False
    allow_background_daemons: bool = False
    allow_real_market_download: bool = False
    generate_aliases: bool = True
    generate_prompt_packs: bool = True
    generate_cheat_sheets: bool = True
    generate_task_board: bool = True
    max_command_suggestions: int = 10
    min_intent_confidence: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_UX_PROFILES = {
    "balanced_analyst_productivity": AnalystUXProfile(
        name="balanced_analyst_productivity",
        description="Balanced productivity profile",
        notes="Genel amaçlı Türkçe offline analyst UX ve productivity profili."
    ),
    "operator_fast_access": AnalystUXProfile(
        name="operator_fast_access",
        description="Fast access for operators",
        max_command_suggestions=8,
        notes="Operatörün güvenli status, final review, quality gate ve maintenance komutlarına hızlı erişmesi için profil."
    ),
    "codex_agent_productivity": AnalystUXProfile(
        name="codex_agent_productivity",
        description="Codex agent productivity",
        max_command_suggestions=12,
        notes="Codex ajanına faz, script, test, kalite ve dokümantasyon komutlarını güvenli önermek için profil."
    ),
    "documentation_first_productivity": AnalystUXProfile(
        name="documentation_first_productivity",
        description="Documentation first profile",
        notes="Dokümantasyon, user guide, script reference ve safe command reference odaklı profil."
    )
}

class ConfigError(Exception):
    pass

def get_analyst_ux_profile(name: str) -> AnalystUXProfile:
    if name not in _UX_PROFILES:
        raise ConfigError(f"Unknown analyst UX profile: {name}")
    return _UX_PROFILES[name]

def list_analyst_ux_profiles(enabled_only: bool = True) -> list[AnalystUXProfile]:
    return [p for p in _UX_PROFILES.values() if not enabled_only or p.enabled]

def validate_analyst_ux_profiles() -> None:
    for profile in _UX_PROFILES.values():
        if not profile.language:
            raise ConfigError(f"Profile {profile.name} missing language.")
        if profile.max_command_suggestions <= 0:
            raise ConfigError(f"Profile {profile.name} has invalid max_command_suggestions.")
        if not (0 <= profile.min_intent_confidence <= 1):
            raise ConfigError(f"Profile {profile.name} has invalid min_intent_confidence.")
        if not (0 <= profile.min_quality_score <= 1):
            raise ConfigError(f"Profile {profile.name} has invalid min_quality_score.")
        if profile.allow_live_commands or profile.allow_broker_commands or profile.allow_deploy_commands or profile.allow_background_daemons or profile.allow_real_market_download:
             raise ConfigError(f"Profile {profile.name} cannot have live/broker/deploy/daemon/market download enabled.")
        if not any([profile.generate_aliases, profile.generate_prompt_packs, profile.generate_cheat_sheets, profile.generate_task_board]):
             raise ConfigError(f"Profile {profile.name} must have at least one generate flag True.")

def get_default_analyst_ux_profile() -> AnalystUXProfile:
    return get_analyst_ux_profile("balanced_analyst_productivity")
