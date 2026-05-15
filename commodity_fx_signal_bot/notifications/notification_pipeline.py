import logging
from config.settings import Settings
from data.storage.data_lake import DataLake
from notifications.notification_config import NotificationProfile, get_notification_profile
from notifications.notification_models import DeliveryResult
from notifications.telegram_client import TelegramClient
from notifications.message_formatter import MessageFormatter
from notifications.telegram_sender import TelegramSender
from notifications.report_collector import ReportCollector
from notifications.delivery_log import DeliveryLog, build_delivery_audit
from notifications.paper_summary_builder import build_paper_summary_message
from notifications.status_summary_builder import build_system_status_message
from notifications.alert_builder import build_quality_alert_message
from notifications.daily_digest import DailyDigestBuilder
from notifications.notification_quality import build_notification_quality_report

logger = logging.getLogger(__name__)

class NotificationPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        profile: NotificationProfile | None = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        if profile is None:
            profile = get_notification_profile(settings.default_notification_profile)
        self.profile = profile
        self.collector = ReportCollector(data_lake)
        self.delivery_log = DeliveryLog()

    def build_sender(self) -> TelegramSender:
        # Respect overriding profile settings if we want to run dry-run locally despite settings
        dry_run = self.profile.dry_run or self.settings.telegram_dry_run

        client = TelegramClient(
            bot_token=self.settings.telegram_bot_token,
            chat_id=self.settings.telegram_chat_id,
            parse_mode=self.profile.parse_mode,
            disable_web_page_preview=self.settings.telegram_disable_web_page_preview,
            timeout_seconds=15
        )
        formatter = MessageFormatter(self.profile)

        # We need a slightly modified profile to pass the effective dry_run
        effective_profile = NotificationProfile(
            name=self.profile.name,
            description=self.profile.description,
            telegram_enabled=self.settings.telegram_enabled,
            dry_run=dry_run,
            parse_mode=self.profile.parse_mode,
            message_max_chars=self.profile.message_max_chars,
            rate_limit_seconds=self.profile.rate_limit_seconds,
            include_paper_summary=self.profile.include_paper_summary,
            include_backtest_summary=self.profile.include_backtest_summary,
            include_ml_summary=self.profile.include_ml_summary,
            include_quality_alerts=self.profile.include_quality_alerts,
            include_error_alerts=self.profile.include_error_alerts,
            max_symbols_in_digest=self.profile.max_symbols_in_digest,
            max_rows_per_section=self.profile.max_rows_per_section,
            enabled=self.profile.enabled,
            notes=self.profile.notes
        )

        return TelegramSender(client, formatter, effective_profile)

    def _process_message(self, message, sender, save: bool):
        results = sender.send(message)
        self.delivery_log.add_delivery_results(results)

        if save and self.settings.notification_save_message_logs:
            msg_dict = {"message_id": message.message_id, "body": message.body, "title": message.title} # Simplified
            self.data_lake.save_notification_message(msg_dict)

        formatted_text = sender.formatter.format_message(message)
        quality_report = build_notification_quality_report(message, formatted_text, results, self.profile)

        if save:
            self.data_lake.save_notification_quality(message.message_id, quality_report)
            if self.settings.notification_save_delivery_audit:
                df = self.delivery_log.to_dataframe()
                if not df.empty:
                    self.data_lake.save_notification_delivery_log(self.profile.name, df)
                    audit = build_delivery_audit(df)
                    self.data_lake.save_notification_delivery_audit(self.profile.name, audit)

        return results, quality_report

    def send_test_message(self, save: bool = True) -> tuple[list[DeliveryResult], dict]:
        sender = self.build_sender()

        # Actually we need NotificationMessage
        from notifications.notification_models import NotificationMessage, build_notification_message_id
        from datetime import datetime, timezone

        title = "Test Message"
        created_at = datetime.now(timezone.utc).isoformat()
        msg_id = build_notification_message_id("test_message", title, created_at)

        msg = NotificationMessage(
            message_id=msg_id,
            notification_type="test_message",
            severity="info",
            title=title,
            body="Sistem raporlama altyapısı testi başarılı. Bu bir canlı emir veya sinyal mesajı değildir.",
            created_at_utc=created_at,
            profile_name=self.profile.name
        )

        return self._process_message(msg, sender, save)

    def send_paper_summary(
        self,
        symbol: str | None = None,
        timeframe: str = "1d",
        save: bool = True,
    ) -> tuple[list[DeliveryResult], dict]:

        summary, _ = self.collector.collect_latest_paper_summary(symbol, timeframe, self.profile.name)
        msg = build_paper_summary_message(summary, self.profile)
        sender = self.build_sender()

        return self._process_message(msg, sender, save)

    def send_system_status(self, save: bool = True) -> tuple[list[DeliveryResult], dict]:
        summary = {"Pipeline": "Running", "DataLake": "Healthy"}
        msg = build_system_status_message(summary, self.profile)
        sender = self.build_sender()

        return self._process_message(msg, sender, save)

    def send_quality_alerts(self, timeframe: str = "1d", save: bool = True) -> tuple[list[DeliveryResult], dict]:
        alerts, _ = self.collector.collect_quality_alerts(timeframe)
        summary = {"Total Alerts": len(alerts), "Latest": alerts[0]['message'] if alerts else "None"}
        msg = build_quality_alert_message(summary, self.profile)
        sender = self.build_sender()

        return self._process_message(msg, sender, save)

    def send_daily_digest(
        self,
        timeframe: str = "1d",
        symbols: list[str] | None = None,
        save: bool = True,
    ) -> tuple[list[DeliveryResult], dict]:

        builder = DailyDigestBuilder(self.collector, self.profile)
        msg, _ = builder.build_digest(timeframe, symbols)
        sender = self.build_sender()

        return self._process_message(msg, sender, save)
