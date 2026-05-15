import pandas as pd
from datetime import datetime, timezone
from notifications.notification_models import NotificationMessage, build_notification_message_id
from notifications.notification_config import NotificationProfile
from notifications.message_templates import build_header, build_section, build_key_value_lines, build_table_like_lines, build_footer, build_disclaimer

def build_paper_summary_message(summary: dict, profile: NotificationProfile) -> NotificationMessage:
    title = "Paper Trading Sanal Portföy Özeti"
    created_at = datetime.now(timezone.utc).isoformat()
    msg_id = build_notification_message_id("paper_summary", title, created_at)

    header = build_header(title, "info")

    lines = build_key_value_lines(summary)
    section = build_section("Özet Veriler", lines)

    disclaimer = build_disclaimer()
    footer = build_footer(created_at)

    body = f"{header}{section}{disclaimer}{footer}"

    return NotificationMessage(
        message_id=msg_id,
        notification_type="paper_summary",
        severity="info",
        title=title,
        body=body,
        created_at_utc=created_at,
        profile_name=profile.name
    )

def build_paper_order_book_message(orders_df: pd.DataFrame, summary: dict, profile: NotificationProfile) -> NotificationMessage:
    title = "Sanal Order Book Özeti"
    created_at = datetime.now(timezone.utc).isoformat()
    msg_id = build_notification_message_id("order_book_summary", title, created_at)

    header = build_header(title, "info")

    cols = ["symbol", "action", "status", "price"]
    if "symbol" not in orders_df.columns:
        cols = orders_df.columns.tolist()[:4]

    lines = build_table_like_lines(orders_df, cols, max_rows=profile.max_rows_per_section)
    section = build_section("Sanal Emirler", lines)

    disclaimer = build_disclaimer()
    footer = build_footer(created_at)

    body = f"{header}{section}{disclaimer}{footer}"

    return NotificationMessage(
        message_id=msg_id,
        notification_type="order_book_summary",
        severity="info",
        title=title,
        body=body,
        created_at_utc=created_at,
        profile_name=profile.name
    )

def build_paper_portfolio_message(portfolio_df: pd.DataFrame, summary: dict, profile: NotificationProfile) -> NotificationMessage:
    title = "Sanal Portföy Özeti"
    created_at = datetime.now(timezone.utc).isoformat()
    msg_id = build_notification_message_id("portfolio_summary", title, created_at)

    header = build_header(title, "info")

    cols = ["asset", "quantity", "value"]
    if "asset" not in portfolio_df.columns:
        cols = portfolio_df.columns.tolist()[:3]

    lines = build_table_like_lines(portfolio_df, cols, max_rows=profile.max_rows_per_section)
    section = build_section("Sanal Varlıklar", lines)

    disclaimer = build_disclaimer()
    footer = build_footer(created_at)

    body = f"{header}{section}{disclaimer}{footer}"

    return NotificationMessage(
        message_id=msg_id,
        notification_type="portfolio_summary",
        severity="info",
        title=title,
        body=body,
        created_at_utc=created_at,
        profile_name=profile.name
    )

def build_paper_position_message(positions_df: pd.DataFrame, summary: dict, profile: NotificationProfile) -> NotificationMessage:
    title = "Sanal Pozisyon Özeti"
    created_at = datetime.now(timezone.utc).isoformat()
    msg_id = build_notification_message_id("paper_summary", title, created_at)

    header = build_header(title, "info")

    cols = ["symbol", "side", "size", "pnl"]
    if "symbol" not in positions_df.columns:
        cols = positions_df.columns.tolist()[:4]

    lines = build_table_like_lines(positions_df, cols, max_rows=profile.max_rows_per_section)
    section = build_section("Açık Sanal Pozisyonlar", lines)

    disclaimer = build_disclaimer()
    footer = build_footer(created_at)

    body = f"{header}{section}{disclaimer}{footer}"

    return NotificationMessage(
        message_id=msg_id,
        notification_type="paper_summary",
        severity="info",
        title=title,
        body=body,
        created_at_utc=created_at,
        profile_name=profile.name
    )
