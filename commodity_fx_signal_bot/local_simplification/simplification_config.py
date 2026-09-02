from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalSimplificationProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_auto_refactor: bool = False
    allow_file_modification: bool = False
    allow_file_deletion: bool = False
    allow_file_move: bool = False
    allow_overwrite: bool = False
    allow_cleanup_execution: bool = False
    allow_package_publish: bool = False
    allow_cloud_upload: bool = False
    allow_external_service: bool = False
    allow_external_llm: bool = False
    allow_production_cleanup_claim: bool = False
    allow_architecture_approval_claim: bool = False
    allow_compliance_claim: bool = False
    allow_live_trading_claim: bool = False
    allow_broker_readiness_claim: bool = False
    allow_investment_advice: bool = False
    allow_model_deployment_claim: bool = False
    scan_source: bool = True
    scan_docs: bool = True
    scan_reports: bool = True
    scan_data_lake: bool = True
    scan_scripts: bool = True
    scan_tests: bool = True
    scan_generated_docs: bool = True
    scan_reuse_outputs: bool = True
    scan_closure_outputs: bool = True
    scan_safety_outputs: bool = True
    max_items: int = 500000
    max_candidate_items: int = 100000
    min_readiness_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_PROFILES = {
    "balanced_local_simplification": LocalSimplificationProfile(
        name="balanced_local_simplification",
        description="Genel amacli local/offline modular simplification, complexity map ve maintainability rehearsal profili.",
        notes="Genel amaçlı local/offline modular simplification, complexity map ve maintainability rehearsal profili."
    ),
    "complexity_map_focus": LocalSimplificationProfile(
        name="complexity_map_focus",
        description="Module/folder/file/function/script/test/report/DataLake/docs complexity ve sprawl haritalaması odaklı profil.",
        notes="Module/folder/file/function/script/test/report/DataLake/docs complexity ve sprawl haritalaması odaklı profil.",
    ),
    "slimming_plan_focus": LocalSimplificationProfile(
        name="slimming_plan_focus",
        description="Optional slimming plan, consolidation candidates ve maintainability seed odaklı profil.",
        notes="Optional slimming plan, consolidation candidates ve maintainability seed odaklı profil.",
        max_candidate_items=50000
    ),
    "strict_simplification_safety": LocalSimplificationProfile(
        name="strict_simplification_safety",
        description="Auto-refactor, file action, production cleanup, architecture approval, live/broker/advice overclaim denetimini sıkılaştıran profil.",
        notes="Auto-refactor, file action, production cleanup, architecture approval, live/broker/advice overclaim denetimini sıkılaştıran profil.",
        max_items=300000,
        max_candidate_items=50000,
        min_readiness_score=0.60,
        min_quality_score=0.60
    )
}

def get_local_simplification_profile(name: str) -> LocalSimplificationProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Unknown simplification profile: {name}")
    return _PROFILES[name]

def list_local_simplification_profiles(enabled_only: bool = True) -> list[LocalSimplificationProfile]:
    return [p for p in _PROFILES.values() if not enabled_only or p.enabled]

def validate_local_simplification_profiles() -> None:
    for name, p in _PROFILES.items():
        if not p.language:
            raise ConfigError(f"Profile {name} missing language")
        if p.max_items <= 0 or p.max_candidate_items <= 0:
            raise ConfigError(f"Profile {name} max_items must be positive")
        if not (0 <= p.min_readiness_score <= 1) or not (0 <= p.min_quality_score <= 1):
            raise ConfigError(f"Profile {name} min_scores must be in 0-1")
        if not p.dry_run_default:
            raise ConfigError(f"Profile {name} dry_run_default must be True")
        if p.allow_auto_refactor or p.allow_file_modification or p.allow_file_deletion:
            raise ConfigError(f"Profile {name} must not allow destructive actions")

def get_default_local_simplification_profile() -> LocalSimplificationProfile:
    return _PROFILES["balanced_local_simplification"]
