"""
Master orchestration profile configuration and definitions.
"""

from dataclasses import dataclass
from config.settings import Settings

class ConfigError(Exception):
    """Exception raised for configuration errors."""
    pass

@dataclass(frozen=True)
class MasterOrchestrationProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_execute: bool = False
    allow_live_commands: bool = False
    allow_broker_commands: bool = False
    allow_deploy_commands: bool = False
    allow_background_daemons: bool = False
    allow_real_market_download: bool = False
    allow_external_llm: bool = False
    generate_layer_map: bool = True
    generate_dependency_graphs: bool = True
    generate_master_plan: bool = True
    generate_playbook: bool = True
    generate_handoff_checklists: bool = True
    generate_phase_consolidation: bool = True
    max_commands_per_plan: int = 200
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

def get_master_orchestration_profile(name: str) -> MasterOrchestrationProfile:
    for p in _PROFILES:
        if p.name == name:
            return p
    raise ConfigError(f"Unknown profile: {name}")

def list_master_orchestration_profiles(enabled_only: bool = True) -> list[MasterOrchestrationProfile]:
    if enabled_only:
        return [p for p in _PROFILES if p.enabled]
    return _PROFILES

def validate_master_orchestration_profiles() -> None:
    for p in _PROFILES:
        if not p.language:
            raise ConfigError(f"Profile {p.name} must specify a language.")
        if p.max_commands_per_plan <= 0:
            raise ConfigError(f"Profile {p.name} max_commands_per_plan must be positive.")
        if not (0.0 <= p.min_quality_score <= 1.0):
            raise ConfigError(f"Profile {p.name} min_quality_score must be between 0 and 1.")
        if not p.dry_run_default:
            raise ConfigError(f"Profile {p.name} must have dry_run_default=True for safety.")
        if p.allow_execute:
            raise ConfigError(f"Profile {p.name} must have allow_execute=False by default.")
        if any([
            p.allow_live_commands,
            p.allow_broker_commands,
            p.allow_deploy_commands,
            p.allow_background_daemons,
            p.allow_real_market_download,
            p.allow_external_llm
        ]):
            raise ConfigError(f"Profile {p.name} must not allow dangerous permissions.")

        # Check if at least one generate flag is True
        generate_flags = [
            p.generate_layer_map,
            p.generate_dependency_graphs,
            p.generate_master_plan,
            p.generate_playbook,
            p.generate_handoff_checklists,
            p.generate_phase_consolidation
        ]
        if not any(generate_flags):
            raise ConfigError(f"Profile {p.name} must have at least one generate flag set to True.")

def get_default_master_orchestration_profile() -> MasterOrchestrationProfile:
    try:
        settings = Settings()
        return get_master_orchestration_profile(settings.default_master_orchestration_profile)
    except Exception:
        return get_master_orchestration_profile("balanced_offline_master")

_PROFILES = [
    MasterOrchestrationProfile(
        name="balanced_offline_master",
        description="Balanced Offline Master",
        language="tr",
        dry_run_default=True,
        allow_execute=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        allow_real_market_download=False,
        allow_external_llm=False,
        generate_layer_map=True,
        generate_dependency_graphs=True,
        generate_master_plan=True,
        generate_playbook=True,
        generate_handoff_checklists=True,
        generate_phase_consolidation=True,
        max_commands_per_plan=200,
        notes="Genel amaçlı offline master orchestration, playbook ve phase 1-60 consolidation profili."
    ),
    MasterOrchestrationProfile(
        name="operator_master_plan",
        description="Operator Master Plan",
        language="tr",
        dry_run_default=True,
        allow_execute=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        allow_real_market_download=False,
        allow_external_llm=False,
        generate_layer_map=True,
        generate_dependency_graphs=True,
        generate_master_plan=True,
        generate_playbook=True,
        generate_handoff_checklists=True,
        generate_phase_consolidation=False,
        max_commands_per_plan=120,
        notes="Operatörün günlük/haftalık offline çalışma planlarını görmesi için profil."
    ),
    MasterOrchestrationProfile(
        name="codex_handoff_master",
        description="Codex Handoff Master",
        language="tr",
        dry_run_default=True,
        allow_execute=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        allow_real_market_download=False,
        allow_external_llm=False,
        generate_layer_map=True,
        generate_dependency_graphs=True,
        generate_master_plan=True,
        generate_playbook=True,
        generate_handoff_checklists=True,
        generate_phase_consolidation=True,
        max_commands_per_plan=250,
        notes="Codex ajanına proje haritası, güvenli komut planı ve geliştirme devri için profil."
    ),
    MasterOrchestrationProfile(
        name="strict_safety_master",
        description="Strict Safety Master",
        language="tr",
        dry_run_default=True,
        allow_execute=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        allow_real_market_download=False,
        allow_external_llm=False,
        generate_layer_map=True,
        generate_dependency_graphs=True,
        generate_master_plan=True,
        generate_playbook=True,
        generate_handoff_checklists=True,
        generate_phase_consolidation=True,
        max_commands_per_plan=150,
        min_quality_score=0.60,
        notes="Güvenlik sınırları ve blocked command denetimini öne çıkaran profil."
    ),
]
