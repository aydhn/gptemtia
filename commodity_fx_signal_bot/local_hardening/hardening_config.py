
from dataclasses import dataclass

class ConfigError(Exception): pass

@dataclass(frozen=True)
class LocalHardeningProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_auto_refactor: bool = False
    allow_dead_code_delete: bool = False
    allow_file_modification: bool = False
    allow_file_deletion: bool = False
    allow_file_move: bool = False
    allow_overwrite: bool = False
    allow_package_publish: bool = False
    allow_cloud_upload: bool = False
    allow_external_service: bool = False
    allow_external_llm: bool = False
    allow_live_commands: bool = False
    allow_broker_commands: bool = False
    allow_deploy_commands: bool = False
    allow_background_daemons: bool = False
    allow_investment_advice: bool = False
    allow_production_release_claim: bool = False
    allow_real_rc_claim: bool = False
    scan_source: bool = True
    scan_docs: bool = True
    scan_reports: bool = True
    scan_data_lake: bool = True
    scan_scripts: bool = True
    scan_tests: bool = True
    scan_contracts: bool = True
    scan_safety_outputs: bool = True
    max_files: int = 500000
    max_functions: int = 300000
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

PROFILES = {
    "balanced_local_hardening": LocalHardeningProfile(
        name="balanced_local_hardening",
        description="Genel amacli local/offline final hardening, contract freeze ve RC dry-run freeze profili.",
        notes="Genel amacli local/offline final hardening, contract freeze ve RC dry-run freeze profili."
    ),
    "strict_freeze_safety": LocalHardeningProfile(
        name="strict_freeze_safety",
        description="Release overclaim, destructive action, vb. siki denetleyen profil.",
        max_files=300000,
        max_functions=200000,
        min_quality_score=0.60,
        notes="Release overclaim, destructive action, live/broker/deploy, package publish ve official release iddialarini siki denetleyen profil."
    ),
    "contract_freeze_focus": LocalHardeningProfile(
        name="contract_freeze_focus",
        description="Contract catalog odakli profil.",
        notes="DataLake, FeatureStore, script CLI, report builder, config, path ve test contract catalog odakli profil."
    ),
    "dead_code_review_focus": LocalHardeningProfile(
        name="dead_code_review_focus",
        description="Dead-code review odakli profil.",
        scan_docs=False, scan_reports=False, scan_data_lake=False,
        notes="Dead-code candidate, unused module, orphan script/test ve duplicate utility adaylarini yalnizca raporlayan profil."
    )
}

def get_local_hardening_profile(name: str) -> LocalHardeningProfile:
    if name not in PROFILES: raise ConfigError(f"Unknown profile: {name}")
    return PROFILES[name]

def list_local_hardening_profiles(enabled_only: bool = True) -> list[LocalHardeningProfile]:
    return [p for p in PROFILES.values() if not enabled_only or p.enabled]

def validate_local_hardening_profiles() -> None:
    for p in PROFILES.values():
        if not p.language: raise ConfigError("Language cannot be empty")
        if p.max_files <= 0 or p.max_functions <= 0: raise ConfigError("Max limits must be positive")
        if not (0 <= p.min_quality_score <= 1): raise ConfigError("Min quality score must be between 0 and 1")
        if not p.dry_run_default: raise ConfigError("dry_run_default must be True")
        if p.allow_auto_refactor or p.allow_dead_code_delete or p.allow_package_publish or p.allow_production_release_claim or p.allow_real_rc_claim:
            raise ConfigError("Forbidden flags cannot be True")

def get_default_local_hardening_profile() -> LocalHardeningProfile:
    return PROFILES["balanced_local_hardening"]
