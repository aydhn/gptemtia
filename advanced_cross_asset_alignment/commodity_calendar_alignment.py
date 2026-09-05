from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_cross_asset_alignment.cross_asset_alignment_config import (
    CrossAssetAlignmentProfile,
    get_default_cross_asset_alignment_profile,
)


COMMODITY_CALENDAR_ITEMS: List[Dict[str, Any]] = [
    {
        "alignment_id": "comcal_wti_eia_crude",
        "commodity_symbol": "WTI_CRUDE_CONTINUOUS_PLACEHOLDER",
        "calendar_event": "EIA_CRUDE_INVENTORY_RELEASE",
        "event_window_policy": "event_timestamp_backward_alignment",
        "direction_claim_allowed": False,
        "non_signal": True,
        "notes": "Haftalık EIA ham petrol stok değişimi açıklanma anı takvim hizalaması.",
    },
    {
        "alignment_id": "comcal_ng_eia_storage",
        "commodity_symbol": "NATURAL_GAS_CONTINUOUS_PLACEHOLDER",
        "calendar_event": "EIA_NATURAL_GAS_STORAGE_RELEASE",
        "event_window_policy": "event_timestamp_backward_alignment",
        "direction_claim_allowed": False,
        "non_signal": True,
        "notes": "Haftalık EIA doğal gaz depolama değişimi olay penceresi.",
    },
    {
        "alignment_id": "comcal_gold_fomc",
        "commodity_symbol": "XAU/USD",
        "calendar_event": "FOMC_RATE_DECISION",
        "event_window_policy": "event_timestamp_backward_alignment",
        "direction_claim_allowed": False,
        "non_signal": True,
        "notes": "Altın ve FOMC faiz kararı zaman penceresi eşlemesi.",
    },
]


def build_commodity_calendar_alignment_registry(
    profile: CrossAssetAlignmentProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_cross_asset_alignment_profile()
    df = pd.DataFrame(COMMODITY_CALENDAR_ITEMS)
    summary = summarize_commodity_calendar_alignment(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_commodity_calendar_alignment(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_alignments": 0, "status": "EMPTY"}

    all_non_signal = bool(df["non_signal"].all()) if "non_signal" in df.columns else False
    return {
        "total_alignments": len(df),
        "commodities": list(df["commodity_symbol"].unique()) if "commodity_symbol" in df.columns else [],
        "calendar_events": list(df["calendar_event"].unique()) if "calendar_event" in df.columns else [],
        "all_non_signal": all_non_signal,
        "status": "READY" if all_non_signal else "SAFETY_VIOLATION",
    }
