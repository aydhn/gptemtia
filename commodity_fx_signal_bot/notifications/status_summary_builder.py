import pandas as pd
from datetime import datetime, timezone
from notifications.notification_models import NotificationMessage, build_notification_message_id
from notifications.notification_config import NotificationProfile
from notifications.message_templates import build_header, build_section, build_key_value_lines, build_table_like_lines, build_footer, build_disclaimer

def build_system_status_message(status_summary: dict, profile: NotificationProfile) -> NotificationMessage:
    title = "Sistem Durum Özeti"
    created_at = datetime.now(timezone.utc).isoformat()
    msg_id = build_notification_message_id("system_status", title, created_at)

    header = build_header(title, "info")

    # Hide token length or secret in status if any passed accidentally
    safe_summary = {k: v for k, v in status_summary.items() if "token" not in k.lower()}

    lines = build_key_value_lines(safe_summary)
    section = build_section("Sistem Durumu", lines)

    disclaimer = build_disclaimer()
    footer = build_footer(created_at)

    body = f"{header}{section}{disclaimer}{footer}"

    return NotificationMessage(
        message_id=msg_id,
        notification_type="system_status",
        severity="info",
        title=title,
        body=body,
        created_at_utc=created_at,
        profile_name=profile.name
    )

def build_pipeline_status_message(status_df: pd.DataFrame, profile: NotificationProfile) -> NotificationMessage:
    title = "Pipeline Durum Özeti"
    created_at = datetime.now(timezone.utc).isoformat()
    msg_id = build_notification_message_id("system_status", title, created_at)

    header = build_header(title, "info")

    cols = status_df.columns.tolist()[:3]
    lines = build_table_like_lines(status_df, cols, max_rows=profile.max_rows_per_section)
    section = build_section("Pipeline Adımları", lines)

    disclaimer = build_disclaimer()
    footer = build_footer(created_at)

    body = f"{header}{section}{disclaimer}{footer}"

    return NotificationMessage(
        message_id=msg_id,
        notification_type="system_status",
        severity="info",
        title=title,
        body=body,
        created_at_utc=created_at,
        profile_name=profile.name
    )

def build_data_lake_status_message(status_summary: dict, profile: NotificationProfile) -> NotificationMessage:
    title = "Data Lake Durum Özeti"
    created_at = datetime.now(timezone.utc).isoformat()
    msg_id = build_notification_message_id("system_status", title, created_at)

    header = build_header(title, "info")

    lines = build_key_value_lines(status_summary)
    section = build_section("Data Lake Klasörleri", lines)

    disclaimer = build_disclaimer()
    footer = build_footer(created_at)

    body = f"{header}{section}{disclaimer}{footer}"

    return NotificationMessage(
        message_id=msg_id,
        notification_type="system_status",
        severity="info",
        title=title,
        body=body,
        created_at_utc=created_at,
        profile_name=profile.name
    )

def build_model_registry_status_message(status_df: pd.DataFrame, profile: NotificationProfile) -> NotificationMessage:
    title = "Model Registry Durum Özeti"
    created_at = datetime.now(timezone.utc).isoformat()
    msg_id = build_notification_message_id("system_status", title, created_at)

    header = build_header(title, "info")

    cols = status_df.columns.tolist()[:4]
    lines = build_table_like_lines(status_df, cols, max_rows=profile.max_rows_per_section)
    section = build_section("Modeller", lines)

    disclaimer = build_disclaimer()
    footer = build_footer(created_at)

    body = f"{header}{section}{disclaimer}{footer}"

    return NotificationMessage(
        message_id=msg_id,
        notification_type="system_status",
        severity="info",
        title=title,
        body=body,
        created_at_utc=created_at,
        profile_name=profile.name
    )
