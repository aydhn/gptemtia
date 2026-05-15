from datetime import datetime, timezone
from notifications.notification_models import NotificationMessage, build_notification_message_id
from notifications.notification_config import NotificationProfile
from notifications.message_templates import build_header, build_section, build_key_value_lines, build_footer, build_disclaimer
from notifications.report_collector import ReportCollector

class DailyDigestBuilder:
    def __init__(self, collector: ReportCollector, profile: NotificationProfile):
        self.collector = collector
        self.profile = profile

    def build_digest(
        self,
        timeframe: str = "1d",
        symbols: list[str] | None = None,
    ) -> tuple[NotificationMessage, dict]:

        title = "Günlük Sistem Özeti"
        created_at = datetime.now(timezone.utc).isoformat()
        msg_id = build_notification_message_id("daily_digest", title, created_at)

        warnings = []
        body_parts = []

        header = build_header(title, "info")
        body_parts.append(header)

        if self.profile.include_paper_summary:
            try:
                paper_sum, _ = self.collector.collect_latest_paper_summary(timeframe=timeframe)
                section = build_section("Paper Trading Portföyü", build_key_value_lines(paper_sum))
                body_parts.append(section)
            except Exception as e:
                warnings.append(f"Failed to collect paper summary: {e}")

        if self.profile.include_backtest_summary:
            try:
                backtest_sum, _ = self.collector.collect_latest_backtest_summary(timeframe=timeframe)
                section = build_section("Backtest / Performans Özeti", build_key_value_lines(backtest_sum))
                body_parts.append(section)
            except Exception as e:
                warnings.append(f"Failed to collect backtest summary: {e}")

        if self.profile.include_ml_summary:
            try:
                ml_sum, _ = self.collector.collect_latest_ml_summary(timeframe=timeframe)
                section = build_section("ML Context Özeti", build_key_value_lines(ml_sum))
                body_parts.append(section)
            except Exception as e:
                warnings.append(f"Failed to collect ML summary: {e}")

        if self.profile.include_quality_alerts:
            try:
                alerts, _ = self.collector.collect_quality_alerts(timeframe=timeframe)
                if alerts:
                    alert_lines = [f"• {a['severity']}: {a['message']}" for a in alerts[:5]]
                    if len(alerts) > 5:
                        alert_lines.append(f"... (+{len(alerts)-5} diğer uyarı)")
                    section = build_section("Kalite ve Veri Uyarıları", alert_lines)
                    body_parts.append(section)
            except Exception as e:
                warnings.append(f"Failed to collect quality alerts: {e}")

        body_parts.append(build_disclaimer())
        body_parts.append(build_footer(created_at))

        body = "".join(body_parts)

        msg = NotificationMessage(
            message_id=msg_id,
            notification_type="daily_digest",
            severity="info",
            title=title,
            body=body,
            created_at_utc=created_at,
            profile_name=self.profile.name,
            warnings=warnings
        )

        return msg, {"warnings": warnings}
