from dataclasses import dataclass
from typing import List, Dict

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalMaintenanceProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_production_scheduler: bool = False
    allow_background_daemon: bool = False
    allow_auto_upgrade: bool = False
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
    allow_real_market_download: bool = False
    scan_docs: bool = True
    scan_tests: bool = True
    scan_scripts: bool = True
    scan_reports: bool = True
    scan_data_lake: bool = True
    scan_configs: bool = True
    scan_requirements: bool = True
    scan_cross_layer_outputs: bool = True
    default_monthly_review_day: int = 1
    default_quarterly_review_month_interval: int = 3
    stale_report_days_warning: int = 45
    stale_doc_days_warning: int = 90
    stale_test_days_warning: int = 90
    dependency_age_days_warning: int = 180
    max_checks: int = 300000
    min_sustainability_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

def _build_default_profiles() -> Dict[str, LocalMaintenanceProfile]:
    return {
        "balanced_local_maintenance": LocalMaintenanceProfile(
            name="balanced_local_maintenance",
            description="Genel amacli local/offline long-term maintenance ve sustainability planning profili.",
            notes="Genel amaçlı local/offline long-term maintenance ve sustainability planning profili."
        ),
        "strict_sustainability_review": LocalMaintenanceProfile(
            name="strict_sustainability_review",
            description="Stale output, dependency aging, safety boundary ve manual review kontrollerini sikilastiran profil.",
            stale_report_days_warning=30,
            stale_doc_days_warning=60,
            stale_test_days_warning=60,
            dependency_age_days_warning=120,
            min_sustainability_score=0.60,
            min_quality_score=0.60,
            notes="Stale output, dependency aging, safety boundary ve manual review kontrollerini sıkılaştıran profil."
        ),
        "documentation_cadence_focus": LocalMaintenanceProfile(
            name="documentation_cadence_focus",
            description="Docs, operator manual, SAFE_USAGE, PHASE_LOG ve generated documentation cadence odakli profil.",
            scan_data_lake=False,
            scan_requirements=False,
            stale_doc_days_warning=45,
            notes="Docs, operator manual, SAFE_USAGE, PHASE_LOG ve generated documentation cadence odaklı profil."
        ),
        "dependency_watch_focus": LocalMaintenanceProfile(
            name="dependency_watch_focus",
            description="requirements, pyproject, imports ve dependency review checklist odakli profil.",
            scan_reports=False,
            scan_data_lake=False,
            scan_cross_layer_outputs=False,
            dependency_age_days_warning=90,
            notes="requirements, pyproject, imports ve dependency review checklist odaklı profil."
        )
    }

_PROFILES = _build_default_profiles()

def get_local_maintenance_profile(name: str) -> LocalMaintenanceProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Unknown local maintenance profile: {name}")
    return _PROFILES[name]

def list_local_maintenance_profiles(enabled_only: bool = True) -> List[LocalMaintenanceProfile]:
    profiles = list(_PROFILES.values())
    if enabled_only:
        return [p for p in profiles if p.enabled]
    return profiles

def validate_local_maintenance_profiles() -> None:
    for profile in _PROFILES.values():
        if not profile.language:
            raise ConfigError(f"Profile {profile.name} has no language specified.")
        if not (1 <= profile.default_monthly_review_day <= 28):
            raise ConfigError(f"Profile {profile.name} has invalid default_monthly_review_day (must be 1-28).")
        if profile.default_quarterly_review_month_interval <= 0:
            raise ConfigError(f"Profile {profile.name} has invalid default_quarterly_review_month_interval.")
        if profile.stale_report_days_warning <= 0:
            raise ConfigError(f"Profile {profile.name} has invalid stale_report_days_warning.")
        if profile.stale_doc_days_warning <= 0:
            raise ConfigError(f"Profile {profile.name} has invalid stale_doc_days_warning.")
        if profile.stale_test_days_warning <= 0:
            raise ConfigError(f"Profile {profile.name} has invalid stale_test_days_warning.")
        if profile.dependency_age_days_warning <= 0:
            raise ConfigError(f"Profile {profile.name} has invalid dependency_age_days_warning.")
        if profile.max_checks <= 0:
            raise ConfigError(f"Profile {profile.name} has invalid max_checks.")
        if not (0.0 <= profile.min_sustainability_score <= 1.0):
            raise ConfigError(f"Profile {profile.name} has invalid min_sustainability_score.")
        if not (0.0 <= profile.min_quality_score <= 1.0):
            raise ConfigError(f"Profile {profile.name} has invalid min_quality_score.")
        if not profile.dry_run_default:
            raise ConfigError(f"Profile {profile.name} must have dry_run_default set to True.")
        if any([
            profile.allow_production_scheduler,
            profile.allow_background_daemon,
            profile.allow_auto_upgrade,
            profile.allow_auto_fix,
            profile.allow_file_modification,
            profile.allow_file_deletion,
            profile.allow_overwrite,
            profile.allow_cloud_upload,
            profile.allow_external_service,
            profile.allow_external_llm,
            profile.allow_live_commands,
            profile.allow_broker_commands,
            profile.allow_deploy_commands,
            profile.allow_real_market_download
        ]):
            raise ConfigError(f"Profile {profile.name} has forbidden allow_* flags set to True.")

def get_default_local_maintenance_profile() -> LocalMaintenanceProfile:
    return get_local_maintenance_profile("balanced_local_maintenance")

validate_local_maintenance_profiles()
