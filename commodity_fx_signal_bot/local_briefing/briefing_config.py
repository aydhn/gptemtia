from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalBriefingProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_investment_advice: bool = False
    allow_live_trading_claim: bool = False
    allow_broker_readiness_claim: bool = False
    allow_production_release_claim: bool = False
    allow_model_deployment_claim: bool = False
    allow_official_board_decision_claim: bool = False
    allow_cloud_upload: bool = False
    allow_external_service: bool = False
    allow_external_llm: bool = False
    allow_file_modification: bool = False
    allow_file_deletion: bool = False
    allow_file_move: bool = False
    allow_overwrite: bool = False
    scan_docs: bool = True
    scan_reports: bool = True
    scan_data_lake: bool = True
    scan_cross_layer_outputs: bool = True
    scan_training_outputs: bool = True
    max_sections: int = 5000
    max_slide_items: int = 200
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

PROFILES = {
    "balanced_local_briefing": LocalBriefingProfile(
        name="balanced_local_briefing",
        description="Genel amacli local/offline stakeholder communication ve executive briefing profili.",
        notes="Genel amacli local/offline stakeholder communication ve executive briefing profili."
    ),
    "executive_summary_focus": LocalBriefingProfile(
        name="executive_summary_focus",
        description="Executive summary odakli profil.",
        max_sections=2500,
        max_slide_items=120,
        notes="Executive summary, one-pager ve decision-context binder odakli profil."
    ),
    "nontechnical_deck_focus": LocalBriefingProfile(
        name="nontechnical_deck_focus",
        description="Nontechnical deck odakli profil.",
        max_slide_items=80,
        notes="Teknik olmayan paydaslar icin briefing deck source ve anlati sadelestirme odakli profil."
    ),
    "strict_communication_safety": LocalBriefingProfile(
        name="strict_communication_safety",
        description="Strict safety profil.",
        max_sections=3000,
        max_slide_items=100,
        min_quality_score=0.60,
        notes="Yatirim tavsiyesi, canli trading, broker readiness, production release ve official decision iddialarini siki denetleyen profil."
    )
}

def get_local_briefing_profile(name: str) -> LocalBriefingProfile:
    if name not in PROFILES:
        raise ConfigError(f"Unknown profile: {name}")
    return PROFILES[name]

def list_local_briefing_profiles(enabled_only: bool = True) -> list[LocalBriefingProfile]:
    if enabled_only:
        return [p for p in PROFILES.values() if p.enabled]
    return list(PROFILES.values())

def validate_local_briefing_profiles() -> None:
    for p in PROFILES.values():
        if not p.language:
            raise ConfigError("language bos olmamali.")
        if p.max_sections <= 0:
            raise ConfigError("max_sections pozitif olmali.")
        if p.max_slide_items <= 0:
            raise ConfigError("max_slide_items pozitif olmali.")
        if not (0 <= p.min_quality_score <= 1):
            raise ConfigError("min_quality_score 0-1 araliginda olmali.")
        if not p.dry_run_default:
            raise ConfigError("dry_run_default True olmali.")
        if any([
            p.allow_investment_advice, p.allow_live_trading_claim,
            p.allow_broker_readiness_claim, p.allow_production_release_claim,
            p.allow_model_deployment_claim, p.allow_official_board_decision_claim,
            p.allow_cloud_upload, p.allow_external_service, p.allow_external_llm,
            p.allow_file_modification, p.allow_file_deletion, p.allow_file_move,
            p.allow_overwrite
        ]):
            raise ConfigError("advice/live/broker/production/deployment/official/cloud/external/file action flagleri False olmali.")

def get_default_local_briefing_profile() -> LocalBriefingProfile:
    return PROFILES["balanced_local_briefing"]
