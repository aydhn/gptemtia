from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class AdvancedContinuationProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    current_phase: int = 101
    target_final_phase: int = 160
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
    scan_phase_1_100_outputs: bool = True
    scan_docs: bool = True
    scan_reports: bool = True
    scan_data_lake: bool = True
    scan_scripts: bool = True
    scan_tests: bool = True
    max_items: int = 1000000
    max_rows: int = 500000
    min_readiness_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_PROFILES = {
    "balanced_advanced_continuation": AdvancedContinuationProfile(
        name="balanced_advanced_continuation",
        description="Phase 101-160 ileri seviye geliştirme hattını başlatan dengeli continuation profili.",
        notes="Phase 101-160 ileri seviye geliştirme hattını başlatan dengeli continuation profili."
    ),
    "functional_reopen_focus": AdvancedContinuationProfile(
        name="functional_reopen_focus",
        description="MVP sonrası fonksiyonel yeniden açılış ve eksik haritalama odaklı profil.",
        notes="MVP sonrası fonksiyonel yeniden açılış ve eksik haritalama odaklı profil."
    ),
    "strict_continuation_safety": AdvancedContinuationProfile(
        name="strict_continuation_safety",
        description="Canlı trading, broker, deployment, scraping, external API ve yatırım tavsiyesi sınırlarını sıkı denetleyen profil.",
        min_readiness_score=0.60,
        notes="Canlı trading, broker, deployment, scraping, external API ve yatırım tavsiyesi sınırlarını sıkı denetleyen profil."
    )
}

def get_advanced_continuation_profile(name: str) -> AdvancedContinuationProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Unknown profile: {name}")
    return _PROFILES[name]

def list_advanced_continuation_profiles(enabled_only: bool = True) -> list[AdvancedContinuationProfile]:
    return [p for p in _PROFILES.values() if not enabled_only or p.enabled]

def validate_advanced_continuation_profiles() -> None:
    for name, p in _PROFILES.items():
        if p.target_final_phase != 160:
            raise ConfigError(f"Profile {name}: target_final_phase must be 160.")
        if p.current_phase != 101:
            raise ConfigError(f"Profile {name}: current_phase must be 101.")
        if not p.language:
            raise ConfigError(f"Profile {name}: language cannot be empty.")
        if p.max_items <= 0 or p.max_rows <= 0:
            raise ConfigError(f"Profile {name}: max_items and max_rows must be positive.")
        if not (0 <= p.min_readiness_score <= 1):
            raise ConfigError(f"Profile {name}: min_readiness_score must be between 0 and 1.")
        if any([p.allow_live_trading, p.allow_broker_integration, p.allow_real_order, p.allow_investment_advice, p.allow_model_deployment, p.allow_production_deployment, p.allow_web_server, p.allow_dashboard, p.allow_gui_tui, p.allow_external_llm, p.allow_vector_db, p.allow_embedding_api, p.allow_web_scraping, p.allow_cloud_publish, p.allow_docker_push, p.allow_git_tag, p.allow_archive_creation, p.allow_file_deletion, p.allow_file_move, p.allow_overwrite]):
            raise ConfigError(f"Profile {name}: risky allow flags must be False.")

def get_default_advanced_continuation_profile() -> AdvancedContinuationProfile:
    return _PROFILES["balanced_advanced_continuation"]

validate_advanced_continuation_profiles()
