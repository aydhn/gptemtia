import time
from datetime import datetime, timezone
import logging
from notifications.telegram_client import TelegramClient
from notifications.message_formatter import MessageFormatter
from notifications.notification_config import NotificationProfile
from notifications.notification_models import NotificationMessage, DeliveryResult, build_notification_message_id

logger = logging.getLogger(__name__)

class TelegramSender:
    def __init__(
        self,
        client: TelegramClient,
        formatter: MessageFormatter,
        profile: NotificationProfile,
    ):
        self.client = client
        self.formatter = formatter
        self.profile = profile

    def send(self, message: NotificationMessage) -> list[DeliveryResult]:
        formatted_text = self.formatter.format_message(message)
        parts = self.formatter.split_message(formatted_text)

        results = []
        for i, part in enumerate(parts):
            if i > 0 and self.profile.rate_limit_seconds > 0:
                time.sleep(self.profile.rate_limit_seconds)

            if self.profile.dry_run:
                logger.info(f"Dry run enabled. Skipping Telegram delivery for {message.message_id} part {i+1}")
                results.append(DeliveryResult(
                    message_id=message.message_id,
                    delivery_status="delivery_dry_run",
                    dry_run=True,
                    destination=self.client.get_safe_destination_label(),
                    sent_at_utc=datetime.now(timezone.utc).isoformat(),
                    error_message=None
                ))
            elif not self.client.is_configured():
                logger.warning(f"Telegram client not configured. Skipping delivery for {message.message_id} part {i+1}")
                results.append(DeliveryResult(
                    message_id=message.message_id,
                    delivery_status="delivery_not_configured",
                    dry_run=False,
                    destination="not_configured",
                    sent_at_utc=None,
                    error_message="Telegram bot token or chat ID is missing."
                ))
            else:
                resp = self.client.send_message(part)
                results.append(DeliveryResult(
                    message_id=message.message_id,
                    delivery_status=resp["status"],
                    dry_run=False,
                    destination=self.client.get_safe_destination_label(),
                    sent_at_utc=datetime.now(timezone.utc).isoformat() if resp["success"] else None,
                    error_message=resp.get("error_message"),
                    response_metadata=resp.get("response", {})
                ))

        return results

    def send_text(self, text: str, notification_type: str = "system_status", severity: str = "info") -> list[DeliveryResult]:
        title = "Mesaj"
        created_at = datetime.now(timezone.utc).isoformat()
        msg_id = build_notification_message_id(notification_type, title, created_at)

        message = NotificationMessage(
            message_id=msg_id,
            notification_type=notification_type,
            severity=severity,
            title=title,
            body=text,
            created_at_utc=created_at,
            profile_name=self.profile.name
        )
        return self.send(message)
