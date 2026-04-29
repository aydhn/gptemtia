"""
Main entry point for Commodity & FX Signal Bot.
Phase 1 focuses on loading settings, verifying directories,
and validating the symbol universe.
"""

import sys
from pathlib import Path

# Setup path so we can import from within the project directory if run from root
sys.path.append(str(Path(__file__).parent))

from config.paths import ensure_project_directories
from config.settings import settings
from config.symbols import get_enabled_symbols, validate_symbol_universe
from core.exceptions import ConfigError
from core.logger import get_logger

# Initialize logger (after settings are loaded)
logger = get_logger("main", log_file="system.log")


def main():
    logger.info("=" * 50)
    logger.info(f"Starting {settings.app_name} [Env: {settings.environment}]")
    logger.info("=" * 50)

    try:
        # Step 1: Ensure required directories exist
        ensure_project_directories()
        logger.info("Project directories verified.")

        # Step 2: Validate live trading constraints
        if settings.live_trading_enabled:
            raise ConfigError("Live trading is explicitly disabled in Phase 1.")

        # Step 3: Validate Symbol Universe
        is_valid, errors = validate_symbol_universe()
        if not is_valid:
            logger.error("Symbol universe validation failed:")
            for err in errors:
                logger.error(f" - {err}")
            raise ConfigError("Symbol universe contains errors.")

        # Output basic stats
        enabled_symbols = get_enabled_symbols()
        logger.info(
            f"System initialized successfully. Loaded {len(enabled_symbols)} enabled symbols."
        )
        logger.info("Phase 1 initialization complete. Ready for Phase 2.")

    except Exception as e:
        logger.critical(f"System failed to start: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
