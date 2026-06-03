import os
from dataclasses import dataclass
from typing import List

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class PortablePackagingProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_archive_create: bool = False
    allow_package_publish: bool = False
    allow_docker: bool = False
    allow_cloud_deploy: bool = False
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
    max_inventory_files: int = 100000
    max_manifest_file_mb: int = 50
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

def _build_profiles() -> dict[str, PortablePackagingProfile]:
    return {
        "balanced_local_packaging": PortablePackagingProfile(
            name="balanced_local_packaging",
            description="Genel amaçlı local/offline packaging manifest ve kurulum doğrulama profili.",
            language="tr",
            dry_run_default=True,
            allow_archive_create=False,
            allow_package_publish=False,
            allow_docker=False,
            allow_cloud_deploy=False,
            allow_live_commands=False,
            allow_broker_commands=False,
            allow_deploy_commands=False,
            allow_background_daemons=False,
            allow_real_market_download=False,
            allow_external_llm=False,
            include_source=True,
            include_docs=True,
            include_tests=True,
            include_configs=True,
            include_reports_manifest_only=True,
            include_data_manifest_only=True,
            max_inventory_files=100000,
            max_manifest_file_mb=50,
            min_quality_score=0.40,
            notes="Genel amaçlı local/offline packaging manifest ve kurulum doğrulama profili."
        ),
        "minimal_portable_manifest": PortablePackagingProfile(
            name="minimal_portable_manifest",
            description="Daha küçük taşınabilir manifest ve hızlı kurulum kontrolü profili.",
            language="tr",
            dry_run_default=True,
            allow_archive_create=False,
            allow_package_publish=False,
            allow_docker=False,
            allow_cloud_deploy=False,
            allow_live_commands=False,
            allow_broker_commands=False,
            allow_deploy_commands=False,
            allow_background_daemons=False,
            allow_real_market_download=False,
            allow_external_llm=False,
            include_source=True,
            include_docs=True,
            include_tests=False,
            include_configs=True,
            include_reports_manifest_only=True,
            include_data_manifest_only=True,
            max_inventory_files=50000,
            max_manifest_file_mb=50,
            min_quality_score=0.40,
            notes="Daha küçük taşınabilir manifest ve hızlı kurulum kontrolü profili."
        ),
        "full_local_reproducibility": PortablePackagingProfile(
            name="full_local_reproducibility",
            description="Tam local reproducibility, dependency snapshot ve install verification profili.",
            language="tr",
            dry_run_default=True,
            allow_archive_create=False,
            allow_package_publish=False,
            allow_docker=False,
            allow_cloud_deploy=False,
            allow_live_commands=False,
            allow_broker_commands=False,
            allow_deploy_commands=False,
            allow_background_daemons=False,
            allow_real_market_download=False,
            allow_external_llm=False,
            include_source=True,
            include_docs=True,
            include_tests=True,
            include_configs=True,
            include_reports_manifest_only=True,
            include_data_manifest_only=True,
            max_inventory_files=150000,
            max_manifest_file_mb=50,
            min_quality_score=0.40,
            notes="Tam local reproducibility, dependency snapshot ve install verification profili."
        ),
        "strict_packaging_safety": PortablePackagingProfile(
            name="strict_packaging_safety",
            description="Package publish/deploy/credential leakage ve forbidden command denetimi öncelikli profil.",
            language="tr",
            dry_run_default=True,
            allow_archive_create=False,
            allow_package_publish=False,
            allow_docker=False,
            allow_cloud_deploy=False,
            allow_live_commands=False,
            allow_broker_commands=False,
            allow_deploy_commands=False,
            allow_background_daemons=False,
            allow_real_market_download=False,
            allow_external_llm=False,
            include_source=True,
            include_docs=True,
            include_tests=True,
            include_configs=True,
            include_reports_manifest_only=True,
            include_data_manifest_only=True,
            max_inventory_files=100000,
            max_manifest_file_mb=50,
            min_quality_score=0.60,
            notes="Package publish/deploy/credential leakage ve forbidden command denetimi öncelikli profil."
        )
    }

def get_portable_packaging_profile(name: str) -> PortablePackagingProfile:
    profiles = _build_profiles()
    if name not in profiles:
        raise ConfigError(f"Unknown profile: {name}")
    return profiles[name]

def list_portable_packaging_profiles(enabled_only: bool = True) -> List[PortablePackagingProfile]:
    profiles = list(_build_profiles().values())
    if enabled_only:
        return [p for p in profiles if p.enabled]
    return profiles

def validate_portable_packaging_profiles() -> None:
    profiles = _build_profiles()
    for name, p in profiles.items():
        if not p.language:
            raise ConfigError(f"Profile {name} missing language")
        if p.max_inventory_files <= 0:
            raise ConfigError(f"Profile {name} max_inventory_files must be positive")
        if p.max_manifest_file_mb <= 0:
            raise ConfigError(f"Profile {name} max_manifest_file_mb must be positive")
        if not (0.0 <= p.min_quality_score <= 1.0):
            raise ConfigError(f"Profile {name} min_quality_score must be between 0 and 1")
        if not p.dry_run_default:
            raise ConfigError(f"Profile {name} dry_run_default must be True")
        if p.allow_archive_create or p.allow_package_publish or p.allow_docker or p.allow_cloud_deploy:
            raise ConfigError(f"Profile {name} allows deployment/archiving")
        if p.allow_live_commands or p.allow_broker_commands or p.allow_deploy_commands or p.allow_background_daemons or p.allow_real_market_download or p.allow_external_llm:
            raise ConfigError(f"Profile {name} allows live/broker/daemon actions")

def get_default_portable_packaging_profile() -> PortablePackagingProfile:
    from config.settings import settings
    return get_portable_packaging_profile(settings.default_portable_packaging_profile)
