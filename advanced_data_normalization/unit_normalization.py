from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_normalization.data_normalization_config import DataNormalizationProfile
from advanced_data_normalization.data_normalization_models import (
    NormalizationFinding,
    build_normalization_finding_id,
)

UNIT_MAPPINGS = {
    "PERCENT": "percent",
    "PERCENTAGE": "percent",
    "%": "percent",
    "PCT": "percent",
    "BASIS POINTS": "bps",
    "BPS": "bps",
    "BP": "bps",
    "USD/BARREL": "usd_per_barrel",
    "USD/BBL": "usd_per_barrel",
    "$/BBL": "usd_per_barrel",
    "USD/OZ": "usd_per_oz",
    "USD/OUNCE": "usd_per_oz",
    "$/OZ": "usd_per_oz",
    "INDEX POINTS": "index_points",
    "INDEX": "index_points",
    "POINTS": "index_points",
    "METRIC TON": "metric_ton",
    "MT": "metric_ton",
    "CONTRACTS": "contracts",
    "THOUSANDS": "thousands",
    "MILLIONS": "millions",
}


def normalize_unit_value(value: str) -> str:
    if not value or not isinstance(value, str):
        return "unknown_unit"
    clean = value.strip().upper()
    return UNIT_MAPPINGS.get(clean, clean.lower().replace(" ", "_").replace("/", "_per_"))


def normalize_unit_dataframe(
    df: pd.DataFrame,
    field: str = "unit",
) -> Tuple[pd.DataFrame, List[NormalizationFinding]]:
    out_df = df.copy()
    findings: List[NormalizationFinding] = []
    if field not in out_df.columns:
        return out_df, findings

    normalized_col = []
    for idx, raw_val in enumerate(out_df[field]):
        norm_val = normalize_unit_value(str(raw_val))
        normalized_col.append(norm_val)
        if norm_val == "unknown_unit":
            f = NormalizationFinding(
                finding_id=build_normalization_finding_id("unit_std", "dataset_macro_timeseries", f"{field}_{idx}"),
                rule_id="norm_rule_unit_unit_vocabulary_standard",
                dataset_type="dataset_macro_timeseries",
                source_field=field,
                original_value_repr=str(raw_val),
                normalized_value_repr=norm_val,
                status_label="normalization_manual_review_required",
                severity_label="normalization_medium",
                message=f"Bilinmeyen birim sözlüğü: {raw_val}",
                manual_review_required=True,
            )
            findings.append(f)
        elif str(raw_val) != norm_val:
            f = NormalizationFinding(
                finding_id=build_normalization_finding_id("unit_std", "dataset_macro_timeseries", f"{field}_{idx}"),
                rule_id="norm_rule_unit_unit_vocabulary_standard",
                dataset_type="dataset_macro_timeseries",
                source_field=field,
                original_value_repr=str(raw_val),
                normalized_value_repr=norm_val,
                status_label="normalization_applied",
                severity_label="normalization_info",
                message=f"Birim sözlüğü kanonikleştirildi: {raw_val} -> {norm_val}",
                manual_review_required=False,
            )
            findings.append(f)

    out_df["normalized_unit"] = normalized_col
    return out_df, findings


def build_unit_normalization_registry(
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records = []
    for raw, norm in UNIT_MAPPINGS.items():
        records.append({
            "raw_unit": raw,
            "normalized_unit": norm,
            "conversion_applied": False,
            "current_phase": 113,
        })
    df = pd.DataFrame.from_records(records)
    summary = summarize_unit_normalization(df)
    return df, summary


def summarize_unit_normalization(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_mappings": len(df),
        "canonical_units": df["normalized_unit"].unique().tolist() if "normalized_unit" in df.columns else [],
        "conversion_deferred_to_future_phase": True,
        "current_phase": 113,
        "target_final_phase": 160,
    }
