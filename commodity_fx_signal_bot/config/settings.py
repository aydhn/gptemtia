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

    # Secrets Hygiene Settings
    secrets_hygiene_enabled: bool = True
    default_secrets_hygiene_profile: str = "balanced_local_secrets_hygiene"
    secrets_hygiene_default_language: str = "tr"
    secrets_hygiene_dry_run_default: bool = True
    secrets_hygiene_allow_secret_value_output: bool = False
    secrets_hygiene_allow_file_modification: bool = False
    secrets_hygiene_allow_secret_deletion: bool = False
    secrets_hygiene_allow_cloud_vault: bool = False
    secrets_hygiene_allow_external_scanner: bool = False
    secrets_hygiene_allow_live_commands: bool = False
    secrets_hygiene_allow_broker_commands: bool = False
    secrets_hygiene_allow_deploy_commands: bool = False
    secrets_hygiene_allow_background_daemons: bool = False
    secrets_hygiene_allow_real_market_download: bool = False
    secrets_hygiene_allow_external_llm: bool = False
    secrets_hygiene_scan_source: bool = True
    secrets_hygiene_scan_docs: bool = True
    secrets_hygiene_scan_tests: bool = True
    secrets_hygiene_scan_configs: bool = True
    secrets_hygiene_scan_reports: bool = True
    secrets_hygiene_scan_data_manifests: bool = True
    secrets_hygiene_scan_generated_outputs: bool = True
    secrets_hygiene_max_files: int = 150000
    secrets_hygiene_max_file_mb: int = 20
    secrets_hygiene_entropy_threshold: float = 4.2
    secrets_hygiene_mask_keep_start: int = 4
    secrets_hygiene_mask_keep_end: int = 4
    secrets_hygiene_save_reports: bool = True
    secrets_hygiene_min_quality_score: float = 0.40



    # Master Orchestration Settings
    master_orchestration_enabled: bool = True
    default_master_orchestration_profile: str = "balanced_offline_master"
    master_orchestration_default_language: str = "tr"
    master_orchestration_dry_run_default: bool = True
    master_orchestration_allow_execute: bool = False
    master_orchestration_allow_live_commands: bool = False
    master_orchestration_allow_broker_commands: bool = False
    master_orchestration_allow_deploy_commands: bool = False
    master_orchestration_allow_background_daemons: bool = False
    master_orchestration_allow_real_market_download: bool = False
    master_orchestration_allow_external_llm: bool = False
    master_orchestration_generate_layer_map: bool = True
    master_orchestration_generate_dependency_graphs: bool = True
    master_orchestration_generate_master_plan: bool = True
    master_orchestration_generate_playbook: bool = True
    master_orchestration_generate_handoff_checklists: bool = True
    master_orchestration_generate_phase_consolidation: bool = True
    master_orchestration_max_commands_per_plan: int = 200
    master_orchestration_min_quality_score: float = 0.40
    master_orchestration_save_reports: bool = True
    """
    Application settings loaded from environment variables with defaults.
    """

    app_name: str = "commodity_fx_signal_bot"

    # Report Summarization Settings
    report_summarization_enabled: bool = True
    default_report_summary_profile: str = "balanced_local_summaries"
    report_summary_default_language: str = "tr"
    report_summary_use_local_only: bool = True
    report_summary_allow_external_llm: bool = False
    report_summary_allow_live_commands: bool = False
    report_summary_allow_broker_commands: bool = False
    report_summary_allow_deploy_commands: bool = False
    report_summary_allow_background_daemons: bool = False
    report_summary_allow_real_market_download: bool = False
    report_summary_scan_reports_output: bool = True
    report_summary_scan_data_lake: bool = True
    report_summary_scan_docs: bool = True
    report_summary_max_reports: int = 5000
    report_summary_max_chars_per_report: int = 20000
    report_summary_max_summary_bullets: int = 12
    report_summary_max_findings: int = 100
    report_summary_max_warnings: int = 100
    report_summary_max_follow_up_tasks: int = 50
    report_summary_save_reports: bool = True
    report_summary_min_quality_score: float = 0.40

    environment: str = field(
        default_factory=lambda: os.getenv("APP_ENV", "development")
    )
    log_level: str = field(default_factory=lambda: os.getenv("LOG_LEVEL", "INFO"))
    base_currency: str = field(
        default_factory=lambda: os.getenv("BASE_CURRENCY", "TRY")
    )


    # Scenarios settings
    scenarios_enabled: bool = field(default_factory=lambda: os.getenv("SCENARIOS_ENABLED", "true").lower() == "true")
    default_scenario_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_SCENARIO_PROFILE", "balanced_offline_scenarios"))
    scenario_default_timeframe: str = field(default_factory=lambda: os.getenv("SCENARIO_DEFAULT_TIMEFRAME", "1d"))
    scenario_use_synthetic_data_only: bool = field(default_factory=lambda: os.getenv("SCENARIO_USE_SYNTHETIC_DATA_ONLY", "true").lower() == "true")
    scenario_allow_real_market_download: bool = field(default_factory=lambda: os.getenv("SCENARIO_ALLOW_REAL_MARKET_DOWNLOAD", "false").lower() == "true")
    scenario_allow_live_commands: bool = field(default_factory=lambda: os.getenv("SCENARIO_ALLOW_LIVE_COMMANDS", "false").lower() == "true")
    scenario_allow_broker_commands: bool = field(default_factory=lambda: os.getenv("SCENARIO_ALLOW_BROKER_COMMANDS", "false").lower() == "true")
    scenario_allow_deploy_commands: bool = field(default_factory=lambda: os.getenv("SCENARIO_ALLOW_DEPLOY_COMMANDS", "false").lower() == "true")
    scenario_allow_background_daemons: bool = field(default_factory=lambda: os.getenv("SCENARIO_ALLOW_BACKGROUND_DAEMONS", "false").lower() == "true")
    scenario_generate_sample_data: bool = field(default_factory=lambda: os.getenv("SCENARIO_GENERATE_SAMPLE_DATA", "true").lower() == "true")
    scenario_generate_fixtures: bool = field(default_factory=lambda: os.getenv("SCENARIO_GENERATE_FIXTURES", "true").lower() == "true")
    scenario_generate_expected_outputs: bool = field(default_factory=lambda: os.getenv("SCENARIO_GENERATE_EXPECTED_OUTPUTS", "true").lower() == "true")
    scenario_run_dry_run_validation: bool = field(default_factory=lambda: os.getenv("SCENARIO_RUN_DRY_RUN_VALIDATION", "true").lower() == "true")
    scenario_max_symbols: int = field(default_factory=lambda: int(os.getenv("SCENARIO_MAX_SYMBOLS", "20")))
    scenario_max_rows_per_symbol: int = field(default_factory=lambda: int(os.getenv("SCENARIO_MAX_ROWS_PER_SYMBOL", "500")))
    scenario_random_seed: int = field(default_factory=lambda: int(os.getenv("SCENARIO_RANDOM_SEED", "42")))
    scenario_save_reports: bool = field(default_factory=lambda: os.getenv("SCENARIO_SAVE_REPORTS", "true").lower() == "true")
    scenario_min_quality_score: float = field(default_factory=lambda: float(os.getenv("SCENARIO_MIN_QUALITY_SCORE", "0.40")))

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
    data_lake_enabled: bool = field(default_factory=lambda: os.getenv("DATA_LAKE_ENABLED", "true").lower() == "true")

    # Documentation Pack
    documentation_pack_enabled: bool = field(default_factory=lambda: str(os.getenv("DOCUMENTATION_PACK_ENABLED", "true")).lower() == "true")
    default_documentation_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_DOCUMENTATION_PROFILE", "balanced_documentation_pack"))
    documentation_default_language: str = field(default_factory=lambda: os.getenv("DOCUMENTATION_DEFAULT_LANGUAGE", "tr"))
    documentation_generate_user_guide: bool = field(default_factory=lambda: str(os.getenv("DOCUMENTATION_GENERATE_USER_GUIDE", "true")).lower() == "true")
    documentation_generate_operator_manual: bool = field(default_factory=lambda: str(os.getenv("DOCUMENTATION_GENERATE_OPERATOR_MANUAL", "true")).lower() == "true")
    documentation_generate_analyst_handbook: bool = field(default_factory=lambda: str(os.getenv("DOCUMENTATION_GENERATE_ANALYST_HANDBOOK", "true")).lower() == "true")
    documentation_generate_developer_guide: bool = field(default_factory=lambda: str(os.getenv("DOCUMENTATION_GENERATE_DEVELOPER_GUIDE", "true")).lower() == "true")
    documentation_generate_codex_agent_guide: bool = field(default_factory=lambda: str(os.getenv("DOCUMENTATION_GENERATE_CODEX_AGENT_GUIDE", "true")).lower() == "true")
    documentation_generate_safe_usage_guide: bool = field(default_factory=lambda: str(os.getenv("DOCUMENTATION_GENERATE_SAFE_USAGE_GUIDE", "true")).lower() == "true")
    documentation_generate_troubleshooting: bool = field(default_factory=lambda: str(os.getenv("DOCUMENTATION_GENERATE_TROUBLESHOOTING", "true")).lower() == "true")
    documentation_generate_references: bool = field(default_factory=lambda: str(os.getenv("DOCUMENTATION_GENERATE_REFERENCES", "true")).lower() == "true")
    documentation_check_internal_links: bool = field(default_factory=lambda: str(os.getenv("DOCUMENTATION_CHECK_INTERNAL_LINKS", "true")).lower() == "true")
    documentation_check_safety_language: bool = field(default_factory=lambda: str(os.getenv("DOCUMENTATION_CHECK_SAFETY_LANGUAGE", "true")).lower() == "true")
    documentation_check_consistency: bool = field(default_factory=lambda: str(os.getenv("DOCUMENTATION_CHECK_CONSISTENCY", "true")).lower() == "true")
    documentation_require_disclaimers: bool = field(default_factory=lambda: str(os.getenv("DOCUMENTATION_REQUIRE_DISCLAIMERS", "true")).lower() == "true")
    documentation_require_no_investment_advice: bool = field(default_factory=lambda: str(os.getenv("DOCUMENTATION_REQUIRE_NO_INVESTMENT_ADVICE", "true")).lower() == "true")
    documentation_require_no_live_trading_language: bool = field(default_factory=lambda: str(os.getenv("DOCUMENTATION_REQUIRE_NO_LIVE_TRADING_LANGUAGE", "true")).lower() == "true")
    documentation_save_reports: bool = field(default_factory=lambda: str(os.getenv("DOCUMENTATION_SAVE_REPORTS", "true")).lower() == "true")
    documentation_min_quality_score: float = field(default_factory=lambda: float(os.getenv("DOCUMENTATION_MIN_QUALITY_SCORE", "0.40")))

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
        default_factory=lambda: os.getenv("REGIME_FEATURES_ENABLED", "true").lower()
        == "true"
    )
    regime_events_enabled: bool = field(
        default_factory=lambda: os.getenv("REGIME_EVENTS_ENABLED", "true").lower()
        == "true"
    )
    default_regime_profile: str = field(
        default_factory=lambda: os.getenv("DEFAULT_REGIME_PROFILE", "balanced_regime")
    )
    default_regime_timeframe: str = field(
        default_factory=lambda: os.getenv("DEFAULT_REGIME_TIMEFRAME", "1d")
    )
    default_regime_feature_sets: tuple[str, ...] = field(
        default_factory=lambda: tuple(
            os.getenv(
                "DEFAULT_REGIME_FEATURE_SETS",
                "trend,momentum,volatility,mean_reversion,price_action,mtf",
            ).split(",")
        )
    )
    default_adx_trend_threshold: float = field(
        default_factory=lambda: float(os.getenv("DEFAULT_ADX_TREND_THRESHOLD", "25.0"))
    )
    default_strong_trend_threshold: float = field(
        default_factory=lambda: float(
            os.getenv("DEFAULT_STRONG_TREND_THRESHOLD", "35.0")
        )
    )
    default_low_volatility_percentile: float = field(
        default_factory=lambda: float(
            os.getenv("DEFAULT_LOW_VOLATILITY_PERCENTILE", "0.20")
        )
    )
    default_high_volatility_percentile: float = field(
        default_factory=lambda: float(
            os.getenv("DEFAULT_HIGH_VOLATILITY_PERCENTILE", "0.80")
        )
    )
    default_range_adx_threshold: float = field(
        default_factory=lambda: float(os.getenv("DEFAULT_RANGE_ADX_THRESHOLD", "20.0"))
    )
    default_regime_transition_lookback: int = field(
        default_factory=lambda: int(
            os.getenv("DEFAULT_REGIME_TRANSITION_LOOKBACK", "5")
        )
    )
    save_regime_features: bool = field(
        default_factory=lambda: os.getenv("SAVE_REGIME_FEATURES", "true").lower()
        == "true"
    )
    save_regime_events: bool = field(
        default_factory=lambda: os.getenv("SAVE_REGIME_EVENTS", "true").lower()
        == "true"
    )

    # Phase 17: Macro Regime Layer Settings
    macro_features_enabled: bool = field(
        default_factory=lambda: os.getenv("MACRO_FEATURES_ENABLED", "true").lower()
        == "true"
    )
    macro_events_enabled: bool = field(
        default_factory=lambda: os.getenv("MACRO_EVENTS_ENABLED", "true").lower()
        == "true"
    )
    macro_data_enabled: bool = field(
        default_factory=lambda: os.getenv("MACRO_DATA_ENABLED", "true").lower()
        == "true"
    )
    default_macro_frequency: str = field(
        default_factory=lambda: os.getenv("DEFAULT_MACRO_FREQUENCY", "monthly")
    )
    default_macro_start_date: str = field(
        default_factory=lambda: os.getenv("DEFAULT_MACRO_START_DATE", "2010-01-01")
    )
    default_macro_base_currency: str = field(
        default_factory=lambda: os.getenv("DEFAULT_MACRO_BASE_CURRENCY", "TRY")
    )
    use_evds_for_turkey_macro: bool = field(
        default_factory=lambda: os.getenv("USE_EVDS_FOR_TURKEY_MACRO", "true").lower()
        == "true"
    )
    use_fred_for_us_macro: bool = field(
        default_factory=lambda: os.getenv("USE_FRED_FOR_US_MACRO", "true").lower()
        == "true"
    )
    macro_forward_fill_to_daily: bool = field(
        default_factory=lambda: os.getenv("MACRO_FORWARD_FILL_TO_DAILY", "true").lower()
        == "true"
    )
    macro_max_staleness_days: int = field(
        default_factory=lambda: int(os.getenv("MACRO_MAX_STALENESS_DAYS", "45"))
    )
    benchmark_features_enabled: bool = field(
        default_factory=lambda: os.getenv("BENCHMARK_FEATURES_ENABLED", "true").lower()
        == "true"
    )
    save_macro_features: bool = field(
        default_factory=lambda: os.getenv("SAVE_MACRO_FEATURES", "true").lower()
        == "true"
    )
    save_macro_events: bool = field(
        default_factory=lambda: os.getenv("SAVE_MACRO_EVENTS", "true").lower() == "true"
    )
    save_benchmark_features: bool = field(
        default_factory=lambda: os.getenv("SAVE_BENCHMARK_FEATURES", "true").lower()
        == "true"
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

    # Phase 18: Asset Profiles and Group Features
    asset_profiles_enabled: bool = field(
        default_factory=lambda: os.getenv("ASSET_PROFILES_ENABLED", "true").lower()
        == "true"
    )
    asset_profile_events_enabled: bool = field(
        default_factory=lambda: os.getenv(
            "ASSET_PROFILE_EVENTS_ENABLED", "true"
        ).lower()
        == "true"
    )
    default_asset_profile_timeframe: str = field(
        default_factory=lambda: os.getenv("DEFAULT_ASSET_PROFILE_TIMEFRAME", "1d")
    )
    default_asset_profile_lookback: int = field(
        default_factory=lambda: int(os.getenv("DEFAULT_ASSET_PROFILE_LOOKBACK", "252"))
    )
    default_group_correlation_window: int = field(
        default_factory=lambda: int(os.getenv("DEFAULT_GROUP_CORRELATION_WINDOW", "90"))
    )
    # Using string for parsing tuple because tuple env parsing is tricky
    default_relative_strength_windows: tuple[int, ...] = (21, 63, 126, 252)
    default_dispersion_window: int = field(
        default_factory=lambda: int(os.getenv("DEFAULT_DISPERSION_WINDOW", "63"))
    )
    default_group_momentum_window: int = field(
        default_factory=lambda: int(os.getenv("DEFAULT_GROUP_MOMENTUM_WINDOW", "63"))
    )
    default_group_volatility_window: int = field(
        default_factory=lambda: int(os.getenv("DEFAULT_GROUP_VOLATILITY_WINDOW", "63"))
    )
    min_group_members_for_group_features: int = field(
        default_factory=lambda: int(
            os.getenv("MIN_GROUP_MEMBERS_FOR_GROUP_FEATURES", "3")
        )
    )
    save_asset_profile_features: bool = field(
        default_factory=lambda: os.getenv("SAVE_ASSET_PROFILE_FEATURES", "true").lower()
        == "true"
    )
    save_asset_profile_events: bool = field(
        default_factory=lambda: os.getenv("SAVE_ASSET_PROFILE_EVENTS", "true").lower()
        == "true"
    )
    save_group_features: bool = field(
        default_factory=lambda: os.getenv("SAVE_GROUP_FEATURES", "true").lower()
        == "true"
    )

    # Phase 19: Signal Candidates and Scoring
    signal_candidates_enabled: bool = field(
        default_factory=lambda: os.getenv("SIGNAL_CANDIDATES_ENABLED", "true").lower()
        == "true"
    )
    signal_scoring_enabled: bool = field(
        default_factory=lambda: os.getenv("SIGNAL_SCORING_ENABLED", "true").lower()
        == "true"
    )
    default_signal_profile: str = field(
        default_factory=lambda: os.getenv(
            "DEFAULT_SIGNAL_PROFILE", "balanced_candidate_scoring"
        )
    )
    default_signal_timeframe: str = field(
        default_factory=lambda: os.getenv("DEFAULT_SIGNAL_TIMEFRAME", "1d")
    )
    signal_min_candidate_score: float = field(
        default_factory=lambda: float(os.getenv("SIGNAL_MIN_CANDIDATE_SCORE", "0.40"))
    )
    signal_min_quality_score: float = field(
        default_factory=lambda: float(os.getenv("SIGNAL_MIN_QUALITY_SCORE", "0.50"))
    )
    signal_min_context_score: float = field(
        default_factory=lambda: float(os.getenv("SIGNAL_MIN_CONTEXT_SCORE", "0.40"))
    )
    signal_max_conflict_score: float = field(
        default_factory=lambda: float(os.getenv("SIGNAL_MAX_CONFLICT_SCORE", "0.70"))
    )
    signal_event_lookback_bars: int = field(
        default_factory=lambda: int(os.getenv("SIGNAL_EVENT_LOOKBACK_BARS", "5"))
    )
    signal_decay_half_life_bars: int = field(
        default_factory=lambda: int(os.getenv("SIGNAL_DECAY_HALF_LIFE_BARS", "3"))
    )
    signal_use_regime_filter: bool = field(
        default_factory=lambda: os.getenv("SIGNAL_USE_REGIME_FILTER", "true").lower()
        == "true"
    )
    signal_use_mtf_filter: bool = field(
        default_factory=lambda: os.getenv("SIGNAL_USE_MTF_FILTER", "true").lower()
        == "true"
    )
    signal_use_macro_filter: bool = field(
        default_factory=lambda: os.getenv("SIGNAL_USE_MACRO_FILTER", "true").lower()
        == "true"
    )
    signal_use_asset_profile_filter: bool = field(
        default_factory=lambda: os.getenv(
            "SIGNAL_USE_ASSET_PROFILE_FILTER", "true"
        ).lower()
        == "true"
    )
    save_signal_candidates: bool = field(
        default_factory=lambda: os.getenv("SAVE_SIGNAL_CANDIDATES", "true").lower()
        == "true"
    )
    save_signal_pool: bool = field(
        default_factory=lambda: os.getenv("SAVE_SIGNAL_POOL", "true").lower() == "true"
    )
    # Decision Candidate Settings
    decision_candidates_enabled: bool = field(
        default_factory=lambda: os.getenv("DECISION_CANDIDATES_ENABLED", "true").lower()
        == "true"
    )
    directional_decision_enabled: bool = field(
        default_factory=lambda: os.getenv(
            "DIRECTIONAL_DECISION_ENABLED", "true"
        ).lower()
        == "true"
    )
    default_decision_profile: str = field(
        default_factory=lambda: os.getenv(
            "DEFAULT_DECISION_PROFILE", "balanced_directional_decision"
        )
    )
    default_decision_timeframe: str = field(
        default_factory=lambda: os.getenv("DEFAULT_DECISION_TIMEFRAME", "1d")
    )
    decision_min_signal_score: float = field(
        default_factory=lambda: float(os.getenv("DECISION_MIN_SIGNAL_SCORE", "0.45"))
    )
    decision_min_confidence: float = field(
        default_factory=lambda: float(os.getenv("DECISION_MIN_CONFIDENCE", "0.50"))
    )
    decision_min_quality: float = field(
        default_factory=lambda: float(os.getenv("DECISION_MIN_QUALITY", "0.50"))
    )
    decision_max_conflict: float = field(
        default_factory=lambda: float(os.getenv("DECISION_MAX_CONFLICT", "0.65"))
    )
    decision_min_strategy_readiness: float = field(
        default_factory=lambda: float(
            os.getenv("DECISION_MIN_STRATEGY_READINESS", "0.45")
        )
    )
    decision_neutral_zone_threshold: float = field(
        default_factory=lambda: float(
            os.getenv("DECISION_NEUTRAL_ZONE_THRESHOLD", "0.15")
        )
    )
    decision_require_regime_confirmation: bool = field(
        default_factory=lambda: os.getenv(
            "DECISION_REQUIRE_REGIME_CONFIRMATION", "true"
        ).lower()
        == "true"
    )
    decision_require_mtf_confirmation: bool = field(
        default_factory=lambda: os.getenv(
            "DECISION_REQUIRE_MTF_CONFIRMATION", "true"
        ).lower()
        == "true"
    )
    decision_allow_macro_override: bool = field(
        default_factory=lambda: os.getenv(
            "DECISION_ALLOW_MACRO_OVERRIDE", "false"
        ).lower()
        == "true"
    )
    save_decision_candidates: bool = field(
        default_factory=lambda: os.getenv("SAVE_DECISION_CANDIDATES", "true").lower()
        == "true"
    )
    save_decision_pool: bool = field(
        default_factory=lambda: os.getenv("SAVE_DECISION_POOL", "true").lower()
        == "true"
    )

    # Phase 21: Strategy Engine Skeleton
    strategy_candidates_enabled: bool = field(
        default_factory=lambda: os.getenv("STRATEGY_CANDIDATES_ENABLED", "true").lower()
        == "true"
    )
    strategy_selection_enabled: bool = field(
        default_factory=lambda: os.getenv("STRATEGY_SELECTION_ENABLED", "true").lower()
        == "true"
    )
    default_strategy_profile: str = field(
        default_factory=lambda: os.getenv(
            "DEFAULT_STRATEGY_PROFILE", "balanced_strategy_selection"
        )
    )
    default_strategy_timeframe: str = field(
        default_factory=lambda: os.getenv("DEFAULT_STRATEGY_TIMEFRAME", "1d")
    )
    strategy_min_selection_score: float = field(
        default_factory=lambda: float(os.getenv("STRATEGY_MIN_SELECTION_SCORE", "0.45"))
    )
    strategy_min_fit_score: float = field(
        default_factory=lambda: float(os.getenv("STRATEGY_MIN_FIT_SCORE", "0.45"))
    )
    strategy_min_decision_confidence: float = field(
        default_factory=lambda: float(
            os.getenv("STRATEGY_MIN_DECISION_CONFIDENCE", "0.50")
        )
    )
    strategy_min_decision_quality: float = field(
        default_factory=lambda: float(
            os.getenv("STRATEGY_MIN_DECISION_QUALITY", "0.50")
        )
    )
    strategy_max_conflict_score: float = field(
        default_factory=lambda: float(os.getenv("STRATEGY_MAX_CONFLICT_SCORE", "0.65"))
    )
    strategy_allow_no_trade_family: bool = field(
        default_factory=lambda: os.getenv(
            "STRATEGY_ALLOW_NO_TRADE_FAMILY", "true"
        ).lower()
        == "true"
    )
    strategy_allow_watchlist_family: bool = field(
        default_factory=lambda: os.getenv(
            "STRATEGY_ALLOW_WATCHLIST_FAMILY", "true"
        ).lower()
        == "true"
    )
    save_strategy_candidates: bool = field(
        default_factory=lambda: os.getenv("SAVE_STRATEGY_CANDIDATES", "true").lower()
        == "true"
    )
    save_strategy_pool: bool = field(
        default_factory=lambda: os.getenv("SAVE_STRATEGY_POOL", "true").lower()
        == "true"
    )
    # Phase 22: Strategy Rule Settings
    strategy_rules_enabled: bool = field(
        default_factory=lambda: os.getenv("STRATEGY_RULES_ENABLED", "true").lower()
        == "true"
    )
    strategy_rule_engine_enabled: bool = field(
        default_factory=lambda: os.getenv(
            "STRATEGY_RULE_ENGINE_ENABLED", "true"
        ).lower()
        == "true"
    )
    default_strategy_rule_profile: str = field(
        default_factory=lambda: os.getenv(
            "DEFAULT_STRATEGY_RULE_PROFILE", "balanced_rule_evaluation"
        )
    )
    default_strategy_rule_timeframe: str = field(
        default_factory=lambda: os.getenv("DEFAULT_STRATEGY_RULE_TIMEFRAME", "1d")
    )
    rule_min_match_score: float = field(
        default_factory=lambda: float(os.getenv("RULE_MIN_MATCH_SCORE", "0.45"))
    )
    rule_min_confidence: float = field(
        default_factory=lambda: float(os.getenv("RULE_MIN_CONFIDENCE", "0.50"))
    )
    rule_min_quality_score: float = field(
        default_factory=lambda: float(os.getenv("RULE_MIN_QUALITY_SCORE", "0.50"))
    )
    rule_max_conflict_score: float = field(
        default_factory=lambda: float(os.getenv("RULE_MAX_CONFLICT_SCORE", "0.65"))
    )
    rule_min_readiness_score: float = field(
        default_factory=lambda: float(os.getenv("RULE_MIN_READINESS_SCORE", "0.45"))
    )
    rule_require_strategy_candidate_passed: bool = field(
        default_factory=lambda: os.getenv(
            "RULE_REQUIRE_STRATEGY_CANDIDATE_PASSED", "true"
        ).lower()
        == "true"
    )
    rule_require_decision_candidate_passed: bool = field(
        default_factory=lambda: os.getenv(
            "RULE_REQUIRE_DECISION_CANDIDATE_PASSED", "false"
        ).lower()
        == "true"
    )
    rule_allow_wait_candidates: bool = field(
        default_factory=lambda: os.getenv("RULE_ALLOW_WAIT_CANDIDATES", "true").lower()
        == "true"
    )
    rule_allow_invalidation_candidates: bool = field(
        default_factory=lambda: os.getenv(
            "RULE_ALLOW_INVALIDATION_CANDIDATES", "true"
        ).lower()
        == "true"
    )
    save_strategy_rule_candidates: bool = field(
        default_factory=lambda: os.getenv(
            "SAVE_STRATEGY_RULE_CANDIDATES", "true"
        ).lower()
        == "true"
    )
    save_entry_exit_candidates: bool = field(
        default_factory=lambda: os.getenv("SAVE_ENTRY_EXIT_CANDIDATES", "true").lower()
        == "true"
    )
    save_strategy_rule_pool: bool = field(
        default_factory=lambda: os.getenv("SAVE_STRATEGY_RULE_POOL", "true").lower()
        == "true"
    )

    # Phase 27: Performance and Benchmark
    performance_analysis_enabled: bool = field(
        default_factory=lambda: str(
            os.getenv("PERFORMANCE_ANALYSIS_ENABLED", "true")
        ).lower()
        == "true"
    )
    benchmark_comparison_enabled: bool = field(
        default_factory=lambda: str(
            os.getenv("BENCHMARK_COMPARISON_ENABLED", "true")
        ).lower()
        == "true"
    )
    inflation_adjusted_performance_enabled: bool = field(
        default_factory=lambda: str(
            os.getenv("INFLATION_ADJUSTED_PERFORMANCE_ENABLED", "true")
        ).lower()
        == "true"
    )
    default_performance_profile: str = field(
        default_factory=lambda: os.getenv(
            "DEFAULT_PERFORMANCE_PROFILE", "balanced_performance_analysis"
        )
    )
    default_performance_timeframe: str = field(
        default_factory=lambda: os.getenv("DEFAULT_PERFORMANCE_TIMEFRAME", "1d")
    )
    performance_risk_free_rate_annual: float = field(
        default_factory=lambda: float(
            os.getenv("PERFORMANCE_RISK_FREE_RATE_ANNUAL", "0.0")
        )
    )
    performance_trading_days_per_year: int = field(
        default_factory=lambda: int(
            os.getenv("PERFORMANCE_TRADING_DAYS_PER_YEAR", "252")
        )
    )
    performance_rolling_windows: tuple[int, ...] = field(
        default_factory=lambda: tuple(
            int(x)
            for x in os.getenv("PERFORMANCE_ROLLING_WINDOWS", "20,60,120,252").split(
                ","
            )
        )
    )
    performance_min_trades_for_summary: int = field(
        default_factory=lambda: int(
            os.getenv("PERFORMANCE_MIN_TRADES_FOR_SUMMARY", "5")
        )
    )
    performance_min_observations_for_rolling: int = field(
        default_factory=lambda: int(
            os.getenv("PERFORMANCE_MIN_OBSERVATIONS_FOR_ROLLING", "30")
        )
    )
    performance_compare_to_tr_inflation: bool = field(
        default_factory=lambda: str(
            os.getenv("PERFORMANCE_COMPARE_TO_TR_INFLATION", "true")
        ).lower()
        == "true"
    )
    performance_compare_to_us_cpi: bool = field(
        default_factory=lambda: str(
            os.getenv("PERFORMANCE_COMPARE_TO_US_CPI", "true")
        ).lower()
        == "true"
    )
    performance_compare_to_usdtry: bool = field(
        default_factory=lambda: str(
            os.getenv("PERFORMANCE_COMPARE_TO_USDTRY", "true")
        ).lower()
        == "true"
    )
    performance_compare_to_gold: bool = field(
        default_factory=lambda: str(
            os.getenv("PERFORMANCE_COMPARE_TO_GOLD", "true")
        ).lower()
        == "true"
    )
    performance_compare_to_commodity_basket: bool = field(
        default_factory=lambda: str(
            os.getenv("PERFORMANCE_COMPARE_TO_COMMODITY_BASKET", "true")
        ).lower()
        == "true"
    )
    save_performance_reports: bool = field(
        default_factory=lambda: str(
            os.getenv("SAVE_PERFORMANCE_REPORTS", "true")
        ).lower()
        == "true"
    )
    save_benchmark_comparisons: bool = field(
        default_factory=lambda: str(
            os.getenv("SAVE_BENCHMARK_COMPARISONS", "true")
        ).lower()
        == "true"
    )
    save_performance_tables: bool = field(
        default_factory=lambda: str(
            os.getenv("SAVE_PERFORMANCE_TABLES", "true")
        ).lower()
        == "true"
    )


    # Phase 29: ML Dataset Preparation
    ml_dataset_enabled: bool = field(
        default_factory=lambda: str(os.getenv("ML_DATASET_ENABLED", "true")).lower()
        == "true"
    )
    ml_target_engineering_enabled: bool = field(
        default_factory=lambda: str(
            os.getenv("ML_TARGET_ENGINEERING_ENABLED", "true")
        ).lower()
        == "true"
    )
    default_ml_dataset_profile: str = field(
        default_factory=lambda: os.getenv(
            "DEFAULT_ML_DATASET_PROFILE", "balanced_supervised_dataset"
        )
    )
    default_ml_dataset_timeframe: str = field(
        default_factory=lambda: os.getenv("DEFAULT_ML_DATASET_TIMEFRAME", "1d")
    )
    ml_default_forward_return_horizons: tuple[int, ...] = field(
        default_factory=lambda: tuple(
            int(x.strip())
            for x in os.getenv("ML_DEFAULT_FORWARD_RETURN_HORIZONS", "1,3,5,10,20").split(",")
            if x.strip()
        )
    )
    ml_default_forward_volatility_horizons: tuple[int, ...] = field(
        default_factory=lambda: tuple(
            int(x.strip())
            for x in os.getenv("ML_DEFAULT_FORWARD_VOLATILITY_HORIZONS", "5,10,20").split(",")
            if x.strip()
        )
    )
    ml_default_future_drawdown_horizons: tuple[int, ...] = field(
        default_factory=lambda: tuple(
            int(x.strip())
            for x in os.getenv("ML_DEFAULT_FUTURE_DRAWDOWN_HORIZONS", "5,10,20").split(",")
            if x.strip()
        )
    )
    ml_direction_threshold: float = field(
        default_factory=lambda: float(os.getenv("ML_DIRECTION_THRESHOLD", "0.002"))
    )
    ml_positive_return_threshold: float = field(
        default_factory=lambda: float(os.getenv("ML_POSITIVE_RETURN_THRESHOLD", "0.005"))
    )
    ml_negative_return_threshold: float = field(
        default_factory=lambda: float(os.getenv("ML_NEGATIVE_RETURN_THRESHOLD", "-0.005"))
    )
    ml_min_rows_for_dataset: int = field(
        default_factory=lambda: int(os.getenv("ML_MIN_ROWS_FOR_DATASET", "200"))
    )
    ml_max_feature_nan_ratio: float = field(
        default_factory=lambda: float(os.getenv("ML_MAX_FEATURE_NAN_RATIO", "0.35"))
    )
    ml_max_target_nan_ratio: float = field(
        default_factory=lambda: float(os.getenv("ML_MAX_TARGET_NAN_RATIO", "0.20"))
    )
    ml_use_purged_split: bool = field(
        default_factory=lambda: str(os.getenv("ML_USE_PURGED_SPLIT", "true")).lower()
        == "true"
    )
    ml_embargo_bars: int = field(
        default_factory=lambda: int(os.getenv("ML_EMBARGO_BARS", "5"))
    )
    ml_test_size_ratio: float = field(
        default_factory=lambda: float(os.getenv("ML_TEST_SIZE_RATIO", "0.20"))
    )
    ml_validation_size_ratio: float = field(
        default_factory=lambda: float(os.getenv("ML_VALIDATION_SIZE_RATIO", "0.20"))
    )
    ml_save_feature_matrix: bool = field(
        default_factory=lambda: str(os.getenv("ML_SAVE_FEATURE_MATRIX", "true")).lower()
        == "true"
    )
    ml_save_target_frame: bool = field(
        default_factory=lambda: str(os.getenv("ML_SAVE_TARGET_FRAME", "true")).lower()
        == "true"
    )
    ml_save_supervised_dataset: bool = field(
        default_factory=lambda: str(
            os.getenv("ML_SAVE_SUPERVISED_DATASET", "true")
        ).lower()
        == "true"
    )

    # Phase 30: ML Training Baseline
    ml_training_enabled: bool = field(
        default_factory=lambda: str(os.getenv("ML_TRAINING_ENABLED", "true")).lower() == "true"
    )
    ml_baseline_models_enabled: bool = field(
        default_factory=lambda: str(os.getenv("ML_BASELINE_MODELS_ENABLED", "true")).lower() == "true"
    )
    ml_model_registry_enabled: bool = field(
        default_factory=lambda: str(os.getenv("ML_MODEL_REGISTRY_ENABLED", "true")).lower() == "true"
    )
    default_ml_training_profile: str = field(
        default_factory=lambda: os.getenv("DEFAULT_ML_TRAINING_PROFILE", "balanced_baseline_training")
    )
    default_ml_training_timeframe: str = field(
        default_factory=lambda: os.getenv("DEFAULT_ML_TRAINING_TIMEFRAME", "1d")
    )
    default_ml_training_dataset_profile: str = field(
        default_factory=lambda: os.getenv("DEFAULT_ML_TRAINING_DATASET_PROFILE", "balanced_supervised_dataset")
    )
    default_ml_target_column: str = field(
        default_factory=lambda: os.getenv("DEFAULT_ML_TARGET_COLUMN", "target_direction_class_5")
    )
    ml_training_task_type: str = field(
        default_factory=lambda: os.getenv("ML_TRAINING_TASK_TYPE", "classification")
    )
    ml_allowed_model_families: tuple = field(
        default_factory=lambda: tuple(os.getenv("ML_ALLOWED_MODEL_FAMILIES", "dummy,logistic_regression,random_forest,hist_gradient_boosting").split(","))
    )
    ml_default_model_family: str = field(
        default_factory=lambda: os.getenv("ML_DEFAULT_MODEL_FAMILY", "random_forest")
    )
    ml_cv_n_splits: int = field(
        default_factory=lambda: int(os.getenv("ML_CV_N_SPLITS", "5"))
    )
    ml_cv_embargo_bars: int = field(
        default_factory=lambda: int(os.getenv("ML_CV_EMBARGO_BARS", "5"))
    )
    ml_min_train_rows: int = field(
        default_factory=lambda: int(os.getenv("ML_MIN_TRAIN_ROWS", "300"))
    )
    ml_min_test_rows: int = field(
        default_factory=lambda: int(os.getenv("ML_MIN_TEST_ROWS", "50"))
    )
    ml_max_feature_nan_ratio_for_training: float = field(
        default_factory=lambda: float(os.getenv("ML_MAX_FEATURE_NAN_RATIO_FOR_TRAINING", "0.35"))
    )
    ml_drop_high_nan_features: bool = field(
        default_factory=lambda: str(os.getenv("ML_DROP_HIGH_NAN_FEATURES", "true")).lower() == "true"
    )
    ml_enable_basic_imputation: bool = field(
        default_factory=lambda: str(os.getenv("ML_ENABLE_BASIC_IMPUTATION", "true")).lower() == "true"
    )
    ml_enable_basic_scaling: bool = field(
        default_factory=lambda: str(os.getenv("ML_ENABLE_BASIC_SCALING", "true")).lower() == "true"
    )
    ml_save_model_artifacts: bool = field(
        default_factory=lambda: str(os.getenv("ML_SAVE_MODEL_ARTIFACTS", "true")).lower() == "true"
    )
    ml_save_model_registry_entries: bool = field(
        default_factory=lambda: str(os.getenv("ML_SAVE_MODEL_REGISTRY_ENTRIES", "true")).lower() == "true"
    )
    ml_save_model_evaluation_reports: bool = field(
        default_factory=lambda: str(os.getenv("ML_SAVE_MODEL_EVALUATION_REPORTS", "true")).lower() == "true"
    )

    # Phase 32: ML Context Integration
    ml_context_integration_enabled: bool = field(
        default_factory=lambda: str(os.getenv("ML_CONTEXT_INTEGRATION_ENABLED", "true")).lower() == "true"
    )
    ml_model_aware_scoring_enabled: bool = field(
        default_factory=lambda: str(os.getenv("ML_MODEL_AWARE_SCORING_ENABLED", "true")).lower() == "true"
    )
    ml_conflict_filter_enabled: bool = field(
        default_factory=lambda: str(os.getenv("ML_CONFLICT_FILTER_ENABLED", "true")).lower() == "true"
    )
    ml_uncertainty_filter_enabled: bool = field(
        default_factory=lambda: str(os.getenv("ML_UNCERTAINTY_FILTER_ENABLED", "true")).lower() == "true"
    )
    default_ml_integration_profile: str = field(
        default_factory=lambda: os.getenv("DEFAULT_ML_INTEGRATION_PROFILE", "balanced_ml_context_integration")
    )
    default_ml_integration_timeframe: str = field(
        default_factory=lambda: os.getenv("DEFAULT_ML_INTEGRATION_TIMEFRAME", "1d")
    )
    ml_context_min_confidence_score: float = field(
        default_factory=lambda: float(os.getenv("ML_CONTEXT_MIN_CONFIDENCE_SCORE", "0.45"))
    )
    ml_context_max_uncertainty_score: float = field(
        default_factory=lambda: float(os.getenv("ML_CONTEXT_MAX_UNCERTAINTY_SCORE", "0.70"))
    )
    ml_context_max_leakage_risk_score: float = field(
        default_factory=lambda: float(os.getenv("ML_CONTEXT_MAX_LEAKAGE_RISK_SCORE", "0.20"))
    )
    ml_context_min_model_quality_score: float = field(
        default_factory=lambda: float(os.getenv("ML_CONTEXT_MIN_MODEL_QUALITY_SCORE", "0.50"))
    )
    ml_context_min_dataset_quality_score: float = field(
        default_factory=lambda: float(os.getenv("ML_CONTEXT_MIN_DATASET_QUALITY_SCORE", "0.50"))
    )
    ml_context_support_weight: float = field(
        default_factory=lambda: float(os.getenv("ML_CONTEXT_SUPPORT_WEIGHT", "0.10"))
    )
    ml_context_conflict_penalty_weight: float = field(
        default_factory=lambda: float(os.getenv("ML_CONTEXT_CONFLICT_PENALTY_WEIGHT", "0.10"))
    )
    ml_context_uncertainty_penalty_weight: float = field(
        default_factory=lambda: float(os.getenv("ML_CONTEXT_UNCERTAINTY_PENALTY_WEIGHT", "0.05"))
    )
    ml_context_enable_signal_scoring: bool = field(
        default_factory=lambda: str(os.getenv("ML_CONTEXT_ENABLE_SIGNAL_SCORING", "true")).lower() == "true"
    )
    ml_context_enable_decision_scoring: bool = field(
        default_factory=lambda: str(os.getenv("ML_CONTEXT_ENABLE_DECISION_SCORING", "true")).lower() == "true"
    )
    ml_context_enable_strategy_scoring: bool = field(
        default_factory=lambda: str(os.getenv("ML_CONTEXT_ENABLE_STRATEGY_SCORING", "true")).lower() == "true"
    )
    ml_context_enable_risk_precheck: bool = field(
        default_factory=lambda: str(os.getenv("ML_CONTEXT_ENABLE_RISK_PRECHECK", "false")).lower() == "true"
    )
    ml_context_save_integration_features: bool = field(
        default_factory=lambda: str(os.getenv("ML_CONTEXT_SAVE_INTEGRATION_FEATURES", "true")).lower() == "true"
    )
    ml_context_save_alignment_reports: bool = field(
        default_factory=lambda: str(os.getenv("ML_CONTEXT_SAVE_ALIGNMENT_REPORTS", "true")).lower() == "true"
    )



    # Phase 34: Notification Settings
    notifications_enabled: bool = field(
        default_factory=lambda: str(os.getenv("NOTIFICATIONS_ENABLED", "true")).lower() == "true"
    )
    telegram_enabled: bool = field(
        default_factory=lambda: str(os.getenv("TELEGRAM_ENABLED", "false")).lower() == "true"
    )
    telegram_dry_run: bool = field(
        default_factory=lambda: str(os.getenv("TELEGRAM_DRY_RUN", "true")).lower() == "true"
    )
    default_notification_profile: str = field(
        default_factory=lambda: os.getenv("DEFAULT_NOTIFICATION_PROFILE", "balanced_telegram_reporting")
    )
    telegram_bot_token: str | None = field(
        default_factory=lambda: os.getenv("TELEGRAM_BOT_TOKEN")
    )
    telegram_chat_id: str | None = field(
        default_factory=lambda: os.getenv("TELEGRAM_CHAT_ID")
    )
    telegram_parse_mode: str = field(
        default_factory=lambda: os.getenv("TELEGRAM_PARSE_MODE", "HTML")
    )
    telegram_disable_web_page_preview: bool = field(
        default_factory=lambda: str(os.getenv("TELEGRAM_DISABLE_WEB_PAGE_PREVIEW", "true")).lower() == "true"
    )
    telegram_message_max_chars: int = field(
        default_factory=lambda: int(os.getenv("TELEGRAM_MESSAGE_MAX_CHARS", "3500"))
    )
    telegram_rate_limit_seconds: float = field(
        default_factory=lambda: float(os.getenv("TELEGRAM_RATE_LIMIT_SECONDS", "1.0"))
    )
    telegram_send_test_on_startup: bool = field(
        default_factory=lambda: str(os.getenv("TELEGRAM_SEND_TEST_ON_STARTUP", "false")).lower() == "true"
    )
    notification_save_message_logs: bool = field(
        default_factory=lambda: str(os.getenv("NOTIFICATION_SAVE_MESSAGE_LOGS", "true")).lower() == "true"
    )
    notification_save_delivery_audit: bool = field(
        default_factory=lambda: str(os.getenv("NOTIFICATION_SAVE_DELIVERY_AUDIT", "true")).lower() == "true"
    )
    notification_include_paper_summary: bool = field(
        default_factory=lambda: str(os.getenv("NOTIFICATION_INCLUDE_PAPER_SUMMARY", "true")).lower() == "true"
    )
    notification_include_backtest_summary: bool = field(
        default_factory=lambda: str(os.getenv("NOTIFICATION_INCLUDE_BACKTEST_SUMMARY", "true")).lower() == "true"
    )
    notification_include_ml_summary: bool = field(
        default_factory=lambda: str(os.getenv("NOTIFICATION_INCLUDE_ML_SUMMARY", "true")).lower() == "true"
    )
    notification_include_quality_alerts: bool = field(
        default_factory=lambda: str(os.getenv("NOTIFICATION_INCLUDE_QUALITY_ALERTS", "true")).lower() == "true"
    )
    notification_include_error_alerts: bool = field(
        default_factory=lambda: str(os.getenv("NOTIFICATION_INCLUDE_ERROR_ALERTS", "true")).lower() == "true"
    )
    notification_max_symbols_in_digest: int = field(
        default_factory=lambda: int(os.getenv("NOTIFICATION_MAX_SYMBOLS_IN_DIGEST", "20"))
    )
    notification_max_rows_per_section: int = field(
        default_factory=lambda: int(os.getenv("NOTIFICATION_MAX_ROWS_PER_SECTION", "10"))
    )


    # Orchestration Settings
    orchestration_enabled: bool = field(
        default_factory=lambda: str(os.getenv("ORCHESTRATION_ENABLED", "true")).lower() == "true"
    )
    pipeline_orchestrator_enabled: bool = field(
        default_factory=lambda: str(os.getenv("PIPELINE_ORCHESTRATOR_ENABLED", "true")).lower() == "true"
    )
    default_orchestration_profile: str = field(
        default_factory=lambda: os.getenv("DEFAULT_ORCHESTRATION_PROFILE", "balanced_research_orchestration")
    )
    default_workflow_name: str = field(
        default_factory=lambda: os.getenv("DEFAULT_WORKFLOW_NAME", "daily_research_workflow")
    )
    orchestration_default_timeframe: str = field(
        default_factory=lambda: os.getenv("ORCHESTRATION_DEFAULT_TIMEFRAME", "1d")
    )
    orchestration_max_symbols_per_run: int = field(
        default_factory=lambda: int(os.getenv("ORCHESTRATION_MAX_SYMBOLS_PER_RUN", "50"))
    )
    orchestration_continue_on_symbol_error: bool = field(
        default_factory=lambda: str(os.getenv("ORCHESTRATION_CONTINUE_ON_SYMBOL_ERROR", "true")).lower() == "true"
    )
    orchestration_continue_on_job_error: bool = field(
        default_factory=lambda: str(os.getenv("ORCHESTRATION_CONTINUE_ON_JOB_ERROR", "true")).lower() == "true"
    )
    orchestration_retry_failed_jobs: bool = field(
        default_factory=lambda: str(os.getenv("ORCHESTRATION_RETRY_FAILED_JOBS", "false")).lower() == "true"
    )
    orchestration_max_retries: int = field(
        default_factory=lambda: int(os.getenv("ORCHESTRATION_MAX_RETRIES", "1"))
    )
    orchestration_retry_delay_seconds: float = field(
        default_factory=lambda: float(os.getenv("ORCHESTRATION_RETRY_DELAY_SECONDS", "2.0"))
    )
    orchestration_save_run_manifest: bool = field(
        default_factory=lambda: str(os.getenv("ORCHESTRATION_SAVE_RUN_MANIFEST", "true")).lower() == "true"
    )
    orchestration_save_dependency_graph: bool = field(
        default_factory=lambda: str(os.getenv("ORCHESTRATION_SAVE_DEPENDENCY_GRAPH", "true")).lower() == "true"
    )
    orchestration_save_execution_plan: bool = field(
        default_factory=lambda: str(os.getenv("ORCHESTRATION_SAVE_EXECUTION_PLAN", "true")).lower() == "true"
    )
    orchestration_save_job_logs: bool = field(
        default_factory=lambda: str(os.getenv("ORCHESTRATION_SAVE_JOB_LOGS", "true")).lower() == "true"
    )
    orchestration_enable_notifications: bool = field(
        default_factory=lambda: str(os.getenv("ORCHESTRATION_ENABLE_NOTIFICATIONS", "false")).lower() == "true"
    )
    orchestration_notification_on_failure: bool = field(
        default_factory=lambda: str(os.getenv("ORCHESTRATION_NOTIFICATION_ON_FAILURE", "true")).lower() == "true"
    )
    orchestration_notification_on_success: bool = field(
        default_factory=lambda: str(os.getenv("ORCHESTRATION_NOTIFICATION_ON_SUCCESS", "false")).lower() == "true"
    )
    orchestration_dry_run: bool = field(
        default_factory=lambda: str(os.getenv("ORCHESTRATION_DRY_RUN", "true")).lower() == "true"
    )

    # Phase 36: Observability Settings
    observability_enabled: bool = field(
        default_factory=lambda: str(os.getenv("OBSERVABILITY_ENABLED", "true")).lower() == "true"
    )
    structured_logging_enabled: bool = field(
        default_factory=lambda: str(os.getenv("STRUCTURED_LOGGING_ENABLED", "true")).lower() == "true"
    )
    default_observability_profile: str = field(
        default_factory=lambda: os.getenv("DEFAULT_OBSERVABILITY_PROFILE", "balanced_system_observability")
    )
    observability_log_level: str = field(
        default_factory=lambda: os.getenv("OBSERVABILITY_LOG_LEVEL", "INFO")
    )
    observability_log_to_file: bool = field(
        default_factory=lambda: str(os.getenv("OBSERVABILITY_LOG_TO_FILE", "true")).lower() == "true"
    )
    observability_log_to_console: bool = field(
        default_factory=lambda: str(os.getenv("OBSERVABILITY_LOG_TO_CONSOLE", "true")).lower() == "true"
    )
    observability_json_logs_enabled: bool = field(
        default_factory=lambda: str(os.getenv("OBSERVABILITY_JSON_LOGS_ENABLED", "true")).lower() == "true"
    )
    observability_max_log_files: int = field(
        default_factory=lambda: int(os.getenv("OBSERVABILITY_MAX_LOG_FILES", "20"))
    )
    observability_healthcheck_enabled: bool = field(
        default_factory=lambda: str(os.getenv("OBSERVABILITY_HEALTHCHECK_ENABLED", "true")).lower() == "true"
    )
    observability_runtime_metrics_enabled: bool = field(
        default_factory=lambda: str(os.getenv("OBSERVABILITY_RUNTIME_METRICS_ENABLED", "true")).lower() == "true"
    )
    observability_data_freshness_enabled: bool = field(
        default_factory=lambda: str(os.getenv("OBSERVABILITY_DATA_FRESHNESS_ENABLED", "true")).lower() == "true"
    )
    observability_artifact_integrity_enabled: bool = field(
        default_factory=lambda: str(os.getenv("OBSERVABILITY_ARTIFACT_INTEGRITY_ENABLED", "true")).lower() == "true"
    )
    observability_dependency_diagnostics_enabled: bool = field(
        default_factory=lambda: str(os.getenv("OBSERVABILITY_DEPENDENCY_DIAGNOSTICS_ENABLED", "true")).lower() == "true"
    )
    observability_max_stale_hours_daily: float = field(
        default_factory=lambda: float(os.getenv("OBSERVABILITY_MAX_STALE_HOURS_DAILY", "48.0"))
    )
    observability_max_stale_hours_intraday: float = field(
        default_factory=lambda: float(os.getenv("OBSERVABILITY_MAX_STALE_HOURS_INTRADAY", "12.0"))
    )
    observability_min_required_disk_free_mb: int = field(
        default_factory=lambda: int(os.getenv("OBSERVABILITY_MIN_REQUIRED_DISK_FREE_MB", "1024"))
    )
    observability_save_health_reports: bool = field(
        default_factory=lambda: str(os.getenv("OBSERVABILITY_SAVE_HEALTH_REPORTS", "true")).lower() == "true"
    )
    observability_save_runtime_metrics: bool = field(
        default_factory=lambda: str(os.getenv("OBSERVABILITY_SAVE_RUNTIME_METRICS", "true")).lower() == "true"
    )
    observability_save_diagnostics: bool = field(
        default_factory=lambda: str(os.getenv("OBSERVABILITY_SAVE_DIAGNOSTICS", "true")).lower() == "true"
    )
    observability_notification_on_critical: bool = field(
        default_factory=lambda: str(os.getenv("OBSERVABILITY_NOTIFICATION_ON_CRITICAL", "false")).lower() == "true"
    )


    # Phase 37: Security, Hardening & Readiness
    security_audit_enabled: bool = field(default_factory=lambda: str(os.getenv("SECURITY_AUDIT_ENABLED", "true")).lower() == "true")
    config_hardening_enabled: bool = field(default_factory=lambda: str(os.getenv("CONFIG_HARDENING_ENABLED", "true")).lower() == "true")
    secret_hygiene_enabled: bool = field(default_factory=lambda: str(os.getenv("SECRET_HYGIENE_ENABLED", "true")).lower() == "true")
    production_readiness_audit_enabled: bool = field(default_factory=lambda: str(os.getenv("PRODUCTION_READINESS_AUDIT_ENABLED", "true")).lower() == "true")
    default_security_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_SECURITY_PROFILE", "balanced_local_security"))
    security_fail_on_secret_leak: bool = field(default_factory=lambda: str(os.getenv("SECURITY_FAIL_ON_SECRET_LEAK", "true")).lower() == "true")
    security_fail_on_unsafe_live_flags: bool = field(default_factory=lambda: str(os.getenv("SECURITY_FAIL_ON_UNSAFE_LIVE_FLAGS", "true")).lower() == "true")
    security_fail_on_path_traversal_risk: bool = field(default_factory=lambda: str(os.getenv("SECURITY_FAIL_ON_PATH_TRAVERSAL_RISK", "true")).lower() == "true")
    security_allow_telegram_send: bool = field(default_factory=lambda: str(os.getenv("SECURITY_ALLOW_TELEGRAM_SEND", "false")).lower() == "true")
    security_allow_live_trading: bool = field(default_factory=lambda: str(os.getenv("SECURITY_ALLOW_LIVE_TRADING", "false")).lower() == "true")
    security_allow_broker_credentials: bool = field(default_factory=lambda: str(os.getenv("SECURITY_ALLOW_BROKER_CREDENTIALS", "false")).lower() == "true")
    security_allow_network_calls_except_data_and_telegram: bool = field(default_factory=lambda: str(os.getenv("SECURITY_ALLOW_NETWORK_CALLS_EXCEPT_DATA_AND_TELEGRAM", "true")).lower() == "true")
    security_require_dry_run_defaults: bool = field(default_factory=lambda: str(os.getenv("SECURITY_REQUIRE_DRY_RUN_DEFAULTS", "true")).lower() == "true")
    security_required_gitignore_patterns: tuple[str, ...] = field(default_factory=lambda: tuple(os.getenv("SECURITY_REQUIRED_GITIGNORE_PATTERNS", ".env,*.key,*.pem,data/lake/ml/model_artifacts/*.joblib").split(",")))
    security_sensitive_env_names: tuple[str, ...] = field(default_factory=lambda: tuple(os.getenv("SECURITY_SENSITIVE_ENV_NAMES", "TOKEN,SECRET,KEY,PASSWORD,CHAT_ID,API").split(",")))
    security_scan_text_extensions: tuple[str, ...] = field(default_factory=lambda: tuple(os.getenv("SECURITY_SCAN_TEXT_EXTENSIONS", ".py,.md,.txt,.json,.yaml,.yml,.env,.example").split(",")))
    security_max_file_scan_mb: int = field(default_factory=lambda: int(os.getenv("SECURITY_MAX_FILE_SCAN_MB", "5")))
    security_save_audit_reports: bool = field(default_factory=lambda: str(os.getenv("SECURITY_SAVE_AUDIT_REPORTS", "true")).lower() == "true")
    security_save_readiness_reports: bool = field(default_factory=lambda: str(os.getenv("SECURITY_SAVE_READINESS_REPORTS", "true")).lower() == "true")
    security_notification_on_critical: bool = field(default_factory=lambda: str(os.getenv("SECURITY_NOTIFICATION_ON_CRITICAL", "false")).lower() == "true")


    # Phase 40: Report Exports, Archive and Comparisons
    report_exports_enabled: bool = field(default_factory=lambda: str(os.getenv("REPORT_EXPORTS_ENABLED", "true")).lower() == "true")
    report_html_export_enabled: bool = field(default_factory=lambda: str(os.getenv("REPORT_HTML_EXPORT_ENABLED", "true")).lower() == "true")
    report_pdf_export_enabled: bool = field(default_factory=lambda: str(os.getenv("REPORT_PDF_EXPORT_ENABLED", "true")).lower() == "true")
    default_report_export_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_REPORT_EXPORT_PROFILE", "balanced_report_export"))
    report_export_default_timeframe: str = field(default_factory=lambda: os.getenv("REPORT_EXPORT_DEFAULT_TIMEFRAME", "1d"))
    report_export_language: str = field(default_factory=lambda: os.getenv("REPORT_EXPORT_LANGUAGE", "tr"))
    report_export_include_html: bool = field(default_factory=lambda: str(os.getenv("REPORT_EXPORT_INCLUDE_HTML", "true")).lower() == "true")
    report_export_include_pdf: bool = field(default_factory=lambda: str(os.getenv("REPORT_EXPORT_INCLUDE_PDF", "true")).lower() == "true")
    report_export_include_csv_bundle: bool = field(default_factory=lambda: str(os.getenv("REPORT_EXPORT_INCLUDE_CSV_BUNDLE", "true")).lower() == "true")
    report_export_archive_enabled: bool = field(default_factory=lambda: str(os.getenv("REPORT_EXPORT_ARCHIVE_ENABLED", "true")).lower() == "true")
    report_export_comparison_enabled: bool = field(default_factory=lambda: str(os.getenv("REPORT_EXPORT_COMPARISON_ENABLED", "true")).lower() == "true")
    report_export_periodic_tracking_enabled: bool = field(default_factory=lambda: str(os.getenv("REPORT_EXPORT_PERIODIC_TRACKING_ENABLED", "true")).lower() == "true")
    report_export_max_archive_records: int = field(default_factory=lambda: int(os.getenv("REPORT_EXPORT_MAX_ARCHIVE_RECORDS", "5000")))
    report_export_max_comparison_rows: int = field(default_factory=lambda: int(os.getenv("REPORT_EXPORT_MAX_COMPARISON_ROWS", "100")))
    report_export_pdf_engine: str = field(default_factory=lambda: os.getenv("REPORT_EXPORT_PDF_ENGINE", "auto"))
    report_export_html_theme: str = field(default_factory=lambda: os.getenv("REPORT_EXPORT_HTML_THEME", "clean_research"))
    report_export_save_manifest: bool = field(default_factory=lambda: str(os.getenv("REPORT_EXPORT_SAVE_MANIFEST", "true")).lower() == "true")
    report_export_save_quality: bool = field(default_factory=lambda: str(os.getenv("REPORT_EXPORT_SAVE_QUALITY", "true")).lower() == "true")
    report_export_require_disclaimer: bool = field(default_factory=lambda: str(os.getenv("REPORT_EXPORT_REQUIRE_DISCLAIMER", "true")).lower() == "true")
    report_export_min_quality_score: float = field(default_factory=lambda: float(os.getenv("REPORT_EXPORT_MIN_QUALITY_SCORE", "0.40")))


    # Phase 42: Portfolio Regime Research
    portfolio_regime_research_enabled: bool = field(default_factory=lambda: str(os.getenv("PORTFOLIO_REGIME_RESEARCH_ENABLED", "true")).lower() == "true")
    default_portfolio_regime_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_PORTFOLIO_REGIME_PROFILE", "balanced_regime_portfolio_research"))
    portfolio_regime_default_timeframe: str = field(default_factory=lambda: os.getenv("PORTFOLIO_REGIME_DEFAULT_TIMEFRAME", "1d"))
    portfolio_regime_min_symbols: int = field(default_factory=lambda: int(os.getenv("PORTFOLIO_REGIME_MIN_SYMBOLS", "3")))
    portfolio_regime_min_observations: int = field(default_factory=lambda: int(os.getenv("PORTFOLIO_REGIME_MIN_OBSERVATIONS", "180")))
    portfolio_regime_volatility_window: int = field(default_factory=lambda: int(os.getenv("PORTFOLIO_REGIME_VOLATILITY_WINDOW", "20")))
    portfolio_regime_trend_window: int = field(default_factory=lambda: int(os.getenv("PORTFOLIO_REGIME_TREND_WINDOW", "50")))
    portfolio_regime_correlation_window: int = field(default_factory=lambda: int(os.getenv("PORTFOLIO_REGIME_CORRELATION_WINDOW", "60")))
    portfolio_regime_drawdown_cluster_threshold: float = field(default_factory=lambda: float(os.getenv("PORTFOLIO_REGIME_DRAWDOWN_CLUSTER_THRESHOLD", "-0.05")))
    portfolio_regime_stress_window_min_bars: int = field(default_factory=lambda: int(os.getenv("PORTFOLIO_REGIME_STRESS_WINDOW_MIN_BARS", "20")))
    portfolio_regime_stress_window_max_bars: int = field(default_factory=lambda: int(os.getenv("PORTFOLIO_REGIME_STRESS_WINDOW_MAX_BARS", "90")))
    portfolio_regime_tail_quantile: float = field(default_factory=lambda: float(os.getenv("PORTFOLIO_REGIME_TAIL_QUANTILE", "0.05")))
    portfolio_regime_scenario_shock_small: float = field(default_factory=lambda: float(os.getenv("PORTFOLIO_REGIME_SCENARIO_SHOCK_SMALL", "0.03")))
    portfolio_regime_scenario_shock_medium: float = field(default_factory=lambda: float(os.getenv("PORTFOLIO_REGIME_SCENARIO_SHOCK_MEDIUM", "0.07")))
    portfolio_regime_scenario_shock_large: float = field(default_factory=lambda: float(os.getenv("PORTFOLIO_REGIME_SCENARIO_SHOCK_LARGE", "0.12")))
    portfolio_regime_save_reports: bool = field(default_factory=lambda: str(os.getenv("PORTFOLIO_REGIME_SAVE_REPORTS", "true")).lower() == "true")
    portfolio_regime_save_tables: bool = field(default_factory=lambda: str(os.getenv("PORTFOLIO_REGIME_SAVE_TABLES", "true")).lower() == "true")
    portfolio_regime_min_quality_score: float = field(default_factory=lambda: float(os.getenv("PORTFOLIO_REGIME_MIN_QUALITY_SCORE", "0.40")))


    # Phase 43: Synthetic Benchmark Baskets & Composite Indices
    synthetic_indices_enabled: bool = field(default_factory=lambda: str(os.getenv("SYNTHETIC_INDICES_ENABLED", "true")).lower() == "true")
    default_synthetic_index_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_SYNTHETIC_INDEX_PROFILE", "balanced_synthetic_index_research"))
    synthetic_index_default_timeframe: str = field(default_factory=lambda: os.getenv("SYNTHETIC_INDEX_DEFAULT_TIMEFRAME", "1d"))
    synthetic_index_base_value: float = field(default_factory=lambda: float(os.getenv("SYNTHETIC_INDEX_BASE_VALUE", "100.0")))
    synthetic_index_return_method: str = field(default_factory=lambda: os.getenv("SYNTHETIC_INDEX_RETURN_METHOD", "log"))
    synthetic_index_rebalance_method: str = field(default_factory=lambda: os.getenv("SYNTHETIC_INDEX_REBALANCE_METHOD", "static"))
    synthetic_index_rebalance_frequency: str = field(default_factory=lambda: os.getenv("SYNTHETIC_INDEX_REBALANCE_FREQUENCY", "monthly"))
    synthetic_index_min_symbols: int = field(default_factory=lambda: int(os.getenv("SYNTHETIC_INDEX_MIN_SYMBOLS", "3")))
    synthetic_index_min_observations: int = field(default_factory=lambda: int(os.getenv("SYNTHETIC_INDEX_MIN_OBSERVATIONS", "120")))
    synthetic_index_max_symbols_per_index: int = field(default_factory=lambda: int(os.getenv("SYNTHETIC_INDEX_MAX_SYMBOLS_PER_INDEX", "20")))
    synthetic_index_max_single_weight: float = field(default_factory=lambda: float(os.getenv("SYNTHETIC_INDEX_MAX_SINGLE_WEIGHT", "0.35")))
    synthetic_index_relative_strength_windows: tuple[int, ...] = field(default_factory=lambda: tuple(map(int, os.getenv("SYNTHETIC_INDEX_RELATIVE_STRENGTH_WINDOWS", "20,60,120").split(","))))
    synthetic_index_rotation_lookback: int = field(default_factory=lambda: int(os.getenv("SYNTHETIC_INDEX_ROTATION_LOOKBACK", "60")))
    synthetic_index_rotation_top_n: int = field(default_factory=lambda: int(os.getenv("SYNTHETIC_INDEX_ROTATION_TOP_N", "5")))
    synthetic_index_rotation_bottom_n: int = field(default_factory=lambda: int(os.getenv("SYNTHETIC_INDEX_ROTATION_BOTTOM_N", "5")))
    synthetic_index_save_definitions: bool = field(default_factory=lambda: str(os.getenv("SYNTHETIC_INDEX_SAVE_DEFINITIONS", "true")).lower() == "true")
    synthetic_index_save_levels: bool = field(default_factory=lambda: str(os.getenv("SYNTHETIC_INDEX_SAVE_LEVELS", "true")).lower() == "true")
    synthetic_index_save_reports: bool = field(default_factory=lambda: str(os.getenv("SYNTHETIC_INDEX_SAVE_REPORTS", "true")).lower() == "true")
    synthetic_index_min_quality_score: float = field(default_factory=lambda: float(os.getenv("SYNTHETIC_INDEX_MIN_QUALITY_SCORE", "0.40")))


    # Phase 44: Factor Research and Cross-Sectional Analysis
    factor_research_enabled: bool = field(default_factory=lambda: str(os.getenv("FACTOR_RESEARCH_ENABLED", "true")).lower() == "true")
    default_factor_research_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_FACTOR_RESEARCH_PROFILE", "balanced_factor_research"))
    factor_research_default_timeframe: str = field(default_factory=lambda: os.getenv("FACTOR_RESEARCH_DEFAULT_TIMEFRAME", "1d"))
    factor_research_return_method: str = field(default_factory=lambda: os.getenv("FACTOR_RESEARCH_RETURN_METHOD", "log"))
    factor_research_min_symbols: int = field(default_factory=lambda: int(os.getenv("FACTOR_RESEARCH_MIN_SYMBOLS", "5")))
    factor_research_min_observations: int = field(default_factory=lambda: int(os.getenv("FACTOR_RESEARCH_MIN_OBSERVATIONS", "180")))
    factor_research_forward_return_horizon: int = field(default_factory=lambda: int(os.getenv("FACTOR_RESEARCH_FORWARD_RETURN_HORIZON", "20")))
    factor_research_rank_top_quantile: float = field(default_factory=lambda: float(os.getenv("FACTOR_RESEARCH_RANK_TOP_QUANTILE", "0.30")))
    factor_research_rank_bottom_quantile: float = field(default_factory=lambda: float(os.getenv("FACTOR_RESEARCH_RANK_BOTTOM_QUANTILE", "0.30")))
    factor_research_trend_windows: tuple[int, ...] = field(default_factory=lambda: tuple(map(int, os.getenv("FACTOR_RESEARCH_TREND_WINDOWS", "20,60,120").split(","))))
    factor_research_momentum_windows: tuple[int, ...] = field(default_factory=lambda: tuple(map(int, os.getenv("FACTOR_RESEARCH_MOMENTUM_WINDOWS", "20,60,120").split(","))))
    factor_research_volatility_windows: tuple[int, ...] = field(default_factory=lambda: tuple(map(int, os.getenv("FACTOR_RESEARCH_VOLATILITY_WINDOWS", "20,60").split(","))))
    factor_research_decay_windows: tuple[int, ...] = field(default_factory=lambda: tuple(map(int, os.getenv("FACTOR_RESEARCH_DECAY_WINDOWS", "5,10,20,60").split(","))))
    factor_research_neutralize_asset_class: bool = field(default_factory=lambda: str(os.getenv("FACTOR_RESEARCH_NEUTRALIZE_ASSET_CLASS", "true")).lower() == "true")
    factor_research_neutralize_volatility: bool = field(default_factory=lambda: str(os.getenv("FACTOR_RESEARCH_NEUTRALIZE_VOLATILITY", "true")).lower() == "true")
    factor_research_max_single_symbol_weight: float = field(default_factory=lambda: float(os.getenv("FACTOR_RESEARCH_MAX_SINGLE_SYMBOL_WEIGHT", "0.20")))
    factor_research_save_scores: bool = field(default_factory=lambda: str(os.getenv("FACTOR_RESEARCH_SAVE_SCORES", "true")).lower() == "true")
    factor_research_save_backtests: bool = field(default_factory=lambda: str(os.getenv("FACTOR_RESEARCH_SAVE_BACKTESTS", "true")).lower() == "true")
    factor_research_save_reports: bool = field(default_factory=lambda: str(os.getenv("FACTOR_RESEARCH_SAVE_REPORTS", "true")).lower() == "true")
    factor_research_min_quality_score: float = field(default_factory=lambda: float(os.getenv("FACTOR_RESEARCH_MIN_QUALITY_SCORE", "0.40")))


    # Phase 45: Meta Research and Consensus Engine
    meta_research_enabled: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_ENABLED", "true")).lower() == "true")
    default_meta_research_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_META_RESEARCH_PROFILE", "balanced_meta_research"))
    meta_research_default_timeframe: str = field(default_factory=lambda: os.getenv("META_RESEARCH_DEFAULT_TIMEFRAME", "1d"))
    meta_research_min_sources: int = field(default_factory=lambda: int(os.getenv("META_RESEARCH_MIN_SOURCES", "3")))
    meta_research_min_evidence_quality: float = field(default_factory=lambda: float(os.getenv("META_RESEARCH_MIN_EVIDENCE_QUALITY", "0.40")))
    meta_research_conflict_threshold: float = field(default_factory=lambda: float(os.getenv("META_RESEARCH_CONFLICT_THRESHOLD", "0.35")))
    meta_research_high_agreement_threshold: float = field(default_factory=lambda: float(os.getenv("META_RESEARCH_HIGH_AGREEMENT_THRESHOLD", "0.70")))
    meta_research_uncertainty_penalty_enabled: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_UNCERTAINTY_PENALTY_ENABLED", "true")).lower() == "true")
    meta_research_quality_penalty_enabled: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_QUALITY_PENALTY_ENABLED", "true")).lower() == "true")
    meta_research_missing_source_penalty_enabled: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_MISSING_SOURCE_PENALTY_ENABLED", "true")).lower() == "true")
    meta_research_include_technical: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_TECHNICAL", "true")).lower() == "true")
    meta_research_include_strategy: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_STRATEGY", "true")).lower() == "true")
    meta_research_include_risk_level: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_RISK_LEVEL", "true")).lower() == "true")
    meta_research_include_backtest: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_BACKTEST", "true")).lower() == "true")
    meta_research_include_validation: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_VALIDATION", "true")).lower() == "true")
    meta_research_include_ml: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_ML", "true")).lower() == "true")
    meta_research_include_paper: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_PAPER", "true")).lower() == "true")
    meta_research_include_factor: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_FACTOR", "true")).lower() == "true")
    meta_research_include_synthetic_index: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_SYNTHETIC_INDEX", "true")).lower() == "true")
    meta_research_include_portfolio: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_PORTFOLIO", "true")).lower() == "true")
    meta_research_include_regime: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_REGIME", "true")).lower() == "true")
    meta_research_save_reports: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_SAVE_REPORTS", "true")).lower() == "true")
    meta_research_save_tables: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_SAVE_TABLES", "true")).lower() == "true")
    meta_research_min_quality_score: float = field(default_factory=lambda: float(os.getenv("META_RESEARCH_MIN_QUALITY_SCORE", "0.40")))



    # Phase 46: Experiment Tracking and Research Versioning
    experiment_tracking_enabled: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_TRACKING_ENABLED", "true")).lower() == "true")

    # Governance Settings (Phase 47)
    governance_enabled: bool = True
    default_governance_profile: str = "balanced_research_governance"
    governance_default_timeframe: str = "1d"
    governance_scan_data_lake: bool = True
    governance_scan_reports_output: bool = True
    governance_capture_file_hashes: bool = True
    governance_capture_schema_fingerprints: bool = True
    governance_capture_row_counts: bool = True
    governance_capture_modified_times: bool = True
    governance_capture_artifact_sizes: bool = True
    governance_max_file_hash_mb: int = 50
    governance_lineage_max_depth: int = 8
    governance_require_provenance_for_research_outputs: bool = True
    governance_require_fingerprint_for_key_artifacts: bool = True
    governance_require_audit_trail: bool = True
    governance_save_inventory: bool = True
    governance_save_lineage: bool = True
    governance_save_audit_trail: bool = True
    governance_save_reports: bool = True
    governance_min_quality_score: float = 0.40
    default_experiment_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_EXPERIMENT_PROFILE", "balanced_experiment_tracking"))
    experiment_default_timeframe: str = field(default_factory=lambda: os.getenv("EXPERIMENT_DEFAULT_TIMEFRAME", "1d"))
    experiment_save_run_manifest: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_SAVE_RUN_MANIFEST", "true")).lower() == "true")
    experiment_save_artifact_manifest: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_SAVE_ARTIFACT_MANIFEST", "true")).lower() == "true")
    experiment_save_reproducibility_manifest: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_SAVE_REPRODUCIBILITY_MANIFEST", "true")).lower() == "true")
    experiment_save_quality_report: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_SAVE_QUALITY_REPORT", "true")).lower() == "true")
    experiment_max_runs_in_leaderboard: int = field(default_factory=lambda: int(os.getenv("EXPERIMENT_MAX_RUNS_IN_LEADERBOARD", "500")))
    experiment_min_quality_score: float = field(default_factory=lambda: float(os.getenv("EXPERIMENT_MIN_QUALITY_SCORE", "0.40")))
    experiment_default_baseline_name: str = field(default_factory=lambda: os.getenv("EXPERIMENT_DEFAULT_BASELINE_NAME", "baseline_research_run"))
    experiment_enable_ablation_studies: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_ENABLE_ABLATION_STUDIES", "true")).lower() == "true")
    experiment_enable_comparison: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_ENABLE_COMPARISON", "true")).lower() == "true")
    experiment_enable_leaderboard: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_ENABLE_LEADERBOARD", "true")).lower() == "true")
    experiment_require_hypothesis: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_REQUIRE_HYPOTHESIS", "false")).lower() == "true")
    experiment_require_reproducibility_manifest: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_REQUIRE_REPRODUCIBILITY_MANIFEST", "true")).lower() == "true")
    experiment_capture_environment: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_CAPTURE_ENVIRONMENT", "true")).lower() == "true")
    experiment_capture_config_snapshot: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_CAPTURE_CONFIG_SNAPSHOT", "true")).lower() == "true")
    experiment_capture_artifact_snapshot: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_CAPTURE_ARTIFACT_SNAPSHOT", "true")).lower() == "true")
    experiment_allow_rerun_candidates: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_ALLOW_RERUN_CANDIDATES", "true")).lower() == "true")
    experiment_tracking_dry_run: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_TRACKING_DRY_RUN", "true")).lower() == "true")

    # Research Planning Settings
    research_planning_enabled: bool = True
    default_research_planning_profile: str = "balanced_research_planning"
    research_planning_default_timeframe: str = "1d"
    research_planning_max_backlog_items: int = 500
    research_planning_max_next_best_experiments: int = 25
    research_planning_min_priority_score: float = 0.35
    research_planning_high_priority_threshold: float = 0.70
    research_planning_include_governance_signals: bool = True
    research_planning_include_experiment_signals: bool = True
    research_planning_include_meta_signals: bool = True
    research_planning_include_factor_signals: bool = True
    research_planning_include_portfolio_signals: bool = True
    research_planning_include_regime_signals: bool = True
    research_planning_include_validation_signals: bool = True
    research_planning_include_ml_signals: bool = True
    research_planning_include_paper_signals: bool = True
    research_planning_include_observability_signals: bool = True
    research_planning_save_backlog: bool = True
    research_planning_save_reports: bool = True
    research_planning_dry_run: bool = True
    research_planning_min_quality_score: float = 0.40

# Phase 49: Knowledge Base & Analyst Workspace
    knowledge_base_enabled: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_ENABLED", "true")).lower() == "true")
    default_knowledge_base_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_KNOWLEDGE_BASE_PROFILE", "balanced_local_knowledge_base"))
    knowledge_base_default_timeframe: str = field(default_factory=lambda: os.getenv("KNOWLEDGE_BASE_DEFAULT_TIMEFRAME", "1d"))
    knowledge_base_scan_reports_output: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_SCAN_REPORTS_OUTPUT", "true")).lower() == "true")
    knowledge_base_scan_docs: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_SCAN_DOCS", "true")).lower() == "true")
    knowledge_base_scan_data_lake_reports: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_SCAN_DATA_LAKE_REPORTS", "true")).lower() == "true")
    knowledge_base_scan_experiments: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_SCAN_EXPERIMENTS", "true")).lower() == "true")
    knowledge_base_scan_governance: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_SCAN_GOVERNANCE", "true")).lower() == "true")
    knowledge_base_scan_planning: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_SCAN_PLANNING", "true")).lower() == "true")
    knowledge_base_scan_meta_research: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_SCAN_META_RESEARCH", "true")).lower() == "true")
    knowledge_base_max_documents: int = field(default_factory=lambda: int(os.getenv("KNOWLEDGE_BASE_MAX_DOCUMENTS", "5000")))
    knowledge_base_max_document_mb: int = field(default_factory=lambda: int(os.getenv("KNOWLEDGE_BASE_MAX_DOCUMENT_MB", "10")))
    knowledge_base_chunk_size_chars: int = field(default_factory=lambda: int(os.getenv("KNOWLEDGE_BASE_CHUNK_SIZE_CHARS", "1200")))
    knowledge_base_chunk_overlap_chars: int = field(default_factory=lambda: int(os.getenv("KNOWLEDGE_BASE_CHUNK_OVERLAP_CHARS", "150")))
    knowledge_base_max_chunks: int = field(default_factory=lambda: int(os.getenv("KNOWLEDGE_BASE_MAX_CHUNKS", "50000")))
    knowledge_base_retrieval_top_k: int = field(default_factory=lambda: int(os.getenv("KNOWLEDGE_BASE_RETRIEVAL_TOP_K", "10")))
    knowledge_base_enable_tfidf: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_ENABLE_TFIDF", "true")).lower() == "true")
    knowledge_base_enable_fuzzy: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_ENABLE_FUZZY", "true")).lower() == "true")
    knowledge_base_enable_hybrid: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_ENABLE_HYBRID", "true")).lower() == "true")
    knowledge_base_save_index: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_SAVE_INDEX", "true")).lower() == "true")
    knowledge_base_save_memory_cards: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_SAVE_MEMORY_CARDS", "true")).lower() == "true")
    knowledge_base_save_reports: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_SAVE_REPORTS", "true")).lower() == "true")
    knowledge_base_min_quality_score: float = field(default_factory=lambda: float(os.getenv("KNOWLEDGE_BASE_MIN_QUALITY_SCORE", "0.40")))

    # Phase 50: Command Center
    command_center_enabled: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_ENABLED", "true")).lower() == "true")
    default_command_center_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_COMMAND_CENTER_PROFILE", "balanced_offline_command_center"))
    command_center_default_timeframe: str = field(default_factory=lambda: os.getenv("COMMAND_CENTER_DEFAULT_TIMEFRAME", "1d"))
    command_center_dry_run_default: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_DRY_RUN_DEFAULT", "true")).lower() == "true")
    command_center_require_safe_commands: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_REQUIRE_SAFE_COMMANDS", "true")).lower() == "true")
    command_center_allow_live_commands: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_ALLOW_LIVE_COMMANDS", "false")).lower() == "true")
    command_center_allow_broker_commands: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_ALLOW_BROKER_COMMANDS", "false")).lower() == "true")
    command_center_allow_deploy_commands: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_ALLOW_DEPLOY_COMMANDS", "false")).lower() == "true")
    command_center_allow_background_daemons: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_ALLOW_BACKGROUND_DAEMONS", "false")).lower() == "true")
    command_center_max_suggested_commands: int = field(default_factory=lambda: int(os.getenv("COMMAND_CENTER_MAX_SUGGESTED_COMMANDS", "50")))
    command_center_include_research_reports: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_INCLUDE_RESEARCH_REPORTS", "true")).lower() == "true")
    command_center_include_portfolio_reports: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_INCLUDE_PORTFOLIO_REPORTS", "true")).lower() == "true")
    command_center_include_regime_reports: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_INCLUDE_REGIME_REPORTS", "true")).lower() == "true")
    command_center_include_synthetic_indices: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_INCLUDE_SYNTHETIC_INDICES", "true")).lower() == "true")
    command_center_include_factor_research: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_INCLUDE_FACTOR_RESEARCH", "true")).lower() == "true")
    command_center_include_meta_research: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_INCLUDE_META_RESEARCH", "true")).lower() == "true")
    command_center_include_experiments: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_INCLUDE_EXPERIMENTS", "true")).lower() == "true")
    command_center_include_governance: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_INCLUDE_GOVERNANCE", "true")).lower() == "true")
    command_center_include_planning: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_INCLUDE_PLANNING", "true")).lower() == "true")
    command_center_include_knowledge_base: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_INCLUDE_KNOWLEDGE_BASE", "true")).lower() == "true")
    command_center_save_reports: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_SAVE_REPORTS", "true")).lower() == "true")
    command_center_min_quality_score: float = field(default_factory=lambda: float(os.getenv("COMMAND_CENTER_MIN_QUALITY_SCORE", "0.40")))


    # Phase 51: Quality Gates
    quality_gates_enabled: bool = field(default_factory=lambda: str(os.getenv("QUALITY_GATES_ENABLED", "true")).lower() == "true")
    default_quality_gate_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_QUALITY_GATE_PROFILE", "balanced_local_quality_gate"))
    quality_gate_default_timeframe: str = field(default_factory=lambda: os.getenv("QUALITY_GATE_DEFAULT_TIMEFRAME", "1d"))
    quality_gate_run_pytest: bool = field(default_factory=lambda: str(os.getenv("QUALITY_GATE_RUN_PYTEST", "true")).lower() == "true")
    quality_gate_run_import_validation: bool = field(default_factory=lambda: str(os.getenv("QUALITY_GATE_RUN_IMPORT_VALIDATION", "true")).lower() == "true")
    quality_gate_run_static_safety_scan: bool = field(default_factory=lambda: str(os.getenv("QUALITY_GATE_RUN_STATIC_SAFETY_SCAN", "true")).lower() == "true")
    quality_gate_run_repo_hygiene: bool = field(default_factory=lambda: str(os.getenv("QUALITY_GATE_RUN_REPO_HYGIENE", "true")).lower() == "true")
    quality_gate_run_dependency_audit: bool = field(default_factory=lambda: str(os.getenv("QUALITY_GATE_RUN_DEPENDENCY_AUDIT", "true")).lower() == "true")
    quality_gate_run_smoke_tests: bool = field(default_factory=lambda: str(os.getenv("QUALITY_GATE_RUN_SMOKE_TESTS", "true")).lower() == "true")
    quality_gate_run_output_contracts: bool = field(default_factory=lambda: str(os.getenv("QUALITY_GATE_RUN_OUTPUT_CONTRACTS", "true")).lower() == "true")
    quality_gate_run_documentation_coverage: bool = field(default_factory=lambda: str(os.getenv("QUALITY_GATE_RUN_DOCUMENTATION_COVERAGE", "true")).lower() == "true")
    quality_gate_max_test_runtime_seconds: int = field(default_factory=lambda: int(os.getenv("QUALITY_GATE_MAX_TEST_RUNTIME_SECONDS", "900")))
    quality_gate_allow_network_calls: bool = field(default_factory=lambda: str(os.getenv("QUALITY_GATE_ALLOW_NETWORK_CALLS", "false")).lower() == "true")
    quality_gate_allow_live_commands: bool = field(default_factory=lambda: str(os.getenv("QUALITY_GATE_ALLOW_LIVE_COMMANDS", "false")).lower() == "true")
    quality_gate_allow_broker_commands: bool = field(default_factory=lambda: str(os.getenv("QUALITY_GATE_ALLOW_BROKER_COMMANDS", "false")).lower() == "true")
    quality_gate_allow_deploy_commands: bool = field(default_factory=lambda: str(os.getenv("QUALITY_GATE_ALLOW_DEPLOY_COMMANDS", "false")).lower() == "true")
    quality_gate_allow_background_daemons: bool = field(default_factory=lambda: str(os.getenv("QUALITY_GATE_ALLOW_BACKGROUND_DAEMONS", "false")).lower() == "true")
    quality_gate_min_pass_rate: float = field(default_factory=lambda: float(os.getenv("QUALITY_GATE_MIN_PASS_RATE", "0.85")))
    quality_gate_min_quality_score: float = field(default_factory=lambda: float(os.getenv("QUALITY_GATE_MIN_QUALITY_SCORE", "0.40")))
    release_candidate_enabled: bool = field(default_factory=lambda: str(os.getenv("RELEASE_CANDIDATE_ENABLED", "true")).lower() == "true")
    release_candidate_dry_run: bool = field(default_factory=lambda: str(os.getenv("RELEASE_CANDIDATE_DRY_RUN", "true")).lower() == "true")
    release_candidate_include_reports: bool = field(default_factory=lambda: str(os.getenv("RELEASE_CANDIDATE_INCLUDE_REPORTS", "true")).lower() == "true")
    release_candidate_include_docs: bool = field(default_factory=lambda: str(os.getenv("RELEASE_CANDIDATE_INCLUDE_DOCS", "true")).lower() == "true")
    release_candidate_include_manifests: bool = field(default_factory=lambda: str(os.getenv("RELEASE_CANDIDATE_INCLUDE_MANIFESTS", "true")).lower() == "true")


    # Phase 55: Final Review
    final_review_enabled: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_ENABLED", "true")).lower() == "true")
    default_final_review_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_FINAL_REVIEW_PROFILE", "balanced_final_review"))
    final_review_default_timeframe: str = field(default_factory=lambda: os.getenv("FINAL_REVIEW_DEFAULT_TIMEFRAME", "1d"))
    final_review_run_architecture_audit: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_RUN_ARCHITECTURE_AUDIT", "true")).lower() == "true")
    final_review_run_safety_audit: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_RUN_SAFETY_AUDIT", "true")).lower() == "true")
    final_review_run_integration_audit: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_RUN_INTEGRATION_AUDIT", "true")).lower() == "true")
    final_review_run_command_audit: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_RUN_COMMAND_AUDIT", "true")).lower() == "true")
    final_review_run_datalake_audit: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_RUN_DATALAKE_AUDIT", "true")).lower() == "true")
    final_review_run_report_output_audit: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_RUN_REPORT_OUTPUT_AUDIT", "true")).lower() == "true")
    final_review_run_documentation_audit: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_RUN_DOCUMENTATION_AUDIT", "true")).lower() == "true")
    final_review_run_quality_gate_audit: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_RUN_QUALITY_GATE_AUDIT", "true")).lower() == "true")
    final_review_run_performance_audit: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_RUN_PERFORMANCE_AUDIT", "true")).lower() == "true")
    final_review_run_maintenance_audit: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_RUN_MAINTENANCE_AUDIT", "true")).lower() == "true")
    final_review_run_release_readiness_dry_run: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_RUN_RELEASE_READINESS_DRY_RUN", "true")).lower() == "true")
    final_review_require_no_live_trading: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_REQUIRE_NO_LIVE_TRADING", "true")).lower() == "true")
    final_review_require_no_broker_execution: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_REQUIRE_NO_BROKER_EXECUTION", "true")).lower() == "true")
    final_review_require_no_model_deploy: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_REQUIRE_NO_MODEL_DEPLOY", "true")).lower() == "true")
    final_review_require_no_background_daemon: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_REQUIRE_NO_BACKGROUND_DAEMON", "true")).lower() == "true")
    final_review_require_no_web_scraping: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_REQUIRE_NO_WEB_SCRAPING", "true")).lower() == "true")
    final_review_min_acceptance_score: float = field(default_factory=lambda: float(os.getenv("FINAL_REVIEW_MIN_ACCEPTANCE_SCORE", "0.75")))
    final_review_min_safety_score: float = field(default_factory=lambda: float(os.getenv("FINAL_REVIEW_MIN_SAFETY_SCORE", "0.95")))
    final_review_save_reports: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_SAVE_REPORTS", "true")).lower() == "true")
    final_review_dry_run: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_DRY_RUN", "true")).lower() == "true")
    final_review_min_quality_score: float = field(default_factory=lambda: float(os.getenv("FINAL_REVIEW_MIN_QUALITY_SCORE", "0.40")))


    # Phase 57: Scenario Regression
    scenario_regression_enabled: bool = field(default_factory=lambda: str(os.getenv("SCENARIO_REGRESSION_ENABLED", "true")).lower() == "true")
    default_scenario_regression_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_SCENARIO_REGRESSION_PROFILE", "balanced_scenario_regression"))
    scenario_regression_default_timeframe: str = field(default_factory=lambda: os.getenv("SCENARIO_REGRESSION_DEFAULT_TIMEFRAME", "1d"))
    scenario_regression_use_synthetic_only: bool = field(default_factory=lambda: str(os.getenv("SCENARIO_REGRESSION_USE_SYNTHETIC_ONLY", "true")).lower() == "true")
    scenario_regression_allow_real_market_download: bool = field(default_factory=lambda: str(os.getenv("SCENARIO_REGRESSION_ALLOW_REAL_MARKET_DOWNLOAD", "false")).lower() == "true")
    scenario_regression_allow_live_commands: bool = field(default_factory=lambda: str(os.getenv("SCENARIO_REGRESSION_ALLOW_LIVE_COMMANDS", "false")).lower() == "true")
    scenario_regression_allow_broker_commands: bool = field(default_factory=lambda: str(os.getenv("SCENARIO_REGRESSION_ALLOW_BROKER_COMMANDS", "false")).lower() == "true")
    scenario_regression_allow_deploy_commands: bool = field(default_factory=lambda: str(os.getenv("SCENARIO_REGRESSION_ALLOW_DEPLOY_COMMANDS", "false")).lower() == "true")
    scenario_regression_allow_background_daemons: bool = field(default_factory=lambda: str(os.getenv("SCENARIO_REGRESSION_ALLOW_BACKGROUND_DAEMONS", "false")).lower() == "true")
    scenario_regression_generate_golden_outputs: bool = field(default_factory=lambda: str(os.getenv("SCENARIO_REGRESSION_GENERATE_GOLDEN_OUTPUTS", "true")).lower() == "true")
    scenario_regression_capture_snapshots: bool = field(default_factory=lambda: str(os.getenv("SCENARIO_REGRESSION_CAPTURE_SNAPSHOTS", "true")).lower() == "true")
    scenario_regression_compare_snapshots: bool = field(default_factory=lambda: str(os.getenv("SCENARIO_REGRESSION_COMPARE_SNAPSHOTS", "true")).lower() == "true")
    scenario_regression_run_deterministic_replay: bool = field(default_factory=lambda: str(os.getenv("SCENARIO_REGRESSION_RUN_DETERMINISTIC_REPLAY", "true")).lower() == "true")
    scenario_regression_validate_output_contracts: bool = field(default_factory=lambda: str(os.getenv("SCENARIO_REGRESSION_VALIDATE_OUTPUT_CONTRACTS", "true")).lower() == "true")
    scenario_regression_max_scenarios: int = field(default_factory=lambda: int(os.getenv("SCENARIO_REGRESSION_MAX_SCENARIOS", "50")))
    scenario_regression_max_snapshot_rows: int = field(default_factory=lambda: int(os.getenv("SCENARIO_REGRESSION_MAX_SNAPSHOT_ROWS", "1000")))
    scenario_regression_numeric_tolerance: float = field(default_factory=lambda: float(os.getenv("SCENARIO_REGRESSION_NUMERIC_TOLERANCE", "1e-8")))
    scenario_regression_text_similarity_threshold: float = field(default_factory=lambda: float(os.getenv("SCENARIO_REGRESSION_TEXT_SIMILARITY_THRESHOLD", "0.95")))
    scenario_regression_acceptance_threshold: float = field(default_factory=lambda: float(os.getenv("SCENARIO_REGRESSION_ACCEPTANCE_THRESHOLD", "0.85")))
    scenario_regression_random_seed: int = field(default_factory=lambda: int(os.getenv("SCENARIO_REGRESSION_RANDOM_SEED", "42")))
    scenario_regression_save_reports: bool = field(default_factory=lambda: str(os.getenv("SCENARIO_REGRESSION_SAVE_REPORTS", "true")).lower() == "true")
    scenario_regression_min_quality_score: float = field(default_factory=lambda: float(os.getenv("SCENARIO_REGRESSION_MIN_QUALITY_SCORE", "0.40")))


    # Phase 58: Analyst UX & Operator Productivity
    analyst_ux_enabled: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_ENABLED", "true")).lower() == "true")
    default_analyst_ux_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_ANALYST_UX_PROFILE", "balanced_analyst_productivity"))
    analyst_ux_default_language: str = field(default_factory=lambda: os.getenv("ANALYST_UX_DEFAULT_LANGUAGE", "tr"))
    analyst_ux_allow_live_commands: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_ALLOW_LIVE_COMMANDS", "false")).lower() == "true")
    analyst_ux_allow_broker_commands: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_ALLOW_BROKER_COMMANDS", "false")).lower() == "true")
    analyst_ux_allow_deploy_commands: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_ALLOW_DEPLOY_COMMANDS", "false")).lower() == "true")
    analyst_ux_allow_background_daemons: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_ALLOW_BACKGROUND_DAEMONS", "false")).lower() == "true")
    analyst_ux_allow_real_market_download: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_ALLOW_REAL_MARKET_DOWNLOAD", "false")).lower() == "true")
    analyst_ux_generate_aliases: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_GENERATE_ALIASES", "true")).lower() == "true")
    analyst_ux_generate_prompt_packs: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_GENERATE_PROMPT_PACKS", "true")).lower() == "true")
    analyst_ux_generate_cheat_sheets: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_GENERATE_CHEAT_SHEETS", "true")).lower() == "true")
    analyst_ux_generate_task_board: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_GENERATE_TASK_BOARD", "true")).lower() == "true")
    analyst_ux_max_command_suggestions: int = field(default_factory=lambda: int(os.getenv("ANALYST_UX_MAX_COMMAND_SUGGESTIONS", "10")))
    analyst_ux_min_intent_confidence: float = field(default_factory=lambda: float(os.getenv("ANALYST_UX_MIN_INTENT_CONFIDENCE", "0.40")))
    analyst_ux_save_reports: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_SAVE_REPORTS", "true")).lower() == "true")
    analyst_ux_min_quality_score: float = field(default_factory=lambda: float(os.getenv("ANALYST_UX_MIN_QUALITY_SCORE", "0.40")))


    # Phase 61: Portable Packaging
    portable_packaging_enabled: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ENABLED", "true")).lower() == "true")
    default_portable_packaging_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_PORTABLE_PACKAGING_PROFILE", "balanced_local_packaging"))
    portable_packaging_default_language: str = field(default_factory=lambda: os.getenv("PORTABLE_PACKAGING_DEFAULT_LANGUAGE", "tr"))
    portable_packaging_dry_run_default: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_DRY_RUN_DEFAULT", "true")).lower() == "true")
    portable_packaging_allow_archive_create: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ALLOW_ARCHIVE_CREATE", "false")).lower() == "true")
    portable_packaging_allow_package_publish: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ALLOW_PACKAGE_PUBLISH", "false")).lower() == "true")
    portable_packaging_allow_docker: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ALLOW_DOCKER", "false")).lower() == "true")
    portable_packaging_allow_cloud_deploy: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ALLOW_CLOUD_DEPLOY", "false")).lower() == "true")
    portable_packaging_allow_live_commands: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ALLOW_LIVE_COMMANDS", "false")).lower() == "true")
    portable_packaging_allow_broker_commands: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ALLOW_BROKER_COMMANDS", "false")).lower() == "true")
    portable_packaging_allow_deploy_commands: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ALLOW_DEPLOY_COMMANDS", "false")).lower() == "true")
    portable_packaging_allow_background_daemons: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ALLOW_BACKGROUND_DAEMONS", "false")).lower() == "true")
    portable_packaging_allow_real_market_download: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ALLOW_REAL_MARKET_DOWNLOAD", "false")).lower() == "true")
    portable_packaging_allow_external_llm: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ALLOW_EXTERNAL_LLM", "false")).lower() == "true")
    portable_packaging_include_source: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_INCLUDE_SOURCE", "true")).lower() == "true")
    portable_packaging_include_docs: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_INCLUDE_DOCS", "true")).lower() == "true")
    portable_packaging_include_tests: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_INCLUDE_TESTS", "true")).lower() == "true")
    portable_packaging_include_configs: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_INCLUDE_CONFIGS", "true")).lower() == "true")
    portable_packaging_include_reports_manifest_only: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_INCLUDE_REPORTS_MANIFEST_ONLY", "true")).lower() == "true")
    portable_packaging_include_data_manifest_only: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_INCLUDE_DATA_MANIFEST_ONLY", "true")).lower() == "true")
    portable_packaging_max_inventory_files: int = field(default_factory=lambda: int(os.getenv("PORTABLE_PACKAGING_MAX_INVENTORY_FILES", "100000")))
    portable_packaging_max_manifest_file_mb: int = field(default_factory=lambda: int(os.getenv("PORTABLE_PACKAGING_MAX_MANIFEST_FILE_MB", "50")))
    portable_packaging_save_reports: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_SAVE_REPORTS", "true")).lower() == "true")
    portable_packaging_min_quality_score: float = field(default_factory=lambda: float(os.getenv("PORTABLE_PACKAGING_MIN_QUALITY_SCORE", "0.40")))


    backup_recovery_enabled: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_ENABLED", "true")).lower() == "true")
    default_backup_recovery_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_BACKUP_RECOVERY_PROFILE", "balanced_local_backup_recovery"))
    backup_recovery_default_language: str = field(default_factory=lambda: os.getenv("BACKUP_RECOVERY_DEFAULT_LANGUAGE", "tr"))
    backup_recovery_dry_run_default: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_DRY_RUN_DEFAULT", "true")).lower() == "true")
    backup_recovery_allow_backup_copy: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_ALLOW_BACKUP_COPY", "false")).lower() == "true")
    backup_recovery_allow_restore_copy: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_ALLOW_RESTORE_COPY", "false")).lower() == "true")
    backup_recovery_allow_overwrite: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_ALLOW_OVERWRITE", "false")).lower() == "true")
    backup_recovery_allow_delete: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_ALLOW_DELETE", "false")).lower() == "true")
    backup_recovery_allow_cloud_backup: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_ALLOW_CLOUD_BACKUP", "false")).lower() == "true")
    backup_recovery_allow_external_storage: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_ALLOW_EXTERNAL_STORAGE", "false")).lower() == "true")
    backup_recovery_allow_live_commands: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_ALLOW_LIVE_COMMANDS", "false")).lower() == "true")
    backup_recovery_allow_broker_commands: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_ALLOW_BROKER_COMMANDS", "false")).lower() == "true")
    backup_recovery_allow_deploy_commands: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_ALLOW_DEPLOY_COMMANDS", "false")).lower() == "true")
    backup_recovery_allow_background_daemons: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_ALLOW_BACKGROUND_DAEMONS", "false")).lower() == "true")
    backup_recovery_allow_real_market_download: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_ALLOW_REAL_MARKET_DOWNLOAD", "false")).lower() == "true")
    backup_recovery_allow_external_llm: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_ALLOW_EXTERNAL_LLM", "false")).lower() == "true")
    backup_recovery_include_source: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_INCLUDE_SOURCE", "true")).lower() == "true")
    backup_recovery_include_docs: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_INCLUDE_DOCS", "true")).lower() == "true")
    backup_recovery_include_tests: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_INCLUDE_TESTS", "true")).lower() == "true")
    backup_recovery_include_configs: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_INCLUDE_CONFIGS", "true")).lower() == "true")
    backup_recovery_include_reports_manifest_only: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_INCLUDE_REPORTS_MANIFEST_ONLY", "true")).lower() == "true")
    backup_recovery_include_data_manifest_only: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_INCLUDE_DATA_MANIFEST_ONLY", "true")).lower() == "true")
    backup_recovery_include_generated_manifests: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_INCLUDE_GENERATED_MANIFESTS", "true")).lower() == "true")
    backup_recovery_max_inventory_files: int = field(default_factory=lambda: int(os.getenv("BACKUP_RECOVERY_MAX_INVENTORY_FILES", "150000")))
    backup_recovery_max_hash_file_mb: int = field(default_factory=lambda: int(os.getenv("BACKUP_RECOVERY_MAX_HASH_FILE_MB", "100")))
    backup_recovery_save_reports: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_SAVE_REPORTS", "true")).lower() == "true")
    backup_recovery_min_quality_score: float = field(default_factory=lambda: float(os.getenv("BACKUP_RECOVERY_MIN_QUALITY_SCORE", "0.40")))

    @classmethod
    def from_env(cls) -> "Settings":
        return cls()


    # Evidence Governance Settings
    evidence_governance_enabled: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ENABLED", "true")).lower() == "true")
    default_evidence_governance_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_EVIDENCE_GOVERNANCE_PROFILE", "balanced_local_evidence"))
    evidence_governance_default_language: str = field(default_factory=lambda: os.getenv("EVIDENCE_GOVERNANCE_DEFAULT_LANGUAGE", "tr"))
    evidence_governance_dry_run_default: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_DRY_RUN_DEFAULT", "true")).lower() == "true")
    evidence_governance_allow_official_compliance_claims: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_OFFICIAL_COMPLIANCE_CLAIMS", "false")).lower() == "true")
    evidence_governance_allow_legal_opinion: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_LEGAL_OPINION", "false")).lower() == "true")
    evidence_governance_allow_cloud_export: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_CLOUD_EXPORT", "false")).lower() == "true")
    evidence_governance_allow_external_auditor_upload: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_EXTERNAL_AUDITOR_UPLOAD", "false")).lower() == "true")
    evidence_governance_allow_file_modification: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_FILE_MODIFICATION", "false")).lower() == "true")
    evidence_governance_allow_file_deletion: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_FILE_DELETION", "false")).lower() == "true")
    evidence_governance_allow_live_commands: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_LIVE_COMMANDS", "false")).lower() == "true")
    evidence_governance_allow_broker_commands: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_BROKER_COMMANDS", "false")).lower() == "true")
    evidence_governance_allow_deploy_commands: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_DEPLOY_COMMANDS", "false")).lower() == "true")
    evidence_governance_allow_background_daemons: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_BACKGROUND_DAEMONS", "false")).lower() == "true")
    evidence_governance_allow_real_market_download: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_REAL_MARKET_DOWNLOAD", "false")).lower() == "true")
    evidence_governance_allow_external_llm: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_EXTERNAL_LLM", "false")).lower() == "true")
    evidence_governance_scan_reports: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_SCAN_REPORTS", "true")).lower() == "true")
    evidence_governance_scan_data_lake: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_SCAN_DATA_LAKE", "true")).lower() == "true")
    evidence_governance_scan_docs: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_SCAN_DOCS", "true")).lower() == "true")
    evidence_governance_scan_generated_docs: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_SCAN_GENERATED_DOCS", "true")).lower() == "true")
    evidence_governance_scan_quality_outputs: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_SCAN_QUALITY_OUTPUTS", "true")).lower() == "true")
    evidence_governance_scan_security_outputs: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_SCAN_SECURITY_OUTPUTS", "true")).lower() == "true")
    evidence_governance_max_artifacts: int = field(default_factory=lambda: int(os.getenv("EVIDENCE_GOVERNANCE_MAX_ARTIFACTS", "200000")))
    evidence_governance_max_artifact_mb: int = field(default_factory=lambda: int(os.getenv("EVIDENCE_GOVERNANCE_MAX_ARTIFACT_MB", "50")))
    evidence_governance_freshness_days_warning: int = field(default_factory=lambda: int(os.getenv("EVIDENCE_GOVERNANCE_FRESHNESS_DAYS_WARNING", "30")))
    evidence_governance_save_reports: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_SAVE_REPORTS", "true")).lower() == "true")
    evidence_governance_min_quality_score: float = field(default_factory=lambda: float(os.getenv("EVIDENCE_GOVERNANCE_MIN_QUALITY_SCORE", "0.40")))

    def __post_init__(self):


        # Secrets Hygiene
        self.secrets_hygiene_enabled = str(os.getenv("SECRETS_HYGIENE_ENABLED", str(self.secrets_hygiene_enabled))).lower() == "true"
        self.default_secrets_hygiene_profile = str(os.getenv("DEFAULT_SECRETS_HYGIENE_PROFILE", self.default_secrets_hygiene_profile))
        self.secrets_hygiene_default_language = str(os.getenv("SECRETS_HYGIENE_DEFAULT_LANGUAGE", self.secrets_hygiene_default_language))
        self.secrets_hygiene_dry_run_default = str(os.getenv("SECRETS_HYGIENE_DRY_RUN_DEFAULT", str(self.secrets_hygiene_dry_run_default))).lower() == "true"
        self.secrets_hygiene_allow_secret_value_output = str(os.getenv("SECRETS_HYGIENE_ALLOW_SECRET_VALUE_OUTPUT", str(self.secrets_hygiene_allow_secret_value_output))).lower() == "true"
        self.secrets_hygiene_allow_file_modification = str(os.getenv("SECRETS_HYGIENE_ALLOW_FILE_MODIFICATION", str(self.secrets_hygiene_allow_file_modification))).lower() == "true"
        self.secrets_hygiene_allow_secret_deletion = str(os.getenv("SECRETS_HYGIENE_ALLOW_SECRET_DELETION", str(self.secrets_hygiene_allow_secret_deletion))).lower() == "true"
        self.secrets_hygiene_allow_cloud_vault = str(os.getenv("SECRETS_HYGIENE_ALLOW_CLOUD_VAULT", str(self.secrets_hygiene_allow_cloud_vault))).lower() == "true"
        self.secrets_hygiene_allow_external_scanner = str(os.getenv("SECRETS_HYGIENE_ALLOW_EXTERNAL_SCANNER", str(self.secrets_hygiene_allow_external_scanner))).lower() == "true"
        self.secrets_hygiene_allow_live_commands = str(os.getenv("SECRETS_HYGIENE_ALLOW_LIVE_COMMANDS", str(self.secrets_hygiene_allow_live_commands))).lower() == "true"
        self.secrets_hygiene_allow_broker_commands = str(os.getenv("SECRETS_HYGIENE_ALLOW_BROKER_COMMANDS", str(self.secrets_hygiene_allow_broker_commands))).lower() == "true"
        self.secrets_hygiene_allow_deploy_commands = str(os.getenv("SECRETS_HYGIENE_ALLOW_DEPLOY_COMMANDS", str(self.secrets_hygiene_allow_deploy_commands))).lower() == "true"
        self.secrets_hygiene_allow_background_daemons = str(os.getenv("SECRETS_HYGIENE_ALLOW_BACKGROUND_DAEMONS", str(self.secrets_hygiene_allow_background_daemons))).lower() == "true"
        self.secrets_hygiene_allow_real_market_download = str(os.getenv("SECRETS_HYGIENE_ALLOW_REAL_MARKET_DOWNLOAD", str(self.secrets_hygiene_allow_real_market_download))).lower() == "true"
        self.secrets_hygiene_allow_external_llm = str(os.getenv("SECRETS_HYGIENE_ALLOW_EXTERNAL_LLM", str(self.secrets_hygiene_allow_external_llm))).lower() == "true"
        self.secrets_hygiene_scan_source = str(os.getenv("SECRETS_HYGIENE_SCAN_SOURCE", str(self.secrets_hygiene_scan_source))).lower() == "true"
        self.secrets_hygiene_scan_docs = str(os.getenv("SECRETS_HYGIENE_SCAN_DOCS", str(self.secrets_hygiene_scan_docs))).lower() == "true"
        self.secrets_hygiene_scan_tests = str(os.getenv("SECRETS_HYGIENE_SCAN_TESTS", str(self.secrets_hygiene_scan_tests))).lower() == "true"
        self.secrets_hygiene_scan_configs = str(os.getenv("SECRETS_HYGIENE_SCAN_CONFIGS", str(self.secrets_hygiene_scan_configs))).lower() == "true"
        self.secrets_hygiene_scan_reports = str(os.getenv("SECRETS_HYGIENE_SCAN_REPORTS", str(self.secrets_hygiene_scan_reports))).lower() == "true"
        self.secrets_hygiene_scan_data_manifests = str(os.getenv("SECRETS_HYGIENE_SCAN_DATA_MANIFESTS", str(self.secrets_hygiene_scan_data_manifests))).lower() == "true"
        self.secrets_hygiene_scan_generated_outputs = str(os.getenv("SECRETS_HYGIENE_SCAN_GENERATED_OUTPUTS", str(self.secrets_hygiene_scan_generated_outputs))).lower() == "true"

        try:
            self.secrets_hygiene_max_files = int(os.getenv("SECRETS_HYGIENE_MAX_FILES", str(self.secrets_hygiene_max_files)))
        except ValueError:
            pass

        try:
            self.secrets_hygiene_max_file_mb = int(os.getenv("SECRETS_HYGIENE_MAX_FILE_MB", str(self.secrets_hygiene_max_file_mb)))
        except ValueError:
            pass

        try:
            self.secrets_hygiene_entropy_threshold = float(os.getenv("SECRETS_HYGIENE_ENTROPY_THRESHOLD", str(self.secrets_hygiene_entropy_threshold)))
        except ValueError:
            pass

        try:
            self.secrets_hygiene_mask_keep_start = int(os.getenv("SECRETS_HYGIENE_MASK_KEEP_START", str(self.secrets_hygiene_mask_keep_start)))
        except ValueError:
            pass

        try:
            self.secrets_hygiene_mask_keep_end = int(os.getenv("SECRETS_HYGIENE_MASK_KEEP_END", str(self.secrets_hygiene_mask_keep_end)))
        except ValueError:
            pass

        self.secrets_hygiene_save_reports = str(os.getenv("SECRETS_HYGIENE_SAVE_REPORTS", str(self.secrets_hygiene_save_reports))).lower() == "true"

        try:
            self.secrets_hygiene_min_quality_score = float(os.getenv("SECRETS_HYGIENE_MIN_QUALITY_SCORE", str(self.secrets_hygiene_min_quality_score)))
        except ValueError:
            pass







        """Validate settings after initialization."""
        # Enforce live trading is False regardless of env variable
        env_live_trading = os.getenv("LIVE_TRADING_ENABLED", "false").lower() == "true"
        if env_live_trading:
            logger.warning(
                "LIVE_TRADING_ENABLED is set to true in environment, but this project "
                "does not support live trading. Forcing live_trading_enabled to False."
            )
        # Risk Precheck Layer parameters

    risk_precheck_enabled: bool = field(
        default_factory=lambda: str(os.getenv("RISK_PRECHECK_ENABLED", "true")).lower()
        == "true"
    )
    risk_candidates_enabled: bool = field(
        default_factory=lambda: str(
            os.getenv("RISK_CANDIDATES_ENABLED", "true")
        ).lower()
        == "true"
    )
    default_risk_profile: str = field(
        default_factory=lambda: os.getenv(
            "DEFAULT_RISK_PROFILE", "balanced_pretrade_risk"
        )
    )
    default_risk_timeframe: str = field(
        default_factory=lambda: os.getenv("DEFAULT_RISK_TIMEFRAME", "1d")
    )
    risk_max_total_pretrade_risk: float = field(
        default_factory=lambda: float(os.getenv("RISK_MAX_TOTAL_PRETRADE_RISK", "0.70"))
    )
    risk_min_readiness_score: float = field(
        default_factory=lambda: float(os.getenv("RISK_MIN_READINESS_SCORE", "0.45"))
    )
    risk_max_volatility_risk: float = field(
        default_factory=lambda: float(os.getenv("RISK_MAX_VOLATILITY_RISK", "0.75"))
    )
    risk_max_gap_risk: float = field(
        default_factory=lambda: float(os.getenv("RISK_MAX_GAP_RISK", "0.75"))
    )
    risk_max_liquidity_risk: float = field(
        default_factory=lambda: float(os.getenv("RISK_MAX_LIQUIDITY_RISK", "0.75"))
    )
    risk_max_data_quality_risk: float = field(
        default_factory=lambda: float(os.getenv("RISK_MAX_DATA_QUALITY_RISK", "0.60"))
    )
    risk_max_regime_risk: float = field(
        default_factory=lambda: float(os.getenv("RISK_MAX_REGIME_RISK", "0.70"))
    )
    risk_max_mtf_risk: float = field(
        default_factory=lambda: float(os.getenv("RISK_MAX_MTF_RISK", "0.70"))
    )
    risk_max_macro_risk: float = field(
        default_factory=lambda: float(os.getenv("RISK_MAX_MACRO_RISK", "0.80"))
    )
    risk_block_on_invalid_data_quality: bool = field(
        default_factory=lambda: str(
            os.getenv("RISK_BLOCK_ON_INVALID_DATA_QUALITY", "true")
        ).lower()
        == "true"
    )
    risk_block_on_extreme_volatility: bool = field(
        default_factory=lambda: str(
            os.getenv("RISK_BLOCK_ON_EXTREME_VOLATILITY", "true")
        ).lower()
        == "true"
    )
    risk_block_on_high_conflict: bool = field(
        default_factory=lambda: str(
            os.getenv("RISK_BLOCK_ON_HIGH_CONFLICT", "true")
        ).lower()
        == "true"
    )
    risk_allow_watchlist_when_borderline: bool = field(
        default_factory=lambda: str(
            os.getenv("RISK_ALLOW_WATCHLIST_WHEN_BORDERLINE", "true")
        ).lower()
        == "true"
    )
    save_risk_candidates: bool = field(
        default_factory=lambda: str(os.getenv("SAVE_RISK_CANDIDATES", "true")).lower()
        == "true"
    )
    save_risk_pool: bool = field(
        default_factory=lambda: str(os.getenv("SAVE_RISK_POOL", "true")).lower()
        == "true"
    )

    # Phase 24: Theoretical Sizing Candidate Layer
    sizing_candidates_enabled: bool = field(
        default_factory=lambda: str(
            os.getenv("SIZING_CANDIDATES_ENABLED", "true")
        ).lower()
        == "true"
    )
    theoretical_position_sizing_enabled: bool = field(
        default_factory=lambda: str(
            os.getenv("THEORETICAL_POSITION_SIZING_ENABLED", "true")
        ).lower()
        == "true"
    )
    default_sizing_profile: str = field(
        default_factory=lambda: os.getenv(
            "DEFAULT_SIZING_PROFILE", "balanced_theoretical_sizing"
        )
    )
    default_sizing_timeframe: str = field(
        default_factory=lambda: os.getenv("DEFAULT_SIZING_TIMEFRAME", "1d")
    )
    theoretical_account_equity: float = field(
        default_factory=lambda: float(
            os.getenv("THEORETICAL_ACCOUNT_EQUITY", "100000.0")
        )
    )
    theoretical_base_currency: str = field(
        default_factory=lambda: os.getenv("THEORETICAL_BASE_CURRENCY", "TRY")
    )
    theoretical_risk_per_candidate: float = field(
        default_factory=lambda: float(
            os.getenv("THEORETICAL_RISK_PER_CANDIDATE", "0.005")
        )
    )
    theoretical_max_risk_per_symbol: float = field(
        default_factory=lambda: float(
            os.getenv("THEORETICAL_MAX_RISK_PER_SYMBOL", "0.02")
        )
    )
    theoretical_max_risk_per_asset_class: float = field(
        default_factory=lambda: float(
            os.getenv("THEORETICAL_MAX_RISK_PER_ASSET_CLASS", "0.05")
        )
    )
    theoretical_max_total_portfolio_risk: float = field(
        default_factory=lambda: float(
            os.getenv("THEORETICAL_MAX_TOTAL_PORTFOLIO_RISK", "0.15")
        )
    )
    sizing_min_risk_readiness_score: float = field(
        default_factory=lambda: float(
            os.getenv("SIZING_MIN_RISK_READINESS_SCORE", "0.50")
        )
    )
    sizing_max_total_pretrade_risk: float = field(
        default_factory=lambda: float(
            os.getenv("SIZING_MAX_TOTAL_PRETRADE_RISK", "0.70")
        )
    )
    sizing_min_data_quality_score: float = field(
        default_factory=lambda: float(
            os.getenv("SIZING_MIN_DATA_QUALITY_SCORE", "0.50")
        )
    )
    sizing_use_atr_based_unit: bool = field(
        default_factory=lambda: str(
            os.getenv("SIZING_USE_ATR_BASED_UNIT", "true")
        ).lower()
        == "true"
    )
    sizing_use_volatility_adjustment: bool = field(
        default_factory=lambda: str(
            os.getenv("SIZING_USE_VOLATILITY_ADJUSTMENT", "true")
        ).lower()
        == "true"
    )
    sizing_block_on_risk_rejection: bool = field(
        default_factory=lambda: str(
            os.getenv("SIZING_BLOCK_ON_RISK_REJECTION", "true")
        ).lower()
        == "true"
    )
    sizing_allow_watchlist_for_borderline: bool = field(
        default_factory=lambda: str(
            os.getenv("SIZING_ALLOW_WATCHLIST_FOR_BORDERLINE", "true")
        ).lower()
        == "true"
    )
    save_sizing_candidates: bool = field(
        default_factory=lambda: str(os.getenv("SAVE_SIZING_CANDIDATES", "true")).lower()
        == "true"
    )
    save_sizing_pool: bool = field(
        default_factory=lambda: str(os.getenv("SAVE_SIZING_POOL", "true")).lower()
        == "true"
    )

    # Force live trading off

    # Phase 26: Backtest Engine and Trade Lifecycle
    backtest_enabled: bool = field(
        default_factory=lambda: str(os.getenv("BACKTEST_ENABLED", "true")).lower()
        == "true"
    )
    backtest_engine_enabled: bool = field(
        default_factory=lambda: str(
            os.getenv("BACKTEST_ENGINE_ENABLED", "true")
        ).lower()
        == "true"
    )
    default_backtest_profile: str = field(
        default_factory=lambda: os.getenv(
            "DEFAULT_BACKTEST_PROFILE", "balanced_candidate_backtest"
        )
    )
    default_backtest_timeframe: str = field(
        default_factory=lambda: os.getenv("DEFAULT_BACKTEST_TIMEFRAME", "1d")
    )
    default_backtest_initial_equity: float = field(
        default_factory=lambda: float(
            os.getenv("DEFAULT_BACKTEST_INITIAL_EQUITY", "100000.0")
        )
    )
    default_backtest_base_currency: str = field(
        default_factory=lambda: os.getenv("DEFAULT_BACKTEST_BASE_CURRENCY", "TRY")
    )
    backtest_allow_same_bar_exit: bool = field(
        default_factory=lambda: str(
            os.getenv("BACKTEST_ALLOW_SAME_BAR_EXIT", "false")
        ).lower()
        == "true"
    )
    backtest_entry_delay_bars: int = field(
        default_factory=lambda: int(os.getenv("BACKTEST_ENTRY_DELAY_BARS", "1"))
    )
    backtest_exit_delay_bars: int = field(
        default_factory=lambda: int(os.getenv("BACKTEST_EXIT_DELAY_BARS", "1"))
    )
    backtest_use_next_bar_open_for_entry: bool = field(
        default_factory=lambda: str(
            os.getenv("BACKTEST_USE_NEXT_BAR_OPEN_FOR_ENTRY", "true")
        ).lower()
        == "true"
    )
    backtest_use_next_bar_open_for_exit: bool = field(
        default_factory=lambda: str(
            os.getenv("BACKTEST_USE_NEXT_BAR_OPEN_FOR_EXIT", "true")
        ).lower()
        == "true"
    )
    backtest_include_transaction_costs: bool = field(
        default_factory=lambda: str(
            os.getenv("BACKTEST_INCLUDE_TRANSACTION_COSTS", "true")
        ).lower()
        == "true"
    )
    backtest_default_fee_bps: float = field(
        default_factory=lambda: float(os.getenv("BACKTEST_DEFAULT_FEE_BPS", "5.0"))
    )
    backtest_default_slippage_bps: float = field(
        default_factory=lambda: float(os.getenv("BACKTEST_DEFAULT_SLIPPAGE_BPS", "5.0"))
    )
    backtest_max_holding_bars: int = field(
        default_factory=lambda: int(os.getenv("BACKTEST_MAX_HOLDING_BARS", "20"))
    )
    backtest_single_position_per_symbol: bool = field(
        default_factory=lambda: str(
            os.getenv("BACKTEST_SINGLE_POSITION_PER_SYMBOL", "true")
        ).lower()
        == "true"
    )
    backtest_block_overlapping_positions: bool = field(
        default_factory=lambda: str(
            os.getenv("BACKTEST_BLOCK_OVERLAPPING_POSITIONS", "true")
        ).lower()
        == "true"
    )
    backtest_require_level_candidate: bool = field(
        default_factory=lambda: str(
            os.getenv("BACKTEST_REQUIRE_LEVEL_CANDIDATE", "true")
        ).lower()
        == "true"
    )
    backtest_require_sizing_candidate: bool = field(
        default_factory=lambda: str(
            os.getenv("BACKTEST_REQUIRE_SIZING_CANDIDATE", "true")
        ).lower()
        == "true"
    )
    save_backtest_results: bool = field(
        default_factory=lambda: str(os.getenv("SAVE_BACKTEST_RESULTS", "true")).lower()
        == "true"
    )
    save_backtest_trades: bool = field(
        default_factory=lambda: str(os.getenv("SAVE_BACKTEST_TRADES", "true")).lower()
        == "true"
    )
    save_backtest_equity_curve: bool = field(
        default_factory=lambda: str(
            os.getenv("SAVE_BACKTEST_EQUITY_CURVE", "true")
        ).lower()
        == "true"
    )


    # Phase 29: ML Dataset Preparation
    ml_dataset_enabled: bool = field(
        default_factory=lambda: str(os.getenv("ML_DATASET_ENABLED", "true")).lower()
        == "true"
    )
    ml_target_engineering_enabled: bool = field(
        default_factory=lambda: str(
            os.getenv("ML_TARGET_ENGINEERING_ENABLED", "true")
        ).lower()
        == "true"
    )
    default_ml_dataset_profile: str = field(
        default_factory=lambda: os.getenv(
            "DEFAULT_ML_DATASET_PROFILE", "balanced_supervised_dataset"
        )
    )
    default_ml_dataset_timeframe: str = field(
        default_factory=lambda: os.getenv("DEFAULT_ML_DATASET_TIMEFRAME", "1d")
    )
    ml_default_forward_return_horizons: tuple[int, ...] = field(
        default_factory=lambda: tuple(
            int(x.strip())
            for x in os.getenv("ML_DEFAULT_FORWARD_RETURN_HORIZONS", "1,3,5,10,20").split(",")
            if x.strip()
        )
    )
    ml_default_forward_volatility_horizons: tuple[int, ...] = field(
        default_factory=lambda: tuple(
            int(x.strip())
            for x in os.getenv("ML_DEFAULT_FORWARD_VOLATILITY_HORIZONS", "5,10,20").split(",")
            if x.strip()
        )
    )
    ml_default_future_drawdown_horizons: tuple[int, ...] = field(
        default_factory=lambda: tuple(
            int(x.strip())
            for x in os.getenv("ML_DEFAULT_FUTURE_DRAWDOWN_HORIZONS", "5,10,20").split(",")
            if x.strip()
        )
    )
    ml_direction_threshold: float = field(
        default_factory=lambda: float(os.getenv("ML_DIRECTION_THRESHOLD", "0.002"))
    )
    ml_positive_return_threshold: float = field(
        default_factory=lambda: float(os.getenv("ML_POSITIVE_RETURN_THRESHOLD", "0.005"))
    )
    ml_negative_return_threshold: float = field(
        default_factory=lambda: float(os.getenv("ML_NEGATIVE_RETURN_THRESHOLD", "-0.005"))
    )
    ml_min_rows_for_dataset: int = field(
        default_factory=lambda: int(os.getenv("ML_MIN_ROWS_FOR_DATASET", "200"))
    )
    ml_max_feature_nan_ratio: float = field(
        default_factory=lambda: float(os.getenv("ML_MAX_FEATURE_NAN_RATIO", "0.35"))
    )
    ml_max_target_nan_ratio: float = field(
        default_factory=lambda: float(os.getenv("ML_MAX_TARGET_NAN_RATIO", "0.20"))
    )
    ml_use_purged_split: bool = field(
        default_factory=lambda: str(os.getenv("ML_USE_PURGED_SPLIT", "true")).lower()
        == "true"
    )
    ml_embargo_bars: int = field(
        default_factory=lambda: int(os.getenv("ML_EMBARGO_BARS", "5"))
    )
    ml_test_size_ratio: float = field(
        default_factory=lambda: float(os.getenv("ML_TEST_SIZE_RATIO", "0.20"))
    )
    ml_validation_size_ratio: float = field(
        default_factory=lambda: float(os.getenv("ML_VALIDATION_SIZE_RATIO", "0.20"))
    )
    ml_save_feature_matrix: bool = field(
        default_factory=lambda: str(os.getenv("ML_SAVE_FEATURE_MATRIX", "true")).lower()
        == "true"
    )
    ml_save_target_frame: bool = field(
        default_factory=lambda: str(os.getenv("ML_SAVE_TARGET_FRAME", "true")).lower()
        == "true"
    )
    ml_save_supervised_dataset: bool = field(
        default_factory=lambda: str(
            os.getenv("ML_SAVE_SUPERVISED_DATASET", "true")
        ).lower()
        == "true"
    )

    # Phase 30: ML Training Baseline
    ml_training_enabled: bool = field(
        default_factory=lambda: str(os.getenv("ML_TRAINING_ENABLED", "true")).lower() == "true"
    )
    ml_baseline_models_enabled: bool = field(
        default_factory=lambda: str(os.getenv("ML_BASELINE_MODELS_ENABLED", "true")).lower() == "true"
    )
    ml_model_registry_enabled: bool = field(
        default_factory=lambda: str(os.getenv("ML_MODEL_REGISTRY_ENABLED", "true")).lower() == "true"
    )
    default_ml_training_profile: str = field(
        default_factory=lambda: os.getenv("DEFAULT_ML_TRAINING_PROFILE", "balanced_baseline_training")
    )
    default_ml_training_timeframe: str = field(
        default_factory=lambda: os.getenv("DEFAULT_ML_TRAINING_TIMEFRAME", "1d")
    )
    default_ml_training_dataset_profile: str = field(
        default_factory=lambda: os.getenv("DEFAULT_ML_TRAINING_DATASET_PROFILE", "balanced_supervised_dataset")
    )
    default_ml_target_column: str = field(
        default_factory=lambda: os.getenv("DEFAULT_ML_TARGET_COLUMN", "target_direction_class_5")
    )
    ml_training_task_type: str = field(
        default_factory=lambda: os.getenv("ML_TRAINING_TASK_TYPE", "classification")
    )
    ml_allowed_model_families: tuple = field(
        default_factory=lambda: tuple(os.getenv("ML_ALLOWED_MODEL_FAMILIES", "dummy,logistic_regression,random_forest,hist_gradient_boosting").split(","))
    )
    ml_default_model_family: str = field(
        default_factory=lambda: os.getenv("ML_DEFAULT_MODEL_FAMILY", "random_forest")
    )
    ml_cv_n_splits: int = field(
        default_factory=lambda: int(os.getenv("ML_CV_N_SPLITS", "5"))
    )
    ml_cv_embargo_bars: int = field(
        default_factory=lambda: int(os.getenv("ML_CV_EMBARGO_BARS", "5"))
    )
    ml_min_train_rows: int = field(
        default_factory=lambda: int(os.getenv("ML_MIN_TRAIN_ROWS", "300"))
    )
    ml_min_test_rows: int = field(
        default_factory=lambda: int(os.getenv("ML_MIN_TEST_ROWS", "50"))
    )
    ml_max_feature_nan_ratio_for_training: float = field(
        default_factory=lambda: float(os.getenv("ML_MAX_FEATURE_NAN_RATIO_FOR_TRAINING", "0.35"))
    )
    ml_drop_high_nan_features: bool = field(
        default_factory=lambda: str(os.getenv("ML_DROP_HIGH_NAN_FEATURES", "true")).lower() == "true"
    )
    ml_enable_basic_imputation: bool = field(
        default_factory=lambda: str(os.getenv("ML_ENABLE_BASIC_IMPUTATION", "true")).lower() == "true"
    )
    ml_enable_basic_scaling: bool = field(
        default_factory=lambda: str(os.getenv("ML_ENABLE_BASIC_SCALING", "true")).lower() == "true"
    )
    ml_save_model_artifacts: bool = field(
        default_factory=lambda: str(os.getenv("ML_SAVE_MODEL_ARTIFACTS", "true")).lower() == "true"
    )
    ml_save_model_registry_entries: bool = field(
        default_factory=lambda: str(os.getenv("ML_SAVE_MODEL_REGISTRY_ENTRIES", "true")).lower() == "true"
    )
    ml_save_model_evaluation_reports: bool = field(
        default_factory=lambda: str(os.getenv("ML_SAVE_MODEL_EVALUATION_REPORTS", "true")).lower() == "true"
    )

    # Phase 32: ML Context Integration
    ml_context_integration_enabled: bool = field(
        default_factory=lambda: str(os.getenv("ML_CONTEXT_INTEGRATION_ENABLED", "true")).lower() == "true"
    )
    ml_model_aware_scoring_enabled: bool = field(
        default_factory=lambda: str(os.getenv("ML_MODEL_AWARE_SCORING_ENABLED", "true")).lower() == "true"
    )
    ml_conflict_filter_enabled: bool = field(
        default_factory=lambda: str(os.getenv("ML_CONFLICT_FILTER_ENABLED", "true")).lower() == "true"
    )
    ml_uncertainty_filter_enabled: bool = field(
        default_factory=lambda: str(os.getenv("ML_UNCERTAINTY_FILTER_ENABLED", "true")).lower() == "true"
    )
    default_ml_integration_profile: str = field(
        default_factory=lambda: os.getenv("DEFAULT_ML_INTEGRATION_PROFILE", "balanced_ml_context_integration")
    )
    default_ml_integration_timeframe: str = field(
        default_factory=lambda: os.getenv("DEFAULT_ML_INTEGRATION_TIMEFRAME", "1d")
    )
    ml_context_min_confidence_score: float = field(
        default_factory=lambda: float(os.getenv("ML_CONTEXT_MIN_CONFIDENCE_SCORE", "0.45"))
    )
    ml_context_max_uncertainty_score: float = field(
        default_factory=lambda: float(os.getenv("ML_CONTEXT_MAX_UNCERTAINTY_SCORE", "0.70"))
    )
    ml_context_max_leakage_risk_score: float = field(
        default_factory=lambda: float(os.getenv("ML_CONTEXT_MAX_LEAKAGE_RISK_SCORE", "0.20"))
    )
    ml_context_min_model_quality_score: float = field(
        default_factory=lambda: float(os.getenv("ML_CONTEXT_MIN_MODEL_QUALITY_SCORE", "0.50"))
    )
    ml_context_min_dataset_quality_score: float = field(
        default_factory=lambda: float(os.getenv("ML_CONTEXT_MIN_DATASET_QUALITY_SCORE", "0.50"))
    )
    ml_context_support_weight: float = field(
        default_factory=lambda: float(os.getenv("ML_CONTEXT_SUPPORT_WEIGHT", "0.10"))
    )
    ml_context_conflict_penalty_weight: float = field(
        default_factory=lambda: float(os.getenv("ML_CONTEXT_CONFLICT_PENALTY_WEIGHT", "0.10"))
    )
    ml_context_uncertainty_penalty_weight: float = field(
        default_factory=lambda: float(os.getenv("ML_CONTEXT_UNCERTAINTY_PENALTY_WEIGHT", "0.05"))
    )
    ml_context_enable_signal_scoring: bool = field(
        default_factory=lambda: str(os.getenv("ML_CONTEXT_ENABLE_SIGNAL_SCORING", "true")).lower() == "true"
    )
    ml_context_enable_decision_scoring: bool = field(
        default_factory=lambda: str(os.getenv("ML_CONTEXT_ENABLE_DECISION_SCORING", "true")).lower() == "true"
    )
    ml_context_enable_strategy_scoring: bool = field(
        default_factory=lambda: str(os.getenv("ML_CONTEXT_ENABLE_STRATEGY_SCORING", "true")).lower() == "true"
    )
    ml_context_enable_risk_precheck: bool = field(
        default_factory=lambda: str(os.getenv("ML_CONTEXT_ENABLE_RISK_PRECHECK", "false")).lower() == "true"
    )
    ml_context_save_integration_features: bool = field(
        default_factory=lambda: str(os.getenv("ML_CONTEXT_SAVE_INTEGRATION_FEATURES", "true")).lower() == "true"
    )
    ml_context_save_alignment_reports: bool = field(
        default_factory=lambda: str(os.getenv("ML_CONTEXT_SAVE_ALIGNMENT_REPORTS", "true")).lower() == "true"
    )



    # Phase 34: Notification Settings
    notifications_enabled: bool = field(
        default_factory=lambda: str(os.getenv("NOTIFICATIONS_ENABLED", "true")).lower() == "true"
    )
    telegram_enabled: bool = field(
        default_factory=lambda: str(os.getenv("TELEGRAM_ENABLED", "false")).lower() == "true"
    )
    telegram_dry_run: bool = field(
        default_factory=lambda: str(os.getenv("TELEGRAM_DRY_RUN", "true")).lower() == "true"
    )
    default_notification_profile: str = field(
        default_factory=lambda: os.getenv("DEFAULT_NOTIFICATION_PROFILE", "balanced_telegram_reporting")
    )
    telegram_bot_token: str | None = field(
        default_factory=lambda: os.getenv("TELEGRAM_BOT_TOKEN")
    )
    telegram_chat_id: str | None = field(
        default_factory=lambda: os.getenv("TELEGRAM_CHAT_ID")
    )
    telegram_parse_mode: str = field(
        default_factory=lambda: os.getenv("TELEGRAM_PARSE_MODE", "HTML")
    )
    telegram_disable_web_page_preview: bool = field(
        default_factory=lambda: str(os.getenv("TELEGRAM_DISABLE_WEB_PAGE_PREVIEW", "true")).lower() == "true"
    )
    telegram_message_max_chars: int = field(
        default_factory=lambda: int(os.getenv("TELEGRAM_MESSAGE_MAX_CHARS", "3500"))
    )
    telegram_rate_limit_seconds: float = field(
        default_factory=lambda: float(os.getenv("TELEGRAM_RATE_LIMIT_SECONDS", "1.0"))
    )
    telegram_send_test_on_startup: bool = field(
        default_factory=lambda: str(os.getenv("TELEGRAM_SEND_TEST_ON_STARTUP", "false")).lower() == "true"
    )
    notification_save_message_logs: bool = field(
        default_factory=lambda: str(os.getenv("NOTIFICATION_SAVE_MESSAGE_LOGS", "true")).lower() == "true"
    )
    notification_save_delivery_audit: bool = field(
        default_factory=lambda: str(os.getenv("NOTIFICATION_SAVE_DELIVERY_AUDIT", "true")).lower() == "true"
    )
    notification_include_paper_summary: bool = field(
        default_factory=lambda: str(os.getenv("NOTIFICATION_INCLUDE_PAPER_SUMMARY", "true")).lower() == "true"
    )
    notification_include_backtest_summary: bool = field(
        default_factory=lambda: str(os.getenv("NOTIFICATION_INCLUDE_BACKTEST_SUMMARY", "true")).lower() == "true"
    )
    notification_include_ml_summary: bool = field(
        default_factory=lambda: str(os.getenv("NOTIFICATION_INCLUDE_ML_SUMMARY", "true")).lower() == "true"
    )
    notification_include_quality_alerts: bool = field(
        default_factory=lambda: str(os.getenv("NOTIFICATION_INCLUDE_QUALITY_ALERTS", "true")).lower() == "true"
    )
    notification_include_error_alerts: bool = field(
        default_factory=lambda: str(os.getenv("NOTIFICATION_INCLUDE_ERROR_ALERTS", "true")).lower() == "true"
    )
    notification_max_symbols_in_digest: int = field(
        default_factory=lambda: int(os.getenv("NOTIFICATION_MAX_SYMBOLS_IN_DIGEST", "20"))
    )
    notification_max_rows_per_section: int = field(
        default_factory=lambda: int(os.getenv("NOTIFICATION_MAX_ROWS_PER_SECTION", "10"))
    )


    # Orchestration Settings
    orchestration_enabled: bool = field(
        default_factory=lambda: str(os.getenv("ORCHESTRATION_ENABLED", "true")).lower() == "true"
    )
    pipeline_orchestrator_enabled: bool = field(
        default_factory=lambda: str(os.getenv("PIPELINE_ORCHESTRATOR_ENABLED", "true")).lower() == "true"
    )
    default_orchestration_profile: str = field(
        default_factory=lambda: os.getenv("DEFAULT_ORCHESTRATION_PROFILE", "balanced_research_orchestration")
    )
    default_workflow_name: str = field(
        default_factory=lambda: os.getenv("DEFAULT_WORKFLOW_NAME", "daily_research_workflow")
    )
    orchestration_default_timeframe: str = field(
        default_factory=lambda: os.getenv("ORCHESTRATION_DEFAULT_TIMEFRAME", "1d")
    )
    orchestration_max_symbols_per_run: int = field(
        default_factory=lambda: int(os.getenv("ORCHESTRATION_MAX_SYMBOLS_PER_RUN", "50"))
    )
    orchestration_continue_on_symbol_error: bool = field(
        default_factory=lambda: str(os.getenv("ORCHESTRATION_CONTINUE_ON_SYMBOL_ERROR", "true")).lower() == "true"
    )
    orchestration_continue_on_job_error: bool = field(
        default_factory=lambda: str(os.getenv("ORCHESTRATION_CONTINUE_ON_JOB_ERROR", "true")).lower() == "true"
    )
    orchestration_retry_failed_jobs: bool = field(
        default_factory=lambda: str(os.getenv("ORCHESTRATION_RETRY_FAILED_JOBS", "false")).lower() == "true"
    )
    orchestration_max_retries: int = field(
        default_factory=lambda: int(os.getenv("ORCHESTRATION_MAX_RETRIES", "1"))
    )
    orchestration_retry_delay_seconds: float = field(
        default_factory=lambda: float(os.getenv("ORCHESTRATION_RETRY_DELAY_SECONDS", "2.0"))
    )
    orchestration_save_run_manifest: bool = field(
        default_factory=lambda: str(os.getenv("ORCHESTRATION_SAVE_RUN_MANIFEST", "true")).lower() == "true"
    )
    orchestration_save_dependency_graph: bool = field(
        default_factory=lambda: str(os.getenv("ORCHESTRATION_SAVE_DEPENDENCY_GRAPH", "true")).lower() == "true"
    )
    orchestration_save_execution_plan: bool = field(
        default_factory=lambda: str(os.getenv("ORCHESTRATION_SAVE_EXECUTION_PLAN", "true")).lower() == "true"
    )
    orchestration_save_job_logs: bool = field(
        default_factory=lambda: str(os.getenv("ORCHESTRATION_SAVE_JOB_LOGS", "true")).lower() == "true"
    )
    orchestration_enable_notifications: bool = field(
        default_factory=lambda: str(os.getenv("ORCHESTRATION_ENABLE_NOTIFICATIONS", "false")).lower() == "true"
    )
    orchestration_notification_on_failure: bool = field(
        default_factory=lambda: str(os.getenv("ORCHESTRATION_NOTIFICATION_ON_FAILURE", "true")).lower() == "true"
    )
    orchestration_notification_on_success: bool = field(
        default_factory=lambda: str(os.getenv("ORCHESTRATION_NOTIFICATION_ON_SUCCESS", "false")).lower() == "true"
    )
    orchestration_dry_run: bool = field(
        default_factory=lambda: str(os.getenv("ORCHESTRATION_DRY_RUN", "true")).lower() == "true"
    )


    # Phase 37: Security, Hardening & Readiness
    security_audit_enabled: bool = field(default_factory=lambda: str(os.getenv("SECURITY_AUDIT_ENABLED", "true")).lower() == "true")
    config_hardening_enabled: bool = field(default_factory=lambda: str(os.getenv("CONFIG_HARDENING_ENABLED", "true")).lower() == "true")
    secret_hygiene_enabled: bool = field(default_factory=lambda: str(os.getenv("SECRET_HYGIENE_ENABLED", "true")).lower() == "true")
    production_readiness_audit_enabled: bool = field(default_factory=lambda: str(os.getenv("PRODUCTION_READINESS_AUDIT_ENABLED", "true")).lower() == "true")
    default_security_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_SECURITY_PROFILE", "balanced_local_security"))
    security_fail_on_secret_leak: bool = field(default_factory=lambda: str(os.getenv("SECURITY_FAIL_ON_SECRET_LEAK", "true")).lower() == "true")
    security_fail_on_unsafe_live_flags: bool = field(default_factory=lambda: str(os.getenv("SECURITY_FAIL_ON_UNSAFE_LIVE_FLAGS", "true")).lower() == "true")
    security_fail_on_path_traversal_risk: bool = field(default_factory=lambda: str(os.getenv("SECURITY_FAIL_ON_PATH_TRAVERSAL_RISK", "true")).lower() == "true")
    security_allow_telegram_send: bool = field(default_factory=lambda: str(os.getenv("SECURITY_ALLOW_TELEGRAM_SEND", "false")).lower() == "true")
    security_allow_live_trading: bool = field(default_factory=lambda: str(os.getenv("SECURITY_ALLOW_LIVE_TRADING", "false")).lower() == "true")
    security_allow_broker_credentials: bool = field(default_factory=lambda: str(os.getenv("SECURITY_ALLOW_BROKER_CREDENTIALS", "false")).lower() == "true")
    security_allow_network_calls_except_data_and_telegram: bool = field(default_factory=lambda: str(os.getenv("SECURITY_ALLOW_NETWORK_CALLS_EXCEPT_DATA_AND_TELEGRAM", "true")).lower() == "true")
    security_require_dry_run_defaults: bool = field(default_factory=lambda: str(os.getenv("SECURITY_REQUIRE_DRY_RUN_DEFAULTS", "true")).lower() == "true")
    security_required_gitignore_patterns: tuple[str, ...] = field(default_factory=lambda: tuple(os.getenv("SECURITY_REQUIRED_GITIGNORE_PATTERNS", ".env,*.key,*.pem,data/lake/ml/model_artifacts/*.joblib").split(",")))
    security_sensitive_env_names: tuple[str, ...] = field(default_factory=lambda: tuple(os.getenv("SECURITY_SENSITIVE_ENV_NAMES", "TOKEN,SECRET,KEY,PASSWORD,CHAT_ID,API").split(",")))
    security_scan_text_extensions: tuple[str, ...] = field(default_factory=lambda: tuple(os.getenv("SECURITY_SCAN_TEXT_EXTENSIONS", ".py,.md,.txt,.json,.yaml,.yml,.env,.example").split(",")))
    security_max_file_scan_mb: int = field(default_factory=lambda: int(os.getenv("SECURITY_MAX_FILE_SCAN_MB", "5")))
    security_save_audit_reports: bool = field(default_factory=lambda: str(os.getenv("SECURITY_SAVE_AUDIT_REPORTS", "true")).lower() == "true")
    security_save_readiness_reports: bool = field(default_factory=lambda: str(os.getenv("SECURITY_SAVE_READINESS_REPORTS", "true")).lower() == "true")
    security_notification_on_critical: bool = field(default_factory=lambda: str(os.getenv("SECURITY_NOTIFICATION_ON_CRITICAL", "false")).lower() == "true")


    # Phase 40: Report Exports, Archive and Comparisons
    report_exports_enabled: bool = field(default_factory=lambda: str(os.getenv("REPORT_EXPORTS_ENABLED", "true")).lower() == "true")
    report_html_export_enabled: bool = field(default_factory=lambda: str(os.getenv("REPORT_HTML_EXPORT_ENABLED", "true")).lower() == "true")
    report_pdf_export_enabled: bool = field(default_factory=lambda: str(os.getenv("REPORT_PDF_EXPORT_ENABLED", "true")).lower() == "true")
    default_report_export_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_REPORT_EXPORT_PROFILE", "balanced_report_export"))
    report_export_default_timeframe: str = field(default_factory=lambda: os.getenv("REPORT_EXPORT_DEFAULT_TIMEFRAME", "1d"))
    report_export_language: str = field(default_factory=lambda: os.getenv("REPORT_EXPORT_LANGUAGE", "tr"))
    report_export_include_html: bool = field(default_factory=lambda: str(os.getenv("REPORT_EXPORT_INCLUDE_HTML", "true")).lower() == "true")
    report_export_include_pdf: bool = field(default_factory=lambda: str(os.getenv("REPORT_EXPORT_INCLUDE_PDF", "true")).lower() == "true")
    report_export_include_csv_bundle: bool = field(default_factory=lambda: str(os.getenv("REPORT_EXPORT_INCLUDE_CSV_BUNDLE", "true")).lower() == "true")
    report_export_archive_enabled: bool = field(default_factory=lambda: str(os.getenv("REPORT_EXPORT_ARCHIVE_ENABLED", "true")).lower() == "true")
    report_export_comparison_enabled: bool = field(default_factory=lambda: str(os.getenv("REPORT_EXPORT_COMPARISON_ENABLED", "true")).lower() == "true")
    report_export_periodic_tracking_enabled: bool = field(default_factory=lambda: str(os.getenv("REPORT_EXPORT_PERIODIC_TRACKING_ENABLED", "true")).lower() == "true")
    report_export_max_archive_records: int = field(default_factory=lambda: int(os.getenv("REPORT_EXPORT_MAX_ARCHIVE_RECORDS", "5000")))
    report_export_max_comparison_rows: int = field(default_factory=lambda: int(os.getenv("REPORT_EXPORT_MAX_COMPARISON_ROWS", "100")))
    report_export_pdf_engine: str = field(default_factory=lambda: os.getenv("REPORT_EXPORT_PDF_ENGINE", "auto"))
    report_export_html_theme: str = field(default_factory=lambda: os.getenv("REPORT_EXPORT_HTML_THEME", "clean_research"))
    report_export_save_manifest: bool = field(default_factory=lambda: str(os.getenv("REPORT_EXPORT_SAVE_MANIFEST", "true")).lower() == "true")
    report_export_save_quality: bool = field(default_factory=lambda: str(os.getenv("REPORT_EXPORT_SAVE_QUALITY", "true")).lower() == "true")
    report_export_require_disclaimer: bool = field(default_factory=lambda: str(os.getenv("REPORT_EXPORT_REQUIRE_DISCLAIMER", "true")).lower() == "true")
    report_export_min_quality_score: float = field(default_factory=lambda: float(os.getenv("REPORT_EXPORT_MIN_QUALITY_SCORE", "0.40")))


    # Phase 42: Portfolio Regime Research
    portfolio_regime_research_enabled: bool = field(default_factory=lambda: str(os.getenv("PORTFOLIO_REGIME_RESEARCH_ENABLED", "true")).lower() == "true")
    default_portfolio_regime_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_PORTFOLIO_REGIME_PROFILE", "balanced_regime_portfolio_research"))
    portfolio_regime_default_timeframe: str = field(default_factory=lambda: os.getenv("PORTFOLIO_REGIME_DEFAULT_TIMEFRAME", "1d"))
    portfolio_regime_min_symbols: int = field(default_factory=lambda: int(os.getenv("PORTFOLIO_REGIME_MIN_SYMBOLS", "3")))
    portfolio_regime_min_observations: int = field(default_factory=lambda: int(os.getenv("PORTFOLIO_REGIME_MIN_OBSERVATIONS", "180")))
    portfolio_regime_volatility_window: int = field(default_factory=lambda: int(os.getenv("PORTFOLIO_REGIME_VOLATILITY_WINDOW", "20")))
    portfolio_regime_trend_window: int = field(default_factory=lambda: int(os.getenv("PORTFOLIO_REGIME_TREND_WINDOW", "50")))
    portfolio_regime_correlation_window: int = field(default_factory=lambda: int(os.getenv("PORTFOLIO_REGIME_CORRELATION_WINDOW", "60")))
    portfolio_regime_drawdown_cluster_threshold: float = field(default_factory=lambda: float(os.getenv("PORTFOLIO_REGIME_DRAWDOWN_CLUSTER_THRESHOLD", "-0.05")))
    portfolio_regime_stress_window_min_bars: int = field(default_factory=lambda: int(os.getenv("PORTFOLIO_REGIME_STRESS_WINDOW_MIN_BARS", "20")))
    portfolio_regime_stress_window_max_bars: int = field(default_factory=lambda: int(os.getenv("PORTFOLIO_REGIME_STRESS_WINDOW_MAX_BARS", "90")))
    portfolio_regime_tail_quantile: float = field(default_factory=lambda: float(os.getenv("PORTFOLIO_REGIME_TAIL_QUANTILE", "0.05")))
    portfolio_regime_scenario_shock_small: float = field(default_factory=lambda: float(os.getenv("PORTFOLIO_REGIME_SCENARIO_SHOCK_SMALL", "0.03")))
    portfolio_regime_scenario_shock_medium: float = field(default_factory=lambda: float(os.getenv("PORTFOLIO_REGIME_SCENARIO_SHOCK_MEDIUM", "0.07")))
    portfolio_regime_scenario_shock_large: float = field(default_factory=lambda: float(os.getenv("PORTFOLIO_REGIME_SCENARIO_SHOCK_LARGE", "0.12")))
    portfolio_regime_save_reports: bool = field(default_factory=lambda: str(os.getenv("PORTFOLIO_REGIME_SAVE_REPORTS", "true")).lower() == "true")
    portfolio_regime_save_tables: bool = field(default_factory=lambda: str(os.getenv("PORTFOLIO_REGIME_SAVE_TABLES", "true")).lower() == "true")
    portfolio_regime_min_quality_score: float = field(default_factory=lambda: float(os.getenv("PORTFOLIO_REGIME_MIN_QUALITY_SCORE", "0.40")))


    # Phase 43: Synthetic Benchmark Baskets & Composite Indices
    synthetic_indices_enabled: bool = field(default_factory=lambda: str(os.getenv("SYNTHETIC_INDICES_ENABLED", "true")).lower() == "true")
    default_synthetic_index_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_SYNTHETIC_INDEX_PROFILE", "balanced_synthetic_index_research"))
    synthetic_index_default_timeframe: str = field(default_factory=lambda: os.getenv("SYNTHETIC_INDEX_DEFAULT_TIMEFRAME", "1d"))
    synthetic_index_base_value: float = field(default_factory=lambda: float(os.getenv("SYNTHETIC_INDEX_BASE_VALUE", "100.0")))
    synthetic_index_return_method: str = field(default_factory=lambda: os.getenv("SYNTHETIC_INDEX_RETURN_METHOD", "log"))
    synthetic_index_rebalance_method: str = field(default_factory=lambda: os.getenv("SYNTHETIC_INDEX_REBALANCE_METHOD", "static"))
    synthetic_index_rebalance_frequency: str = field(default_factory=lambda: os.getenv("SYNTHETIC_INDEX_REBALANCE_FREQUENCY", "monthly"))
    synthetic_index_min_symbols: int = field(default_factory=lambda: int(os.getenv("SYNTHETIC_INDEX_MIN_SYMBOLS", "3")))
    synthetic_index_min_observations: int = field(default_factory=lambda: int(os.getenv("SYNTHETIC_INDEX_MIN_OBSERVATIONS", "120")))
    synthetic_index_max_symbols_per_index: int = field(default_factory=lambda: int(os.getenv("SYNTHETIC_INDEX_MAX_SYMBOLS_PER_INDEX", "20")))
    synthetic_index_max_single_weight: float = field(default_factory=lambda: float(os.getenv("SYNTHETIC_INDEX_MAX_SINGLE_WEIGHT", "0.35")))
    synthetic_index_relative_strength_windows: tuple[int, ...] = field(default_factory=lambda: tuple(map(int, os.getenv("SYNTHETIC_INDEX_RELATIVE_STRENGTH_WINDOWS", "20,60,120").split(","))))
    synthetic_index_rotation_lookback: int = field(default_factory=lambda: int(os.getenv("SYNTHETIC_INDEX_ROTATION_LOOKBACK", "60")))
    synthetic_index_rotation_top_n: int = field(default_factory=lambda: int(os.getenv("SYNTHETIC_INDEX_ROTATION_TOP_N", "5")))
    synthetic_index_rotation_bottom_n: int = field(default_factory=lambda: int(os.getenv("SYNTHETIC_INDEX_ROTATION_BOTTOM_N", "5")))
    synthetic_index_save_definitions: bool = field(default_factory=lambda: str(os.getenv("SYNTHETIC_INDEX_SAVE_DEFINITIONS", "true")).lower() == "true")
    synthetic_index_save_levels: bool = field(default_factory=lambda: str(os.getenv("SYNTHETIC_INDEX_SAVE_LEVELS", "true")).lower() == "true")
    synthetic_index_save_reports: bool = field(default_factory=lambda: str(os.getenv("SYNTHETIC_INDEX_SAVE_REPORTS", "true")).lower() == "true")
    synthetic_index_min_quality_score: float = field(default_factory=lambda: float(os.getenv("SYNTHETIC_INDEX_MIN_QUALITY_SCORE", "0.40")))


    # Phase 45: Meta Research and Consensus Engine
    meta_research_enabled: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_ENABLED", "true")).lower() == "true")
    default_meta_research_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_META_RESEARCH_PROFILE", "balanced_meta_research"))
    meta_research_default_timeframe: str = field(default_factory=lambda: os.getenv("META_RESEARCH_DEFAULT_TIMEFRAME", "1d"))
    meta_research_min_sources: int = field(default_factory=lambda: int(os.getenv("META_RESEARCH_MIN_SOURCES", "3")))
    meta_research_min_evidence_quality: float = field(default_factory=lambda: float(os.getenv("META_RESEARCH_MIN_EVIDENCE_QUALITY", "0.40")))
    meta_research_conflict_threshold: float = field(default_factory=lambda: float(os.getenv("META_RESEARCH_CONFLICT_THRESHOLD", "0.35")))
    meta_research_high_agreement_threshold: float = field(default_factory=lambda: float(os.getenv("META_RESEARCH_HIGH_AGREEMENT_THRESHOLD", "0.70")))
    meta_research_uncertainty_penalty_enabled: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_UNCERTAINTY_PENALTY_ENABLED", "true")).lower() == "true")
    meta_research_quality_penalty_enabled: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_QUALITY_PENALTY_ENABLED", "true")).lower() == "true")
    meta_research_missing_source_penalty_enabled: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_MISSING_SOURCE_PENALTY_ENABLED", "true")).lower() == "true")
    meta_research_include_technical: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_TECHNICAL", "true")).lower() == "true")
    meta_research_include_strategy: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_STRATEGY", "true")).lower() == "true")
    meta_research_include_risk_level: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_RISK_LEVEL", "true")).lower() == "true")
    meta_research_include_backtest: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_BACKTEST", "true")).lower() == "true")
    meta_research_include_validation: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_VALIDATION", "true")).lower() == "true")
    meta_research_include_ml: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_ML", "true")).lower() == "true")
    meta_research_include_paper: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_PAPER", "true")).lower() == "true")
    meta_research_include_factor: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_FACTOR", "true")).lower() == "true")
    meta_research_include_synthetic_index: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_SYNTHETIC_INDEX", "true")).lower() == "true")
    meta_research_include_portfolio: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_PORTFOLIO", "true")).lower() == "true")
    meta_research_include_regime: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_INCLUDE_REGIME", "true")).lower() == "true")
    meta_research_save_reports: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_SAVE_REPORTS", "true")).lower() == "true")
    meta_research_save_tables: bool = field(default_factory=lambda: str(os.getenv("META_RESEARCH_SAVE_TABLES", "true")).lower() == "true")
    meta_research_min_quality_score: float = field(default_factory=lambda: float(os.getenv("META_RESEARCH_MIN_QUALITY_SCORE", "0.40")))



    # Phase 46: Experiment Tracking and Research Versioning
    experiment_tracking_enabled: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_TRACKING_ENABLED", "true")).lower() == "true")
    default_experiment_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_EXPERIMENT_PROFILE", "balanced_experiment_tracking"))
    experiment_default_timeframe: str = field(default_factory=lambda: os.getenv("EXPERIMENT_DEFAULT_TIMEFRAME", "1d"))
    experiment_save_run_manifest: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_SAVE_RUN_MANIFEST", "true")).lower() == "true")
    experiment_save_artifact_manifest: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_SAVE_ARTIFACT_MANIFEST", "true")).lower() == "true")
    experiment_save_reproducibility_manifest: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_SAVE_REPRODUCIBILITY_MANIFEST", "true")).lower() == "true")
    experiment_save_quality_report: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_SAVE_QUALITY_REPORT", "true")).lower() == "true")
    experiment_max_runs_in_leaderboard: int = field(default_factory=lambda: int(os.getenv("EXPERIMENT_MAX_RUNS_IN_LEADERBOARD", "500")))
    experiment_min_quality_score: float = field(default_factory=lambda: float(os.getenv("EXPERIMENT_MIN_QUALITY_SCORE", "0.40")))
    experiment_default_baseline_name: str = field(default_factory=lambda: os.getenv("EXPERIMENT_DEFAULT_BASELINE_NAME", "baseline_research_run"))
    experiment_enable_ablation_studies: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_ENABLE_ABLATION_STUDIES", "true")).lower() == "true")
    experiment_enable_comparison: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_ENABLE_COMPARISON", "true")).lower() == "true")
    experiment_enable_leaderboard: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_ENABLE_LEADERBOARD", "true")).lower() == "true")
    experiment_require_hypothesis: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_REQUIRE_HYPOTHESIS", "false")).lower() == "true")
    experiment_require_reproducibility_manifest: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_REQUIRE_REPRODUCIBILITY_MANIFEST", "true")).lower() == "true")
    experiment_capture_environment: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_CAPTURE_ENVIRONMENT", "true")).lower() == "true")
    experiment_capture_config_snapshot: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_CAPTURE_CONFIG_SNAPSHOT", "true")).lower() == "true")
    experiment_capture_artifact_snapshot: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_CAPTURE_ARTIFACT_SNAPSHOT", "true")).lower() == "true")
    experiment_allow_rerun_candidates: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_ALLOW_RERUN_CANDIDATES", "true")).lower() == "true")
    experiment_tracking_dry_run: bool = field(default_factory=lambda: str(os.getenv("EXPERIMENT_TRACKING_DRY_RUN", "true")).lower() == "true")



    # Research Planning Settings
    research_planning_enabled: bool = True
    default_research_planning_profile: str = "balanced_research_planning"
    research_planning_default_timeframe: str = "1d"
    research_planning_max_backlog_items: int = 500
    research_planning_max_next_best_experiments: int = 25
    research_planning_min_priority_score: float = 0.35
    research_planning_high_priority_threshold: float = 0.70
    research_planning_include_governance_signals: bool = True
    research_planning_include_experiment_signals: bool = True
    research_planning_include_meta_signals: bool = True
    research_planning_include_factor_signals: bool = True
    research_planning_include_portfolio_signals: bool = True
    research_planning_include_regime_signals: bool = True
    research_planning_include_validation_signals: bool = True
    research_planning_include_ml_signals: bool = True
    research_planning_include_paper_signals: bool = True
    research_planning_include_observability_signals: bool = True
    research_planning_save_backlog: bool = True
    research_planning_save_reports: bool = True
    research_planning_dry_run: bool = True
    research_planning_min_quality_score: float = 0.40

# Phase 49: Knowledge Base & Analyst Workspace
    knowledge_base_enabled: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_ENABLED", "true")).lower() == "true")
    default_knowledge_base_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_KNOWLEDGE_BASE_PROFILE", "balanced_local_knowledge_base"))
    knowledge_base_default_timeframe: str = field(default_factory=lambda: os.getenv("KNOWLEDGE_BASE_DEFAULT_TIMEFRAME", "1d"))
    knowledge_base_scan_reports_output: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_SCAN_REPORTS_OUTPUT", "true")).lower() == "true")
    knowledge_base_scan_docs: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_SCAN_DOCS", "true")).lower() == "true")
    knowledge_base_scan_data_lake_reports: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_SCAN_DATA_LAKE_REPORTS", "true")).lower() == "true")
    knowledge_base_scan_experiments: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_SCAN_EXPERIMENTS", "true")).lower() == "true")
    knowledge_base_scan_governance: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_SCAN_GOVERNANCE", "true")).lower() == "true")
    knowledge_base_scan_planning: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_SCAN_PLANNING", "true")).lower() == "true")
    knowledge_base_scan_meta_research: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_SCAN_META_RESEARCH", "true")).lower() == "true")
    knowledge_base_max_documents: int = field(default_factory=lambda: int(os.getenv("KNOWLEDGE_BASE_MAX_DOCUMENTS", "5000")))
    knowledge_base_max_document_mb: int = field(default_factory=lambda: int(os.getenv("KNOWLEDGE_BASE_MAX_DOCUMENT_MB", "10")))
    knowledge_base_chunk_size_chars: int = field(default_factory=lambda: int(os.getenv("KNOWLEDGE_BASE_CHUNK_SIZE_CHARS", "1200")))
    knowledge_base_chunk_overlap_chars: int = field(default_factory=lambda: int(os.getenv("KNOWLEDGE_BASE_CHUNK_OVERLAP_CHARS", "150")))
    knowledge_base_max_chunks: int = field(default_factory=lambda: int(os.getenv("KNOWLEDGE_BASE_MAX_CHUNKS", "50000")))
    knowledge_base_retrieval_top_k: int = field(default_factory=lambda: int(os.getenv("KNOWLEDGE_BASE_RETRIEVAL_TOP_K", "10")))
    knowledge_base_enable_tfidf: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_ENABLE_TFIDF", "true")).lower() == "true")
    knowledge_base_enable_fuzzy: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_ENABLE_FUZZY", "true")).lower() == "true")
    knowledge_base_enable_hybrid: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_ENABLE_HYBRID", "true")).lower() == "true")
    knowledge_base_save_index: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_SAVE_INDEX", "true")).lower() == "true")
    knowledge_base_save_memory_cards: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_SAVE_MEMORY_CARDS", "true")).lower() == "true")
    knowledge_base_save_reports: bool = field(default_factory=lambda: str(os.getenv("KNOWLEDGE_BASE_SAVE_REPORTS", "true")).lower() == "true")
    knowledge_base_min_quality_score: float = field(default_factory=lambda: float(os.getenv("KNOWLEDGE_BASE_MIN_QUALITY_SCORE", "0.40")))

    # Phase 50: Command Center
    command_center_enabled: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_ENABLED", "true")).lower() == "true")
    default_command_center_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_COMMAND_CENTER_PROFILE", "balanced_offline_command_center"))
    command_center_default_timeframe: str = field(default_factory=lambda: os.getenv("COMMAND_CENTER_DEFAULT_TIMEFRAME", "1d"))
    command_center_dry_run_default: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_DRY_RUN_DEFAULT", "true")).lower() == "true")
    command_center_require_safe_commands: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_REQUIRE_SAFE_COMMANDS", "true")).lower() == "true")
    command_center_allow_live_commands: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_ALLOW_LIVE_COMMANDS", "false")).lower() == "true")
    command_center_allow_broker_commands: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_ALLOW_BROKER_COMMANDS", "false")).lower() == "true")
    command_center_allow_deploy_commands: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_ALLOW_DEPLOY_COMMANDS", "false")).lower() == "true")
    command_center_allow_background_daemons: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_ALLOW_BACKGROUND_DAEMONS", "false")).lower() == "true")
    command_center_max_suggested_commands: int = field(default_factory=lambda: int(os.getenv("COMMAND_CENTER_MAX_SUGGESTED_COMMANDS", "50")))
    command_center_include_research_reports: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_INCLUDE_RESEARCH_REPORTS", "true")).lower() == "true")
    command_center_include_portfolio_reports: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_INCLUDE_PORTFOLIO_REPORTS", "true")).lower() == "true")
    command_center_include_regime_reports: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_INCLUDE_REGIME_REPORTS", "true")).lower() == "true")
    command_center_include_synthetic_indices: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_INCLUDE_SYNTHETIC_INDICES", "true")).lower() == "true")
    command_center_include_factor_research: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_INCLUDE_FACTOR_RESEARCH", "true")).lower() == "true")
    command_center_include_meta_research: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_INCLUDE_META_RESEARCH", "true")).lower() == "true")
    command_center_include_experiments: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_INCLUDE_EXPERIMENTS", "true")).lower() == "true")
    command_center_include_governance: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_INCLUDE_GOVERNANCE", "true")).lower() == "true")
    command_center_include_planning: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_INCLUDE_PLANNING", "true")).lower() == "true")
    command_center_include_knowledge_base: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_INCLUDE_KNOWLEDGE_BASE", "true")).lower() == "true")
    command_center_save_reports: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_SAVE_REPORTS", "true")).lower() == "true")
    command_center_min_quality_score: float = field(default_factory=lambda: float(os.getenv("COMMAND_CENTER_MIN_QUALITY_SCORE", "0.40")))


    # Phase 51: Quality Gates
    quality_gates_enabled: bool = field(default_factory=lambda: str(os.getenv("QUALITY_GATES_ENABLED", "true")).lower() == "true")
    default_quality_gate_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_QUALITY_GATE_PROFILE", "balanced_local_quality_gate"))
    quality_gate_default_timeframe: str = field(default_factory=lambda: os.getenv("QUALITY_GATE_DEFAULT_TIMEFRAME", "1d"))
    quality_gate_run_pytest: bool = field(default_factory=lambda: str(os.getenv("QUALITY_GATE_RUN_PYTEST", "true")).lower() == "true")
    quality_gate_run_import_validation: bool = field(default_factory=lambda: str(os.getenv("QUALITY_GATE_RUN_IMPORT_VALIDATION", "true")).lower() == "true")
    quality_gate_run_static_safety_scan: bool = field(default_factory=lambda: str(os.getenv("QUALITY_GATE_RUN_STATIC_SAFETY_SCAN", "true")).lower() == "true")
    quality_gate_run_repo_hygiene: bool = field(default_factory=lambda: str(os.getenv("QUALITY_GATE_RUN_REPO_HYGIENE", "true")).lower() == "true")
    quality_gate_run_dependency_audit: bool = field(default_factory=lambda: str(os.getenv("QUALITY_GATE_RUN_DEPENDENCY_AUDIT", "true")).lower() == "true")
    quality_gate_run_smoke_tests: bool = field(default_factory=lambda: str(os.getenv("QUALITY_GATE_RUN_SMOKE_TESTS", "true")).lower() == "true")
    quality_gate_run_output_contracts: bool = field(default_factory=lambda: str(os.getenv("QUALITY_GATE_RUN_OUTPUT_CONTRACTS", "true")).lower() == "true")
    quality_gate_run_documentation_coverage: bool = field(default_factory=lambda: str(os.getenv("QUALITY_GATE_RUN_DOCUMENTATION_COVERAGE", "true")).lower() == "true")
    quality_gate_max_test_runtime_seconds: int = field(default_factory=lambda: int(os.getenv("QUALITY_GATE_MAX_TEST_RUNTIME_SECONDS", "900")))
    quality_gate_allow_network_calls: bool = field(default_factory=lambda: str(os.getenv("QUALITY_GATE_ALLOW_NETWORK_CALLS", "false")).lower() == "true")
    quality_gate_allow_live_commands: bool = field(default_factory=lambda: str(os.getenv("QUALITY_GATE_ALLOW_LIVE_COMMANDS", "false")).lower() == "true")
    quality_gate_allow_broker_commands: bool = field(default_factory=lambda: str(os.getenv("QUALITY_GATE_ALLOW_BROKER_COMMANDS", "false")).lower() == "true")
    quality_gate_allow_deploy_commands: bool = field(default_factory=lambda: str(os.getenv("QUALITY_GATE_ALLOW_DEPLOY_COMMANDS", "false")).lower() == "true")
    quality_gate_allow_background_daemons: bool = field(default_factory=lambda: str(os.getenv("QUALITY_GATE_ALLOW_BACKGROUND_DAEMONS", "false")).lower() == "true")
    quality_gate_min_pass_rate: float = field(default_factory=lambda: float(os.getenv("QUALITY_GATE_MIN_PASS_RATE", "0.85")))
    quality_gate_min_quality_score: float = field(default_factory=lambda: float(os.getenv("QUALITY_GATE_MIN_QUALITY_SCORE", "0.40")))
    release_candidate_enabled: bool = field(default_factory=lambda: str(os.getenv("RELEASE_CANDIDATE_ENABLED", "true")).lower() == "true")
    release_candidate_dry_run: bool = field(default_factory=lambda: str(os.getenv("RELEASE_CANDIDATE_DRY_RUN", "true")).lower() == "true")
    release_candidate_include_reports: bool = field(default_factory=lambda: str(os.getenv("RELEASE_CANDIDATE_INCLUDE_REPORTS", "true")).lower() == "true")
    release_candidate_include_docs: bool = field(default_factory=lambda: str(os.getenv("RELEASE_CANDIDATE_INCLUDE_DOCS", "true")).lower() == "true")
    release_candidate_include_manifests: bool = field(default_factory=lambda: str(os.getenv("RELEASE_CANDIDATE_INCLUDE_MANIFESTS", "true")).lower() == "true")


    # Phase 55: Final Review
    final_review_enabled: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_ENABLED", "true")).lower() == "true")
    default_final_review_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_FINAL_REVIEW_PROFILE", "balanced_final_review"))
    final_review_default_timeframe: str = field(default_factory=lambda: os.getenv("FINAL_REVIEW_DEFAULT_TIMEFRAME", "1d"))
    final_review_run_architecture_audit: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_RUN_ARCHITECTURE_AUDIT", "true")).lower() == "true")
    final_review_run_safety_audit: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_RUN_SAFETY_AUDIT", "true")).lower() == "true")
    final_review_run_integration_audit: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_RUN_INTEGRATION_AUDIT", "true")).lower() == "true")
    final_review_run_command_audit: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_RUN_COMMAND_AUDIT", "true")).lower() == "true")
    final_review_run_datalake_audit: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_RUN_DATALAKE_AUDIT", "true")).lower() == "true")
    final_review_run_report_output_audit: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_RUN_REPORT_OUTPUT_AUDIT", "true")).lower() == "true")
    final_review_run_documentation_audit: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_RUN_DOCUMENTATION_AUDIT", "true")).lower() == "true")
    final_review_run_quality_gate_audit: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_RUN_QUALITY_GATE_AUDIT", "true")).lower() == "true")
    final_review_run_performance_audit: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_RUN_PERFORMANCE_AUDIT", "true")).lower() == "true")
    final_review_run_maintenance_audit: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_RUN_MAINTENANCE_AUDIT", "true")).lower() == "true")
    final_review_run_release_readiness_dry_run: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_RUN_RELEASE_READINESS_DRY_RUN", "true")).lower() == "true")
    final_review_require_no_live_trading: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_REQUIRE_NO_LIVE_TRADING", "true")).lower() == "true")
    final_review_require_no_broker_execution: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_REQUIRE_NO_BROKER_EXECUTION", "true")).lower() == "true")
    final_review_require_no_model_deploy: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_REQUIRE_NO_MODEL_DEPLOY", "true")).lower() == "true")
    final_review_require_no_background_daemon: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_REQUIRE_NO_BACKGROUND_DAEMON", "true")).lower() == "true")
    final_review_require_no_web_scraping: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_REQUIRE_NO_WEB_SCRAPING", "true")).lower() == "true")
    final_review_min_acceptance_score: float = field(default_factory=lambda: float(os.getenv("FINAL_REVIEW_MIN_ACCEPTANCE_SCORE", "0.75")))
    final_review_min_safety_score: float = field(default_factory=lambda: float(os.getenv("FINAL_REVIEW_MIN_SAFETY_SCORE", "0.95")))
    final_review_save_reports: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_SAVE_REPORTS", "true")).lower() == "true")
    final_review_dry_run: bool = field(default_factory=lambda: str(os.getenv("FINAL_REVIEW_DRY_RUN", "true")).lower() == "true")
    final_review_min_quality_score: float = field(default_factory=lambda: float(os.getenv("FINAL_REVIEW_MIN_QUALITY_SCORE", "0.40")))


    # Phase 58: Analyst UX & Operator Productivity
    analyst_ux_enabled: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_ENABLED", "true")).lower() == "true")
    default_analyst_ux_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_ANALYST_UX_PROFILE", "balanced_analyst_productivity"))
    analyst_ux_default_language: str = field(default_factory=lambda: os.getenv("ANALYST_UX_DEFAULT_LANGUAGE", "tr"))
    analyst_ux_allow_live_commands: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_ALLOW_LIVE_COMMANDS", "false")).lower() == "true")
    analyst_ux_allow_broker_commands: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_ALLOW_BROKER_COMMANDS", "false")).lower() == "true")
    analyst_ux_allow_deploy_commands: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_ALLOW_DEPLOY_COMMANDS", "false")).lower() == "true")
    analyst_ux_allow_background_daemons: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_ALLOW_BACKGROUND_DAEMONS", "false")).lower() == "true")
    analyst_ux_allow_real_market_download: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_ALLOW_REAL_MARKET_DOWNLOAD", "false")).lower() == "true")
    analyst_ux_generate_aliases: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_GENERATE_ALIASES", "true")).lower() == "true")
    analyst_ux_generate_prompt_packs: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_GENERATE_PROMPT_PACKS", "true")).lower() == "true")
    analyst_ux_generate_cheat_sheets: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_GENERATE_CHEAT_SHEETS", "true")).lower() == "true")
    analyst_ux_generate_task_board: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_GENERATE_TASK_BOARD", "true")).lower() == "true")
    analyst_ux_max_command_suggestions: int = field(default_factory=lambda: int(os.getenv("ANALYST_UX_MAX_COMMAND_SUGGESTIONS", "10")))
    analyst_ux_min_intent_confidence: float = field(default_factory=lambda: float(os.getenv("ANALYST_UX_MIN_INTENT_CONFIDENCE", "0.40")))
    analyst_ux_save_reports: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_SAVE_REPORTS", "true")).lower() == "true")
    analyst_ux_min_quality_score: float = field(default_factory=lambda: float(os.getenv("ANALYST_UX_MIN_QUALITY_SCORE", "0.40")))


    # Phase 61: Portable Packaging
    portable_packaging_enabled: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ENABLED", "true")).lower() == "true")
    default_portable_packaging_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_PORTABLE_PACKAGING_PROFILE", "balanced_local_packaging"))
    portable_packaging_default_language: str = field(default_factory=lambda: os.getenv("PORTABLE_PACKAGING_DEFAULT_LANGUAGE", "tr"))
    portable_packaging_dry_run_default: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_DRY_RUN_DEFAULT", "true")).lower() == "true")
    portable_packaging_allow_archive_create: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ALLOW_ARCHIVE_CREATE", "false")).lower() == "true")
    portable_packaging_allow_package_publish: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ALLOW_PACKAGE_PUBLISH", "false")).lower() == "true")
    portable_packaging_allow_docker: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ALLOW_DOCKER", "false")).lower() == "true")
    portable_packaging_allow_cloud_deploy: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ALLOW_CLOUD_DEPLOY", "false")).lower() == "true")
    portable_packaging_allow_live_commands: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ALLOW_LIVE_COMMANDS", "false")).lower() == "true")
    portable_packaging_allow_broker_commands: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ALLOW_BROKER_COMMANDS", "false")).lower() == "true")
    portable_packaging_allow_deploy_commands: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ALLOW_DEPLOY_COMMANDS", "false")).lower() == "true")
    portable_packaging_allow_background_daemons: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ALLOW_BACKGROUND_DAEMONS", "false")).lower() == "true")
    portable_packaging_allow_real_market_download: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ALLOW_REAL_MARKET_DOWNLOAD", "false")).lower() == "true")
    portable_packaging_allow_external_llm: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_ALLOW_EXTERNAL_LLM", "false")).lower() == "true")
    portable_packaging_include_source: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_INCLUDE_SOURCE", "true")).lower() == "true")
    portable_packaging_include_docs: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_INCLUDE_DOCS", "true")).lower() == "true")
    portable_packaging_include_tests: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_INCLUDE_TESTS", "true")).lower() == "true")
    portable_packaging_include_configs: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_INCLUDE_CONFIGS", "true")).lower() == "true")
    portable_packaging_include_reports_manifest_only: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_INCLUDE_REPORTS_MANIFEST_ONLY", "true")).lower() == "true")
    portable_packaging_include_data_manifest_only: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_INCLUDE_DATA_MANIFEST_ONLY", "true")).lower() == "true")
    portable_packaging_max_inventory_files: int = field(default_factory=lambda: int(os.getenv("PORTABLE_PACKAGING_MAX_INVENTORY_FILES", "100000")))
    portable_packaging_max_manifest_file_mb: int = field(default_factory=lambda: int(os.getenv("PORTABLE_PACKAGING_MAX_MANIFEST_FILE_MB", "50")))
    portable_packaging_save_reports: bool = field(default_factory=lambda: str(os.getenv("PORTABLE_PACKAGING_SAVE_REPORTS", "true")).lower() == "true")
    portable_packaging_min_quality_score: float = field(default_factory=lambda: float(os.getenv("PORTABLE_PACKAGING_MIN_QUALITY_SCORE", "0.40")))


    backup_recovery_enabled: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_ENABLED", "true")).lower() == "true")
    default_backup_recovery_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_BACKUP_RECOVERY_PROFILE", "balanced_local_backup_recovery"))
    backup_recovery_default_language: str = field(default_factory=lambda: os.getenv("BACKUP_RECOVERY_DEFAULT_LANGUAGE", "tr"))
    backup_recovery_dry_run_default: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_DRY_RUN_DEFAULT", "true")).lower() == "true")
    backup_recovery_allow_backup_copy: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_ALLOW_BACKUP_COPY", "false")).lower() == "true")
    backup_recovery_allow_restore_copy: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_ALLOW_RESTORE_COPY", "false")).lower() == "true")
    backup_recovery_allow_overwrite: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_ALLOW_OVERWRITE", "false")).lower() == "true")
    backup_recovery_allow_delete: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_ALLOW_DELETE", "false")).lower() == "true")
    backup_recovery_allow_cloud_backup: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_ALLOW_CLOUD_BACKUP", "false")).lower() == "true")
    backup_recovery_allow_external_storage: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_ALLOW_EXTERNAL_STORAGE", "false")).lower() == "true")
    backup_recovery_allow_live_commands: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_ALLOW_LIVE_COMMANDS", "false")).lower() == "true")
    backup_recovery_allow_broker_commands: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_ALLOW_BROKER_COMMANDS", "false")).lower() == "true")
    backup_recovery_allow_deploy_commands: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_ALLOW_DEPLOY_COMMANDS", "false")).lower() == "true")
    backup_recovery_allow_background_daemons: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_ALLOW_BACKGROUND_DAEMONS", "false")).lower() == "true")
    backup_recovery_allow_real_market_download: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_ALLOW_REAL_MARKET_DOWNLOAD", "false")).lower() == "true")
    backup_recovery_allow_external_llm: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_ALLOW_EXTERNAL_LLM", "false")).lower() == "true")
    backup_recovery_include_source: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_INCLUDE_SOURCE", "true")).lower() == "true")
    backup_recovery_include_docs: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_INCLUDE_DOCS", "true")).lower() == "true")
    backup_recovery_include_tests: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_INCLUDE_TESTS", "true")).lower() == "true")
    backup_recovery_include_configs: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_INCLUDE_CONFIGS", "true")).lower() == "true")
    backup_recovery_include_reports_manifest_only: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_INCLUDE_REPORTS_MANIFEST_ONLY", "true")).lower() == "true")
    backup_recovery_include_data_manifest_only: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_INCLUDE_DATA_MANIFEST_ONLY", "true")).lower() == "true")
    backup_recovery_include_generated_manifests: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_INCLUDE_GENERATED_MANIFESTS", "true")).lower() == "true")
    backup_recovery_max_inventory_files: int = field(default_factory=lambda: int(os.getenv("BACKUP_RECOVERY_MAX_INVENTORY_FILES", "150000")))
    backup_recovery_max_hash_file_mb: int = field(default_factory=lambda: int(os.getenv("BACKUP_RECOVERY_MAX_HASH_FILE_MB", "100")))
    backup_recovery_save_reports: bool = field(default_factory=lambda: str(os.getenv("BACKUP_RECOVERY_SAVE_REPORTS", "true")).lower() == "true")
    backup_recovery_min_quality_score: float = field(default_factory=lambda: float(os.getenv("BACKUP_RECOVERY_MIN_QUALITY_SCORE", "0.40")))

    @classmethod
    def from_env(cls) -> "Settings":
        return cls()


    # Evidence Governance Settings
    evidence_governance_enabled: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ENABLED", "true")).lower() == "true")
    default_evidence_governance_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_EVIDENCE_GOVERNANCE_PROFILE", "balanced_local_evidence"))
    evidence_governance_default_language: str = field(default_factory=lambda: os.getenv("EVIDENCE_GOVERNANCE_DEFAULT_LANGUAGE", "tr"))
    evidence_governance_dry_run_default: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_DRY_RUN_DEFAULT", "true")).lower() == "true")
    evidence_governance_allow_official_compliance_claims: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_OFFICIAL_COMPLIANCE_CLAIMS", "false")).lower() == "true")
    evidence_governance_allow_legal_opinion: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_LEGAL_OPINION", "false")).lower() == "true")
    evidence_governance_allow_cloud_export: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_CLOUD_EXPORT", "false")).lower() == "true")
    evidence_governance_allow_external_auditor_upload: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_EXTERNAL_AUDITOR_UPLOAD", "false")).lower() == "true")
    evidence_governance_allow_file_modification: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_FILE_MODIFICATION", "false")).lower() == "true")
    evidence_governance_allow_file_deletion: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_FILE_DELETION", "false")).lower() == "true")
    evidence_governance_allow_live_commands: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_LIVE_COMMANDS", "false")).lower() == "true")
    evidence_governance_allow_broker_commands: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_BROKER_COMMANDS", "false")).lower() == "true")
    evidence_governance_allow_deploy_commands: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_DEPLOY_COMMANDS", "false")).lower() == "true")
    evidence_governance_allow_background_daemons: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_BACKGROUND_DAEMONS", "false")).lower() == "true")
    evidence_governance_allow_real_market_download: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_REAL_MARKET_DOWNLOAD", "false")).lower() == "true")
    evidence_governance_allow_external_llm: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_EXTERNAL_LLM", "false")).lower() == "true")
    evidence_governance_scan_reports: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_SCAN_REPORTS", "true")).lower() == "true")
    evidence_governance_scan_data_lake: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_SCAN_DATA_LAKE", "true")).lower() == "true")
    evidence_governance_scan_docs: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_SCAN_DOCS", "true")).lower() == "true")
    evidence_governance_scan_generated_docs: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_SCAN_GENERATED_DOCS", "true")).lower() == "true")
    evidence_governance_scan_quality_outputs: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_SCAN_QUALITY_OUTPUTS", "true")).lower() == "true")
    evidence_governance_scan_security_outputs: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_SCAN_SECURITY_OUTPUTS", "true")).lower() == "true")
    evidence_governance_max_artifacts: int = field(default_factory=lambda: int(os.getenv("EVIDENCE_GOVERNANCE_MAX_ARTIFACTS", "200000")))
    evidence_governance_max_artifact_mb: int = field(default_factory=lambda: int(os.getenv("EVIDENCE_GOVERNANCE_MAX_ARTIFACT_MB", "50")))
    evidence_governance_freshness_days_warning: int = field(default_factory=lambda: int(os.getenv("EVIDENCE_GOVERNANCE_FRESHNESS_DAYS_WARNING", "30")))
    evidence_governance_save_reports: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_SAVE_REPORTS", "true")).lower() == "true")
    evidence_governance_min_quality_score: float = field(default_factory=lambda: float(os.getenv("EVIDENCE_GOVERNANCE_MIN_QUALITY_SCORE", "0.40")))

    def __post_init__(self):


        # Secrets Hygiene
        self.secrets_hygiene_enabled = str(os.getenv("SECRETS_HYGIENE_ENABLED", str(self.secrets_hygiene_enabled))).lower() == "true"
        self.default_secrets_hygiene_profile = str(os.getenv("DEFAULT_SECRETS_HYGIENE_PROFILE", self.default_secrets_hygiene_profile))
        self.secrets_hygiene_default_language = str(os.getenv("SECRETS_HYGIENE_DEFAULT_LANGUAGE", self.secrets_hygiene_default_language))
        self.secrets_hygiene_dry_run_default = str(os.getenv("SECRETS_HYGIENE_DRY_RUN_DEFAULT", str(self.secrets_hygiene_dry_run_default))).lower() == "true"
        self.secrets_hygiene_allow_secret_value_output = str(os.getenv("SECRETS_HYGIENE_ALLOW_SECRET_VALUE_OUTPUT", str(self.secrets_hygiene_allow_secret_value_output))).lower() == "true"
        self.secrets_hygiene_allow_file_modification = str(os.getenv("SECRETS_HYGIENE_ALLOW_FILE_MODIFICATION", str(self.secrets_hygiene_allow_file_modification))).lower() == "true"
        self.secrets_hygiene_allow_secret_deletion = str(os.getenv("SECRETS_HYGIENE_ALLOW_SECRET_DELETION", str(self.secrets_hygiene_allow_secret_deletion))).lower() == "true"
        self.secrets_hygiene_allow_cloud_vault = str(os.getenv("SECRETS_HYGIENE_ALLOW_CLOUD_VAULT", str(self.secrets_hygiene_allow_cloud_vault))).lower() == "true"
        self.secrets_hygiene_allow_external_scanner = str(os.getenv("SECRETS_HYGIENE_ALLOW_EXTERNAL_SCANNER", str(self.secrets_hygiene_allow_external_scanner))).lower() == "true"
        self.secrets_hygiene_allow_live_commands = str(os.getenv("SECRETS_HYGIENE_ALLOW_LIVE_COMMANDS", str(self.secrets_hygiene_allow_live_commands))).lower() == "true"
        self.secrets_hygiene_allow_broker_commands = str(os.getenv("SECRETS_HYGIENE_ALLOW_BROKER_COMMANDS", str(self.secrets_hygiene_allow_broker_commands))).lower() == "true"
        self.secrets_hygiene_allow_deploy_commands = str(os.getenv("SECRETS_HYGIENE_ALLOW_DEPLOY_COMMANDS", str(self.secrets_hygiene_allow_deploy_commands))).lower() == "true"
        self.secrets_hygiene_allow_background_daemons = str(os.getenv("SECRETS_HYGIENE_ALLOW_BACKGROUND_DAEMONS", str(self.secrets_hygiene_allow_background_daemons))).lower() == "true"
        self.secrets_hygiene_allow_real_market_download = str(os.getenv("SECRETS_HYGIENE_ALLOW_REAL_MARKET_DOWNLOAD", str(self.secrets_hygiene_allow_real_market_download))).lower() == "true"
        self.secrets_hygiene_allow_external_llm = str(os.getenv("SECRETS_HYGIENE_ALLOW_EXTERNAL_LLM", str(self.secrets_hygiene_allow_external_llm))).lower() == "true"
        self.secrets_hygiene_scan_source = str(os.getenv("SECRETS_HYGIENE_SCAN_SOURCE", str(self.secrets_hygiene_scan_source))).lower() == "true"
        self.secrets_hygiene_scan_docs = str(os.getenv("SECRETS_HYGIENE_SCAN_DOCS", str(self.secrets_hygiene_scan_docs))).lower() == "true"
        self.secrets_hygiene_scan_tests = str(os.getenv("SECRETS_HYGIENE_SCAN_TESTS", str(self.secrets_hygiene_scan_tests))).lower() == "true"
        self.secrets_hygiene_scan_configs = str(os.getenv("SECRETS_HYGIENE_SCAN_CONFIGS", str(self.secrets_hygiene_scan_configs))).lower() == "true"
        self.secrets_hygiene_scan_reports = str(os.getenv("SECRETS_HYGIENE_SCAN_REPORTS", str(self.secrets_hygiene_scan_reports))).lower() == "true"
        self.secrets_hygiene_scan_data_manifests = str(os.getenv("SECRETS_HYGIENE_SCAN_DATA_MANIFESTS", str(self.secrets_hygiene_scan_data_manifests))).lower() == "true"
        self.secrets_hygiene_scan_generated_outputs = str(os.getenv("SECRETS_HYGIENE_SCAN_GENERATED_OUTPUTS", str(self.secrets_hygiene_scan_generated_outputs))).lower() == "true"

        try:
            self.secrets_hygiene_max_files = int(os.getenv("SECRETS_HYGIENE_MAX_FILES", str(self.secrets_hygiene_max_files)))
        except ValueError:
            pass

        try:
            self.secrets_hygiene_max_file_mb = int(os.getenv("SECRETS_HYGIENE_MAX_FILE_MB", str(self.secrets_hygiene_max_file_mb)))
        except ValueError:
            pass

        try:
            self.secrets_hygiene_entropy_threshold = float(os.getenv("SECRETS_HYGIENE_ENTROPY_THRESHOLD", str(self.secrets_hygiene_entropy_threshold)))
        except ValueError:
            pass

        try:
            self.secrets_hygiene_mask_keep_start = int(os.getenv("SECRETS_HYGIENE_MASK_KEEP_START", str(self.secrets_hygiene_mask_keep_start)))
        except ValueError:
            pass

        try:
            self.secrets_hygiene_mask_keep_end = int(os.getenv("SECRETS_HYGIENE_MASK_KEEP_END", str(self.secrets_hygiene_mask_keep_end)))
        except ValueError:
            pass

        self.secrets_hygiene_save_reports = str(os.getenv("SECRETS_HYGIENE_SAVE_REPORTS", str(self.secrets_hygiene_save_reports))).lower() == "true"

        try:
            self.secrets_hygiene_min_quality_score = float(os.getenv("SECRETS_HYGIENE_MIN_QUALITY_SCORE", str(self.secrets_hygiene_min_quality_score)))
        except ValueError:
            pass











        self.live_trading_enabled = False


# Global settings instance
settings = Settings()
