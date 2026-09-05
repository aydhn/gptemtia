from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_normalization.data_normalization_config import DataNormalizationProfile
from advanced_data_normalization.data_normalization_models import (
    NormalizationFinding,
    build_normalization_finding_id,
)

FREQUENCY_MAPPINGS = {
    "DAILY": "1d",
    "1D": "1d",
    "D": "1d",
    "DAY": "1d",
    "WEEKLY": "1w",
    "1W": "1w",
    "W": "1w",
    "WEEK": "1w",
    "MONTHLY": "1mo",
    "1M": "1mo",
    "M": "1mo",
    "1MO": "1mo",
    "MONTH": "1mo",
    "QUARTERLY": "1q",
    "1Q": "1q",
    "Q": "1q",
    "QUARTER": "1q",
    "YEARLY": "1y",
    "ANNUAL": "1y",
    "ANNUALLY": "1y",
    "1Y": "1y",
    "Y": "1y",
    "HOURLY": "1h",
    "1H": "1h",
    "H": "1h",
}


def normalize_frequency_value(value: str) -> str:
    if not value or not isinstance(value, str):
        return "unknown_freq"
    clean = value.strip().upper()
    return FREQUENCY_MAPPINGS.get(clean, clean.lower())


def normalize_frequency_dataframe(
    df: pd.DataFrame,
    field: str = "frequency",
) -> Tuple[pd.DataFrame, List[NormalizationFinding]]:
    out_df = df.copy()
    findings: List[NormalizationFinding] = []
    if field not in out_df.columns:
        return out_df, findings

    normalized_col = []
    for idx, raw_val in enumerate(out_df[field]):
        norm_val = normalize_frequency_value(str(raw_val))
        normalized_col.append(norm_val)
        if norm_val == "unknown_freq":
            f = NormalizationFinding(
                finding_id=build_normalization_finding_id("freq_std", "dataset_macro_timeseries", f"{field}_{idx}"),
                rule_id="norm_rule_frequency_frequency_canonical_standard",
                dataset_type="dataset_macro_timeseries",
                source_field=field,
                original_value_repr=str(raw_val),
                normalized_value_repr=norm_val,
                status_label="normalization_manual_review_required",
                severity_label="normalization_medium",
                message=f"Bilinmeyen frekans değeri: {raw_val}",
                manual_review_required=True,
            )
            findings.append(f)
        elif str(raw_val) != norm_val:
            f = NormalizationFinding(
                finding_id=build_normalization_finding_id("freq_std", "dataset_macro_timeseries", f"{field}_{idx}"),
                rule_id="norm_rule_frequency_frequency_canonical_standard",
                dataset_type="dataset_macro_timeseries",
                source_field=field,
                original_value_repr=str(raw_val),
                normalized_value_repr=norm_val,
                status_label="normalization_applied",
                severity_label="normalization_info",
                message=f"Frekans kanonikleştirildi: {raw_val} -> {norm_val}",
                manual_review_required=False,
            )
            findings.append(f)

    out_df["normalized_frequency"] = normalized_col
    return out_df, findings


def build_frequency_normalization_registry(
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records = []
    for raw, norm in FREQUENCY_MAPPINGS.items():
        records.append({
            "raw_frequency": raw,
            "normalized_frequency": norm,
            "current_phase": 113,
        })
    df = pd.DataFrame.from_records(records)
    summary = summarize_frequency_normalization(df)
    return df, summary


def summarize_frequency_normalization(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_mappings": len(df),
        "canonical_frequencies": df["normalized_frequency"].unique().tolist() if "normalized_frequency" in df.columns else [],
        "current_phase": 113,
        "target_final_phase": 160,
    }
