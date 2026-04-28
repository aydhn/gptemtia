import sys
from pathlib import Path
import json

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from core.logger import get_logger
from config.symbols import get_enabled_symbols, validate_symbol_universe, summarize_universe
from reports.report_builder import build_universe_report, save_text_report

logger = get_logger("run_universe_audit")

def main():
    logger.info("Starting Universe Audit...")

    is_valid, errors = validate_symbol_universe()
    if not is_valid:
        logger.error("Universe validation failed with the following errors:")
        for error in errors:
            logger.error(f" - {error}")
    else:
        logger.info("Universe validation passed.")

    summary = summarize_universe()
    logger.info(f"Universe Summary: {summary}")

    symbols = get_enabled_symbols()
    report_text = build_universe_report(symbols)

    output_dir = Path("reports/output")
    save_text_report(report_text, output_dir / "universe_manifest.txt")

    with open(output_dir / "universe_manifest.json", "w") as f:
        json.dump(summary, f, indent=4)

    logger.info("Universe Audit completed. Reports saved to reports/output/")

if __name__ == "__main__":
    main()
