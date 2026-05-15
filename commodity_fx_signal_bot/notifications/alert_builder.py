import pandas as pd
from datetime import datetime, timezone
from notifications.notification_models import NotificationMessage, build_notification_message_id
from notifications.notification_config import NotificationProfile
from notifications.message_templates import build_header, build_section, build_key_value_lines, build_table_like_lines, build_footer, build_disclaimer

def build_error_alert_message(error_summary: dict, profile: NotificationProfile) -> NotificationMessage:
    title = "Sistem Hata Uyarısı"
    created_at = datetime.now(timezone.utc).isoformat()
    msg_id = build_notification_message_id("error_alert", title, created_at)

    header = build_header(title, "error")

    lines = build_key_value_lines(error_summary)
    section = build_section("Hata Detayları", lines)

    disclaimer = build_disclaimer()
    footer = build_footer(created_at)

    body = f"{header}{section}{disclaimer}{footer}"

    return NotificationMessage(
        message_id=msg_id,
        notification_type="error_alert",
        severity="error",
        title=title,
        body=body,
        created_at_utc=created_at,
        profile_name=profile.name
    )

def build_quality_alert_message(quality_summary: dict, profile: NotificationProfile) -> NotificationMessage:
    title = "Veri Kalite Uyarısı"
    created_at = datetime.now(timezone.utc).isoformat()
    msg_id = build_notification_message_id("quality_alert", title, created_at)

    header = build_header(title, "warning")

    lines = build_key_value_lines(quality_summary)
    section = build_section("Kalite Sorunları", lines)

    disclaimer = build_disclaimer()
    footer = build_footer(created_at)

    body = f"{header}{section}{disclaimer}{footer}"

    return NotificationMessage(
        message_id=msg_id,
        notification_type="quality_alert",
        severity="warning",
        title=title,
        body=body,
        created_at_utc=created_at,
        profile_name=profile.name
    )

def build_missing_data_alert_message(missing_data_summary: dict, profile: NotificationProfile) -> NotificationMessage:
    title = "Eksik Veri Uyarısı"
    created_at = datetime.now(timezone.utc).isoformat()
    msg_id = build_notification_message_id("quality_alert", title, created_at)

    header = build_header(title, "warning")

    lines = build_key_value_lines(missing_data_summary)
    section = build_section("Eksik Veriler", lines)

    disclaimer = build_disclaimer()
    footer = build_footer(created_at)

    body = f"{header}{section}{disclaimer}{footer}"

    return NotificationMessage(
        message_id=msg_id,
        notification_type="quality_alert",
        severity="warning",
        title=title,
        body=body,
        created_at_utc=created_at,
        profile_name=profile.name
    )

def build_high_risk_alert_message(risk_summary: dict, profile: NotificationProfile) -> NotificationMessage:
    title = "Yüksek Risk Uyarısı"
    created_at = datetime.now(timezone.utc).isoformat()
    msg_id = build_notification_message_id("quality_alert", title, created_at)

    header = build_header(title, "warning")

    lines = build_key_value_lines(risk_summary)
    section = build_section("Risk Metrikleri", lines)

    disclaimer = build_disclaimer()
    footer = build_footer(created_at)

    body = f"{header}{section}{disclaimer}{footer}"

    return NotificationMessage(
        message_id=msg_id,
        notification_type="quality_alert",
        severity="warning",
        title=title,
        body=body,
        created_at_utc=created_at,
        profile_name=profile.name
    )

def build_high_uncertainty_alert_message(ml_summary: dict, profile: NotificationProfile) -> NotificationMessage:
    title = "Yüksek Belirsizlik Uyarısı (ML Context)"
    created_at = datetime.now(timezone.utc).isoformat()
    msg_id = build_notification_message_id("quality_alert", title, created_at)

    header = build_header(title, "warning")

    lines = build_key_value_lines(ml_summary)
    section = build_section("ML Modeli Durumu", lines)

    disclaimer = build_disclaimer()
    footer = build_footer(created_at)

    body = f"{header}{section}{disclaimer}{footer}"

    return NotificationMessage(
        message_id=msg_id,
        notification_type="quality_alert",
        severity="warning",
        title=title,
        body=body,
        created_at_utc=created_at,
        profile_name=profile.name
    )
