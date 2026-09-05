from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalFinalClosingProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_real_project_lock: bool = False
    allow_official_project_constitution: bool = False
    allow_official_non_production_seal: bool = False
    allow_official_governance_seal: bool = False
    allow_official_archive: bool = False
    allow_official_handover: bool = False
    allow_official_acceptance: bool = False
    allow_official_release: bool = False
    allow_legal_signoff: bool = False
    allow_compliance_approval: bool = False
    allow_production_approval_claim: bool = False
    allow_broker_readiness_claim: bool = False
    allow_live_trading_claim: bool = False
    allow_investment_advice: bool = False
    allow_model_deployment_claim: bool = False
    allow_real_build: bool = False
    allow_cloud_build: bool = False
    allow_ci_cd: bool = False
    allow_docker_build_push: bool = False
    allow_docker_image_creation: bool = False
    allow_build_artifact: bool = False
    allow_binary_artifact: bool = False
    allow_installer_creation: bool = False
    allow_executable_packaging: bool = False
    allow_dependency_install: bool = False
    allow_environment_provisioning: bool = False
    allow_package_publish: bool = False
    allow_git_tag: bool = False
    allow_cloud_upload: bool = False
    allow_deployment: bool = False
    allow_real_archive_creation: bool = False
    allow_zip_creation: bool = False
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
    scan_terminal_closeout_outputs: bool = True
    scan_completion_outputs: bool = True
    scan_reproducibility_outputs: bool = True
    scan_packaging_outputs: bool = True
    scan_documentation_export_outputs: bool = True
    scan_review_outputs: bool = True
    scan_atlas_outputs: bool = True
    scan_continuity_outputs: bool = True
    scan_preservation_outputs: bool = True
    scan_safety_outputs: bool = True
    max_items: int = 750000
    max_rows: int = 300000
    min_readiness_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_PROFILES = {
    "balanced_local_final_closing": LocalFinalClosingProfile(
        name="balanced_local_final_closing",
        description="Genel amaçlı local/offline final master terminal lock, project constitution ve closing super-binder profili.",
        notes="Genel amaçlı local/offline final master terminal lock, project constitution ve closing super-binder profili."
    ),
    "constitution_focus": LocalFinalClosingProfile(
        name="constitution_focus",
        description="Ultimate offline project constitution, boundaries, role registry ve reading order odaklı profil.",
        scan_data_lake=False,
        scan_scripts=False,
        scan_tests=False,
        max_rows=220000,
        notes="Ultimate offline project constitution, boundaries, role registry ve reading order odaklı profil."
    ),
    "archive_index_focus": LocalFinalClosingProfile(
        name="archive_index_focus",
        description="Local-only terminal archive index, source/output/report/documentation/governance maps ve exclusion register odaklı profil.",
        scan_terminal_closeout_outputs=False,
        scan_completion_outputs=False,
        scan_reproducibility_outputs=False,
        scan_packaging_outputs=False,
        scan_documentation_export_outputs=False,
        scan_review_outputs=False,
        scan_atlas_outputs=False,
        scan_continuity_outputs=False,
        scan_preservation_outputs=False,
        scan_safety_outputs=False,
        max_rows=250000,
        notes="Local-only terminal archive index, source/output/report/documentation/governance maps ve exclusion register odaklı profil."
    ),
    "strict_final_closing_safety": LocalFinalClosingProfile(
        name="strict_final_closing_safety",
        description="Project lock/constitution/seal/archive/handover/acceptance/release/build/deploy/live/broker/advice overclaim denetimini sıkılaştıran profil.",
        max_items=300000,
        max_rows=120000,
        min_readiness_score=0.60,
        min_quality_score=0.60,
        notes="Project lock/constitution/seal/archive/handover/acceptance/release/build/deploy/live/broker/advice overclaim denetimini sıkılaştıran profil."
    )
}

def get_local_final_closing_profile(name: str) -> LocalFinalClosingProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Profile {name} not found.")
    return _PROFILES[name]

def list_local_final_closing_profiles(enabled_only: bool = True) -> list[LocalFinalClosingProfile]:
    return [p for p in _PROFILES.values() if not enabled_only or p.enabled]

def get_default_local_final_closing_profile() -> LocalFinalClosingProfile:
    return _PROFILES["balanced_local_final_closing"]

def validate_local_final_closing_profiles() -> None:
    for name, p in _PROFILES.items():
        if not p.language:
            raise ConfigError(f"Profile {name} has no language.")
        if p.max_items <= 0 or p.max_rows <= 0:
            raise ConfigError(f"Profile {name} max_items and max_rows must be positive.")
        if not (0 <= p.min_readiness_score <= 1) or not (0 <= p.min_quality_score <= 1):
            raise ConfigError(f"Profile {name} scores must be between 0 and 1.")
        if name in ["balanced_local_final_closing", "constitution_focus", "archive_index_focus", "strict_final_closing_safety"]:
            if not p.dry_run_default:
                raise ConfigError(f"Default profile {name} must have dry_run_default=True.")
            if p.allow_real_project_lock or p.allow_official_project_constitution or p.allow_official_non_production_seal or p.allow_official_archive or p.allow_official_handover or p.allow_official_release or p.allow_real_build or p.allow_deployment or p.allow_live_trading_claim or p.allow_investment_advice:
                raise ConfigError(f"Default profile {name} must not allow dangerous actions.")
