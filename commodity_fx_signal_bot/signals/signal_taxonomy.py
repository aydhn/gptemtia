def list_supported_event_groups() -> list[str]:
    return [
        "momentum",
        "trend",
        "volatility",
        "volume",
        "mean_reversion",
        "price_action",
        "divergence",
        "mtf",
        "regime",
        "macro",
        "asset_profile",
    ]


def list_supported_candidate_types() -> list[str]:
    return [
        "trend_following",
        "mean_reversion",
        "breakout",
        "pullback",
        "volatility_expansion",
        "volatility_squeeze",
        "divergence",
        "macro_context",
        "risk_warning",
        "quality_warning",
        "unknown",
    ]


def infer_event_group(event_column: str) -> str:
    col = event_column.lower()
    if any(x in col for x in ["rsi", "macd", "stoch", "momentum"]):
        return "momentum"
    if any(x in col for x in ["ema", "sma", "trend", "adx", "cross"]):
        return "trend"
    if any(x in col for x in ["bb_", "atr", "volatility", "squeeze", "expansion"]):
        return "volatility"
    if any(x in col for x in ["volume", "obv", "vwap"]):
        return "volume"
    if any(x in col for x in ["reversion", "oversold", "overbought", "zscore"]):
        return "mean_reversion"
    if any(
        x in col for x in ["pinbar", "engulfing", "doji", "price_action", "breakout"]
    ):
        return "price_action"
    if "divergence" in col:
        return "divergence"
    if "mtf" in col:
        return "mtf"
    if "regime" in col:
        return "regime"
    if "macro" in col:
        return "macro"
    if any(x in col for x in ["asset_profile", "group_", "dispersion"]):
        return "asset_profile"
    return "unknown"


def infer_directional_bias(event_column: str) -> str:
    col = event_column.lower()
    if any(x in col for x in ["bullish", "long", "buy", "up", "golden", "oversold"]):
        return "bullish"
    if any(
        x in col for x in ["bearish", "short", "sell", "down", "death", "overbought"]
    ):
        return "bearish"
    if any(x in col for x in ["neutral", "squeeze", "consolidation", "flat"]):
        return "neutral"
    if any(x in col for x in ["warning", "risk", "conflict", "quality"]):
        return "warning"
    return "unknown"


def infer_candidate_type(event_column: str) -> str:
    col = event_column.lower()
    if "trend" in col or "cross" in col:
        return "trend_following"
    if "reversion" in col or "oversold" in col or "overbought" in col:
        return "mean_reversion"
    if "breakout" in col:
        return "breakout"
    if "pullback" in col:
        return "pullback"
    if "expansion" in col:
        return "volatility_expansion"
    if "squeeze" in col:
        return "volatility_squeeze"
    if "divergence" in col:
        return "divergence"
    if "macro" in col:
        return "macro_context"
    if "warning" in col or "risk" in col:
        return "risk_warning"
    if "quality" in col or "missing" in col:
        return "quality_warning"
    return "unknown"


def is_warning_event(event_column: str) -> bool:
    return "warning" in event_column.lower() or "risk" in event_column.lower()


def is_context_event(event_column: str) -> bool:
    return (
        infer_directional_bias(event_column) == "neutral"
        or "context" in event_column.lower()
        or "regime" in event_column.lower()
    )


def is_directional_event(event_column: str) -> bool:
    bias = infer_directional_bias(event_column)
    return bias in ["bullish", "bearish"]
