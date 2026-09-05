from datetime import datetime, timezone
from typing import Tuple, Dict, Any, List, Optional
import pandas as pd
from advanced_data_normalization.data_normalization_config import DataNormalizationProfile
from advanced_data_normalization.data_normalization_models import (
    NormalizationFinding,
    build_normalization_finding_id,
)


def normalize_timestamp_to_utc_iso(
    value: Any,
    source_timezone: Optional[str] = None,
) -> str:
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return "INVALID_TIMESTAMP"
    val_str = str(value).strip()
    if not val_str:
        return "INVALID_TIMESTAMP"

    try:
        # Use pandas to parse diverse timestamp strings safely
        dt = pd.to_datetime(val_str, utc=False)
        if pd.isna(dt):
            return "INVALID_TIMESTAMP"
        # Convert to timezone aware UTC if not tz aware
        if dt.tzinfo is None:
            # Treat naive as UTC canonical (or source_timezone if provided)
            dt = dt.tz_localize("UTC")
        else:
            dt = dt.tz_convert("UTC")
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    except Exception:
        return "INVALID_TIMESTAMP"


def normalize_timestamp_dataframe(
    df: pd.DataFrame,
    timestamp_field: str = "timestamp",
    source_timezone: Optional[str] = None,
) -> Tuple[pd.DataFrame, List[NormalizationFinding]]:
    out_df = df.copy()
    findings: List[NormalizationFinding] = []
    if timestamp_field not in out_df.columns:
        return out_df, findings

    normalized_col = []
    for idx, raw_val in enumerate(out_df[timestamp_field]):
        norm_ts = normalize_timestamp_to_utc_iso(raw_val, source_timezone)
        normalized_col.append(norm_ts)
        if norm_ts == "INVALID_TIMESTAMP":
            f = NormalizationFinding(
                finding_id=build_normalization_finding_id("ts_utc", "dataset_timeseries", f"{timestamp_field}_{idx}"),
                rule_id="norm_rule_timestamp_timezone_timestamp_utc_iso_standard",
                dataset_type="dataset_timeseries",
                source_field=timestamp_field,
                original_value_repr=str(raw_val),
                normalized_value_repr=norm_ts,
                status_label="normalization_manual_review_required",
                severity_label="normalization_high",
                message=f"Ayrıştırılamayan zaman damgası: {raw_val}",
                manual_review_required=True,
            )
            findings.append(f)
        elif str(raw_val) != norm_ts:
            f = NormalizationFinding(
                finding_id=build_normalization_finding_id("ts_utc", "dataset_timeseries", f"{timestamp_field}_{idx}"),
                rule_id="norm_rule_timestamp_timezone_timestamp_utc_iso_standard",
                dataset_type="dataset_timeseries",
                source_field=timestamp_field,
                original_value_repr=str(raw_val),
                normalized_value_repr=norm_ts,
                status_label="normalization_applied",
                severity_label="normalization_info",
                message=f"Zaman damgası ISO8601 UTC formatına çevrildi: {raw_val} -> {norm_ts}",
                manual_review_required=False,
            )
            findings.append(f)

    out_df["normalized_timestamp"] = normalized_col
    return out_df, findings


def build_timestamp_timezone_normalization_registry(
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records = [
        {
            "canonical_timezone": "UTC",
            "iso_format": "%Y-%m-%dT%H:%M:%SZ",
            "local_note_timezone": "Europe/Istanbul",
            "policy": "Her zaman UTC kanonik saklanır; yerel saatler yalnızca rapor gösterimi içindir.",
            "source_preserved": True,
            "current_phase": 113,
        }
    ]
    df = pd.DataFrame.from_records(records)
    summary = summarize_timestamp_timezone_normalization(df)
    return df, summary


def summarize_timestamp_timezone_normalization(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "canonical_timezone": "UTC",
        "iso_standard": "ISO 8601 (Zulu UTC)",
        "source_preserved": True,
        "current_phase": 113,
        "target_final_phase": 160,
    }
