from typing import Tuple, Dict, Any, List
import pandas as pd
from datetime import datetime

from advanced_cross_asset_alignment.cross_asset_alignment_config import (
    CrossAssetAlignmentProfile,
    get_default_cross_asset_alignment_profile,
)
from advanced_cross_asset_alignment.timestamp_alignment_contracts import normalize_alignment_timestamp_to_utc


SESSION_POLICIES: List[Dict[str, Any]] = [
    {
        "session_policy": "utc_day",
        "description": "UTC gün kovası (YYYY-MM-DD), standart günlük hizalama için kullanılır.",
        "bucket_granularity": "1d",
    },
    {
        "session_policy": "utc_hour",
        "description": "UTC saatlik kova (YYYY-MM-DDTHH:00:00Z), saatlik çubuk hizalama için kullanılır.",
        "bucket_granularity": "1h",
    },
    {
        "session_policy": "fx_24_5_placeholder",
        "description": "FX 24/5 işlem seansı kovası; Pazar açılışı ve Cuma kapanışı aralığını temsil eder.",
        "bucket_granularity": "session_week",
    },
    {
        "session_policy": "commodity_session_placeholder",
        "description": "Emtia elektronik işlem saatleri (CME/NYMEX) seans kovası.",
        "bucket_granularity": "session_daily",
    },
    {
        "session_policy": "macro_release_session_placeholder",
        "description": "Makro veri yayın saatleri (ör. 08:30 ET / 12:30 UTC) seans öncesi/sonrası kovası.",
        "bucket_granularity": "event_session",
    },
    {
        "session_policy": "calendar_event_window_placeholder",
        "description": "Ekonomik takvim olay penceresi kovası (duyuru anı +/- tolerans penceresi).",
        "bucket_granularity": "window",
    },
    {
        "session_policy": "news_metadata_window_placeholder",
        "description": "Haber metadata kümelenme penceresi kovası (4h / 24h konu etiketleri).",
        "bucket_granularity": "metadata_window",
    },
]


def build_session_bucket(timestamp_value: str, session_policy: str = "utc_day") -> str:
    norm_ts = normalize_alignment_timestamp_to_utc(timestamp_value)
    dt = datetime.fromisoformat(norm_ts.replace("Z", "+00:00"))

    if session_policy == "utc_day":
        return dt.strftime("%Y-%m-%d")
    elif session_policy == "utc_hour":
        return dt.strftime("%Y-%m-%dT%H")
    elif session_policy == "fx_24_5_placeholder":
        # Returns ISO year and week e.g. 2026-W36
        return f"{dt.isocalendar().year}-W{dt.isocalendar().week:02d}"
    elif session_policy == "commodity_session_placeholder":
        return f"cm_sess_{dt.strftime('%Y-%m-%d')}"
    elif session_policy == "macro_release_session_placeholder":
        return f"macro_rel_{dt.strftime('%Y-%m-%d')}"
    elif session_policy == "calendar_event_window_placeholder":
        return f"cal_win_{dt.strftime('%Y-%m-%d')}"
    elif session_policy == "news_metadata_window_placeholder":
        return f"news_win_{dt.strftime('%Y-%m-%d')}"
    else:
        return dt.strftime("%Y-%m-%d")


def build_session_calendar_alignment_registry(
    profile: CrossAssetAlignmentProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_cross_asset_alignment_profile()
    df = pd.DataFrame(SESSION_POLICIES)
    summary = summarize_session_calendar_alignment(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_session_calendar_alignment(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_session_policies": 0, "status": "EMPTY"}

    return {
        "total_session_policies": len(df),
        "total_policies": len(df),
        "policy_list": list(df["session_policy"]) if "session_policy" in df.columns else [],
        "non_signal": True,
        "status": "READY",
    }

