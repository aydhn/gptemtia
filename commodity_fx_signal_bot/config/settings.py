"""
System-wide settings and configuration management.
"""
import os
import logging
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
    environment: str = field(default_factory=lambda: os.getenv("APP_ENV", "development"))
    log_level: str = field(default_factory=lambda: os.getenv("LOG_LEVEL", "INFO"))
    base_currency: str = field(default_factory=lambda: os.getenv("BASE_CURRENCY", "TRY"))
    default_interval: str = field(default_factory=lambda: os.getenv("DEFAULT_INTERVAL", "1h"))
    default_lookback_days: int = field(default_factory=lambda: int(os.getenv("DEFAULT_LOOKBACK_DAYS", "730")))
    max_symbols_per_scan: int = field(default_factory=lambda: int(os.getenv("MAX_SYMBOLS_PER_SCAN", "80")))

    paper_trading_enabled: bool = field(
        default_factory=lambda: os.getenv("PAPER_TRADING_ENABLED", "true").lower() == "true"
    )

    # Live trading MUST be disabled in Phase 1 for safety
    live_trading_enabled: bool = False

    telegram_enabled: bool = field(
        default_factory=lambda: os.getenv("TELEGRAM_ENABLED", "false").lower() == "true"
    )
    telegram_bot_token: str = field(default_factory=lambda: os.getenv("TELEGRAM_BOT_TOKEN", ""))
    telegram_chat_id: str = field(default_factory=lambda: os.getenv("TELEGRAM_CHAT_ID", ""))

    data_cache_enabled: bool = field(
        default_factory=lambda: os.getenv("DATA_CACHE_ENABLED", "true").lower() == "true"
    )

    random_seed: int = field(default_factory=lambda: int(os.getenv("RANDOM_SEED", "42")))

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
