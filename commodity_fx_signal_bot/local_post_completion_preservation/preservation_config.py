from dataclasses import dataclass
from typing import List

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalPostCompletionPreservationProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_real_archive_seal: bool = False
    allow_immutable_file_lock: bool = False
    allow_chmod_or_permission_change: bool = False
    allow_git_tag: bool = False
    allow_release_publish: bool = False
    allow_package_publish: bool = False
    allow_docker_build_push: bool = False
    allow_cloud_upload: bool = False
    allow_deployment: bool = False
    allow_official_archive_approval: bool = False
    allow_production_approval_claim: bool = False
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
    scan_completion_outputs: bool = True
    scan_longterm_outputs: bool = True
    scan_release_outputs: bool = True
    scan_safety_outputs: bool = True
    max_items: int = 500000
    max_inventory_rows: int = 250000
    min_readiness_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

PROFILES = {
    "balanced_local_preservation": LocalPostCompletionPreservationProfile(
        name="balanced_local_preservation",
        description="Genel amacli local/offline archive seal rehearsal, evidence vault index ve final knowledge capsule profili.",
        notes="Genel amaçlı local/offline archive seal rehearsal, evidence vault index ve final knowledge capsule profili."
    ),
    "archive_seal_focus": LocalPostCompletionPreservationProfile(
        name="archive_seal_focus",
        description="Archive seal checklist, boundary registry, fingerprints ve inventory rehearsal odakli profil.",
        max_inventory_rows=200000,
        notes="Archive seal checklist, boundary registry, fingerprints ve inventory rehearsal odaklı profil."
    ),
    "knowledge_capsule_focus": LocalPostCompletionPreservationProfile(
        name="knowledge_capsule_focus",
        description="Final knowledge capsule, capsule recaps, topic map ve terminal access notes odakli profil.",
        max_inventory_rows=150000,
        notes="Final knowledge capsule, capsule recaps, topic map ve terminal access notes odaklı profil."
    ),
    "strict_preservation_safety": LocalPostCompletionPreservationProfile(
        name="strict_preservation_safety",
        description="Archive seal/immutable/chmod/git/release/publish/deploy/live/broker/advice overclaim denetimini sikilastiran profil.",
        max_items=300000,
        max_inventory_rows=100000,
        min_readiness_score=0.60,
        min_quality_score=0.60,
        notes="Archive seal/immutable/chmod/git/release/publish/deploy/live/broker/advice overclaim denetimini sıkılaştıran profil."
    )
}

def get_local_post_completion_preservation_profile(name: str) -> LocalPostCompletionPreservationProfile:
    if name not in PROFILES:
        raise ConfigError(f"Profile {name} not found.")
    return PROFILES[name]

def list_local_post_completion_preservation_profiles(enabled_only: bool = True) -> List[LocalPostCompletionPreservationProfile]:
    if enabled_only:
        return [p for p in PROFILES.values() if p.enabled]
    return list(PROFILES.values())

def validate_local_post_completion_preservation_profiles() -> None:
    for p in PROFILES.values():
        if not p.language:
            raise ConfigError("language bos olmamali.")
        if p.max_items <= 0 or p.max_inventory_rows <= 0:
            raise ConfigError("max_items ve max_inventory_rows pozitif olmali.")
        if not (0 <= p.min_readiness_score <= 1) or not (0 <= p.min_quality_score <= 1):
            raise ConfigError("scores 0-1 araliginda olmali.")
        if not p.dry_run_default:
            raise ConfigError("dry_run_default True olmali.")
        if any([
            p.allow_real_archive_seal, p.allow_immutable_file_lock, p.allow_chmod_or_permission_change,
            p.allow_git_tag, p.allow_release_publish, p.allow_package_publish, p.allow_docker_build_push,
            p.allow_cloud_upload, p.allow_deployment, p.allow_official_archive_approval,
            p.allow_production_approval_claim, p.allow_official_acceptance_claim, p.allow_legal_signoff,
            p.allow_compliance_signoff, p.allow_live_trading_claim, p.allow_broker_readiness_claim,
            p.allow_investment_advice, p.allow_model_deployment_claim, p.allow_telemetry,
            p.allow_dashboard_creation, p.allow_gui_creation, p.allow_tui_creation,
            p.allow_external_service, p.allow_external_llm, p.allow_file_modification,
            p.allow_file_deletion, p.allow_file_move, p.allow_overwrite
        ]):
            raise ConfigError("Action flagleri False olmali.")

def get_default_local_post_completion_preservation_profile() -> LocalPostCompletionPreservationProfile:
    return PROFILES["balanced_local_preservation"]
