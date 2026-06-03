"""
Backup recovery configuration profiles.
"""

from dataclasses import dataclass


class ConfigError(Exception):
    pass


@dataclass(frozen=True)
class BackupRecoveryProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_backup_copy: bool = False
    allow_restore_copy: bool = False
    allow_overwrite: bool = False
    allow_delete: bool = False
    allow_cloud_backup: bool = False
    allow_external_storage: bool = False
    allow_live_commands: bool = False
    allow_broker_commands: bool = False
    allow_deploy_commands: bool = False
    allow_background_daemons: bool = False
    allow_real_market_download: bool = False
    allow_external_llm: bool = False
    include_source: bool = True
    include_docs: bool = True
    include_tests: bool = True
    include_configs: bool = True
    include_reports_manifest_only: bool = True
    include_data_manifest_only: bool = True
    include_generated_manifests: bool = True
    max_inventory_files: int = 150000
    max_hash_file_mb: int = 100
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""


_PROFILES = {
    "balanced_local_backup_recovery": BackupRecoveryProfile(
        name="balanced_local_backup_recovery",
        description="General purpose local backup recovery profile.",
        notes="Genel amaçlı local/offline backup-restore dry-run ve disaster recovery planning profili.",
    ),
    "critical_only_recovery": BackupRecoveryProfile(
        name="critical_only_recovery",
        description="Recovery profile focusing only on critical artifacts.",
        max_inventory_files=75000,
        notes="Kritik kaynak, config, test, docs ve manifestlere odaklı recovery profili.",
    ),
    "full_state_manifest_recovery": BackupRecoveryProfile(
        name="full_state_manifest_recovery",
        description="Full local project state manifest and integrity plan.",
        max_inventory_files=250000,
        max_hash_file_mb=200,
        notes="Tam local project state manifest ve integrity planı odaklı profil.",
    ),
    "strict_backup_safety": BackupRecoveryProfile(
        name="strict_backup_safety",
        description="Strict safety checks, preventing destructive restores and secret leaks.",
        min_quality_score=0.60,
        notes="Secret exclusion, destructive restore ve cloud/external storage risklerini sıkı denetleyen profil.",
    ),
}


def get_backup_recovery_profile(name: str) -> BackupRecoveryProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Unknown backup recovery profile: {name}")
    return _PROFILES[name]


def list_backup_recovery_profiles(enabled_only: bool = True) -> list[BackupRecoveryProfile]:
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())


def validate_backup_recovery_profiles() -> None:
    for name, profile in _PROFILES.items():
        if not profile.language:
            raise ConfigError(f"Profile {name} must have a language.")
        if profile.max_inventory_files <= 0:
            raise ConfigError(f"Profile {name} max_inventory_files must be positive.")
        if profile.max_hash_file_mb <= 0:
            raise ConfigError(f"Profile {name} max_hash_file_mb must be positive.")
        if not (0.0 <= profile.min_quality_score <= 1.0):
            raise ConfigError(f"Profile {name} min_quality_score must be between 0.0 and 1.0.")
        if not profile.dry_run_default:
            raise ConfigError(f"Profile {name} must have dry_run_default=True.")

        # Verify destructive / live flags are False
        if profile.allow_backup_copy or profile.allow_restore_copy or profile.allow_overwrite or profile.allow_delete:
            raise ConfigError(f"Profile {name} must have destructive flags set to False.")
        if profile.allow_cloud_backup or profile.allow_external_storage:
            raise ConfigError(f"Profile {name} must have cloud/external flags set to False.")
        if (profile.allow_live_commands or profile.allow_broker_commands or profile.allow_deploy_commands or
            profile.allow_background_daemons or profile.allow_real_market_download or profile.allow_external_llm):
            raise ConfigError(f"Profile {name} must have live/broker/deploy flags set to False.")


def get_default_backup_recovery_profile() -> BackupRecoveryProfile:
    return _PROFILES["balanced_local_backup_recovery"]
