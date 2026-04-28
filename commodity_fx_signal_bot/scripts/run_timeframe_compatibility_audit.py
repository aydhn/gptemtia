"""
Script to audit timeframe compatibility across the universe and configurations.
"""

import sys
import json
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from core.logger import get_logger
from config.symbols import (
    get_enabled_symbols,
    validate_symbol_universe,
    get_allowed_timeframes_for_symbol,
    get_default_timeframes_for_asset_class,
)
from config.timeframes import validate_timeframe, list_timeframes, DEFAULT_TIMEFRAMES
from config.market_sessions import validate_market_sessions, list_market_sessions
from config.scan_config import validate_scan_profiles, get_default_scan_profile
from core.market_calendar import MarketCalendar
from core.scan_scheduler import ScanScheduler
from reports.report_builder import (
    build_timeframe_compatibility_report,
    build_scan_plan_report,
)

logger = get_logger("run_timeframe_compatibility_audit")


def main():
    logger.info("Starting Timeframe Compatibility Audit...")

    # Validation checks
    try:
        validate_market_sessions()
        logger.info("Market session validation passed.")
    except Exception as e:
        logger.error(f"Market session validation failed: {e}")

    try:
        validate_scan_profiles()
        logger.info("Scan profile validation passed.")
    except Exception as e:
        logger.error(f"Scan profile validation failed: {e}")

    try:
        for tf in DEFAULT_TIMEFRAMES:
            validate_timeframe(tf.name)
        logger.info("Timeframe validation passed.")
    except Exception as e:
        logger.error(f"Timeframe validation failed: {e}")

    is_valid, errors = validate_symbol_universe()
    if not is_valid:
        logger.error("Universe validation failed with the following errors:")
        for error in errors:
            logger.error(f" - {error}")
    else:
        logger.info("Universe validation passed.")

    # Build Scan Plan Preview
    symbols = get_enabled_symbols()
    default_profile = get_default_scan_profile()
    calendar = MarketCalendar()
    scheduler = ScanScheduler(default_profile, calendar)

    scan_plan = scheduler.build_scan_plan(symbols)

    # Save reports
    output_dir = Path("reports/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    json_path = output_dir / "scan_plan_preview.json"
    with open(json_path, "w") as f:
        json.dump(scan_plan, f, indent=2)
    logger.info(f"Saved JSON scan plan to {json_path}")

    # Generate text report
    txt_path = output_dir / "timeframe_compatibility_report.txt"
    report_text = build_timeframe_compatibility_report(symbols, scan_plan)
    with open(txt_path, "w") as f:
        f.write(report_text)
    logger.info(f"Saved TXT report to {txt_path}")

    print("\n" + report_text + "\n")
    logger.info("Timeframe Compatibility Audit completed.")


if __name__ == "__main__":
    main()
