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
    parser = argparse.ArgumentParser(description="Send system status notification")
    parser.add_argument("--send", action="store_true", help="Actually send the message to Telegram")
    args = parser.parse_args()

    paths.ensure_project_directories()

    profile = get_notification_profile(settings.default_notification_profile)

    if args.send:
        settings.telegram_dry_run = False
        settings.telegram_enabled = True

    data_lake = DataLake(paths.LAKE_DIR)
    pipeline = NotificationPipeline(data_lake, settings, profile)

    logger.info("Starting system status script...")

    results, quality = pipeline.send_system_status(save=True)

    summary = {
        "profile": profile.name,
        "results": [r.delivery_status for r in results]
    }

    import reports.report_builder as report_builder
    report_text = report_builder.build_telegram_system_status_report(summary)

    report_path = paths.NOTIFICATION_REPORT_OUTPUT_DIR / "telegram_system_status_report.txt"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_text)

    logger.info(f"Report saved to {report_path}")

if __name__ == "__main__":
    main()
