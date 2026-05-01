"""
System-wide settings and configuration management.
"""

import logging
import os
from dataclasses import dataclass, field

from dotenv import load_dotenv

logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()


@dataclass
class Settings:
    """
    Application settings loaded from environment variables with defaults.
    """

    app_name: str = "commodity_fx_signal_bot"
    environment: str = field(
        default_factory=lambda: os.getenv("APP_ENV", "development")
    )
    log_level: str = field(default_factory=lambda: os.getenv("LOG_LEVEL", "INFO"))
    base_currency: str = field(
        default_factory=lambda: os.getenv("BASE_CURRENCY", "TRY")
    )

    # Data Settings
    default_period: str = field(
        default_factory=lambda: os.getenv("DEFAULT_PERIOD", "2y")
    )
    yahoo_default_period: str = field(
        default_factory=lambda: os.getenv("YAHOO_DEFAULT_PERIOD", "2y")
    )
    yahoo_default_interval: str = field(
        default_factory=lambda: os.getenv("YAHOO_DEFAULT_INTERVAL", "1d")
    )
    default_interval: str = field(
        default_factory=lambda: os.getenv("DEFAULT_INTERVAL", "1h")
    )
    default_lookback_days: int = field(
        default_factory=lambda: int(os.getenv("DEFAULT_LOOKBACK_DAYS", "730"))
    )
    max_symbols_per_scan: int = field(
        default_factory=lambda: int(os.getenv("MAX_SYMBOLS_PER_SCAN", "80"))
    )

    # Cache and Quality Settings
    cache_format: str = field(
        default_factory=lambda: os.getenv("CACHE_FORMAT", "parquet")
    )
    min_ohlcv_rows: int = field(
        default_factory=lambda: int(os.getenv("MIN_OHLCV_ROWS", "50"))
    )
    allow_network_calls: bool = field(
        default_factory=lambda: os.getenv("ALLOW_NETWORK_CALLS", "true").lower()
        == "true"
    )
    data_provider_timeout_seconds: int = field(
        default_factory=lambda: int(os.getenv("DATA_PROVIDER_TIMEOUT_SECONDS", "30"))
    )
    fail_fast_data_downloads: bool = field(
        default_factory=lambda: os.getenv("FAIL_FAST_DATA_DOWNLOADS", "false").lower()
        == "true"
    )

    # Data Lake Settings
    data_lake_enabled: bool = field(
        default_factory=lambda: os.getenv("DATA_LAKE_ENABLED", "true").lower() == "true"
    )
    data_lake_format: str = field(
        default_factory=lambda: os.getenv("DATA_LAKE_FORMAT", "parquet")
    )
    journal_enabled: bool = field(
        default_factory=lambda: os.getenv("JOURNAL_ENABLED", "true").lower() == "true"
    )
    manifest_enabled: bool = field(
        default_factory=lambda: os.getenv("MANIFEST_ENABLED", "true").lower() == "true"
    )
    default_download_period: str = field(
        default_factory=lambda: os.getenv("DEFAULT_DOWNLOAD_PERIOD", "2y")
    )
    max_download_failures_per_run: int = field(
        default_factory=lambda: int(os.getenv("MAX_DOWNLOAD_FAILURES_PER_RUN", "20"))
    )
    skip_synthetic_downloads: bool = field(
        default_factory=lambda: os.getenv("SKIP_SYNTHETIC_DOWNLOADS", "true").lower()
        == "true"
    )
    skip_macro_downloads_in_ohlcv_pipeline: bool = field(
        default_factory=lambda: os.getenv(
            "SKIP_MACRO_DOWNLOADS_IN_OHLCV_PIPELINE", "true"
        ).lower()
        == "true"
    )

    # Phase 6: Data Cleaning and Quality Settings
    processed_data_enabled: bool = field(
        default_factory=lambda: os.getenv("PROCESSED_DATA_ENABLED", "true").lower()
        == "true"
    )
    cleaning_enabled: bool = field(
        default_factory=lambda: os.getenv("CLEANING_ENABLED", "true").lower() == "true"
    )
    outlier_detection_enabled: bool = field(
        default_factory=lambda: os.getenv("OUTLIER_DETECTION_ENABLED", "true").lower()
        == "true"
    )
    default_quality_min_rows: int = field(
        default_factory=lambda: int(os.getenv("DEFAULT_QUALITY_MIN_ROWS", "50"))
    )
    default_outlier_return_threshold: float = field(
        default_factory=lambda: float(
            os.getenv("DEFAULT_OUTLIER_RETURN_THRESHOLD", "0.20")
        )
    )
    default_outlier_zscore_threshold: float = field(
        default_factory=lambda: float(
            os.getenv("DEFAULT_OUTLIER_ZSCORE_THRESHOLD", "6.0")
        )
    )
    allow_forward_fill_small_gaps: bool = field(
        default_factory=lambda: os.getenv(
            "ALLOW_FORWARD_FILL_SMALL_GAPS", "false"
        ).lower()
        == "true"
    )
    max_forward_fill_gap: int = field(
        default_factory=lambda: int(os.getenv("MAX_FORWARD_FILL_GAP", "2"))
    )
    preserve_raw_data: bool = field(
        default_factory=lambda: os.getenv("PRESERVE_RAW_DATA", "true").lower() == "true"
    )

    # Phase 8: Momentum Features & Events Settings
    momentum_features_enabled: bool = field(
        default_factory=lambda: os.getenv("MOMENTUM_FEATURES_ENABLED", "true").lower()
        == "true"
    )
    momentum_events_enabled: bool = field(
        default_factory=lambda: os.getenv("MOMENTUM_EVENTS_ENABLED", "true").lower()
        == "true"
    )
    default_momentum_windows: tuple[int, ...] = field(
        default_factory=lambda: tuple(
            int(x)
            for x in os.getenv("DEFAULT_MOMENTUM_WINDOWS", "7,14,21,28").split(",")
        )
    )
    default_roc_windows: tuple[int, ...] = field(
        default_factory=lambda: tuple(
            int(x) for x in os.getenv("DEFAULT_ROC_WINDOWS", "5,10,20").split(",")
        )
    )
    default_momentum_overbought_rsi: float = field(
        default_factory=lambda: float(
            os.getenv("DEFAULT_MOMENTUM_OVERBOUGHT_RSI", "70.0")
        )
    )
    default_momentum_oversold_rsi: float = field(
        default_factory=lambda: float(
            os.getenv("DEFAULT_MOMENTUM_OVERSOLD_RSI", "30.0")
        )
    )
    default_stochastic_overbought: float = field(
        default_factory=lambda: float(
            os.getenv("DEFAULT_STOCHASTIC_OVERBOUGHT", "80.0")
        )
    )
    default_stochastic_oversold: float = field(
        default_factory=lambda: float(os.getenv("DEFAULT_STOCHASTIC_OVERSOLD", "20.0"))
    )
    save_momentum_features: bool = field(
        default_factory=lambda: os.getenv("SAVE_MOMENTUM_FEATURES", "true").lower()
        == "true"
    )
    save_momentum_events: bool = field(
        default_factory=lambda: os.getenv("SAVE_MOMENTUM_EVENTS", "true").lower()
        == "true"
    )

    # Phase 9: Trend Features & Events Settings
    trend_features_enabled: bool = field(
        default_factory=lambda: os.getenv("TREND_FEATURES_ENABLED", "true").lower()
        == "true"
    )
    trend_events_enabled: bool = field(
        default_factory=lambda: os.getenv("TREND_EVENTS_ENABLED", "true").lower()
        == "true"
    )
    default_trend_ma_windows: tuple[int, ...] = field(
        default_factory=lambda: tuple(
            int(x)
            for x in os.getenv("DEFAULT_TREND_MA_WINDOWS", "10,20,50,100,200").split(
                ","
            )
        )
    )
    default_trend_fast_windows: tuple[int, ...] = field(
        default_factory=lambda: tuple(
            int(x) for x in os.getenv("DEFAULT_TREND_FAST_WINDOWS", "10,20").split(",")
        )
    )
    default_trend_slow_windows: tuple[int, ...] = field(
        default_factory=lambda: tuple(
            int(x)
            for x in os.getenv("DEFAULT_TREND_SLOW_WINDOWS", "50,100,200").split(",")
        )
    )
    default_adx_threshold: float = field(
        default_factory=lambda: float(os.getenv("DEFAULT_ADX_THRESHOLD", "25.0"))
    )
    default_strong_adx_threshold: float = field(
        default_factory=lambda: float(os.getenv("DEFAULT_STRONG_ADX_THRESHOLD", "35.0"))
    )
    default_macd_fast: int = field(
        default_factory=lambda: int(os.getenv("DEFAULT_MACD_FAST", "12"))
    )
    default_macd_slow: int = field(
        default_factory=lambda: int(os.getenv("DEFAULT_MACD_SLOW", "26"))
    )
    default_macd_signal: int = field(
        default_factory=lambda: int(os.getenv("DEFAULT_MACD_SIGNAL", "9"))
    )
    save_trend_features: bool = field(
        default_factory=lambda: os.getenv("SAVE_TREND_FEATURES", "true").lower()
        == "true"
    )
    save_trend_events: bool = field(
        default_factory=lambda: os.getenv("SAVE_TREND_EVENTS", "true").lower() == "true"
    )

    # Phase 13: Price Action Features & Events Settings
    price_action_features_enabled: bool = field(
        default_factory=lambda: os.getenv(
            "PRICE_ACTION_FEATURES_ENABLED", "true"
        ).lower()
        == "true"
    )
    price_action_events_enabled: bool = field(
        default_factory=lambda: os.getenv("PRICE_ACTION_EVENTS_ENABLED", "true").lower()
        == "true"
    )
    default_price_action_windows: tuple[int, ...] = field(
        default_factory=lambda: tuple(
            int(x)
            for x in os.getenv("DEFAULT_PRICE_ACTION_WINDOWS", "5,10,20,50").split(",")
        )
    )
    default_breakout_windows: tuple[int, ...] = field(
        default_factory=lambda: tuple(
            int(x) for x in os.getenv("DEFAULT_BREAKOUT_WINDOWS", "10,20,55").split(",")
        )
    )
    default_large_body_percentile_window: int = field(
        default_factory=lambda: int(
            os.getenv("DEFAULT_LARGE_BODY_PERCENTILE_WINDOW", "120")
        )
    )
    default_large_body_percentile_threshold: float = field(
        default_factory=lambda: float(
            os.getenv("DEFAULT_LARGE_BODY_PERCENTILE_THRESHOLD", "0.90")
        )
    )
    default_large_range_percentile_threshold: float = field(
        default_factory=lambda: float(
            os.getenv("DEFAULT_LARGE_RANGE_PERCENTILE_THRESHOLD", "0.90")
        )
    )
    default_small_range_percentile_threshold: float = field(
        default_factory=lambda: float(
            os.getenv("DEFAULT_SMALL_RANGE_PERCENTILE_THRESHOLD", "0.10")
        )
    )
    default_wick_rejection_ratio: float = field(
        default_factory=lambda: float(os.getenv("DEFAULT_WICK_REJECTION_RATIO", "0.60"))
    )
    default_strong_close_upper_threshold: float = field(
        default_factory=lambda: float(
            os.getenv("DEFAULT_STRONG_CLOSE_UPPER_THRESHOLD", "0.80")
        )
    )
    default_strong_close_lower_threshold: float = field(
        default_factory=lambda: float(
            os.getenv("DEFAULT_STRONG_CLOSE_LOWER_THRESHOLD", "0.20")
        )
    )
    save_price_action_features: bool = field(
        default_factory=lambda: os.getenv("SAVE_PRICE_ACTION_FEATURES", "true").lower()
        == "true"
    )
    save_price_action_events: bool = field(
        default_factory=lambda: os.getenv("SAVE_PRICE_ACTION_EVENTS", "true").lower()
        == "true"
    )

    # Phase 14: Divergence Features & Events Settings
    divergence_features_enabled: bool = field(
        default_factory=lambda: os.getenv("DIVERGENCE_FEATURES_ENABLED", "true").lower()
        == "true"
    )
    divergence_events_enabled: bool = field(
        default_factory=lambda: os.getenv("DIVERGENCE_EVENTS_ENABLED", "true").lower()
        == "true"
    )
    default_divergence_pivot_left: int = field(
        default_factory=lambda: int(os.getenv("DEFAULT_DIVERGENCE_PIVOT_LEFT", "3"))
    )
    default_divergence_pivot_right: int = field(
        default_factory=lambda: int(os.getenv("DEFAULT_DIVERGENCE_PIVOT_RIGHT", "3"))
    )
    default_divergence_lookback: int = field(
        default_factory=lambda: int(os.getenv("DEFAULT_DIVERGENCE_LOOKBACK", "80"))
    )
    default_divergence_min_price_move_pct: float = field(
        default_factory=lambda: float(
            os.getenv("DEFAULT_DIVERGENCE_MIN_PRICE_MOVE_PCT", "0.005")
        )
    )
    default_divergence_min_indicator_move: float = field(
        default_factory=lambda: float(
            os.getenv("DEFAULT_DIVERGENCE_MIN_INDICATOR_MOVE", "0.0")
        )
    )
    default_divergence_confirmation_window: int = field(
        default_factory=lambda: int(
            os.getenv("DEFAULT_DIVERGENCE_CONFIRMATION_WINDOW", "5")
        )
    )
    default_divergence_indicator_columns: tuple[str, ...] = field(
        default_factory=lambda: tuple(
            os.getenv(
                "DEFAULT_DIVERGENCE_INDICATOR_COLUMNS",
                "rsi_14,macd_hist_12_26_9,roc_10,obv,mfi_14,cmf_20",
            ).split(",")
        )
    )
    save_divergence_features: bool = field(
        default_factory=lambda: os.getenv("SAVE_DIVERGENCE_FEATURES", "true").lower()
        == "true"
    )
    save_divergence_events: bool = field(
        default_factory=lambda: os.getenv("SAVE_DIVERGENCE_EVENTS", "true").lower()
        == "true"
    )

    # Phase 15: MTF Settings
    mtf_features_enabled: bool = field(
        default_factory=lambda: os.getenv("MTF_FEATURES_ENABLED", "true").lower()
        == "true"
    )
    mtf_events_enabled: bool = field(
        default_factory=lambda: os.getenv("MTF_EVENTS_ENABLED", "true").lower()
        == "true"
    )
    default_mtf_base_timeframe: str = field(
        default_factory=lambda: os.getenv("DEFAULT_MTF_BASE_TIMEFRAME", "1d")
    )
    default_mtf_context_timeframes: tuple[str, ...] = field(
        default_factory=lambda: tuple(
            os.getenv("DEFAULT_MTF_CONTEXT_TIMEFRAMES", "4h,1d,1wk").split(",")
        )
    )
    default_mtf_feature_sets: tuple[str, ...] = field(
        default_factory=lambda: tuple(
            os.getenv(
                "DEFAULT_MTF_FEATURE_SETS",
                "momentum,trend,volatility,mean_reversion,price_action,divergence",
            ).split(",")
        )
    )
    mtf_forward_fill_context: bool = field(
        default_factory=lambda: os.getenv("MTF_FORWARD_FILL_CONTEXT", "true").lower()
        == "true"
    )
    mtf_max_context_age_bars: int = field(
        default_factory=lambda: int(os.getenv("MTF_MAX_CONTEXT_AGE_BARS", "5"))
    )
    mtf_strict_no_lookahead: bool = field(
        default_factory=lambda: os.getenv("MTF_STRICT_NO_LOOKAHEAD", "true").lower()
        == "true"
    )
    save_mtf_features: bool = field(
        default_factory=lambda: os.getenv("SAVE_MTF_FEATURES", "true").lower() == "true"
    )
    save_mtf_events: bool = field(
        default_factory=lambda: os.getenv("SAVE_MTF_EVENTS", "true").lower() == "true"
    )


    # Phase 16: Regime Classification Layer Settings
    regime_features_enabled: bool = field(
        default_factory=lambda: os.getenv("REGIME_FEATURES_ENABLED", "true").lower() == "true"
    )
    regime_events_enabled: bool = field(
        default_factory=lambda: os.getenv("REGIME_EVENTS_ENABLED", "true").lower() == "true"
    )
    default_regime_profile: str = field(
        default_factory=lambda: os.getenv("DEFAULT_REGIME_PROFILE", "balanced_regime")
    )
    default_regime_timeframe: str = field(
        default_factory=lambda: os.getenv("DEFAULT_REGIME_TIMEFRAME", "1d")
    )
    default_regime_feature_sets: tuple[str, ...] = field(
        default_factory=lambda: tuple(
            os.getenv("DEFAULT_REGIME_FEATURE_SETS", "trend,momentum,volatility,mean_reversion,price_action,mtf").split(",")
        )
    )
    default_adx_trend_threshold: float = field(
        default_factory=lambda: float(os.getenv("DEFAULT_ADX_TREND_THRESHOLD", "25.0"))
    )
    default_strong_trend_threshold: float = field(
        default_factory=lambda: float(os.getenv("DEFAULT_STRONG_TREND_THRESHOLD", "35.0"))
    )
    default_low_volatility_percentile: float = field(
        default_factory=lambda: float(os.getenv("DEFAULT_LOW_VOLATILITY_PERCENTILE", "0.20"))
    )
    default_high_volatility_percentile: float = field(
        default_factory=lambda: float(os.getenv("DEFAULT_HIGH_VOLATILITY_PERCENTILE", "0.80"))
    )
    default_range_adx_threshold: float = field(
        default_factory=lambda: float(os.getenv("DEFAULT_RANGE_ADX_THRESHOLD", "20.0"))
    )
    default_regime_transition_lookback: int = field(
        default_factory=lambda: int(os.getenv("DEFAULT_REGIME_TRANSITION_LOOKBACK", "5"))
    )
    save_regime_features: bool = field(
        default_factory=lambda: os.getenv("SAVE_REGIME_FEATURES", "true").lower() == "true"
    )
    save_regime_events: bool = field(
        default_factory=lambda: os.getenv("SAVE_REGIME_EVENTS", "true").lower() == "true"
    )

    paper_trading_enabled: bool = field(

        default_factory=lambda: os.getenv("PAPER_TRADING_ENABLED", "true").lower()
        == "true"
    )

    # Live trading MUST be disabled
    live_trading_enabled: bool = False

    telegram_enabled: bool = field(
        default_factory=lambda: os.getenv("TELEGRAM_ENABLED", "false").lower() == "true"
    )
    telegram_bot_token: str = field(
        default_factory=lambda: os.getenv("TELEGRAM_BOT_TOKEN", "")
    )
    telegram_chat_id: str = field(
        default_factory=lambda: os.getenv("TELEGRAM_CHAT_ID", "")
    )

    data_cache_enabled: bool = field(
        default_factory=lambda: os.getenv("DATA_CACHE_ENABLED", "true").lower()
        == "true"
    )

    # Scan and Time settings
    default_timezone: str = field(
        default_factory=lambda: os.getenv("DEFAULT_TIMEZONE", "Europe/Istanbul")
    )
    default_scan_profile: str = field(
        default_factory=lambda: os.getenv("DEFAULT_SCAN_PROFILE", "balanced_swing")
    )
    enable_market_session_filter: bool = field(
        default_factory=lambda: os.getenv(
            "ENABLE_MARKET_SESSION_FILTER", "true"
        ).lower()
        == "true"
    )
    allow_derived_timeframes: bool = field(
        default_factory=lambda: os.getenv("ALLOW_DERIVED_TIMEFRAMES", "true").lower()
        == "true"
    )
    max_scan_plan_symbols: int = field(
        default_factory=lambda: int(os.getenv("MAX_SCAN_PLAN_SYMBOLS", "80"))
    )

    random_seed: int = field(
        default_factory=lambda: int(os.getenv("RANDOM_SEED", "42"))
    )

    # Provider API Keys
    evds_api_key: str = field(
        default_factory=lambda: os.getenv("EVDS_API_KEY", "replace_me")
    )
    fred_api_key: str = field(
        default_factory=lambda: os.getenv("FRED_API_KEY", "replace_me")
    )

    def __post_init__(self):
        """Validate settings after initialization."""
        # Enforce live trading is False regardless of env variable
        env_live_trading = os.getenv("LIVE_TRADING_ENABLED", "false").lower() == "true"
        if env_live_trading:
            logger.warning(
                "LIVE_TRADING_ENABLED is set to true in environment, but this project "
                "does not support live trading. Forcing live_trading_enabled to False."
            )
        self.live_trading_enabled = False


# Global settings instance
settings = Settings()
