from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalCompletionGovernanceProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_real_certification: bool = False
    allow_official_acceptance: bool = False
    allow_official_project_closure: bool = False
    allow_official_project_freeze: bool = False
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

PROFILES = {
    "balanced_local_completion_governance": LocalCompletionGovernanceProfile(
        name="balanced_local_completion_governance",
        description="Balanced profile.",
        notes="Genel amaçlı local/offline closure synthesis, certification rehearsal ve completion governance profili."
    ),
    "closure_synthesis_focus": LocalCompletionGovernanceProfile(
        name="closure_synthesis_focus",
        description="Closure synthesis focus.",
        scan_data_lake=False,
        scan_scripts=False,
        scan_tests=False,
        scan_atlas_outputs=False,
        scan_continuity_outputs=False,
        scan_preservation_outputs=False,
        scan_safety_outputs=False,
        scan_documentation_export_outputs=False,
        max_rows=200000,
        notes="Final closure synthesis, phase recap, module recap, output recap ve safety recap odaklı profil."
    ),
    "acceptance_evidence_focus": LocalCompletionGovernanceProfile(
        name="acceptance_evidence_focus",
        description="Acceptance evidence focus.",
        scan_reproducibility_outputs=False,
        scan_packaging_outputs=False,
        scan_documentation_export_outputs=False,
        scan_review_outputs=False,
        scan_atlas_outputs=False,
        scan_continuity_outputs=False,
        scan_preservation_outputs=False,
        scan_safety_outputs=False,
        max_rows=250000,
        notes="Offline acceptance evidence pack, evidence maps, limitation register ve non-approval registry odaklı profil."
    ),
    "strict_completion_safety": LocalCompletionGovernanceProfile(
        name="strict_completion_safety",
        description="Strict safety profile.",
        max_items=300000,
        max_rows=120000,
        min_readiness_score=0.60,
        min_quality_score=0.60,
        notes="Certification/acceptance/closure/freeze/release/build/deploy/live/broker/advice overclaim denetimini sıkılaştıran profil."
    )
}

def get_local_completion_governance_profile(name: str) -> LocalCompletionGovernanceProfile:
    if name not in PROFILES:
        raise ConfigError(f"Profile {name} not found.")
    return PROFILES[name]

def list_local_completion_governance_profiles(enabled_only: bool = True) -> list[LocalCompletionGovernanceProfile]:
    if enabled_only:
        return [p for p in PROFILES.values() if p.enabled]
    return list(PROFILES.values())

def validate_local_completion_governance_profiles() -> None:
    for p in PROFILES.values():
        if not p.language:
            raise ConfigError("language bos olmamali.")
        if p.max_items <= 0 or p.max_rows <= 0:
            raise ConfigError("max_items ve max_rows pozitif olmali.")
        if not (0 <= p.min_readiness_score <= 1) or not (0 <= p.min_quality_score <= 1):
            raise ConfigError("min_readiness_score ve min_quality_score 0-1 araliginda olmali.")
        if not p.dry_run_default:
            raise ConfigError("dry_run_default True olmali.")
        if p.allow_real_certification or p.allow_official_acceptance or p.allow_official_project_closure or p.allow_official_project_freeze or p.allow_official_release or p.allow_legal_signoff or p.allow_compliance_approval or p.allow_production_approval_claim or p.allow_broker_readiness_claim or p.allow_live_trading_claim or p.allow_investment_advice or p.allow_model_deployment_claim or p.allow_real_build or p.allow_cloud_build or p.allow_ci_cd or p.allow_docker_build_push or p.allow_docker_image_creation or p.allow_build_artifact or p.allow_binary_artifact or p.allow_installer_creation or p.allow_executable_packaging or p.allow_dependency_install or p.allow_environment_provisioning or p.allow_package_publish or p.allow_git_tag or p.allow_cloud_upload or p.allow_deployment or p.allow_web_server or p.allow_dashboard_creation or p.allow_gui_creation or p.allow_tui_creation or p.allow_telemetry or p.allow_external_service or p.allow_external_llm or p.allow_vector_db or p.allow_embedding_api or p.allow_file_modification or p.allow_file_deletion or p.allow_file_move or p.allow_overwrite:
            raise ConfigError("Certification/acceptance vs. action flagleri False olmali.")

def get_default_local_completion_governance_profile() -> LocalCompletionGovernanceProfile:
    return PROFILES["balanced_local_completion_governance"]
