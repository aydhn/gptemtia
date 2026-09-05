from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_cross_asset_alignment.cross_asset_alignment_config import (
    CrossAssetAlignmentProfile,
    get_default_cross_asset_alignment_profile,
)


MACRO_CALENDAR_ITEMS: List[Dict[str, Any]] = [
    {
        "alignment_id": "mcal_fed_rate_fomc",
        "macro_indicator": "FED_POLICY_RATE",
        "calendar_event": "FOMC_RATE_DECISION",
        "frequency": "ad_hoc_meeting",
        "revision_lag_policy": "immediate_scheduled_release",
        "non_signal": True,
        "notes": "Fed politika faizi ve FOMC faiz kararı takvim duyurusu eşlemesi.",
    },
    {
        "alignment_id": "mcal_ecb_rate_meeting",
        "macro_indicator": "ECB_POLICY_RATE",
        "calendar_event": "ECB_RATE_DECISION",
        "frequency": "ad_hoc_meeting",
        "revision_lag_policy": "immediate_scheduled_release",
        "non_signal": True,
        "notes": "ECB politika faizi ve duyuru takvimi eşlemesi.",
    },
    {
        "alignment_id": "mcal_cbrt_rate_meeting",
        "macro_indicator": "CBRT_POLICY_RATE",
        "calendar_event": "CBRT_RATE_DECISION",
        "frequency": "monthly_meeting",
        "revision_lag_policy": "immediate_scheduled_release",
        "non_signal": True,
        "notes": "TCMB PPK faiz kararı takvim eşlemesi.",
    },
    {
        "alignment_id": "mcal_us_cpi_release",
        "macro_indicator": "US_CPI_RELEASE",
        "calendar_event": "US_CPI_RELEASE",
        "frequency": "monthly",
        "revision_lag_policy": "monthly_scheduled_release",
        "non_signal": True,
        "notes": "ABD TÜFE enflasyon göstergesi ve aylık açıklanma takvimi eşlemesi.",
    },
    {
        "alignment_id": "mcal_us_nfp_release",
        "macro_indicator": "US_NONFARM_PAYROLLS",
        "calendar_event": "US_NONFARM_PAYROLLS_RELEASE",
        "frequency": "monthly",
        "revision_lag_policy": "monthly_scheduled_release",

        "non_signal": True,
        "notes": "ABD Tarım Dışı İstihdam verisi ve aylık açıklanma anı eşlemesi.",
    },
]


def build_macro_calendar_alignment_registry(
    profile: CrossAssetAlignmentProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_cross_asset_alignment_profile()
    df = pd.DataFrame(MACRO_CALENDAR_ITEMS)
    summary = summarize_macro_calendar_alignment(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_macro_calendar_alignment(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_alignments": 0, "status": "EMPTY"}

    all_non_signal = bool(df["non_signal"].all()) if "non_signal" in df.columns else False
    return {
        "total_alignments": len(df),
        "macro_indicators": list(df["macro_indicator"].unique()) if "macro_indicator" in df.columns else [],
        "calendar_events": list(df["calendar_event"].unique()) if "calendar_event" in df.columns else [],
        "all_non_signal": all_non_signal,
        "status": "READY" if all_non_signal else "SAFETY_VIOLATION",
    }
