from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalDistributionPackagingProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_real_archive_creation: bool = False
    allow_zip_creation: bool = False
    allow_tar_creation: bool = False
    allow_binary_artifact: bool = False
    allow_installer_creation: bool = False
    allow_executable_packaging: bool = False
    allow_package_publish: bool = False
    allow_docker_build_push: bool = False
    allow_git_tag: bool = False
    allow_cloud_upload: bool = False
    allow_deployment: bool = False
    allow_official_release: bool = False
    allow_official_handover: bool = False
    allow_legal_signoff: bool = False
    allow_compliance_approval: bool = False
    allow_production_approval_claim: bool = False
    allow_official_acceptance_claim: bool = False
    allow_broker_readiness_claim: bool = False
    allow_live_trading_claim: bool = False
    allow_investment_advice: bool = False
    allow_model_deployment_claim: bool = False
    allow_web_server: bool = False
    allow_dashboard_creation: bool = False
    allow_gui_creation: bool = False
    allow_tui_creation: bool = False
    allow_telemetry: bool = False
    allow_external_service: bool = False
    allow_external_llm: bool = False
    allow_vector_db: bool = False
    allow_embedding_api: bool = False
    allow_file_modification: bool = False
    allow_file_deletion: bool = False
    allow_file_move: bool = False
    allow_overwrite: bool = False
    scan_docs: bool = True
    scan_reports: bool = True
    scan_data_lake: bool = True
    scan_scripts: bool = True
    scan_tests: bool = True
    scan_generated_docs: bool = True
    scan_documentation_export_outputs: bool = True
    scan_review_outputs: bool = True
    scan_atlas_outputs: bool = True
    scan_continuity_outputs: bool = True
    scan_preservation_outputs: bool = True
    scan_completion_outputs: bool = True
    scan_safety_outputs: bool = True
    max_items: int = 750000
    max_rows: int = 300000
    min_readiness_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

PROFILES = {
    "balanced_local_distribution_packaging": LocalDistributionPackagingProfile(
        name="balanced_local_distribution_packaging",
        description="Genel amacli local/offline distribution bundle rehearsal, portable docs bundle ve packaging governance profili.",
        notes="Genel amacli local/offline distribution bundle rehearsal, portable docs bundle ve packaging governance profili."
    ),
    "portable_docs_focus": LocalDistributionPackagingProfile(
        name="portable_docs_focus",
        description="Portable docs bundle odakli",
        scan_docs=True,
        scan_reports=True,
        scan_generated_docs=True,
        scan_documentation_export_outputs=True,
        scan_review_outputs=True,
        scan_data_lake=False,
        scan_scripts=False,
        scan_tests=False,
        scan_atlas_outputs=False,
        scan_continuity_outputs=False,
        scan_preservation_outputs=False,
        scan_completion_outputs=False,
        scan_safety_outputs=False,
        max_rows=200000,
        notes="Portable docs bundle, reading order, role map ve quickstart packet odakli profil."
    ),
    "release_folder_focus": LocalDistributionPackagingProfile(
        name="release_folder_focus",
        description="Offline release folder manifest odakli",
        scan_docs=True,
        scan_reports=True,
        scan_data_lake=True,
        scan_scripts=True,
        scan_tests=True,
        scan_generated_docs=True,
        scan_documentation_export_outputs=False,
        scan_review_outputs=False,
        scan_atlas_outputs=False,
        scan_continuity_outputs=False,
        scan_preservation_outputs=False,
        scan_completion_outputs=False,
        scan_safety_outputs=False,
        max_rows=250000,
        notes="Offline release folder manifest, folder tree, inclusion/exclusion matrices ve ZIP-map odakli profil."
    ),
    "strict_packaging_safety": LocalDistributionPackagingProfile(
        name="strict_packaging_safety",
        description="Strict safety",
        max_items=300000,
        max_rows=120000,
        min_readiness_score=0.60,
        min_quality_score=0.60,
        notes="Archive/ZIP/release/publish/deploy/binary/installer/live/broker/advice overclaim denetimini sikilastiran profil."
    )
}

def get_local_distribution_packaging_profile(name: str) -> LocalDistributionPackagingProfile:
    if name not in PROFILES:
        raise ConfigError(f"Bilinmeyen profile: {name}")
    return PROFILES[name]

def list_local_distribution_packaging_profiles(enabled_only: bool = True) -> list[LocalDistributionPackagingProfile]:
    return [p for p in PROFILES.values() if not enabled_only or p.enabled]

def validate_local_distribution_packaging_profiles() -> None:
    for p in PROFILES.values():
        if not p.language:
            raise ConfigError(f"Profile {p.name}: language bos olmamali.")
        if p.max_items <= 0 or p.max_rows <= 0:
            raise ConfigError(f"Profile {p.name}: max_items ve max_rows pozitif olmali.")
        if not (0 <= p.min_readiness_score <= 1) or not (0 <= p.min_quality_score <= 1):
            raise ConfigError(f"Profile {p.name}: min_readiness_score ve min_quality_score 0-1 araliginda olmali.")
        if not p.dry_run_default:
            raise ConfigError(f"Profile {p.name}: dry_run_default True olmali.")
        if any([
            p.allow_real_archive_creation, p.allow_zip_creation, p.allow_tar_creation,
            p.allow_binary_artifact, p.allow_installer_creation, p.allow_package_publish,
            p.allow_docker_build_push, p.allow_git_tag, p.allow_cloud_upload,
            p.allow_deployment, p.allow_official_release, p.allow_official_handover,
            p.allow_legal_signoff, p.allow_compliance_approval, p.allow_production_approval_claim,
            p.allow_broker_readiness_claim, p.allow_live_trading_claim, p.allow_investment_advice,
            p.allow_dashboard_creation, p.allow_external_service, p.allow_vector_db,
            p.allow_file_modification, p.allow_file_deletion, p.allow_file_move, p.allow_overwrite
        ]):
            raise ConfigError(f"Profile {p.name}: tehlikeli allow flagleri True olamaz.")

def get_default_local_distribution_packaging_profile() -> LocalDistributionPackagingProfile:
    return PROFILES["balanced_local_distribution_packaging"]
