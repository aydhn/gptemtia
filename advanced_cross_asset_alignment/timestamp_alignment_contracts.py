from typing import Tuple, Dict, Any, List, Optional
import pandas as pd
from datetime import datetime, timezone
import re

from advanced_cross_asset_alignment.cross_asset_alignment_config import (
    CrossAssetAlignmentProfile,
    get_default_cross_asset_alignment_profile,
)


TIMESTAMP_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_id": "tac_fx_daily_utc",
        "domain": "fx",
        "canonical_timestamp_format": "YYYY-MM-DDTHH:MM:SSZ",
        "timezone": "UTC",
        "max_backward_lag": "24h",
        "future_data_allowed": False,
        "description": "FX günlük çubukları için UTC bazlı zaman hizalama sözleşmesi.",
    },
    {
        "contract_id": "tac_commodity_daily_utc",
        "domain": "commodity",
        "canonical_timestamp_format": "YYYY-MM-DDTHH:MM:SSZ",
        "timezone": "UTC",
        "max_backward_lag": "24h",
        "future_data_allowed": False,
        "description": "Emtia sürekli kontratları için UTC bazlı zaman hizalama sözleşmesi.",
    },
    {
        "contract_id": "tac_macro_release_lag_utc",
        "domain": "macro",
        "canonical_timestamp_format": "YYYY-MM-DDTHH:MM:SSZ",
        "timezone": "UTC",
        "max_backward_lag": "90d",
        "future_data_allowed": False,
        "description": "Makro veri açıklamaları için kesin geçmiş tarihli (<= bar) asof bağlantı kuralı.",
    },
    {
        "contract_id": "tac_calendar_event_window_utc",
        "domain": "calendar",
        "canonical_timestamp_format": "YYYY-MM-DDTHH:MM:SSZ",
        "timezone": "UTC",
        "max_backward_lag": "7d",
        "future_data_allowed": False,
        "description": "Ekonomik takvim duyuruları için olay anı ve öncesi pencere hizalaması.",
    },
    {
        "contract_id": "tac_news_metadata_timestamp_utc",
        "domain": "news",
        "canonical_timestamp_format": "YYYY-MM-DDTHH:MM:SSZ",
        "timezone": "UTC",
        "max_backward_lag": "48h",
        "future_data_allowed": False,
        "description": "Haber metadata etiketleri için yayın anı timestamp eşleme kuralı (metadata-only).",
    },
]


def normalize_alignment_timestamp_to_utc(value: str, source_timezone: Optional[str] = None) -> str:
    cleaned = value.strip()
    try:
        # Check standard ISO
        if cleaned.endswith("Z"):
            dt = datetime.fromisoformat(cleaned.replace("Z", "+00:00"))
        elif "+" in cleaned or "-" in cleaned[10:]:
            dt = datetime.fromisoformat(cleaned)
        else:
            # Assume UTC if naive
            dt = datetime.fromisoformat(cleaned)
            dt = dt.replace(tzinfo=timezone.utc)
        utc_dt = dt.astimezone(timezone.utc)
        return utc_dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    except Exception:
        # Fallback date parse YYYY-MM-DD
        if re.match(r"^\d{4}-\d{2}-\d{2}$", cleaned):
            return f"{cleaned}T00:00:00Z"
        raise ValueError(f"Zaman damgası UTC formatına dönüştürülemedi: '{value}'")


def validate_timestamp_alignment_fields(df: pd.DataFrame, timestamp_fields: List[str]) -> Dict[str, Any]:
    issues = []
    missing_fields = [f for f in timestamp_fields if f not in df.columns]
    if missing_fields:
        issues.append(f"DataFrame içinde beklenen zaman damgası sütunları eksik: {missing_fields}")

    valid_fields = [f for f in timestamp_fields if f in df.columns]
    unparseable_counts = {}
    for f in valid_fields:
        unparseable = 0
        for val in df[f].dropna():
            try:
                normalize_alignment_timestamp_to_utc(str(val))
            except ValueError:
                unparseable += 1
        if unparseable > 0:
            unparseable_counts[f] = unparseable
            issues.append(f"Sütun '{f}' içinde {unparseable} adet ayrıştırılamayan zaman damgası bulundu.")

    return {
        "is_valid": len(issues) == 0,
        "checked_fields": timestamp_fields,
        "unparseable_counts": unparseable_counts,
        "issues": issues,
    }


def build_timestamp_alignment_contract_registry(
    profile: CrossAssetAlignmentProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_cross_asset_alignment_profile()
    df = pd.DataFrame(TIMESTAMP_CONTRACTS)
    summary = summarize_timestamp_alignment_contracts(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_timestamp_alignment_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_contracts": 0, "status": "EMPTY"}

    all_no_future = bool((~df["future_data_allowed"]).all()) if "future_data_allowed" in df.columns else False
    return {
        "total_contracts": len(df),
        "domains": list(df["domain"].unique()) if "domain" in df.columns else [],
        "all_future_data_blocked": all_no_future,
        "non_signal": True,
        "status": "READY" if all_no_future else "SAFETY_VIOLATION",
    }
