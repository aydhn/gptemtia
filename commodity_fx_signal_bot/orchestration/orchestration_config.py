"""
Orchestration configuration and profiles.
"""

from dataclasses import dataclass
from config.settings import settings

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class OrchestrationProfile:
    name: str
    description: str
    workflow_name: str
    timeframe: str = "1d"
    max_symbols_per_run: int = 50
    continue_on_symbol_error: bool = True
    continue_on_job_error: bool = True
    retry_failed_jobs: bool = False
    max_retries: int = 1
    retry_delay_seconds: float = 2.0
    enable_notifications: bool = False
    notification_on_failure: bool = True
    notification_on_success: bool = False
    dry_run: bool = True
    enabled: bool = True
    notes: str = ""

_PROFILES = [
    OrchestrationProfile(
        name="balanced_research_orchestration",
        description="Varsayılan güvenli araştırma orkestrasyon profili",
        workflow_name="daily_research_workflow",
        timeframe="1d",
        max_symbols_per_run=50,
        continue_on_symbol_error=True,
        continue_on_job_error=True,
        retry_failed_jobs=False,
        dry_run=True,
        notes="Varsayılan güvenli araştırma orkestrasyon profili. Dry-run açık başlar."
    ),
    OrchestrationProfile(
        name="full_research_orchestration",
        description="Geniş araştırma profili",
        workflow_name="full_research_workflow",
        timeframe="1d",
        max_symbols_per_run=100,
        continue_on_symbol_error=True,
        continue_on_job_error=True,
        dry_run=True,
        notes="Tüm feature/candidate/backtest/ML/paper/notification zincirini planlayan geniş profil."
    ),
    OrchestrationProfile(
        name="paper_reporting_orchestration",
        description="Raporlama odaklı profil",
        workflow_name="paper_reporting_workflow",
        timeframe="1d",
        max_symbols_per_run=50,
        enable_notifications=False,
        notification_on_failure=True,
        dry_run=True,
        notes="Paper trading ve Telegram raporlama odaklı workflow."
    ),
    OrchestrationProfile(
        name="minimal_healthcheck_orchestration",
        description="Sağlık kontrolü profili",
        workflow_name="healthcheck_workflow",
        timeframe="1d",
        max_symbols_per_run=20,
        continue_on_job_error=True,
        dry_run=True,
        notes="Dependency check, status ve kalite raporlarına odaklı hafif workflow."
    ),
    OrchestrationProfile(
        name="debug_single_symbol_orchestration",
        description="Tek sembol debug profili",
        workflow_name="debug_symbol_workflow",
        timeframe="1d",
        max_symbols_per_run=1,
        continue_on_symbol_error=False,
        continue_on_job_error=False,
        retry_failed_jobs=False,
        dry_run=True,
        notes="Tek sembol debug ve pipeline sırası testi için."
    )
]

def get_orchestration_profile(name: str) -> OrchestrationProfile:
    for profile in _PROFILES:
        if profile.name == name:
            return profile
    raise ConfigError(f"Unknown orchestration profile: {name}")

def list_orchestration_profiles(enabled_only: bool = True) -> list[OrchestrationProfile]:
    if enabled_only:
        return [p for p in _PROFILES if p.enabled]
    return list(_PROFILES)

def validate_orchestration_profiles() -> None:
    for profile in _PROFILES:
        if profile.max_symbols_per_run <= 0:
            raise ConfigError(f"Profile {profile.name} has non-positive max_symbols_per_run")
        if profile.max_retries < 0:
            raise ConfigError(f"Profile {profile.name} has negative max_retries")
        if profile.retry_delay_seconds < 0:
            raise ConfigError(f"Profile {profile.name} has negative retry_delay_seconds")
        if not profile.workflow_name:
            raise ConfigError(f"Profile {profile.name} has empty workflow_name")

def get_default_orchestration_profile() -> OrchestrationProfile:
    return get_orchestration_profile(settings.default_orchestration_profile)
