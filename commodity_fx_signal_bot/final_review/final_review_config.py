from dataclasses import dataclass
from typing import List, Dict

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class FinalReviewProfile:
    name: str
    description: str
    run_architecture_audit: bool = True
    run_safety_audit: bool = True
    run_integration_audit: bool = True
    run_command_audit: bool = True
    run_datalake_audit: bool = True
    run_report_output_audit: bool = True
    run_documentation_audit: bool = True
    run_quality_gate_audit: bool = True
    run_performance_audit: bool = True
    run_maintenance_audit: bool = True
    run_release_readiness_dry_run: bool = True
    require_no_live_trading: bool = True
    require_no_broker_execution: bool = True
    require_no_model_deploy: bool = True
    require_no_background_daemon: bool = True
    require_no_web_scraping: bool = True
    min_acceptance_score: float = 0.75
    min_safety_score: float = 0.95
    dry_run: bool = True
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_PROFILES: Dict[str, FinalReviewProfile] = {
    "balanced_final_review": FinalReviewProfile(
        name="balanced_final_review",
        description="General purpose offline final review and acceptance dry-run profile.",
        notes="Genel amaçlı offline final review ve acceptance dry-run profili."
    ),
    "strict_final_review": FinalReviewProfile(
        name="strict_final_review",
        description="Stricter security, documentation, and release readiness dry-run profile.",
        min_acceptance_score=0.90,
        min_safety_score=0.99,
        min_quality_score=0.60,
        notes="Daha sıkı güvenlik, dokümantasyon ve release readiness dry-run denetimi profili."
    ),
    "architecture_focused_final_review": FinalReviewProfile(
        name="architecture_focused_final_review",
        description="Focuses on architecture, integration, datalake, and documentation.",
        run_quality_gate_audit=False,
        run_performance_audit=False,
        run_maintenance_audit=False,
        run_release_readiness_dry_run=False,
        notes="Mimari, entegrasyon, DataLake ve dokümantasyon tutarlılığına odaklı final review profili."
    ),
    "safety_focused_final_review": FinalReviewProfile(
        name="safety_focused_final_review",
        description="Focuses strictly on verifying the absence of live trading features.",
        run_architecture_audit=False,
        run_integration_audit=False,
        run_datalake_audit=False,
        run_report_output_audit=False,
        run_performance_audit=False,
        run_maintenance_audit=False,
        min_safety_score=0.99,
        notes="Canlı emir/broker/deploy/daemon/scraping sınırlarının final denetimine odaklı profil."
    ),
}

def get_final_review_profile(name: str) -> FinalReviewProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Unknown final review profile: {name}")
    return _PROFILES[name]

def list_final_review_profiles(enabled_only: bool = True) -> List[FinalReviewProfile]:
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())

def validate_final_review_profiles() -> None:
    for name, profile in _PROFILES.items():
        if not (0.0 <= profile.min_acceptance_score <= 1.0):
            raise ValueError(f"Profile {name}: min_acceptance_score must be between 0.0 and 1.0")
        if not (0.0 <= profile.min_safety_score <= 1.0):
            raise ValueError(f"Profile {name}: min_safety_score must be between 0.0 and 1.0")
        if not (0.0 <= profile.min_quality_score <= 1.0):
            raise ValueError(f"Profile {name}: min_quality_score must be between 0.0 and 1.0")
        if not profile.dry_run:
             raise ValueError(f"Profile {name}: dry_run must be True in base profiles")
        if not all([profile.require_no_live_trading, profile.require_no_broker_execution, profile.require_no_model_deploy, profile.require_no_background_daemon, profile.require_no_web_scraping]):
            raise ValueError(f"Profile {name}: all require_no_* flags must be True")
        if not any([profile.run_architecture_audit, profile.run_safety_audit, profile.run_integration_audit, profile.run_command_audit, profile.run_datalake_audit, profile.run_report_output_audit, profile.run_documentation_audit, profile.run_quality_gate_audit, profile.run_performance_audit, profile.run_maintenance_audit, profile.run_release_readiness_dry_run]):
            raise ValueError(f"Profile {name}: at least one run flag must be True")

def get_default_final_review_profile() -> FinalReviewProfile:
    from config.settings import settings
    return get_final_review_profile(settings.default_final_review_profile)
