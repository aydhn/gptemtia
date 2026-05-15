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
    parser = argparse.ArgumentParser(description="Send a test notification message")
    parser.add_argument("--profile", type=str, default="balanced_telegram_reporting", help="Notification profile to use")
    parser.add_argument("--send", action="store_true", help="Actually send the message to Telegram (requires env vars)")
    parser.add_argument("--message", type=str, help="Custom message text")
    args = parser.parse_args()

    paths.ensure_project_directories()

    try:
        profile = get_notification_profile(args.profile)
    except Exception as e:
        logger.error(f"Error loading profile: {e}")
        sys.exit(1)

    if args.send:
        # We override dry run if send is explicitly passed
        settings.telegram_dry_run = False
        settings.telegram_enabled = True

    data_lake = DataLake(paths.LAKE_DIR)
    pipeline = NotificationPipeline(data_lake, settings, profile)

    logger.info(f"Starting test message script with profile '{args.profile}'. Dry run: {pipeline.profile.dry_run or settings.telegram_dry_run}")

    results, quality = pipeline.send_test_message(save=True)

    logger.info(f"Delivery results: {results}")

    # Save report

    summary = {
        "profile": profile.name,
        "dry_run": pipeline.profile.dry_run or settings.telegram_dry_run,
        "results": [r.delivery_status for r in results],
        "quality_passed": quality.get("passed", False)
    }

    import reports.report_builder as report_builder
    report_text = report_builder.build_telegram_test_message_report(summary)

    report_path = paths.NOTIFICATION_REPORT_OUTPUT_DIR / "telegram_test_message_report.txt"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_text)

    logger.info(f"Report saved to {report_path}")

if __name__ == "__main__":
    main()
