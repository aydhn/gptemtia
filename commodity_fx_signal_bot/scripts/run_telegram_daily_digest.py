import argparse
import sys
import logging
from config.settings import settings
from data.storage.data_lake import DataLake
from notifications.notification_config import get_notification_profile
from notifications.notification_pipeline import NotificationPipeline
from config import paths

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Send daily digest notification")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe (default: 1d)")
    parser.add_argument("--symbol", type=str, help="Specific symbol")
    parser.add_argument("--asset-class", type=str, help="Specific asset class")
    parser.add_argument("--limit", type=int, help="Limit number of symbols")
    parser.add_argument("--profile", type=str, default="research_digest_reporting", help="Notification profile")
    parser.add_argument("--send", action="store_true", help="Actually send the message to Telegram")
    args = parser.parse_args()

    paths.ensure_project_directories()

    try:
        profile = get_notification_profile(args.profile)
    except Exception as e:
        logger.error(f"Error loading profile: {e}")
        sys.exit(1)

    if args.send:
        settings.telegram_dry_run = False
        settings.telegram_enabled = True

    data_lake = DataLake(paths.LAKE_DIR)
    pipeline = NotificationPipeline(data_lake, settings, profile)

    logger.info("Starting daily digest script...")

    symbols = None
    if args.symbol:
        symbols = [args.symbol]

    results, quality = pipeline.send_daily_digest(args.timeframe, symbols, save=True)

    summary = {
        "profile": profile.name,
        "timeframe": args.timeframe,
        "results": [r.delivery_status for r in results]
    }

    import reports.report_builder as report_builder
    report_text = report_builder.build_telegram_daily_digest_report(summary)

    report_path = paths.NOTIFICATION_REPORT_OUTPUT_DIR / "telegram_daily_digest_report.txt"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_text)

    logger.info(f"Report saved to {report_path}")

if __name__ == "__main__":
    main()
