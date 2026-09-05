from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class FunctionalGapClosureProfile:
    name: str
    description: str
    language: str = "tr"
    current_phase: int = 105
    target_final_phase: int = 160
    next_phase: int = 106
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
    enable_phase_106_handoff: bool = True
    enable_provider_requirements: bool = True
    enable_no_scraping_boundary: bool = True
    enable_readiness_reconciliation: bool = True
    min_readiness_score: float = 0.45
    min_quality_score: float = 0.45
    enabled: bool = True
    notes: str = ""

PROFILES = {
    "balanced_functional_gap_closure": FunctionalGapClosureProfile(
        name="balanced_functional_gap_closure",
        description="Phase 105 functional gap closure ve Phase 106 data foundation handoff için dengeli profil.",
        notes="Phase 105 functional gap closure ve Phase 106 data foundation handoff için dengeli profil."
    ),
    "strict_gap_closure_safety": FunctionalGapClosureProfile(
        name="strict_gap_closure_safety",
        description="Canlı trading, broker, deployment, scraping, external API ve yatırım tavsiyesi sınırlarını sıkı denetleyen gap closure profili.",
        min_readiness_score=0.65,
        min_quality_score=0.65,
        notes="Canlı trading, broker, deployment, scraping, external API ve yatırım tavsiyesi sınırlarını sıkı denetleyen gap closure profili."
    ),
    "phase_106_handoff_focus": FunctionalGapClosureProfile(
        name="phase_106_handoff_focus",
        description="Phase 106 Multi-Provider Data Abstraction handoff gereksinimlerine odaklı profil.",
        notes="Phase 106 Multi-Provider Data Abstraction handoff gereksinimlerine odaklı profil."
    )
}

def get_functional_gap_closure_profile(name: str) -> FunctionalGapClosureProfile:
    if name not in PROFILES:
        raise ConfigError(f"Profile {name} not found")
    return PROFILES[name]

def list_functional_gap_closure_profiles(enabled_only: bool = True) -> list[FunctionalGapClosureProfile]:
    return [p for p in PROFILES.values() if not enabled_only or p.enabled]

def validate_functional_gap_closure_profiles() -> None:
    for p in PROFILES.values():
        assert p.current_phase == 105
        assert p.target_final_phase == 160
        assert p.next_phase == 106
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
        assert 0.0 <= p.min_readiness_score <= 1.0
        assert 0.0 <= p.min_quality_score <= 1.0

def get_default_functional_gap_closure_profile() -> FunctionalGapClosureProfile:
    return PROFILES["balanced_functional_gap_closure"]
