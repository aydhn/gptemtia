from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalReleaseCandidateProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_real_release: bool = False
    allow_package_publish: bool = False
    allow_docker_build_push: bool = False
    allow_git_tag: bool = False
    allow_cloud_upload: bool = False
    allow_deployment: bool = False
    allow_production_acceptance_claim: bool = False
    allow_official_acceptance_claim: bool = False
    allow_legal_signoff: bool = False
    allow_compliance_signoff: bool = False
    allow_live_trading_claim: bool = False
    allow_broker_readiness_claim: bool = False
    allow_investment_advice: bool = False
    allow_model_deployment_claim: bool = False
    allow_telemetry: bool = False
    allow_dashboard_creation: bool = False
    allow_gui_creation: bool = False
    allow_tui_creation: bool = False
    allow_external_service: bool = False
    allow_external_llm: bool = False
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
    scan_incident_outputs: bool = True
    scan_redteam_outputs: bool = True
    scan_governance_outputs: bool = True
    scan_safety_outputs: bool = True
    max_items: int = 500000
    max_inventory_rows: int = 200000
    min_readiness_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_PROFILES = [
    LocalReleaseCandidateProfile(
        name="balanced_local_release_candidate",
        description="Genel amacli profil",
        notes="Genel amaçlı local/offline release-candidate rehearsal, frozen baseline snapshot ve v1.0 dossier profili.",
    ),
    LocalReleaseCandidateProfile(
        name="baseline_snapshot_focus",
        description="Snapshot profil",
        max_inventory_rows=150000,
        notes="Frozen baseline snapshot, inventories, hash manifest rehearsal ve drift warning odaklı profil.",
    ),
    LocalReleaseCandidateProfile(
        name="final_acceptance_focus",
        description="Acceptance profil",
        scan_data_lake=False,
        scan_scripts=False,
        scan_tests=False,
        max_inventory_rows=100000,
        notes="Final acceptance rehearsal, operator sign-off packet ve evidence index odaklı profil.",
    ),
    LocalReleaseCandidateProfile(
        name="strict_release_candidate_safety",
        description="Safety profil",
        max_items=300000,
        max_inventory_rows=100000,
        min_readiness_score=0.60,
        min_quality_score=0.60,
        notes="Release/publish/tag/deploy/acceptance/legal/compliance/live/broker/advice overclaim denetimini sıkılaştıran profil.",
    )
]

def list_local_release_candidate_profiles(enabled_only: bool = True) -> list[LocalReleaseCandidateProfile]:
    return [p for p in _PROFILES if not enabled_only or p.enabled]

def get_local_release_candidate_profile(name: str) -> LocalReleaseCandidateProfile:
    for p in _PROFILES:
        if p.name == name:
            return p
    raise ConfigError(f"Unknown profile: {name}")

def validate_local_release_candidate_profiles() -> None:
    for p in _PROFILES:
        if not p.language:
            raise ValueError("language can not be empty")
        if p.max_items <= 0 or p.max_inventory_rows <= 0:
            raise ValueError("max_items and max_inventory_rows must be positive")
        if not (0 <= p.min_readiness_score <= 1) or not (0 <= p.min_quality_score <= 1):
            raise ValueError("score thresholds must be between 0 and 1")
        if not p.dry_run_default:
            raise ValueError("dry_run_default must be True")
        if any([
            p.allow_real_release, p.allow_package_publish, p.allow_docker_build_push,
            p.allow_git_tag, p.allow_cloud_upload, p.allow_deployment,
            p.allow_production_acceptance_claim, p.allow_official_acceptance_claim,
            p.allow_legal_signoff, p.allow_compliance_signoff, p.allow_live_trading_claim,
            p.allow_broker_readiness_claim, p.allow_investment_advice,
            p.allow_telemetry, p.allow_dashboard_creation, p.allow_external_service,
            p.allow_file_modification
        ]):
            raise ValueError("Action flags must be False")

def get_default_local_release_candidate_profile() -> LocalReleaseCandidateProfile:
    return get_local_release_candidate_profile("balanced_local_release_candidate")
