"""Reproducibility config."""
from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalReproducibilityGovernanceProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_real_build: bool = False
    allow_cloud_build: bool = False
    allow_ci_cd: bool = False
    allow_docker_build_push: bool = False
    allow_docker_image_creation: bool = False
    allow_build_artifact: bool = False
    allow_binary_artifact: bool = False
    allow_installer_creation: bool = False
    allow_executable_packaging: bool = False
    allow_environment_provisioning: bool = False
    allow_dependency_install: bool = False
    allow_pip_install: bool = False
    allow_poetry_install: bool = False
    allow_conda_install: bool = False
    allow_package_publish: bool = False
    allow_git_tag: bool = False
    allow_cloud_upload: bool = False
    allow_deployment: bool = False
    allow_official_build_attestation: bool = False
    allow_reproducibility_certification: bool = False
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
    scan_packaging_outputs: bool = True
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

_PROFILES = {
    "balanced_local_reproducibility": LocalReproducibilityGovernanceProfile(
        name="balanced_local_reproducibility",
        description="Genel amacli local/offline reproducibility dossier, environment replay manifest ve deterministic runbook profili.",
        language="tr",
        dry_run_default=True,
        max_items=750000,
        max_rows=300000,
        min_readiness_score=0.40,
        min_quality_score=0.40,
        notes="Genel amaçlı local/offline reproducibility dossier, environment replay manifest ve deterministic runbook profili."
    ),
    "environment_replay_focus": LocalReproducibilityGovernanceProfile(
        name="environment_replay_focus",
        description="Environment replay manifest, variable/path/dependency-note registries ve non-install boundaries odaklı profil.",
        language="tr",
        dry_run_default=True,
        scan_data_lake=False,
        max_rows=200000,
        notes="Environment replay manifest, variable/path/dependency-note registries ve non-install boundaries odaklı profil."
    ),
    "deterministic_runbook_focus": LocalReproducibilityGovernanceProfile(
        name="deterministic_runbook_focus",
        description="Deterministic runbook, command sequence registry, output expectation registry ve build-free reproduction maps odaklı profil.",
        language="tr",
        dry_run_default=True,
        scan_packaging_outputs=False,
        scan_documentation_export_outputs=False,
        scan_review_outputs=False,
        scan_atlas_outputs=False,
        scan_continuity_outputs=False,
        scan_preservation_outputs=False,
        scan_completion_outputs=False,
        scan_safety_outputs=False,
        max_rows=250000,
        notes="Deterministic runbook, command sequence registry, output expectation registry ve build-free reproduction maps odaklı profil."
    ),
    "strict_reproducibility_safety": LocalReproducibilityGovernanceProfile(
        name="strict_reproducibility_safety",
        description="Build/install/provision/docker/CI/CD/deploy/publish/live/broker/advice overclaim denetimini sıkılaştıran profil.",
        language="tr",
        dry_run_default=True,
        max_items=300000,
        max_rows=120000,
        min_readiness_score=0.60,
        min_quality_score=0.60,
        notes="Build/install/provision/docker/CI/CD/deploy/publish/live/broker/advice overclaim denetimini sıkılaştıran profil."
    )
}

def get_local_reproducibility_governance_profile(name: str) -> LocalReproducibilityGovernanceProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Bilinmeyen profile: {name}")
    return _PROFILES[name]

def list_local_reproducibility_governance_profiles(enabled_only: bool = True) -> list[LocalReproducibilityGovernanceProfile]:
    return [p for p in _PROFILES.values() if not enabled_only or p.enabled]

def validate_local_reproducibility_governance_profiles() -> None:
    for p in _PROFILES.values():
        if not p.language:
            raise ConfigError("language bos olmamali.")
        if p.max_items <= 0 or p.max_rows <= 0:
            raise ConfigError("max_items ve max_rows pozitif olmali.")
        if not (0 <= p.min_readiness_score <= 1) or not (0 <= p.min_quality_score <= 1):
            raise ConfigError("min_readiness_score ve min_quality_score 0-1 araliginda olmali.")
        if not p.dry_run_default:
            raise ConfigError("dry_run_default True olmali.")
        if any([p.allow_real_build, p.allow_cloud_build, p.allow_ci_cd, p.allow_docker_build_push, p.allow_docker_image_creation, p.allow_build_artifact, p.allow_binary_artifact, p.allow_installer_creation, p.allow_executable_packaging, p.allow_environment_provisioning, p.allow_dependency_install, p.allow_pip_install, p.allow_poetry_install, p.allow_conda_install, p.allow_package_publish, p.allow_git_tag, p.allow_cloud_upload, p.allow_deployment, p.allow_official_build_attestation, p.allow_reproducibility_certification, p.allow_legal_signoff, p.allow_compliance_approval, p.allow_production_approval_claim, p.allow_official_acceptance_claim, p.allow_broker_readiness_claim, p.allow_live_trading_claim, p.allow_investment_advice, p.allow_model_deployment_claim, p.allow_web_server, p.allow_dashboard_creation, p.allow_gui_creation, p.allow_tui_creation, p.allow_telemetry, p.allow_external_service, p.allow_external_llm, p.allow_vector_db, p.allow_embedding_api, p.allow_file_modification, p.allow_file_deletion, p.allow_file_move, p.allow_overwrite]):
            raise ConfigError("Baslangic profillerinde build/install/provision/deploy vb. False olmali.")

def get_default_local_reproducibility_governance_profile() -> LocalReproducibilityGovernanceProfile:
    return _PROFILES["balanced_local_reproducibility"]
