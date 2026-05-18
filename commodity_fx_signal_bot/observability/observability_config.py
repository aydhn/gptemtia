"""
Observability profile configuration and registry.
"""

from dataclasses import dataclass
from typing import Dict, List


class ConfigError(Exception):
    """Exception raised for errors in the observability configuration."""
    pass


@dataclass(frozen=True)
class ObservabilityProfile:
    """Configuration profile for observability settings."""

    name: str
    description: str
    log_level: str = "INFO"
    log_to_file: bool = True
    log_to_console: bool = True
    json_logs_enabled: bool = True
    max_log_files: int = 20
    healthcheck_enabled: bool = True
    runtime_metrics_enabled: bool = True
    data_freshness_enabled: bool = True
    artifact_integrity_enabled: bool = True
    dependency_diagnostics_enabled: bool = True
    max_stale_hours_daily: float = 48.0
    max_stale_hours_intraday: float = 12.0
    min_required_disk_free_mb: int = 1024
    notification_on_critical: bool = False
    enabled: bool = True
    notes: str = ""

    def __post_init__(self):
        """Validate profile settings after initialization."""
        valid_log_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if self.log_level.upper() not in valid_log_levels:
            raise ValueError(f"Invalid log level: {self.log_level}")

        if self.max_log_files <= 0:
            raise ValueError(f"max_log_files must be positive: {self.max_log_files}")

        if self.max_stale_hours_daily < 0:
            raise ValueError(f"max_stale_hours_daily cannot be negative: {self.max_stale_hours_daily}")

        if self.max_stale_hours_intraday < 0:
            raise ValueError(f"max_stale_hours_intraday cannot be negative: {self.max_stale_hours_intraday}")

        if self.min_required_disk_free_mb <= 0:
            raise ValueError(f"min_required_disk_free_mb must be positive: {self.min_required_disk_free_mb}")


# Built-in profiles
_OBSERVABILITY_PROFILES: Dict[str, ObservabilityProfile] = {
    "balanced_system_observability": ObservabilityProfile(
        name="balanced_system_observability",
        description="Balanced system observability profile",
        log_level="INFO",
        log_to_file=True,
        log_to_console=True,
        json_logs_enabled=True,
        max_log_files=20,
        max_stale_hours_daily=48.0,
        max_stale_hours_intraday=12.0,
        notification_on_critical=False,
        notes="Genel amaçlı sistem sağlık ve gözlemlenebilirlik profili."
    ),
    "debug_observability": ObservabilityProfile(
        name="debug_observability",
        description="Debug observability profile",
        log_level="DEBUG",
        json_logs_enabled=True,
        max_log_files=50,
        notes="Debug ve geliştirme sırasında daha detaylı log üretir."
    ),
    "minimal_health_observability": ObservabilityProfile(
        name="minimal_health_observability",
        description="Minimal health observability profile",
        log_level="WARNING",
        log_to_file=True,
        log_to_console=True,
        runtime_metrics_enabled=True,
        data_freshness_enabled=True,
        artifact_integrity_enabled=False,
        dependency_diagnostics_enabled=True,
        notes="Hafif healthcheck profili."
    ),
    "strict_integrity_observability": ObservabilityProfile(
        name="strict_integrity_observability",
        description="Strict integrity observability profile",
        log_level="INFO",
        artifact_integrity_enabled=True,
        dependency_diagnostics_enabled=True,
        max_stale_hours_daily=24.0,
        max_stale_hours_intraday=6.0,
        min_required_disk_free_mb=2048,
        notes="Daha sıkı veri tazeliği ve artifact bütünlüğü kontrolü."
    ),
}


def get_observability_profile(name: str) -> ObservabilityProfile:
    """Get an observability profile by name."""
    if name not in _OBSERVABILITY_PROFILES:
        raise ConfigError(f"Unknown observability profile: {name}")
    return _OBSERVABILITY_PROFILES[name]


def list_observability_profiles(enabled_only: bool = True) -> List[ObservabilityProfile]:
    """List all available observability profiles."""
    if enabled_only:
        return [p for p in _OBSERVABILITY_PROFILES.values() if p.enabled]
    return list(_OBSERVABILITY_PROFILES.values())


def validate_observability_profiles() -> None:
    """Validate all built-in observability profiles."""
    for name, profile in _OBSERVABILITY_PROFILES.items():
        try:
            # Trigger dataclass validation (already happens on creation, but good to have explicit check)
            # Creating a dummy object to ensure __post_init__ runs again for validation test
            ObservabilityProfile(**{k: v for k, v in profile.__dict__.items() if k != '__post_init__'})
        except ValueError as e:
            raise ConfigError(f"Invalid configuration in profile '{name}': {e}")


def get_default_observability_profile() -> ObservabilityProfile:
    """Get the default observability profile from settings."""
    from config.settings import settings
    try:
        return get_observability_profile(settings.default_observability_profile)
    except ConfigError:
        # Fallback to balanced if default is not found/configured
        return get_observability_profile("balanced_system_observability")
