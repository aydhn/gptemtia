"""
Security configuration profiles and settings.
"""

from dataclasses import dataclass, field
from config.settings import settings

class ConfigError(Exception):
    """Exception raised for errors in the security configuration."""
    pass

@dataclass(frozen=True)
class SecurityProfile:
    name: str
    description: str
    fail_on_secret_leak: bool = True
    fail_on_unsafe_live_flags: bool = True
    fail_on_path_traversal_risk: bool = True
    allow_telegram_send: bool = False
    allow_live_trading: bool = False
    allow_broker_credentials: bool = False
    require_dry_run_defaults: bool = True
    max_file_scan_mb: int = 5
    required_gitignore_patterns: tuple[str, ...] = (".env", "*.key", "*.pem")
    sensitive_env_names: tuple[str, ...] = ("TOKEN", "SECRET", "KEY", "PASSWORD", "CHAT_ID", "API")
    scan_text_extensions: tuple[str, ...] = (".py", ".md", ".txt", ".json", ".yaml", ".yml", ".env", ".example")
    notification_on_critical: bool = False
    enabled: bool = True
    notes: str = ""

_SECURITY_PROFILES = {
    "balanced_local_security": SecurityProfile(
        name="balanced_local_security",
        description="Balanced local security profile for offline research.",
        fail_on_secret_leak=True,
        fail_on_unsafe_live_flags=True,
        fail_on_path_traversal_risk=True,
        allow_telegram_send=False,
        allow_live_trading=False,
        allow_broker_credentials=False,
        require_dry_run_defaults=True,
        notes="Local/offline araştırma sistemi için güvenli varsayılan security profili."
    ),
    "strict_local_security": SecurityProfile(
        name="strict_local_security",
        description="Strict local security profile.",
        fail_on_secret_leak=True,
        fail_on_unsafe_live_flags=True,
        fail_on_path_traversal_risk=True,
        allow_telegram_send=False,
        allow_live_trading=False,
        allow_broker_credentials=False,
        max_file_scan_mb=10,
        notes="Daha sıkı secret, path ve unsafe flag denetimleri."
    ),
    "telegram_reporting_security": SecurityProfile(
        name="telegram_reporting_security",
        description="Telegram reporting security profile.",
        allow_telegram_send=True,
        allow_live_trading=False,
        allow_broker_credentials=False,
        require_dry_run_defaults=False,
        notes="Sadece Telegram raporlama gönderimine kontrollü izin veren profil. Broker/canlı trade hâlâ kapalıdır."
    ),
    "debug_security": SecurityProfile(
        name="debug_security",
        description="Loose debug profile.",
        fail_on_secret_leak=False,
        fail_on_unsafe_live_flags=True,
        fail_on_path_traversal_risk=True,
        allow_telegram_send=False,
        allow_live_trading=False,
        allow_broker_credentials=False,
        notes="Testlerde warning üretmek için gevşek debug profili. Canlı trade kapalıdır."
    )
}

def get_security_profile(name: str) -> SecurityProfile:
    if name not in _SECURITY_PROFILES:
        raise ConfigError(f"Unknown security profile: {name}")
    return _SECURITY_PROFILES[name]

def list_security_profiles(enabled_only: bool = True) -> list[SecurityProfile]:
    return [p for p in _SECURITY_PROFILES.values() if not enabled_only or p.enabled]

def validate_security_profiles() -> None:
    for name, profile in _SECURITY_PROFILES.items():
        if profile.allow_live_trading:
            raise ConfigError(f"Profile {name} cannot have allow_live_trading=True")
        if profile.allow_broker_credentials:
            raise ConfigError(f"Profile {name} cannot have allow_broker_credentials=True")
        if profile.max_file_scan_mb <= 0:
            raise ConfigError(f"Profile {name} must have max_file_scan_mb > 0")
        if not profile.required_gitignore_patterns:
            raise ConfigError(f"Profile {name} must have required_gitignore_patterns")

def get_default_security_profile() -> SecurityProfile:
    return get_security_profile(settings.default_security_profile)

# Validate at import time
validate_security_profiles()
