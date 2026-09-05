from dataclasses import dataclass
from typing import List

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class AdvancedRuntimeProfile:
    name: str
    description: str
    language: str = "tr"
    current_phase: int = 102
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
    scan_settings: bool = True
    scan_paths: bool = True
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
    "balanced_advanced_runtime": AdvancedRuntimeProfile(
        name="balanced_advanced_runtime",
        description="Balanced offline profile for Phase 102",
        notes="Phase 102 core runtime consolidation için dengeli local/offline runtime profili."
    ),
    "strict_runtime_safety": AdvancedRuntimeProfile(
        name="strict_runtime_safety",
        description="Strict safety profile",
        min_readiness_score=0.65,
        min_quality_score=0.65,
        notes="Canlı trading, broker, deployment, scraping, external API ve yatırım tavsiyesi sınırlarını sıkı denetleyen runtime profili."
    ),
    "runtime_contract_focus": AdvancedRuntimeProfile(
        name="runtime_contract_focus",
        description="Contract focus profile",
        scan_scripts=False,
        scan_tests=False,
        scan_docs=False,
        notes="Settings/paths/DataLake/FeatureStore/report contract üretimine odaklı runtime profili."
    )
}

def get_advanced_runtime_profile(name: str) -> AdvancedRuntimeProfile:
    if name not in PROFILES:
        raise ConfigError(f"Profile {name} not found.")
    return PROFILES[name]

def list_advanced_runtime_profiles(enabled_only: bool = True) -> list[AdvancedRuntimeProfile]:
    return [p for p in PROFILES.values() if not enabled_only or p.enabled]

def get_default_advanced_runtime_profile() -> AdvancedRuntimeProfile:
    return PROFILES["balanced_advanced_runtime"]

def validate_advanced_runtime_profiles() -> None:
    for p in PROFILES.values():
        if p.current_phase != 102: raise ConfigError("current_phase must be 102")
        if p.target_final_phase != 160: raise ConfigError("target_final_phase must be 160")
        if not p.dry_run_default: raise ConfigError("dry_run_default must be True")
        if not (p.local_only and p.non_production and p.research_only): raise ConfigError("Must be local/non-prod/research")
        if not p.language: raise ConfigError("language must not be empty")
        if p.max_items <= 0 or p.max_rows <= 0: raise ConfigError("max items/rows must be positive")
        if not (0 <= p.min_readiness_score <= 1 and 0 <= p.min_quality_score <= 1): raise ConfigError("Scores must be 0-1")
        if any([p.allow_live_trading, p.allow_broker_integration, p.allow_investment_advice, p.allow_model_deployment, p.allow_web_scraping]):
            raise ConfigError("Risk flags must be False")
