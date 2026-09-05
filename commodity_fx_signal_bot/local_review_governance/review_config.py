from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalReviewGovernanceProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_real_approval_workflow: bool = False
    allow_e_signature: bool = False
    allow_official_expert_signoff: bool = False
    allow_legal_signoff: bool = False
    allow_compliance_approval: bool = False
    allow_production_approval_claim: bool = False
    allow_official_acceptance_claim: bool = False
    allow_broker_readiness_claim: bool = False
    allow_live_trading_claim: bool = False
    allow_investment_advice: bool = False
    allow_package_publish: bool = False
    allow_docker_build_push: bool = False
    allow_git_tag: bool = False
    allow_cloud_upload: bool = False
    allow_deployment: bool = False
    allow_model_deployment_claim: bool = False
    allow_telemetry: bool = False
    allow_dashboard_creation: bool = False
    allow_gui_creation: bool = False
    allow_tui_creation: bool = False
    allow_cloud_review_service: bool = False
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
    "balanced_local_review_governance": LocalReviewGovernanceProfile(
        name="balanced_local_review_governance",
        description="Genel amacli local/offline human-review cockpit, manual approval ledger rehearsal ve terminal review governance profili.",
        notes="Genel amacli local/offline human-review cockpit, manual approval ledger rehearsal ve terminal review governance profili."
    ),
    "human_review_focus": LocalReviewGovernanceProfile(
        name="human_review_focus",
        description="Human-review cockpit, route map, status matrix ve reviewer console odakli profil.",
        max_rows=200000,
        scan_data_lake=False,
        scan_scripts=False,
        scan_tests=False,
        scan_preservation_outputs=False,
        scan_completion_outputs=False,
        scan_safety_outputs=False,
        notes="Human-review cockpit, route map, status matrix ve reviewer console odakli profil."
    ),
    "expert_review_focus": LocalReviewGovernanceProfile(
        name="expert_review_focus",
        description="Expert review workbook, evidence map, criteria matrix ve issue register odakli profil.",
        max_rows=250000,
        scan_atlas_outputs=False,
        scan_continuity_outputs=False,
        scan_preservation_outputs=False,
        scan_completion_outputs=False,
        scan_safety_outputs=False,
        notes="Expert review workbook, evidence map, criteria matrix ve issue register odakli profil."
    ),
    "strict_review_safety": LocalReviewGovernanceProfile(
        name="strict_review_safety",
        description="Approval/sign-off/legal/compliance/production/live/broker/advice/deploy/publish overclaim denetimini sikilastiran profil.",
        max_items=300000,
        max_rows=120000,
        min_readiness_score=0.60,
        min_quality_score=0.60,
        notes="Approval/sign-off/legal/compliance/production/live/broker/advice/deploy/publish overclaim denetimini sikilastiran profil."
    )
}

def get_local_review_governance_profile(name: str) -> LocalReviewGovernanceProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Unknown profile: {name}")
    return _PROFILES[name]

def list_local_review_governance_profiles(enabled_only: bool = True) -> list[LocalReviewGovernanceProfile]:
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())

def validate_local_review_governance_profiles() -> None:
    for p in _PROFILES.values():
        if not p.language:
            raise ConfigError("language cannot be empty")
        if p.max_items <= 0 or p.max_rows <= 0:
            raise ConfigError("max_items and max_rows must be positive")
        if not (0.0 <= p.min_readiness_score <= 1.0) or not (0.0 <= p.min_quality_score <= 1.0):
            raise ConfigError("min_readiness_score and min_quality_score must be between 0 and 1")
        if not p.dry_run_default:
            raise ConfigError("dry_run_default must be True")
        if p.allow_real_approval_workflow or p.allow_e_signature or p.allow_official_expert_signoff or p.allow_legal_signoff or p.allow_compliance_approval or p.allow_production_approval_claim or p.allow_broker_readiness_claim or p.allow_live_trading_claim or p.allow_investment_advice or p.allow_package_publish or p.allow_docker_build_push or p.allow_git_tag or p.allow_cloud_upload or p.allow_deployment or p.allow_telemetry or p.allow_dashboard_creation or p.allow_external_service or p.allow_vector_db or p.allow_embedding_api or p.allow_file_modification:
            raise ConfigError("Dangerous flags must be False")

def get_default_local_review_governance_profile() -> LocalReviewGovernanceProfile:
    return _PROFILES["balanced_local_review_governance"]
