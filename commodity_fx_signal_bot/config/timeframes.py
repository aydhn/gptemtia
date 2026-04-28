from dataclasses import dataclass
from typing import List
from core.exceptions import ConfigError


@dataclass(frozen=True)
class TimeframeSpec:
    name: str
    provider_interval: str
    minutes: int
    category: str
    enabled: bool = True
    recommended_for_signal: bool = True
    recommended_for_backtest: bool = True
    min_lookback_days: int = 30
    max_yahoo_period: str = ""
    notes: str = ""


DEFAULT_TIMEFRAMES: List[TimeframeSpec] = [
    TimeframeSpec(
        name="1m",
        provider_interval="1m",
        minutes=1,
        category="intraday",
        enabled=False,
        recommended_for_signal=False,
        recommended_for_backtest=False,
        min_lookback_days=7,
        notes="Yahoo/yfinance sınırlı geçmiş verir; düşük frekanslı bot için ana hedef değildir.",
    ),
    TimeframeSpec(
        name="2m",
        provider_interval="2m",
        minutes=2,
        category="intraday",
        enabled=False,
        recommended_for_signal=False,
        recommended_for_backtest=False,
        min_lookback_days=7,
    ),
    TimeframeSpec(
        name="5m",
        provider_interval="5m",
        minutes=5,
        category="intraday",
        enabled=True,
        recommended_for_signal=False,
        recommended_for_backtest=False,
        min_lookback_days=30,
        notes="Sadece smoke test veya ileride kısa vadeli analiz için.",
    ),
    TimeframeSpec(
        name="15m",
        provider_interval="15m",
        minutes=15,
        category="intraday",
        enabled=True,
        recommended_for_signal=True,
        recommended_for_backtest=True,
        min_lookback_days=60,
    ),
    TimeframeSpec(
        name="30m",
        provider_interval="30m",
        minutes=30,
        category="intraday",
        enabled=True,
        recommended_for_signal=True,
        recommended_for_backtest=True,
        min_lookback_days=90,
    ),
    TimeframeSpec(
        name="1h",
        provider_interval="1h",
        minutes=60,
        category="intraday",
        enabled=True,
        recommended_for_signal=True,
        recommended_for_backtest=True,
        min_lookback_days=180,
    ),
    TimeframeSpec(
        name="4h",
        provider_interval="1h",
        minutes=240,
        category="derived",
        enabled=True,
        recommended_for_signal=True,
        recommended_for_backtest=True,
        min_lookback_days=365,
        notes="Yahoo’dan doğrudan değil, 1h veriden resample edilerek üretilebilir.",
    ),
    TimeframeSpec(
        name="1d",
        provider_interval="1d",
        minutes=1440,
        category="daily",
        enabled=True,
        recommended_for_signal=True,
        recommended_for_backtest=True,
        min_lookback_days=730,
    ),
    TimeframeSpec(
        name="1wk",
        provider_interval="1wk",
        minutes=10080,
        category="weekly",
        enabled=True,
        recommended_for_signal=True,
        recommended_for_backtest=True,
        min_lookback_days=1825,
    ),
    TimeframeSpec(
        name="1mo",
        provider_interval="1mo",
        minutes=43200,
        category="monthly",
        enabled=True,
        recommended_for_signal=False,
        recommended_for_backtest=True,
        min_lookback_days=3650,
    ),
]

_TIMEFRAME_MAP = {tf.name: tf for tf in DEFAULT_TIMEFRAMES}


def get_timeframe(name: str) -> TimeframeSpec:
    if name not in _TIMEFRAME_MAP:
        raise ConfigError(f"Unknown timeframe: {name}")
    return _TIMEFRAME_MAP[name]


def list_timeframes(enabled_only: bool = True) -> List[TimeframeSpec]:
    if enabled_only:
        return [tf for tf in DEFAULT_TIMEFRAMES if tf.enabled]
    return list(DEFAULT_TIMEFRAMES)


def list_signal_timeframes() -> List[TimeframeSpec]:
    return [tf for tf in DEFAULT_TIMEFRAMES if tf.enabled and tf.recommended_for_signal]


def list_backtest_timeframes() -> List[TimeframeSpec]:
    return [
        tf for tf in DEFAULT_TIMEFRAMES if tf.enabled and tf.recommended_for_backtest
    ]


def validate_timeframe(name: str) -> None:
    if name not in _TIMEFRAME_MAP:
        raise ConfigError(f"Validation failed: Unknown timeframe: {name}")

    tf = _TIMEFRAME_MAP[name]
    if not tf.provider_interval:
        raise ConfigError(
            f"Validation failed: Missing provider_interval for timeframe: {name}"
        )

    if tf.minutes <= 0:
        raise ConfigError(
            f"Validation failed: Timeframe minutes must be positive for: {name}"
        )

    valid_categories = {"intraday", "daily", "weekly", "monthly", "derived"}
    if tf.category not in valid_categories:
        raise ConfigError(
            f"Validation failed: Unknown category '{tf.category}' for timeframe: {name}"
        )


def timeframe_to_minutes(name: str) -> int:
    return get_timeframe(name).minutes


def get_provider_interval_for_timeframe(name: str) -> str:
    return get_timeframe(name).provider_interval


def is_derived_timeframe(name: str) -> bool:
    return get_timeframe(name).category == "derived"
