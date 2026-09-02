from dataclasses import dataclass

@dataclass(frozen=True)
class LocalUsabilityProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_real_user_testing: bool = False
    allow_telemetry: bool = False
    allow_analytics_tracking: bool = False
    allow_behavior_monitoring: bool = False
    allow_gui_creation: bool = False
    allow_tui_creation: bool = False
    allow_dashboard_creation: bool = False
    allow_cloud_upload: bool = False
    allow_package_publish: bool = False
    allow_external_service: bool = False
    allow_external_llm: bool = False
    allow_file_modification: bool = False
    allow_file_deletion: bool = False
    allow_file_move: bool = False
    allow_overwrite: bool = False
    allow_production_usability_claim: bool = False
    allow_official_ux_audit_claim: bool = False
    allow_live_trading_claim: bool = False
    allow_broker_readiness_claim: bool = False
    allow_investment_advice: bool = False
    allow_model_deployment_claim: bool = False
    scan_docs: bool = True
    scan_reports: bool = True
    scan_data_lake: bool = True
    scan_scripts: bool = True
    scan_tests: bool = True
    scan_generated_docs: bool = True
    scan_performance_outputs: bool = True
    scan_simplification_outputs: bool = True
    scan_safety_outputs: bool = True
    max_items: int = 500000
    max_questions: int = 5000
    min_readiness_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

PROFILES = {
    "balanced_local_usability": LocalUsabilityProfile(
        name="balanced_local_usability",
        description="Genel amaçlı local/offline usability review, command discoverability ve operator ergonomics rehearsal profili.",
        notes="Genel amaçlı local/offline usability review, command discoverability ve operator ergonomics rehearsal profili."
    ),
    "command_discoverability_focus": LocalUsabilityProfile(
        name="command_discoverability_focus",
        description="Command family index, script purpose index ve what-to-run-first guide odaklı profil.",
        max_questions=3000,
        notes="Command family index, script purpose index ve what-to-run-first guide odaklı profil."
    ),
    "documentation_navigation_focus": LocalUsabilityProfile(
        name="documentation_navigation_focus",
        description="Documentation navigation assistant, reading order ve operator path odaklı profil.",
        max_questions=3000,
        notes="Documentation navigation assistant, reading order ve operator path odaklı profil."
    ),
    "strict_usability_safety": LocalUsabilityProfile(
        name="strict_usability_safety",
        description="Telemetry, analytics, GUI/dashboard, production usability, live/broker/advice overclaim denetimini sıkılaştıran profil.",
        max_items=300000,
        max_questions=3000,
        min_readiness_score=0.60,
        min_quality_score=0.60,
        notes="Telemetry, analytics, GUI/dashboard, production usability, live/broker/advice overclaim denetimini sıkılaştıran profil."
    )
}

class ConfigError(Exception):
    pass

def get_local_usability_profile(name: str) -> LocalUsabilityProfile:
    if name not in PROFILES:
        raise ConfigError(f"Unknown profile: {name}")
    return PROFILES[name]

def list_local_usability_profiles(enabled_only: bool = True) -> list[LocalUsabilityProfile]:
    return [p for p in PROFILES.values() if not enabled_only or p.enabled]

def validate_local_usability_profiles() -> None:
    for p in PROFILES.values():
        if not p.language:
            raise ConfigError("language bos olamaz.")
        if p.max_items <= 0 or p.max_questions <= 0:
            raise ConfigError("max_items ve max_questions pozitif olmali.")
        if not (0 <= p.min_readiness_score <= 1) or not (0 <= p.min_quality_score <= 1):
            raise ConfigError("min_readiness_score ve min_quality_score 0-1 araliginda olmali.")
        if not p.dry_run_default:
            raise ConfigError("dry_run_default True olmali.")
        if p.allow_real_user_testing or p.allow_telemetry or p.allow_analytics_tracking or p.allow_gui_creation or p.allow_dashboard_creation or p.allow_live_trading_claim or p.allow_investment_advice:
            raise ConfigError("testing/telemetry/analytics/gui/tui/dashboard/cloud/package/external/file action/live/broker/advice/deploy flagleri False olmali.")

def get_default_local_usability_profile() -> LocalUsabilityProfile:
    return PROFILES["balanced_local_usability"]
