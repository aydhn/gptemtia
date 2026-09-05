from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class AdvancedConfigSystemProfile:
    name: str
    description: str
    language: str = "tr"
    current_phase: int = 104
    target_final_phase: int = 160
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_real_order: bool = False
    allow_investment_advice: bool = False
    allow_model_deployment: bool = False
    allow_production_deployment: bool = False
    allow_web_server: bool = False
    allow_dashboard: bool = False
    allow_gui_tui: bool = False
    allow_external_llm: bool = False
    allow_vector_db: bool = False
    allow_embedding_api: bool = False
    allow_web_scraping: bool = False
    allow_cloud_publish: bool = False
    allow_docker_push: bool = False
    allow_git_tag: bool = False
    allow_archive_creation: bool = False
    allow_file_deletion: bool = False
    allow_file_move: bool = False
    allow_overwrite: bool = False
    enable_profile_composition: bool = True
    enable_profile_compatibility_matrix: bool = True
    enable_profile_validation: bool = True
    enable_profile_quality_report: bool = True
    max_profiles: int = 1000
    max_composed_profiles: int = 5000
    min_readiness_score: float = 0.45
    min_quality_score: float = 0.45
    enabled: bool = True
    notes: str = ""

def get_default_advanced_config_system_profile() -> AdvancedConfigSystemProfile:
    return AdvancedConfigSystemProfile(
        name="balanced_advanced_config",
        description="Phase 104 Advanced Config Profile System için dengeli local/offline config profili.",
        notes="Phase 104 Advanced Config Profile System için dengeli local/offline config profili."
    )

def list_advanced_config_system_profiles(enabled_only: bool = True) -> list[AdvancedConfigSystemProfile]:
    profiles = [
        get_default_advanced_config_system_profile(),
        AdvancedConfigSystemProfile(
            name="strict_config_safety",
            description="Canlı trading, broker, deployment, scraping, external API ve yatırım tavsiyesi sınırlarını sıkı denetleyen config profili.",
            min_readiness_score=0.65,
            min_quality_score=0.65,
            notes="Canlı trading, broker, deployment, scraping, external API ve yatırım tavsiyesi sınırlarını sıkı denetleyen config profili."
        ),
        AdvancedConfigSystemProfile(
            name="profile_composition_focus",
            description="Araştırma modu, evren, zaman dilimi, strateji ve risk profillerini kompoze etmeye odaklı profil.",
            enable_profile_composition=True,
            enable_profile_compatibility_matrix=True,
            notes="Araştırma modu, evren, zaman dilimi, strateji ve risk profillerini kompoze etmeye odaklı profil."
        )
    ]
    if enabled_only:
        return [p for p in profiles if p.enabled]
    return profiles

def get_advanced_config_system_profile(name: str) -> AdvancedConfigSystemProfile:
    for p in list_advanced_config_system_profiles(enabled_only=False):
        if p.name == name:
            return p
    raise ConfigError(f"Unknown profile: {name}")

def validate_advanced_config_system_profiles() -> None:
    for p in list_advanced_config_system_profiles(enabled_only=False):
        assert p.current_phase == 104
        assert p.target_final_phase == 160
        assert p.dry_run_default is True
        assert p.local_only is True
        assert p.non_production is True
        assert p.research_only is True
        assert not p.allow_live_trading
        assert not p.allow_broker_integration
        assert not p.allow_real_order
        assert not p.allow_investment_advice
        assert not p.allow_model_deployment
        assert not p.allow_production_deployment
        assert not p.allow_web_server
        assert not p.allow_dashboard
        assert not p.allow_gui_tui
        assert not p.allow_external_llm
        assert not p.allow_vector_db
        assert not p.allow_embedding_api
        assert not p.allow_web_scraping
        assert not p.allow_cloud_publish
        assert not p.allow_docker_push
        assert not p.allow_git_tag
        assert not p.allow_archive_creation
        assert not p.allow_file_deletion
        assert not p.allow_file_move
        assert not p.allow_overwrite
        assert 0 <= p.min_readiness_score <= 1
        assert 0 <= p.min_quality_score <= 1
