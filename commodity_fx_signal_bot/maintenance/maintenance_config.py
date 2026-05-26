"""Maintenance configuration models and default profiles."""
from dataclasses import dataclass
from typing import List


class ConfigError(Exception):
    pass


@dataclass(frozen=True)
class MaintenanceProfile:
    name: str
    description: str
    dry_run_default: bool = True
    allow_delete: bool = False
    allow_archive_move: bool = False
    scan_data_lake: bool = True
    scan_reports_output: bool = True
    scan_logs: bool = True
    scan_cache: bool = True
    scan_checkpoints: bool = True
    max_inventory_files: int = 50000
    large_file_threshold_mb: int = 100
    stale_days_default: int = 30
    keep_latest_n_reports: int = 10
    keep_latest_n_runs: int = 20
    keep_quality_reports_days: int = 90
    keep_governance_reports_days: int = 180
    keep_experiment_manifests_days: int = 365
    keep_knowledge_index_days: int = 30
    keep_cache_days: int = 14
    keep_checkpoints_days: int = 30
    archive_format: str = "zip_manifest_only"
    archive_max_bundle_mb: int = 1024
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""


_PROFILES = [
    MaintenanceProfile(
        name="balanced_local_maintenance",
        description="General purpose local dry-run maintenance, retention and archive planning profile.",
        dry_run_default=True,
        allow_delete=False,
        allow_archive_move=False,
        large_file_threshold_mb=100,
        stale_days_default=30,
        keep_latest_n_reports=10,
        keep_latest_n_runs=20,
        keep_cache_days=14,
        keep_checkpoints_days=30,
        archive_format="zip_manifest_only",
        notes="Genel amaçlı local dry-run bakım, retention ve archive planlama profili."
    ),
    MaintenanceProfile(
        name="conservative_local_maintenance",
        description="Longer retention, less aggressive cleanup candidates.",
        dry_run_default=True,
        allow_delete=False,
        allow_archive_move=False,
        large_file_threshold_mb=250,
        stale_days_default=60,
        keep_latest_n_reports=20,
        keep_latest_n_runs=50,
        keep_quality_reports_days=180,
        keep_governance_reports_days=365,
        keep_experiment_manifests_days=730,
        keep_cache_days=30,
        keep_checkpoints_days=60,
        notes="Daha uzun saklama ve daha az agresif cleanup adaylığı profili."
    ),
    MaintenanceProfile(
        name="storage_saving_maintenance",
        description="More aggressive cleanup/archive candidates for storage saving, still dry-run.",
        dry_run_default=True,
        allow_delete=False,
        allow_archive_move=False,
        large_file_threshold_mb=50,
        stale_days_default=14,
        keep_latest_n_reports=5,
        keep_latest_n_runs=10,
        keep_cache_days=7,
        keep_checkpoints_days=14,
        archive_max_bundle_mb=512,
        notes="Disk alanı tasarrufu için daha fazla cleanup/archive adayı üreten ama yine dry-run kalan profil."
    ),
    MaintenanceProfile(
        name="archive_focused_maintenance",
        description="Focused on generating archive manifests and plans.",
        dry_run_default=True,
        allow_delete=False,
        allow_archive_move=False,
        large_file_threshold_mb=100,
        stale_days_default=45,
        archive_format="zip_manifest_only",
        archive_max_bundle_mb=2048,
        notes="Arşiv manifestleri ve archive candidate planı üretmeye odaklı profil."
    )
]


def list_maintenance_profiles(enabled_only: bool = True) -> List[MaintenanceProfile]:
    if enabled_only:
        return [p for p in _PROFILES if p.enabled]
    return _PROFILES


def get_maintenance_profile(name: str) -> MaintenanceProfile:
    for profile in _PROFILES:
        if profile.name == name:
            return profile
    raise ConfigError(f"Unknown maintenance profile: {name}")


def get_default_maintenance_profile() -> MaintenanceProfile:
    return get_maintenance_profile("balanced_local_maintenance")


def validate_maintenance_profiles() -> None:
    for profile in _PROFILES:
        if profile.max_inventory_files <= 0:
            raise ConfigError(f"max_inventory_files must be positive in profile {profile.name}")
        if profile.large_file_threshold_mb <= 0:
            raise ConfigError(f"large_file_threshold_mb must be positive in profile {profile.name}")
        if profile.stale_days_default <= 0:
            raise ConfigError(f"stale_days_default must be positive in profile {profile.name}")
        if profile.keep_latest_n_reports <= 0:
            raise ConfigError(f"keep_latest_n_reports must be positive in profile {profile.name}")
        if profile.keep_latest_n_runs <= 0:
            raise ConfigError(f"keep_latest_n_runs must be positive in profile {profile.name}")
        if profile.archive_max_bundle_mb <= 0:
            raise ConfigError(f"archive_max_bundle_mb must be positive in profile {profile.name}")
        if not (0.0 <= profile.min_quality_score <= 1.0):
            raise ConfigError(f"min_quality_score must be between 0 and 1 in profile {profile.name}")
        if not profile.dry_run_default:
            raise ConfigError(f"dry_run_default must be True in profile {profile.name}")
        if profile.allow_delete:
            raise ConfigError(f"allow_delete must be False in profile {profile.name}")
        if profile.allow_archive_move:
            raise ConfigError(f"allow_archive_move must be False in profile {profile.name}")
        if not any([profile.scan_data_lake, profile.scan_reports_output, profile.scan_logs, profile.scan_cache, profile.scan_checkpoints]):
            raise ConfigError(f"At least one scan flag must be True in profile {profile.name}")
