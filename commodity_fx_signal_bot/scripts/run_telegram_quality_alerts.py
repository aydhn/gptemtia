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
    parser = argparse.ArgumentParser(description="Send quality alerts notification")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe (default: 1d)")
    parser.add_argument("--send", action="store_true", help="Actually send the message to Telegram")
    args = parser.parse_args()

    paths.ensure_project_directories()

    profile = get_notification_profile("minimal_alert_reporting")

    if args.send:
        settings.telegram_dry_run = False
        settings.telegram_enabled = True

    data_lake = DataLake(paths.LAKE_DIR)
    pipeline = NotificationPipeline(data_lake, settings, profile)

    logger.info("Starting quality alerts script...")

    results, quality = pipeline.send_quality_alerts(args.timeframe, save=True)

    summary = {
        "profile": profile.name,
        "timeframe": args.timeframe,
        "results": [r.delivery_status for r in results]
    }

    import reports.report_builder as report_builder
    report_text = report_builder.build_telegram_quality_alerts_report(summary)

    report_path = paths.NOTIFICATION_REPORT_OUTPUT_DIR / "telegram_quality_alerts_report.txt"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_text)

    logger.info(f"Report saved to {report_path}")

if __name__ == "__main__":
    main()
