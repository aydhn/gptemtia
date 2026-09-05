from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_normalization.data_normalization_config import DataNormalizationProfile
from advanced_data_normalization.data_normalization_models import (
    NormalizationFinding,
    build_normalization_finding_id,
)

MACRO_INDICATOR_MAPPINGS = {
    "US10Y": "US_10Y_YIELD",
    "US_10Y": "US_10Y_YIELD",
    "FEDFUNDS": "FED_POLICY_RATE",
    "FED_RATE": "FED_POLICY_RATE",
    "CPI_US_YOY": "US_CPI_YOY",
    "US_CPI": "US_CPI_YOY",
    "CPI_TR_YOY": "TR_CPI_YOY",
    "TR_CPI": "TR_CPI_YOY",
    "DXY": "DXY_PLACEHOLDER",
    "USD_INDEX": "DXY_PLACEHOLDER",
    "CBRT_RATE": "CBRT_POLICY_RATE",
    "1W_REPO_TR": "CBRT_POLICY_RATE",
    "ECB_RATE": "ECB_DEPOSIT_RATE",
    "UNEMP_US": "US_UNEMPLOYMENT_RATE",
    "GDP_US_QOQ": "US_GDP_QOQ",
}


def normalize_macro_indicator_value(value: str) -> str:
    if not value or not isinstance(value, str):
        return "UNKNOWN_INDICATOR"
    clean = value.strip().upper().replace(" ", "_").replace("-", "_")
    return MACRO_INDICATOR_MAPPINGS.get(clean, f"{clean}_CUSTOM")


def normalize_macro_indicator_dataframe(
    df: pd.DataFrame,
    field: str = "indicator",
) -> Tuple[pd.DataFrame, List[NormalizationFinding]]:
    out_df = df.copy()
    findings: List[NormalizationFinding] = []
    if field not in out_df.columns:
        return out_df, findings

    normalized_col = []
    for idx, raw_val in enumerate(out_df[field]):
        norm_val = normalize_macro_indicator_value(raw_val)
        normalized_col.append(norm_val)
        if norm_val == "UNKNOWN_INDICATOR" or norm_val.endswith("_CUSTOM"):
            f = NormalizationFinding(
                finding_id=build_normalization_finding_id("macro_ind_std", "dataset_macro_timeseries", f"{field}_{idx}"),
                rule_id="norm_rule_macro_indicator_macro_indicator_code_standard",
                dataset_type="dataset_macro_timeseries",
                source_field=field,
                original_value_repr=str(raw_val),
                normalized_value_repr=norm_val,
                status_label="normalization_manual_review_required",
                severity_label="normalization_medium",
                message=f"Bilinmeyen veya özel makro gösterge: {raw_val}",
                manual_review_required=True,
            )
            findings.append(f)
        elif str(raw_val) != norm_val:
            f = NormalizationFinding(
                finding_id=build_normalization_finding_id("macro_ind_std", "dataset_macro_timeseries", f"{field}_{idx}"),
                rule_id="norm_rule_macro_indicator_macro_indicator_code_standard",
                dataset_type="dataset_macro_timeseries",
                source_field=field,
                original_value_repr=str(raw_val),
                normalized_value_repr=norm_val,
                status_label="normalization_applied",
                severity_label="normalization_info",
                message=f"Makro gösterge kodu kanonikleştirildi: {raw_val} -> {norm_val}",
                manual_review_required=False,
            )
            findings.append(f)

    out_df["normalized_indicator"] = normalized_col
    return out_df, findings


def build_macro_indicator_normalization_enforcement_report(
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records = []
    for raw, norm in MACRO_INDICATOR_MAPPINGS.items():
        records.append({
            "raw_indicator": raw,
            "normalized_indicator": norm,
            "current_phase": 113,
        })
    df = pd.DataFrame.from_records(records)
    summary = summarize_macro_indicator_normalization_enforcement(df)
    return df, summary


def summarize_macro_indicator_normalization_enforcement(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_mappings": len(df),
        "unique_normalized_indicators": df["normalized_indicator"].unique().tolist() if "normalized_indicator" in df.columns else [],
        "current_phase": 113,
        "target_final_phase": 160,
    }
