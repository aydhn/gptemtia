from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_normalization.data_normalization_config import DataNormalizationProfile
from advanced_data_normalization.data_normalization_models import (
    NormalizationFinding,
    build_normalization_finding_id,
)

CALENDAR_EVENT_MAPPINGS = {
    "FOMC": "FOMC_RATE_DECISION",
    "FOMC_DECISION": "FOMC_RATE_DECISION",
    "US CPI": "US_CPI_RELEASE",
    "US_CPI": "US_CPI_RELEASE",
    "NFP": "US_NONFARM_PAYROLLS_RELEASE",
    "NONFARM PAYROLLS": "US_NONFARM_PAYROLLS_RELEASE",
    "CBRT": "CBRT_RATE_DECISION",
    "CBRT_DECISION": "CBRT_RATE_DECISION",
    "ECB": "ECB_RATE_DECISION",
    "ECB_DECISION": "ECB_RATE_DECISION",
    "BOE": "BOE_RATE_DECISION",
    "BOJ": "BOJ_RATE_DECISION",
    "US GDP": "US_GDP_RELEASE",
    "US_GDP": "US_GDP_RELEASE",
}


def normalize_calendar_event_value(value: str) -> str:
    if not value or not isinstance(value, str):
        return "UNKNOWN_EVENT"
    clean = value.strip().upper().replace("-", "_")
    return CALENDAR_EVENT_MAPPINGS.get(clean, f"{clean.replace(' ', '_')}_RELEASE")


def normalize_calendar_event_dataframe(
    df: pd.DataFrame,
    field: str = "canonical_event",
) -> Tuple[pd.DataFrame, List[NormalizationFinding]]:
    out_df = df.copy()
    findings: List[NormalizationFinding] = []
    if field not in out_df.columns:
        return out_df, findings

    normalized_col = []
    for idx, raw_val in enumerate(out_df[field]):
        norm_val = normalize_calendar_event_value(raw_val)
        normalized_col.append(norm_val)
        if norm_val == "UNKNOWN_EVENT":
            f = NormalizationFinding(
                finding_id=build_normalization_finding_id("cal_event_std", "dataset_calendar_event", f"{field}_{idx}"),
                rule_id="norm_rule_calendar_event_calendar_event_name_standard",
                dataset_type="dataset_calendar_event",
                source_field=field,
                original_value_repr=str(raw_val),
                normalized_value_repr=norm_val,
                status_label="normalization_manual_review_required",
                severity_label="normalization_medium",
                message=f"Bilinmeyen takvim olayı: {raw_val}",
                manual_review_required=True,
            )
            findings.append(f)
        elif str(raw_val) != norm_val:
            f = NormalizationFinding(
                finding_id=build_normalization_finding_id("cal_event_std", "dataset_calendar_event", f"{field}_{idx}"),
                rule_id="norm_rule_calendar_event_calendar_event_name_standard",
                dataset_type="dataset_calendar_event",
                source_field=field,
                original_value_repr=str(raw_val),
                normalized_value_repr=norm_val,
                status_label="normalization_applied",
                severity_label="normalization_info",
                message=f"Takvim olay adı kanonikleştirildi: {raw_val} -> {norm_val}",
                manual_review_required=False,
            )
            findings.append(f)

    out_df["normalized_event"] = normalized_col
    return out_df, findings


def build_calendar_event_normalization_enforcement_report(
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records = []
    for raw, norm in CALENDAR_EVENT_MAPPINGS.items():
        records.append({
            "raw_event_name": raw,
            "normalized_event": norm,
            "current_phase": 113,
        })
    df = pd.DataFrame.from_records(records)
    summary = summarize_calendar_event_normalization_enforcement(df)
    return df, summary


def summarize_calendar_event_normalization_enforcement(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_mappings": len(df),
        "unique_normalized_events": df["normalized_event"].unique().tolist() if "normalized_event" in df.columns else [],
        "current_phase": 113,
        "target_final_phase": 160,
    }
