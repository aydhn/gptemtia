import argparse
import logging
from config.settings import settings
from data.storage.data_lake import DataLake
from config import paths

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Check notification system status")
    args = parser.parse_args()

    paths.ensure_project_directories()

    data_lake = DataLake(paths.LAKE_DIR)

    logger.info("Checking notification system status...")

    messages_df = data_lake.list_notification_messages()
    logs_df = data_lake.list_notification_delivery_logs()

    is_configured = bool(settings.telegram_bot_token) and bool(settings.telegram_chat_id)

    summary = {
        "Total Messages Saved": len(messages_df),
        "Total Delivery Logs": len(logs_df),
        "Telegram Configured": is_configured,
        "Notifications Enabled": settings.notifications_enabled,
        "Telegram Dry Run": settings.telegram_dry_run
    }

    import reports.report_builder as report_builder
    report_text = report_builder.build_notification_status_report(logs_df, summary)

    report_path = paths.NOTIFICATION_REPORT_OUTPUT_DIR / "notification_status_report.txt"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_text)

    csv_path = paths.NOTIFICATION_REPORT_OUTPUT_DIR / "notification_status.csv"
    if not messages_df.empty:
        messages_df.to_csv(csv_path, index=False)

    logger.info(f"Status report saved to {report_path}")

if __name__ == "__main__":
    main()
