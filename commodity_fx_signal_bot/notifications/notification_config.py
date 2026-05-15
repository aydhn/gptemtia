from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class NotificationProfile:
    name: str
    description: str
    telegram_enabled: bool = False
    dry_run: bool = True
    parse_mode: str = "HTML"
    message_max_chars: int = 3500
    rate_limit_seconds: float = 1.0
    include_paper_summary: bool = True
    include_backtest_summary: bool = True
    include_ml_summary: bool = True
    include_quality_alerts: bool = True
    include_error_alerts: bool = True
    max_symbols_in_digest: int = 20
    max_rows_per_section: int = 10
    enabled: bool = True
    notes: str = ""

_PROFILES = {
    "balanced_telegram_reporting": NotificationProfile(
        name="balanced_telegram_reporting",
        description="Varsayılan güvenli Telegram raporlama profili.",
        telegram_enabled=False,
        dry_run=True,
        include_paper_summary=True,
        include_backtest_summary=True,
        include_ml_summary=True,
        include_quality_alerts=True,
        include_error_alerts=True,
        notes="Varsayılan güvenli Telegram raporlama profili. Dry-run açık başlar."
    ),
    "paper_focused_reporting": NotificationProfile(
        name="paper_focused_reporting",
        description="Paper trading sanal portföy odaklı.",
        include_paper_summary=True,
        include_backtest_summary=False,
        include_ml_summary=False,
        include_quality_alerts=True,
        notes="Paper trading sanal portföy ve sanal pozisyon özetlerine odaklanır."
    ),
    "research_digest_reporting": NotificationProfile(
        name="research_digest_reporting",
        description="Araştırma ve günlük geniş özet için.",
        include_paper_summary=True,
        include_backtest_summary=True,
        include_ml_summary=True,
        include_quality_alerts=True,
        max_symbols_in_digest=30,
        notes="Araştırma ve günlük geniş özet için."
    ),
    "minimal_alert_reporting": NotificationProfile(
        name="minimal_alert_reporting",
        description="Sadece kritik hata ve kalite uyarıları.",
        include_paper_summary=False,
        include_backtest_summary=False,
        include_ml_summary=False,
        include_quality_alerts=True,
        include_error_alerts=True,
        max_rows_per_section=5,
        notes="Sadece kritik hata ve kalite uyarıları."
    )
}

def get_notification_profile(name: str) -> NotificationProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Unknown notification profile: {name}")
    return _PROFILES[name]

def list_notification_profiles(enabled_only: bool = True) -> list[NotificationProfile]:
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())

def validate_notification_profiles() -> None:
    for profile in _PROFILES.values():
        if profile.message_max_chars <= 0:
            raise ConfigError(f"Profile {profile.name} has non-positive message_max_chars")
        if profile.rate_limit_seconds < 0:
            raise ConfigError(f"Profile {profile.name} has negative rate_limit_seconds")
        if profile.max_rows_per_section <= 0:
            raise ConfigError(f"Profile {profile.name} has non-positive max_rows_per_section")
        if profile.max_symbols_in_digest <= 0:
            raise ConfigError(f"Profile {profile.name} has non-positive max_symbols_in_digest")
        if profile.parse_mode not in ["HTML", "Markdown", None]:
            raise ConfigError(f"Profile {profile.name} has invalid parse_mode: {profile.parse_mode}")

def get_default_notification_profile() -> NotificationProfile:
    from config.settings import settings
    return get_notification_profile(settings.default_notification_profile)
