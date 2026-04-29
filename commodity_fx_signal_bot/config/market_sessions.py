from dataclasses import dataclass
from typing import List

from core.exceptions import ConfigError


@dataclass(frozen=True)
class MarketSessionSpec:
    asset_class: str
    session_name: str
    timezone: str
    typical_open: str
    typical_close: str
    trades_24h: bool
    weekend_trading: bool
    notes: str = ""


DEFAULT_MARKET_SESSIONS: List[MarketSessionSpec] = [
    MarketSessionSpec(
        asset_class="forex_try",
        session_name="forex_24_5",
        timezone="UTC",
        typical_open="22:00",
        typical_close="22:00",
        trades_24h=True,
        weekend_trading=False,
        notes="FX piyasaları genelde hafta içi 24 saat varsayılır; ücretsiz veri kaynağı gecikmeli/eksik olabilir.",
    ),
    MarketSessionSpec(
        asset_class="forex_major",
        session_name="forex_24_5",
        timezone="UTC",
        typical_open="22:00",
        typical_close="22:00",
        trades_24h=True,
        weekend_trading=False,
    ),
    MarketSessionSpec(
        asset_class="forex_cross",
        session_name="forex_24_5",
        timezone="UTC",
        typical_open="22:00",
        typical_close="22:00",
        trades_24h=True,
        weekend_trading=False,
    ),
    MarketSessionSpec(
        asset_class="metals",
        session_name="futures_extended",
        timezone="America/New_York",
        typical_open="18:00",
        typical_close="17:00",
        trades_24h=False,
        weekend_trading=False,
        notes="Vadeli emtia kontratlarında seans araları ve borsa tatilleri olabilir; bu proje yaklaşık seans mantığı kullanır.",
    ),
    MarketSessionSpec(
        asset_class="energy",
        session_name="futures_extended",
        timezone="America/New_York",
        typical_open="18:00",
        typical_close="17:00",
        trades_24h=False,
        weekend_trading=False,
    ),
    MarketSessionSpec(
        asset_class="agriculture",
        session_name="futures_limited",
        timezone="America/Chicago",
        typical_open="08:30",  # Example approximate time
        typical_close="13:20",
        trades_24h=False,
        weekend_trading=False,
    ),
    MarketSessionSpec(
        asset_class="softs",
        session_name="futures_limited",
        timezone="America/New_York",
        typical_open="03:30",
        typical_close="13:00",
        trades_24h=False,
        weekend_trading=False,
    ),
    MarketSessionSpec(
        asset_class="livestock",
        session_name="futures_limited",
        timezone="America/Chicago",
        typical_open="08:30",
        typical_close="13:05",
        trades_24h=False,
        weekend_trading=False,
    ),
    MarketSessionSpec(
        asset_class="benchmark",
        session_name="synthetic",
        timezone="UTC",
        typical_open="00:00",
        typical_close="00:00",
        trades_24h=False,
        weekend_trading=False,
    ),
    MarketSessionSpec(
        asset_class="macro",
        session_name="macro_periodic",
        timezone="UTC",
        typical_open="00:00",
        typical_close="00:00",
        trades_24h=False,
        weekend_trading=False,
    ),
]

_MARKET_SESSION_MAP = {
    session.asset_class: session for session in DEFAULT_MARKET_SESSIONS
}


def get_market_session(asset_class: str) -> MarketSessionSpec:
    if asset_class not in _MARKET_SESSION_MAP:
        raise ConfigError(f"Unknown asset class for market session: {asset_class}")
    return _MARKET_SESSION_MAP[asset_class]


def list_market_sessions() -> List[MarketSessionSpec]:
    return list(DEFAULT_MARKET_SESSIONS)


def is_weekend_trading_allowed(asset_class: str) -> bool:
    try:
        return get_market_session(asset_class).weekend_trading
    except ConfigError:
        return False


def is_asset_24h(asset_class: str) -> bool:
    try:
        return get_market_session(asset_class).trades_24h
    except ConfigError:
        return False


def validate_market_sessions() -> None:
    for spec in DEFAULT_MARKET_SESSIONS:
        if not spec.asset_class:
            raise ConfigError(
                f"Market session validation failed: Missing asset_class for {spec}"
            )
        if not spec.session_name:
            raise ConfigError(
                f"Market session validation failed: Missing session_name for {spec.asset_class}"
            )
        if not spec.timezone:
            raise ConfigError(
                f"Market session validation failed: Missing timezone for {spec.asset_class}"
            )
