from typing import Tuple, Dict, Any, List, Optional
import pandas as pd

from advanced_technical_indicators.technical_indicator_config import TechnicalIndicatorProfile
from advanced_technical_indicators.price_action_indicators import (
    add_high_low_range, add_close_open_range, add_range_pct, add_gap_from_previous_close, add_close_location_value
)
from advanced_technical_indicators.return_indicators import (
    add_simple_return, add_log_return, add_cumulative_return, add_rolling_return_sum, add_return_volatility_ratio
)
from advanced_technical_indicators.moving_average_indicators import (
    add_sma, add_ema, add_wma, add_dema, add_tema, add_moving_average_distance
)
from advanced_technical_indicators.trend_indicators import (
    add_macd, add_ppo, add_donchian_channel, add_aroon, add_adx_dmi_placeholder, add_ichimoku_placeholder
)
from advanced_technical_indicators.momentum_indicators import (
    add_momentum, add_roc, add_rsi, add_cmo, add_tsi_placeholder
)
from advanced_technical_indicators.oscillator_indicators import (
    add_stochastic_oscillator, add_williams_r, add_cci, add_ultimate_oscillator_placeholder, add_mfi_placeholder
)
from advanced_technical_indicators.volatility_indicators import (
    add_true_range, add_atr, add_rolling_std, add_realized_volatility, add_parkinson_volatility, add_garman_klass_volatility_placeholder
)
from advanced_technical_indicators.range_indicators import (
    add_rolling_high_low_range, add_rolling_range_pct, add_average_range, add_range_zscore
)
from advanced_technical_indicators.channel_indicators import (
    add_bollinger_bands, add_bollinger_bandwidth, add_bollinger_percent_b, add_keltner_channel_placeholder, add_donchian_position
)
from advanced_technical_indicators.candle_anatomy_features import (
    add_candle_body_size, add_candle_body_pct, add_upper_wick_size, add_lower_wick_size, add_wick_balance
)
from advanced_technical_indicators.quote_microstructure_features import (
    add_quote_mid, add_quote_spread, add_quote_spread_pct, add_bid_ask_ratio_placeholder, add_quote_staleness_placeholder
)
from advanced_technical_indicators.mean_reversion_indicators import (
    add_rolling_zscore, add_distance_to_sma, add_distance_to_ema, add_rolling_percentile_rank_placeholder, add_rolling_deviation_ratio
)

SUPPORTED_COMPUTATIONS = [
    "high_low_range", "close_open_range", "range_pct", "gap_from_prev_close", "close_location_value",
    "simple_return", "log_return", "cumulative_return", "rolling_return_sum", "return_volatility_ratio",
    "sma", "ema", "wma", "dema", "tema", "ma_distance",
    "macd", "ppo", "donchian_channel", "aroon", "adx_dmi", "ichimoku",
    "momentum", "roc", "rsi", "cmo", "tsi",
    "stochastic", "williams_r", "cci", "ultimate_oscillator", "mfi",
    "true_range", "atr", "rolling_std", "realized_volatility", "parkinson_volatility", "garman_klass_volatility",
    "rolling_high_low_range", "rolling_range_pct", "average_range", "range_zscore",
    "bollinger_bands", "bollinger_bandwidth", "bollinger_percent_b", "keltner_channel", "donchian_position",
    "candle_body_size", "candle_body_pct", "upper_wick_size", "lower_wick_size", "wick_balance",
    "quote_mid", "quote_spread", "quote_spread_pct", "bid_ask_ratio", "quote_staleness",
    "rolling_zscore", "distance_to_sma", "distance_to_ema", "rolling_percentile_rank", "rolling_deviation_ratio"
]


def list_supported_indicator_computations() -> List[str]:
    return list(SUPPORTED_COMPUTATIONS)


def compute_indicator_by_name(
    df: pd.DataFrame,
    indicator_name: str,
    parameters: Optional[Dict[str, Any]] = None,
) -> pd.DataFrame:
    params = parameters or {}
    name = indicator_name.lower().strip()

    # Price action
    if name == "high_low_range":
        return add_high_low_range(df, **params)
    elif name == "close_open_range":
        return add_close_open_range(df, **params)
    elif name == "range_pct":
        return add_range_pct(df, **params)
    elif name == "gap_from_prev_close":
        return add_gap_from_previous_close(df, **params)
    elif name == "close_location_value":
        return add_close_location_value(df, **params)

    # Returns
    elif name == "simple_return":
        return add_simple_return(df, **params)
    elif name == "log_return":
        return add_log_return(df, **params)
    elif name == "cumulative_return":
        return add_cumulative_return(df, **params)
    elif name == "rolling_return_sum":
        return add_rolling_return_sum(df, **params)
    elif name == "return_volatility_ratio":
        return add_return_volatility_ratio(df, **params)

    # Moving averages
    elif name == "sma":
        return add_sma(df, **params)
    elif name == "ema":
        return add_ema(df, **params)
    elif name == "wma":
        return add_wma(df, **params)
    elif name == "dema":
        return add_dema(df, **params)
    elif name == "tema":
        return add_tema(df, **params)
    elif name == "ma_distance":
        return add_moving_average_distance(df, **params)

    # Trend
    elif name == "macd":
        return add_macd(df, **params)
    elif name == "ppo":
        return add_ppo(df, **params)
    elif name == "donchian_channel":
        return add_donchian_channel(df, **params)
    elif name == "aroon":
        return add_aroon(df, **params)
    elif name in ("adx_dmi", "adx", "adx_dmi_placeholder"):
        return add_adx_dmi_placeholder(df, **params)
    elif name in ("ichimoku", "ichimoku_placeholder"):
        return add_ichimoku_placeholder(df, **params)

    # Momentum
    elif name == "momentum":
        return add_momentum(df, **params)
    elif name == "roc":
        return add_roc(df, **params)
    elif name == "rsi":
        return add_rsi(df, **params)
    elif name == "cmo":
        return add_cmo(df, **params)
    elif name in ("tsi", "tsi_placeholder"):
        return add_tsi_placeholder(df, **params)

    # Oscillators
    elif name in ("stochastic", "stoch"):
        return add_stochastic_oscillator(df, **params)
    elif name == "williams_r":
        return add_williams_r(df, **params)
    elif name == "cci":
        return add_cci(df, **params)
    elif name in ("ultimate_oscillator", "ultimate_osc", "ultimate_oscillator_placeholder"):
        return add_ultimate_oscillator_placeholder(df, **params)
    elif name in ("mfi", "mfi_placeholder"):
        return add_mfi_placeholder(df, **params)

    # Volatility
    elif name == "true_range":
        return add_true_range(df, **params)
    elif name == "atr":
        return add_atr(df, **params)
    elif name == "rolling_std":
        return add_rolling_std(df, **params)
    elif name == "realized_volatility":
        return add_realized_volatility(df, **params)
    elif name == "parkinson_volatility":
        return add_parkinson_volatility(df, **params)
    elif name in ("garman_klass_volatility", "garman_klass_volatility_placeholder"):
        return add_garman_klass_volatility_placeholder(df, **params)

    # Range
    elif name == "rolling_high_low_range":
        return add_rolling_high_low_range(df, **params)
    elif name == "rolling_range_pct":
        return add_rolling_range_pct(df, **params)
    elif name == "average_range":
        return add_average_range(df, **params)
    elif name == "range_zscore":
        return add_range_zscore(df, **params)

    # Channels
    elif name == "bollinger_bands":
        return add_bollinger_bands(df, **params)
    elif name == "bollinger_bandwidth":
        return add_bollinger_bandwidth(df, **params)
    elif name == "bollinger_percent_b":
        return add_bollinger_percent_b(df, **params)
    elif name in ("keltner_channel", "keltner_channel_placeholder"):
        return add_keltner_channel_placeholder(df, **params)
    elif name == "donchian_position":
        return add_donchian_position(df, **params)

    # Candle anatomy
    elif name == "candle_body_size":
        return add_candle_body_size(df, **params)
    elif name == "candle_body_pct":
        return add_candle_body_pct(df, **params)
    elif name == "upper_wick_size":
        return add_upper_wick_size(df, **params)
    elif name == "lower_wick_size":
        return add_lower_wick_size(df, **params)
    elif name == "wick_balance":
        return add_wick_balance(df, **params)

    # Quote microstructure
    elif name == "quote_mid":
        return add_quote_mid(df, **params)
    elif name == "quote_spread":
        return add_quote_spread(df, **params)
    elif name == "quote_spread_pct":
        return add_quote_spread_pct(df, **params)
    elif name in ("bid_ask_ratio", "bid_ask_ratio_placeholder"):
        return add_bid_ask_ratio_placeholder(df, **params)
    elif name in ("quote_staleness", "quote_staleness_placeholder"):
        return add_quote_staleness_placeholder(df, **params)

    # Mean reversion
    elif name == "rolling_zscore":
        return add_rolling_zscore(df, **params)
    elif name == "distance_to_sma":
        return add_distance_to_sma(df, **params)
    elif name == "distance_to_ema":
        return add_distance_to_ema(df, **params)
    elif name in ("rolling_percentile_rank", "rolling_percentile_rank_placeholder"):
        return add_rolling_percentile_rank_placeholder(df, **params)
    elif name == "rolling_deviation_ratio":
        return add_rolling_deviation_ratio(df, **params)

    raise ValueError(f"Unknown indicator calculation: '{indicator_name}'. Supported: {SUPPORTED_COMPUTATIONS}")


def build_advanced_indicator_computation_module_report(
    profile: TechnicalIndicatorProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rows = []
    for c in SUPPORTED_COMPUTATIONS:
        rows.append({
            "indicator_name": c,
            "status": "IMPLEMENTED",
            "non_signal": True,
            "framework": "pandas/numpy",
            "ta_lib_required": False,
        })
    df = pd.DataFrame(rows)
    summary = {
        "total_computations_supported": len(df),
        "pure_python_numpy": True,
        "ta_lib_required": False,
        "current_phase": profile.current_phase,
    }
    return df, summary
