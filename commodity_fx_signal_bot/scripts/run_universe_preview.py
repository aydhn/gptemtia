"""
Script to preview the symbol universe and detect issues.
"""

import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from core.logger import get_logger
from config.symbols import (
    get_enabled_symbols,
    validate_symbol_universe,
    summarize_universe,
)
from reports.report_builder import build_universe_report

logger = get_logger("run_universe_preview")


def main():
    logger.info("Starting Universe Preview...")

    is_valid, errors = validate_symbol_universe()
    if not is_valid:
        logger.error("Universe validation failed with the following errors:")
        for error in errors:
            logger.error(f" - {error}")
    else:
        logger.info("Universe validation passed.")

    symbols = get_enabled_symbols()
    summary = summarize_universe()
    report = build_universe_report(symbols)

    print("\n" + report + "\n")
    print(f"Summary: {summary}\n")
    logger.info("Universe Preview completed.")


if __name__ == "__main__":
    main()
