from dataclasses import dataclass
from typing import List, Tuple
from core.exceptions import ConfigError


@dataclass(frozen=True)
class ScanProfile:
    name: str
    description: str
    timeframes: Tuple[str, ...]
    scan_interval_minutes: int
    max_symbols_per_cycle: int
    enabled: bool = True
    notes: str = ""


DEFAULT_SCAN_PROFILES: List[ScanProfile] = [
    ScanProfile(
        name="conservative_daily",
        description="Daily and weekly scans",
        timeframes=("1d", "1wk"),
        scan_interval_minutes=240,
        max_symbols_per_cycle=80,
        notes="Çok düşük frekanslı, makro ve swing odaklı.",
    ),
    ScanProfile(
        name="balanced_swing",
        description="Balanced scanning for swing trading",
        timeframes=("4h", "1d", "1wk"),
        scan_interval_minutes=60,
        max_symbols_per_cycle=80,
        notes="Varsayılan önerilen profil.",
    ),
    ScanProfile(
        name="intraday_light",
        description="Light intraday scanning",
        timeframes=("1h", "4h", "1d"),
        scan_interval_minutes=30,
        max_symbols_per_cycle=60,
        notes="Saatlik tarama; yerel bilgisayar için makul.",
    ),
    ScanProfile(
        name="intraday_aggressive",
        description="Aggressive intraday scanning",
        timeframes=("15m", "30m", "1h", "4h"),
        scan_interval_minutes=15,
        max_symbols_per_cycle=40,
        enabled=False,
        notes="Daha sık veri çeker; ücretsiz kaynak limitleri açısından dikkatli kullanılmalı.",
    ),
]

_SCAN_PROFILE_MAP = {p.name: p for p in DEFAULT_SCAN_PROFILES}


def get_scan_profile(name: str) -> ScanProfile:
    if name not in _SCAN_PROFILE_MAP:
        raise ConfigError(f"Unknown scan profile: {name}")
    return _SCAN_PROFILE_MAP[name]


def list_scan_profiles(enabled_only: bool = True) -> List[ScanProfile]:
    if enabled_only:
        return [p for p in DEFAULT_SCAN_PROFILES if p.enabled]
    return list(DEFAULT_SCAN_PROFILES)


def validate_scan_profiles() -> None:
    for profile in DEFAULT_SCAN_PROFILES:
        if not profile.name:
            raise ConfigError("Scan profile missing name")
        if not profile.timeframes:
            raise ConfigError(f"Scan profile {profile.name} missing timeframes")
        if profile.scan_interval_minutes <= 0:
            raise ConfigError(
                f"Scan profile {profile.name} scan_interval_minutes must be > 0"
            )
        if profile.max_symbols_per_cycle <= 0:
            raise ConfigError(
                f"Scan profile {profile.name} max_symbols_per_cycle must be > 0"
            )


def get_default_scan_profile() -> ScanProfile:
    return get_scan_profile("balanced_swing")
