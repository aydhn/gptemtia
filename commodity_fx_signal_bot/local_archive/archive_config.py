"""
Archive Configuration Module
Defines the local archive profiles and configuration parameters.
"""

from dataclasses import dataclass
from typing import Dict

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalArchiveProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_cloud_upload: bool = False
    allow_external_archive_service: bool = False
    allow_auto_archive: bool = False
    allow_auto_compress: bool = False
    allow_file_modification: bool = False
    allow_file_deletion: bool = False
    allow_file_move: bool = False
    allow_overwrite: bool = False
    allow_external_llm: bool = False
    allow_live_commands: bool = False
    allow_broker_commands: bool = False
    allow_deploy_commands: bool = False
    allow_background_daemons: bool = False
    allow_real_market_download: bool = False
    scan_docs: bool = True
    scan_reports: bool = True
    scan_data_lake: bool = True
    scan_configs: bool = True
    scan_scripts: bool = True
    scan_tests: bool = True
    scan_cross_layer_outputs: bool = True
    scan_security_layers: bool = True
    max_items: int = 300000
    max_file_mb_for_hash: int = 100
    retention_review_days: int = 180
    integrity_review_days: int = 90
    min_preservation_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_PROFILES: Dict[str, LocalArchiveProfile] = {
    "balanced_local_archive": LocalArchiveProfile(
        name="balanced_local_archive",
        description="Genel amaçlı local/offline archive strategy, snapshot catalog ve preservation planning profili.",
        language="tr",
        dry_run_default=True,
        allow_cloud_upload=False,
        allow_external_archive_service=False,
        allow_auto_archive=False,
        allow_auto_compress=False,
        allow_file_modification=False,
        allow_file_deletion=False,
        allow_file_move=False,
        allow_overwrite=False,
        allow_external_llm=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        allow_real_market_download=False,
        scan_docs=True,
        scan_reports=True,
        scan_data_lake=True,
        scan_configs=True,
        scan_scripts=True,
        scan_tests=True,
        scan_cross_layer_outputs=True,
        scan_security_layers=True,
        max_items=300000,
        max_file_mb_for_hash=100,
        retention_review_days=180,
        integrity_review_days=90,
        min_preservation_score=0.40,
        min_quality_score=0.40,
        notes="Genel amaçlı local/offline archive strategy, snapshot catalog ve preservation planning profili."
    ),
    "strict_preservation_boundary": LocalArchiveProfile(
        name="strict_preservation_boundary",
        description="Secret exclusion, archive boundary, integrity review ve preservation score kontrollerini sıkılaştıran profil.",
        language="tr",
        dry_run_default=True,
        allow_cloud_upload=False,
        allow_external_archive_service=False,
        allow_auto_archive=False,
        allow_auto_compress=False,
        allow_file_modification=False,
        allow_file_deletion=False,
        allow_file_move=False,
        allow_overwrite=False,
        allow_external_llm=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        allow_real_market_download=False,
        scan_docs=True,
        scan_reports=True,
        scan_data_lake=True,
        scan_configs=True,
        scan_scripts=True,
        scan_tests=True,
        scan_cross_layer_outputs=True,
        scan_security_layers=True,
        max_items=200000,
        max_file_mb_for_hash=50,
        retention_review_days=90,
        integrity_review_days=60,
        min_preservation_score=0.60,
        min_quality_score=0.60,
        notes="Secret exclusion, archive boundary, integrity review ve preservation score kontrollerini sıkılaştıran profil."
    ),
    "documentation_archive_focus": LocalArchiveProfile(
        name="documentation_archive_focus",
        description="Dokümantasyon, generated docs, README, operator guide ve phase log arşiv indeksine odaklı profil.",
        language="tr",
        dry_run_default=True,
        allow_cloud_upload=False,
        allow_external_archive_service=False,
        allow_auto_archive=False,
        allow_auto_compress=False,
        allow_file_modification=False,
        allow_file_deletion=False,
        allow_file_move=False,
        allow_overwrite=False,
        allow_external_llm=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        allow_real_market_download=False,
        scan_docs=True,
        scan_reports=True,
        scan_data_lake=False,
        scan_configs=True,
        scan_scripts=False,
        scan_tests=False,
        scan_cross_layer_outputs=True,
        scan_security_layers=True,
        max_items=300000,
        max_file_mb_for_hash=50,
        retention_review_days=180,
        integrity_review_days=90,
        min_preservation_score=0.40,
        min_quality_score=0.40,
        notes="Dokümantasyon, generated docs, README, operator guide ve phase log arşiv indeksine odaklı profil."
    ),
    "cross_layer_archive_focus": LocalArchiveProfile(
        name="cross_layer_archive_focus",
        description="Evidence, metadata, graph, timeline, consistency, readiness ve maintenance outputs arşiv kapsamına odaklı profil.",
        language="tr",
        dry_run_default=True,
        allow_cloud_upload=False,
        allow_external_archive_service=False,
        allow_auto_archive=False,
        allow_auto_compress=False,
        allow_file_modification=False,
        allow_file_deletion=False,
        allow_file_move=False,
        allow_overwrite=False,
        allow_external_llm=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        allow_real_market_download=False,
        scan_docs=True,
        scan_reports=True,
        scan_data_lake=True,
        scan_configs=True,
        scan_scripts=True,
        scan_tests=True,
        scan_cross_layer_outputs=True,
        scan_security_layers=True,
        max_items=300000,
        max_file_mb_for_hash=100,
        retention_review_days=180,
        integrity_review_days=90,
        min_preservation_score=0.40,
        min_quality_score=0.40,
        notes="Evidence, metadata, graph, timeline, consistency, readiness ve maintenance outputs arşiv kapsamına odaklı profil."
    )
}

def get_local_archive_profile(name: str) -> LocalArchiveProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Unknown local archive profile: {name}")
    return _PROFILES[name]

def list_local_archive_profiles(enabled_only: bool = True) -> list[LocalArchiveProfile]:
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())

def validate_local_archive_profiles() -> None:
    for name, profile in _PROFILES.items():
        if not profile.language:
            raise ValueError(f"Profile {name} missing language")
        if profile.max_items <= 0:
            raise ValueError(f"Profile {name} max_items must be positive")
        if profile.max_file_mb_for_hash <= 0:
            raise ValueError(f"Profile {name} max_file_mb_for_hash must be positive")
        if profile.retention_review_days <= 0:
            raise ValueError(f"Profile {name} retention_review_days must be positive")
        if profile.integrity_review_days <= 0:
            raise ValueError(f"Profile {name} integrity_review_days must be positive")
        if not (0 <= profile.min_preservation_score <= 1):
            raise ValueError(f"Profile {name} min_preservation_score must be between 0 and 1")
        if not (0 <= profile.min_quality_score <= 1):
            raise ValueError(f"Profile {name} min_quality_score must be between 0 and 1")
        if not profile.dry_run_default:
            raise ValueError(f"Profile {name} dry_run_default must be True")

        # Security boundaries
        if profile.allow_cloud_upload:
            raise ValueError(f"Profile {name} allow_cloud_upload must be False")
        if profile.allow_external_archive_service:
            raise ValueError(f"Profile {name} allow_external_archive_service must be False")
        if profile.allow_auto_archive:
            raise ValueError(f"Profile {name} allow_auto_archive must be False")
        if profile.allow_auto_compress:
            raise ValueError(f"Profile {name} allow_auto_compress must be False")
        if profile.allow_file_modification:
            raise ValueError(f"Profile {name} allow_file_modification must be False")
        if profile.allow_file_deletion:
            raise ValueError(f"Profile {name} allow_file_deletion must be False")
        if profile.allow_file_move:
            raise ValueError(f"Profile {name} allow_file_move must be False")
        if profile.allow_overwrite:
            raise ValueError(f"Profile {name} allow_overwrite must be False")
        if profile.allow_external_llm:
            raise ValueError(f"Profile {name} allow_external_llm must be False")
        if profile.allow_live_commands:
            raise ValueError(f"Profile {name} allow_live_commands must be False")
        if profile.allow_broker_commands:
            raise ValueError(f"Profile {name} allow_broker_commands must be False")
        if profile.allow_deploy_commands:
            raise ValueError(f"Profile {name} allow_deploy_commands must be False")
        if profile.allow_background_daemons:
            raise ValueError(f"Profile {name} allow_background_daemons must be False")
        if profile.allow_real_market_download:
            raise ValueError(f"Profile {name} allow_real_market_download must be False")

def get_default_local_archive_profile() -> LocalArchiveProfile:
    return _PROFILES["balanced_local_archive"]
