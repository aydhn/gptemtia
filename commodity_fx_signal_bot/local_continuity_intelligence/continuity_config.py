from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalContinuityIntelligenceProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_real_memory_system: bool = False
    allow_cloud_memory_sync: bool = False
    allow_official_lessons_report: bool = False
    allow_official_decision_record: bool = False
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
    scan_preservation_outputs: bool = True
    scan_completion_outputs: bool = True
    scan_longterm_outputs: bool = True
    scan_governance_outputs: bool = True
    scan_safety_outputs: bool = True
    max_items: int = 500000
    max_rows: int = 250000
    min_readiness_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

PROFILES = {
    "balanced_local_continuity": LocalContinuityIntelligenceProfile(
        name="balanced_local_continuity",
        description="Genel amacli profil",
        notes="Genel amaçlı local/offline operator memory book, lessons-learned codex ve future-reader continuity profili."
    ),
    "operator_memory_focus": LocalContinuityIntelligenceProfile(
        name="operator_memory_focus",
        description="Operator memory book",
        scan_data_lake=False,
        max_rows=150000,
        notes="Operator memory book, topic map, reading route ve quick-reference cards odaklı profil."
    ),
    "lessons_decision_focus": LocalContinuityIntelligenceProfile(
        name="lessons_decision_focus",
        description="Lessons-learned codex",
        max_rows=200000,
        notes="Lessons-learned codex, decision rationale capsule ve tradeoff matrix odaklı profil."
    ),
    "strict_continuity_safety": LocalContinuityIntelligenceProfile(
        name="strict_continuity_safety",
        description="Strict safety",
        max_items=300000,
        max_rows=100000,
        min_readiness_score=0.60,
        min_quality_score=0.60,
        notes="Memory/cloud/decision/legal/compliance/release/deploy/live/broker/advice overclaim denetimini sıkılaştıran profil."
    ),
}

def get_local_continuity_intelligence_profile(name: str) -> LocalContinuityIntelligenceProfile:
    if name not in PROFILES:
        raise ConfigError(f"Unknown profile: {name}")
    return PROFILES[name]

def list_local_continuity_intelligence_profiles(enabled_only: bool = True) -> list[LocalContinuityIntelligenceProfile]:
    return [p for p in PROFILES.values() if not enabled_only or p.enabled]

def validate_local_continuity_intelligence_profiles() -> None:
    for p in PROFILES.values():
        if not p.language:
            raise ConfigError("Language bos olamaz")
        if p.max_items <= 0 or p.max_rows <= 0:
            raise ConfigError("max_items ve max_rows pozitif olmali")
        if not (0 <= p.min_readiness_score <= 1) or not (0 <= p.min_quality_score <= 1):
            raise ConfigError("Score 0-1 araliginda olmali")
        if not p.dry_run_default:
            raise ConfigError("dry_run_default True olmali")
        if p.allow_real_memory_system or p.allow_cloud_memory_sync or p.allow_live_trading_claim or p.allow_investment_advice:
            raise ConfigError("Forbidden claims found in profile")

def get_default_local_continuity_intelligence_profile() -> LocalContinuityIntelligenceProfile:
    return PROFILES["balanced_local_continuity"]