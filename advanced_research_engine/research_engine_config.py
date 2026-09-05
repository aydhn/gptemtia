from dataclasses import dataclass
import pandas as pd

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class AdvancedResearchEngineProfile:
    name: str
    description: str
    language: str = "tr"
    current_phase: int = 103
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
    enable_data_interface: bool = True
    enable_feature_interface: bool = True
    enable_regime_interface: bool = True
    enable_ml_interface: bool = True
    enable_backtest_interface: bool = True
    enable_portfolio_interface: bool = True
    enable_report_interface: bool = True
    enable_signal_research_interface: bool = True
    scan_runtime_outputs: bool = True
    scan_continuation_outputs: bool = True
    scan_datalake: bool = True
    scan_featurestore: bool = True
    scan_reports: bool = True
    scan_scripts: bool = True
    scan_tests: bool = True
    scan_docs: bool = True
    max_items: int = 1000000
    max_rows: int = 500000
    min_readiness_score: float = 0.45
    min_quality_score: float = 0.45
    enabled: bool = True
    notes: str = ""

PROFILES = {
    "balanced_research_engine": AdvancedResearchEngineProfile(
        name="balanced_research_engine",
        description="Phase 103 research engine interface layer balanced profile.",
        notes="Phase 103 research engine interface layer için dengeli local/offline profil."
    ),
    "strict_research_engine_safety": AdvancedResearchEngineProfile(
        name="strict_research_engine_safety",
        description="Strict profile.",
        min_readiness_score=0.65,
        min_quality_score=0.65,
        notes="Canlı trading, broker, deployment, scraping, external API ve yatırım tavsiyesi sınırlarını sıkı denetleyen research engine profili."
    ),
    "interface_contract_focus": AdvancedResearchEngineProfile(
        name="interface_contract_focus",
        description="Interface focus.",
        notes="Data/feature/regime/ML/backtest/portfolio/report/signal research interface kontratlarına odaklı profil."
    )
}

def get_advanced_research_engine_profile(name: str) -> AdvancedResearchEngineProfile:
    if name not in PROFILES:
        raise ConfigError(f"Unknown profile: {name}")
    return PROFILES[name]

def list_advanced_research_engine_profiles(enabled_only: bool = True) -> list[AdvancedResearchEngineProfile]:
    return [p for p in PROFILES.values() if not enabled_only or p.enabled]

def validate_advanced_research_engine_profiles() -> None:
    for p in PROFILES.values():
        assert p.current_phase == 103
        assert p.target_final_phase == 160
        assert p.dry_run_default is True
        assert p.local_only is True
        assert p.non_production is True
        assert p.research_only is True
        assert p.language != ""
        assert p.max_items > 0
        assert p.max_rows > 0
        assert 0.0 <= p.min_readiness_score <= 1.0
        assert 0.0 <= p.min_quality_score <= 1.0
        assert not p.allow_live_trading
        assert not p.allow_broker_integration

def get_default_advanced_research_engine_profile() -> AdvancedResearchEngineProfile:
    return PROFILES["balanced_research_engine"]
