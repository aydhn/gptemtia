from dataclasses import dataclass
from typing import List

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalReadinessProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_production_release_claim: bool = False
    allow_deployment_claim: bool = False
    allow_auto_fix: bool = False
    allow_file_modification: bool = False
    allow_file_deletion: bool = False
    allow_overwrite: bool = False
    allow_cloud_upload: bool = False
    allow_external_service: bool = False
    allow_external_llm: bool = False
    allow_live_commands: bool = False
    allow_broker_commands: bool = False
    allow_deploy_commands: bool = False
    allow_background_daemons: bool = False
    allow_real_market_download: bool = False
    scan_docs: bool = True
    scan_tests: bool = True
    scan_scripts: bool = True
    scan_reports: bool = True
    scan_data_lake: bool = True
    scan_security_layers: bool = True
    scan_consistency_layers: bool = True
    scan_metadata_layers: bool = True
    max_checks: int = 300000
    min_readiness_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_PROFILES = {
    "balanced_local_readiness": LocalReadinessProfile(
        name="balanced_local_readiness",
        description="Genel amacli local/offline non-production readiness dry-run profili.",
        notes="Genel amacli local/offline non-production readiness dry-run profili."
    ),
    "strict_pre_handoff_readiness": LocalReadinessProfile(
        name="strict_pre_handoff_readiness",
        description="Pre-handoff boundary, non-use policy, security ve no-go condition denetimlerini sikilastiran profil.",
        max_checks=200000,
        min_readiness_score=0.60,
        min_quality_score=0.60,
        notes="Pre-handoff boundary, non-use policy, security ve no-go condition denetimlerini sikilastiran profil."
    ),
    "operator_handoff_focus": LocalReadinessProfile(
        name="operator_handoff_focus",
        description="Operator checklist, first-run ve handoff manifest odakli profil.",
        scan_metadata_layers=False,
        notes="Operator checklist, first-run ve handoff manifest odakli profil."
    ),
    "stabilization_focus": LocalReadinessProfile(
        name="stabilization_focus",
        description="Known gaps, limitations, manual review ve stabilization plani odakli profil.",
        min_readiness_score=0.50,
        notes="Known gaps, limitations, manual review ve stabilization plani odakli profil."
    )
}

def get_local_readiness_profile(name: str) -> LocalReadinessProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Unknown local readiness profile: {name}")
    return _PROFILES[name]

def list_local_readiness_profiles(enabled_only: bool = True) -> list[LocalReadinessProfile]:
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())

def validate_local_readiness_profiles() -> None:
    for name, p in _PROFILES.items():
        if not p.language:
            raise ConfigError(f"Profile {name} must have a language.")
        if p.max_checks <= 0:
            raise ConfigError(f"Profile {name} max_checks must be positive.")
        if not (0.0 <= p.min_readiness_score <= 1.0):
            raise ConfigError(f"Profile {name} min_readiness_score must be between 0 and 1.")
        if not (0.0 <= p.min_quality_score <= 1.0):
            raise ConfigError(f"Profile {name} min_quality_score must be between 0 and 1.")
        if not p.dry_run_default:
            raise ConfigError(f"Profile {name} must have dry_run_default=True.")
        if p.allow_production_release_claim or p.allow_deployment_claim or p.allow_auto_fix or p.allow_file_modification or p.allow_file_deletion or p.allow_overwrite or p.allow_cloud_upload or p.allow_external_service or p.allow_live_commands or p.allow_broker_commands or p.allow_deploy_commands or p.allow_background_daemons or p.allow_real_market_download or p.allow_external_llm:
            raise ConfigError(f"Profile {name} must not allow dangerous operations.")

def get_default_local_readiness_profile() -> LocalReadinessProfile:
    return _PROFILES["balanced_local_readiness"]
