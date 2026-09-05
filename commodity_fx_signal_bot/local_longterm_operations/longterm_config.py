"""Long-term operations configuration."""
from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalLongTermOperationsProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_real_operations_plan: bool = False
    allow_official_lifecycle_policy: bool = False
    allow_real_deprecation: bool = False
    allow_auto_deprecation: bool = False
    allow_auto_migration: bool = False
    allow_production_roadmap_claim: bool = False
    allow_official_release_commitment: bool = False
    allow_package_publish: bool = False
    allow_docker_build_push: bool = False
    allow_git_tag: bool = False
    allow_cloud_upload: bool = False
    allow_deployment: bool = False
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
    scan_release_candidate_outputs: bool = True
    scan_incident_outputs: bool = True
    scan_governance_outputs: bool = True
    scan_safety_outputs: bool = True
    max_items: int = 500000
    max_calendar_rows: int = 10000
    max_workbook_rows: int = 100000
    min_readiness_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_PROFILES = {
    "balanced_local_longterm_operations": LocalLongTermOperationsProfile(
        name="balanced_local_longterm_operations",
        description="Balanced long-term operations profile.",
        notes="Genel amaçlı local/offline long-term operations binder, lifecycle maintenance workbook ve v1.x roadmap governance profili."
    ),
    "maintenance_calendar_focus": LocalLongTermOperationsProfile(
        name="maintenance_calendar_focus",
        description="Maintenance calendar focus profile.",
        scan_docs=True,
        scan_reports=True,
        scan_data_lake=False,
        scan_scripts=False,
        scan_tests=False,
        scan_generated_docs=True,
        scan_release_candidate_outputs=True,
        scan_incident_outputs=False,
        scan_governance_outputs=False,
        scan_safety_outputs=False,
        max_calendar_rows=8000,
        notes="Yearly/quarterly/monthly/weekly review calendars ve maintenance cadence odaklı profil."
    ),
    "deprecation_roadmap_focus": LocalLongTermOperationsProfile(
        name="deprecation_roadmap_focus",
        description="Deprecation roadmap focus profile.",
        scan_docs=True,
        scan_reports=True,
        scan_data_lake=True,
        scan_scripts=False,
        scan_tests=False,
        scan_generated_docs=False,
        scan_release_candidate_outputs=False,
        scan_incident_outputs=True,
        scan_governance_outputs=True,
        scan_safety_outputs=False,
        max_workbook_rows=80000,
        notes="Deprecation rehearsal, migration readiness ve v1.x roadmap governance odaklı profil."
    ),
    "strict_lifecycle_safety": LocalLongTermOperationsProfile(
        name="strict_lifecycle_safety",
        description="Strict lifecycle safety profile.",
        max_items=300000,
        max_calendar_rows=5000,
        max_workbook_rows=50000,
        min_readiness_score=0.60,
        min_quality_score=0.60,
        notes="Operations/lifecycle/deprecation/migration/roadmap/release/live/broker/advice overclaim denetimini sıkılaştıran profil."
    )
}

def get_local_longterm_operations_profile(name: str) -> LocalLongTermOperationsProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Unknown profile: {name}")
    return _PROFILES[name]

def list_local_longterm_operations_profiles(enabled_only: bool = True) -> list[LocalLongTermOperationsProfile]:
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())

def validate_local_longterm_operations_profiles() -> None:
    for profile in _PROFILES.values():
        if not profile.language:
            raise ConfigError("Language cannot be empty.")
        if profile.max_items <= 0 or profile.max_calendar_rows <= 0 or profile.max_workbook_rows <= 0:
            raise ConfigError("Max limits must be positive.")
        if not (0.0 <= profile.min_readiness_score <= 1.0) or not (0.0 <= profile.min_quality_score <= 1.0):
            raise ConfigError("Scores must be between 0 and 1.")
        if not profile.dry_run_default:
            raise ConfigError("dry_run_default must be True.")
        if any([
            profile.allow_real_operations_plan, profile.allow_official_lifecycle_policy,
            profile.allow_real_deprecation, profile.allow_auto_deprecation,
            profile.allow_auto_migration, profile.allow_production_roadmap_claim,
            profile.allow_official_release_commitment, profile.allow_package_publish,
            profile.allow_docker_build_push, profile.allow_git_tag,
            profile.allow_cloud_upload, profile.allow_deployment,
            profile.allow_legal_signoff, profile.allow_compliance_signoff,
            profile.allow_live_trading_claim, profile.allow_broker_readiness_claim,
            profile.allow_investment_advice, profile.allow_model_deployment_claim,
            profile.allow_telemetry, profile.allow_dashboard_creation,
            profile.allow_gui_creation, profile.allow_tui_creation,
            profile.allow_external_service, profile.allow_external_llm,
            profile.allow_file_modification, profile.allow_file_deletion,
            profile.allow_file_move, profile.allow_overwrite
        ]):
            raise ConfigError("All dangerous allow flags must be False.")

def get_default_local_longterm_operations_profile() -> LocalLongTermOperationsProfile:
    return _PROFILES["balanced_local_longterm_operations"]
