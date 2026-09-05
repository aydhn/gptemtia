from dataclasses import dataclass

@dataclass(frozen=True)
class LocalProjectCompletionProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_real_project_closure: bool = False
    allow_official_completion_approval: bool = False
    allow_production_approval_claim: bool = False
    allow_official_acceptance_claim: bool = False
    allow_legal_signoff: bool = False
    allow_compliance_signoff: bool = False
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
    scan_longterm_outputs: bool = True
    scan_release_candidate_outputs: bool = True
    scan_incident_outputs: bool = True
    scan_redteam_outputs: bool = True
    scan_governance_outputs: bool = True
    scan_safety_outputs: bool = True
    max_items: int = 500000
    max_inventory_rows: int = 250000
    min_readiness_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_PROFILES = {
    "balanced_local_project_completion": LocalProjectCompletionProfile(
        name="balanced_local_project_completion",
        description="Genel amacli local/offline system closure dossier, terminal handoff pack ve project completion rehearsal profili.",
        notes="Genel amaçlı local/offline system closure dossier, terminal handoff pack ve project completion rehearsal profili."
    ),
    "handoff_focus": LocalProjectCompletionProfile(
        name="handoff_focus",
        description="Terminal handoff pack, final checklists ve terminal maps odakli profil.",
        scan_docs=True,
        scan_reports=True,
        scan_generated_docs=True,
        scan_longterm_outputs=True,
        scan_release_candidate_outputs=True,
        max_inventory_rows=150000,
        notes="Terminal handoff pack, final checklists ve terminal maps odaklı profil."
    ),
    "last_mile_audit_focus": LocalProjectCompletionProfile(
        name="last_mile_audit_focus",
        description="Last-mile audit binder, evidence index, criteria matrix ve inventories odakli profil.",
        scan_docs=True,
        scan_reports=True,
        scan_data_lake=True,
        scan_scripts=True,
        scan_tests=True,
        scan_generated_docs=True,
        max_inventory_rows=200000,
        notes="Last-mile audit binder, evidence index, criteria matrix ve inventories odaklı profil."
    ),
    "strict_completion_safety": LocalProjectCompletionProfile(
        name="strict_completion_safety",
        description="Closure/approval/release/publish/deploy/live/broker/advice overclaim denetimini sikilastiran profil.",
        max_items=300000,
        max_inventory_rows=100000,
        min_readiness_score=0.60,
        min_quality_score=0.60,
        notes="Closure/approval/release/publish/deploy/live/broker/advice overclaim denetimini sıkılaştıran profil."
    )
}

def get_local_project_completion_profile(name: str) -> LocalProjectCompletionProfile:
    if name not in _PROFILES:
        raise ValueError(f"ConfigError: Bilinmeyen profile: {name}")
    return _PROFILES[name]

def list_local_project_completion_profiles(enabled_only: bool = True) -> list[LocalProjectCompletionProfile]:
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())

def validate_local_project_completion_profiles() -> None:
    for p in _PROFILES.values():
        if not p.language:
            raise ValueError("language boş olmamalı.")
        if p.max_items <= 0 or p.max_inventory_rows <= 0:
            raise ValueError("max_items ve max_inventory_rows pozitif olmalı.")
        if not (0 <= p.min_readiness_score <= 1) or not (0 <= p.min_quality_score <= 1):
            raise ValueError("min_readiness_score ve min_quality_score 0-1 aralığında olmalı.")
        if not p.dry_run_default:
            raise ValueError("Başlangıç profillerinde dry_run_default True olmalı.")
        if any([
            p.allow_real_project_closure, p.allow_official_completion_approval,
            p.allow_production_approval_claim, p.allow_official_acceptance_claim,
            p.allow_legal_signoff, p.allow_compliance_signoff, p.allow_package_publish,
            p.allow_docker_build_push, p.allow_git_tag, p.allow_cloud_upload,
            p.allow_deployment, p.allow_live_trading_claim, p.allow_broker_readiness_claim,
            p.allow_investment_advice, p.allow_model_deployment_claim, p.allow_telemetry,
            p.allow_dashboard_creation, p.allow_gui_creation, p.allow_tui_creation,
            p.allow_external_service, p.allow_external_llm, p.allow_file_modification,
            p.allow_file_deletion, p.allow_file_move, p.allow_overwrite
        ]):
            raise ValueError("Başlangıç profillerinde unsafe flagler False olmalı.")

def get_default_local_project_completion_profile() -> LocalProjectCompletionProfile:
    return _PROFILES["balanced_local_project_completion"]
