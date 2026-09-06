"""Phase 132: Scheduled vs Actual Release Alignment (Lookahead-Free Assurance)."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

DEFAULT_ALIGNMENT_ENTRIES = [
    {
        "alignment_id": "align_us_cpi",
        "indicator_id": "macro_us_cpi_yoy",
        "scheduled_time_utc": "13:30:00",
        "actual_observed_lag_secs": 2,
        "max_tolerated_drift_secs": 60,
        "alignment_status": "aligned_lookahead_free",
        "requires_backward_asof": True,
    },
    {
        "alignment_id": "align_us_nfp",
        "indicator_id": "macro_us_nfp",
        "scheduled_time_utc": "13:30:00",
        "actual_observed_lag_secs": 1,
        "max_tolerated_drift_secs": 60,
        "alignment_status": "aligned_lookahead_free",
        "requires_backward_asof": True,
    },
    {
        "alignment_id": "align_fomc_decision",
        "indicator_id": "macro_us_fed_funds_rate",
        "scheduled_time_utc": "19:00:00",
        "actual_observed_lag_secs": 5,
        "max_tolerated_drift_secs": 120,
        "alignment_status": "aligned_lookahead_free",
        "requires_backward_asof": True,
    },
]


def build_scheduled_actual_release_alignment_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of scheduled vs actual release alignment rules."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_ALIGNMENT_ENTRIES:
        row = dict(item)
        row["profile_name"] = p.profile_name
        row["non_signal"] = True
        row["source_preserved"] = True
        row["official_approval"] = False
        row["production_ready"] = False
        row["broker_ready"] = False
        rows.append(row)
    df = pd.DataFrame(rows)
    summary = {
        "total_alignments": len(df),
        "alignment_statuses": df["alignment_status"].unique().tolist(),
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def validate_scheduled_actual_release_alignment(
    df: pd.DataFrame,
    scheduled_ts: str,
    actual_ts: str,
) -> Dict[str, Any]:
    """Validate that actual publication timestamp does not introduce future lookahead bias."""
    if df.empty or scheduled_ts not in df.columns or actual_ts not in df.columns:
        return {
            "valid": False,
            "error": "Required timestamp columns not found or DataFrame empty",
            "lookahead_risk": True,
        }

    sched = pd.to_datetime(df[scheduled_ts], errors="coerce")
    actual = pd.to_datetime(df[actual_ts], errors="coerce")

    # If actual is prior to scheduled, potential data leak / revision leak
    premature_count = int((actual < sched).sum())
    null_count = int(actual.isna().sum() + sched.isna().sum())

    is_valid = (premature_count == 0) and (null_count == 0)
    return {
        "valid": is_valid,
        "total_rows": len(df),
        "premature_releases_count": premature_count,
        "null_timestamps_count": null_count,
        "lookahead_risk": not is_valid,
        "alignment_status": "PASS" if is_valid else "LOOKAHEAD_FAIL",
    }


def summarize_scheduled_actual_release_alignment(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for release alignment registry."""
    return {
        "total_alignments": len(df),
        "all_aligned": bool((df["alignment_status"] == "aligned_lookahead_free").all()) if "alignment_status" in df.columns else False,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
