"""Atlas config module."""
from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalProjectAtlasProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_enterprise_search_claim: bool = False
    allow_cloud_index: bool = False
    allow_vector_db: bool = False
    allow_embedding_api: bool = False
    allow_external_search_service: bool = False
    allow_external_llm: bool = False
    allow_official_knowledge_index: bool = False
    allow_legal_evidence_claim: bool = False
    allow_compliance_evidence_claim: bool = False
    allow_production_approval_claim: bool = False
    allow_official_acceptance_claim: bool = False
    allow_package_publish: bool = False
    allow_docker_build_push: bool = False
    allow_git_tag: bool = False
    allow_cloud_upload: bool = False
    allow_deployment: bool = False
    allow_live_trading_claim: bool = False
    allow_broker_readiness_claim: bool = False
    allow_investment_advice: bool = False
    allow_model_deployment_claim: bool = False
    allow_telemetry: bool = False
    allow_dashboard_creation: bool = False
    allow_gui_creation: bool = False
    allow_tui_creation: bool = False
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
    scan_continuity_outputs: bool = True
    scan_preservation_outputs: bool = True
    scan_completion_outputs: bool = True
    scan_longterm_outputs: bool = True
    scan_release_outputs: bool = True
    scan_incident_outputs: bool = True
    scan_governance_outputs: bool = True
    scan_safety_outputs: bool = True
    max_items: int = 750000
    max_rows: int = 300000
    min_readiness_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_PROFILES = {
    "balanced_local_project_atlas": LocalProjectAtlasProfile(
        name="balanced_local_project_atlas",
        description="Genel amacli local/offline meta-index, universal navigation map ve terminal project atlas profili.",
        notes="Genel amaçlı local/offline meta-index, universal navigation map ve terminal project atlas profili."
    ),
    "navigation_focus": LocalProjectAtlasProfile(
        name="navigation_focus",
        description="Navigation odakli.",
        scan_data_lake=False,
        scan_scripts=False,
        scan_tests=False,
        scan_governance_outputs=False,
        scan_safety_outputs=False,
        scan_incident_outputs=False,
        scan_release_outputs=False,
        scan_longterm_outputs=False,
        max_rows=200000,
        notes="Universal navigation map, reading routes, role routes ve semantic TOC odaklı profil."
    ),
    "lookup_focus": LocalProjectAtlasProfile(
        name="lookup_focus",
        description="Lookup odakli.",
        scan_continuity_outputs=False,
        scan_preservation_outputs=False,
        scan_completion_outputs=False,
        scan_governance_outputs=False,
        scan_safety_outputs=False,
        scan_incident_outputs=False,
        scan_release_outputs=False,
        scan_longterm_outputs=False,
        max_rows=250000,
        notes="Cross-phase lookup tables, command/output maps ve family maps odaklı profil."
    ),
    "strict_atlas_safety": LocalProjectAtlasProfile(
        name="strict_atlas_safety",
        description="Strict safety.",
        max_items=300000,
        max_rows=120000,
        min_readiness_score=0.60,
        min_quality_score=0.60,
        notes="Enterprise search/cloud/vector/embedding/approval/release/deploy/live/broker/advice overclaim denetimini sıkılaştıran profil."
    ),
}

def get_local_project_atlas_profile(name: str) -> LocalProjectAtlasProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Profile {name} not found.")
    return _PROFILES[name]

def list_local_project_atlas_profiles(enabled_only: bool = True) -> list[LocalProjectAtlasProfile]:
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())

def validate_local_project_atlas_profiles() -> None:
    for p in _PROFILES.values():
        if not p.language:
            raise ConfigError("Language cannot be empty.")
        if p.max_items <= 0 or p.max_rows <= 0:
            raise ConfigError("max_items and max_rows must be positive.")
        if not (0 <= p.min_readiness_score <= 1) or not (0 <= p.min_quality_score <= 1):
            raise ConfigError("min scores must be between 0 and 1.")
        if not p.dry_run_default:
            raise ConfigError("dry_run_default must be True.")
        if any([
            p.allow_enterprise_search_claim, p.allow_cloud_index, p.allow_vector_db, p.allow_embedding_api,
            p.allow_external_search_service, p.allow_external_llm, p.allow_official_knowledge_index,
            p.allow_legal_evidence_claim, p.allow_compliance_evidence_claim, p.allow_production_approval_claim,
            p.allow_official_acceptance_claim, p.allow_package_publish, p.allow_docker_build_push,
            p.allow_git_tag, p.allow_cloud_upload, p.allow_deployment, p.allow_live_trading_claim,
            p.allow_broker_readiness_claim, p.allow_investment_advice, p.allow_model_deployment_claim,
            p.allow_telemetry, p.allow_dashboard_creation, p.allow_gui_creation, p.allow_tui_creation,
            p.allow_file_modification, p.allow_file_deletion, p.allow_file_move, p.allow_overwrite
        ]):
            raise ConfigError("All dangerous allow flags must be False.")

def get_default_local_project_atlas_profile() -> LocalProjectAtlasProfile:
    return _PROFILES["balanced_local_project_atlas"]
