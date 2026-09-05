from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_cross_asset_alignment.cross_asset_alignment_config import (
    CrossAssetAlignmentProfile,
    get_default_cross_asset_alignment_profile,
)


FX_CALENDAR_ITEMS: List[Dict[str, Any]] = [
    {
        "alignment_id": "fxcal_eur_usd_fomc",
        "fx_pair": "EUR/USD",
        "calendar_event": "FOMC_RATE_DECISION",
        "event_window_policy": "pre_post_event_window_placeholder",
        "direction_claim_allowed": False,
        "non_signal": True,
        "notes": "FOMC faiz duyurusu penceresi; yönlü beklenti ve işlem tavsiyesi içermez.",
    },
    {
        "alignment_id": "fxcal_eur_usd_ecb",
        "fx_pair": "EUR/USD",
        "calendar_event": "ECB_RATE_DECISION",
        "event_window_policy": "pre_post_event_window_placeholder",
        "direction_claim_allowed": False,
        "non_signal": True,
        "notes": "ECB faiz duyurusu penceresi; tarafsız olay zamanı eşlemesi.",
    },
    {
        "alignment_id": "fxcal_eur_usd_nfp",
        "fx_pair": "EUR/USD",
        "calendar_event": "US_NONFARM_PAYROLLS_RELEASE",
        "event_window_policy": "pre_post_event_window_placeholder",
        "direction_claim_allowed": False,
        "non_signal": True,
        "notes": "ABD Tarım Dışı İstihdam veri açıklanma anı hizalaması.",
    },
    {
        "alignment_id": "fxcal_usd_try_cbrt",
        "fx_pair": "USD/TRY",
        "calendar_event": "CBRT_RATE_DECISION",
        "event_window_policy": "pre_post_event_window_placeholder",
        "direction_claim_allowed": False,
        "non_signal": True,
        "notes": "TCMB Para Politikası Kurulu faiz kararı takvim hizalaması.",
    },
    {
        "alignment_id": "fxcal_usd_try_cpi",
        "fx_pair": "USD/TRY",
        "calendar_event": "TR_CPI_RELEASE",
        "event_window_policy": "pre_post_event_window_placeholder",
        "direction_claim_allowed": False,
        "non_signal": True,
        "notes": "TÜİK enflasyon verisi açıklanma anı pencere hizalaması.",
    },
]


def build_fx_calendar_alignment_registry(
    profile: CrossAssetAlignmentProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_cross_asset_alignment_profile()
    df = pd.DataFrame(FX_CALENDAR_ITEMS)
    summary = summarize_fx_calendar_alignment(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_fx_calendar_alignment(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_alignments": 0, "status": "EMPTY"}

    all_non_signal = bool(df["non_signal"].all()) if "non_signal" in df.columns else False
    all_no_direction = bool((~df["direction_claim_allowed"]).all()) if "direction_claim_allowed" in df.columns else False
    return {
        "total_alignments": len(df),
        "fx_pairs": list(df["fx_pair"].unique()) if "fx_pair" in df.columns else [],
        "calendar_events": list(df["calendar_event"].unique()) if "calendar_event" in df.columns else [],
        "all_non_signal": all_non_signal,
        "all_direction_claims_blocked": all_no_direction,
        "status": "READY" if (all_non_signal and all_no_direction) else "SAFETY_VIOLATION",
    }
