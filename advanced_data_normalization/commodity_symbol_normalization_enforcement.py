from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_normalization.data_normalization_config import DataNormalizationProfile
from advanced_data_normalization.data_normalization_models import (
    NormalizationFinding,
    build_normalization_finding_id,
)

COMMODITY_MAPPINGS = {
    "GOLD": "XAU/USD",
    "XAUUSD": "XAU/USD",
    "XAU_USD": "XAU/USD",
    "SILVER": "XAG/USD",
    "XAGUSD": "XAG/USD",
    "XAG_USD": "XAG/USD",
    "CL": "WTI_CRUDE_CONTINUOUS_PLACEHOLDER",
    "WTI": "WTI_CRUDE_CONTINUOUS_PLACEHOLDER",
    "CRUDE_OIL": "WTI_CRUDE_CONTINUOUS_PLACEHOLDER",
    "NG": "NATURAL_GAS_CONTINUOUS_PLACEHOLDER",
    "NATGAS": "NATURAL_GAS_CONTINUOUS_PLACEHOLDER",
    "BRENT": "BRENT_CRUDE_CONTINUOUS_PLACEHOLDER",
    "COPPER": "COPPER_CONTINUOUS_PLACEHOLDER",
    "HG": "COPPER_CONTINUOUS_PLACEHOLDER",
    "PLATINUM": "XPT/USD",
    "PALLADIUM": "XPD/USD",
}


def normalize_commodity_symbol_value(value: str) -> str:
    if not value or not isinstance(value, str):
        return "UNKNOWN_COMMODITY"
    clean = value.strip().upper().replace("-", "_")
    return COMMODITY_MAPPINGS.get(clean, f"{clean}_PLACEHOLDER")


def normalize_commodity_symbol_dataframe(
    df: pd.DataFrame,
    field: str = "symbol",
) -> Tuple[pd.DataFrame, List[NormalizationFinding]]:
    out_df = df.copy()
    findings: List[NormalizationFinding] = []
    if field not in out_df.columns:
        return out_df, findings

    normalized_col = []
    for idx, raw_val in enumerate(out_df[field]):
        norm_val = normalize_commodity_symbol_value(raw_val)
        normalized_col.append(norm_val)
        if norm_val == "UNKNOWN_COMMODITY":
            f = NormalizationFinding(
                finding_id=build_normalization_finding_id("comm_symbol_std", "dataset_commodity_spot", f"{field}_{idx}"),
                rule_id="norm_rule_commodity_symbol_commodity_symbol_root_standard",
                dataset_type="dataset_commodity_spot",
                source_field=field,
                original_value_repr=str(raw_val),
                normalized_value_repr=norm_val,
                status_label="normalization_manual_review_required",
                severity_label="normalization_medium",
                message=f"Tanınmayan emtia sembolü: {raw_val}",
                manual_review_required=True,
            )
            findings.append(f)
        elif str(raw_val) != norm_val:
            f = NormalizationFinding(
                finding_id=build_normalization_finding_id("comm_symbol_std", "dataset_commodity_spot", f"{field}_{idx}"),
                rule_id="norm_rule_commodity_symbol_commodity_symbol_root_standard",
                dataset_type="dataset_commodity_spot",
                source_field=field,
                original_value_repr=str(raw_val),
                normalized_value_repr=norm_val,
                status_label="normalization_applied",
                severity_label="normalization_info",
                message=f"Emtia sembolü kanonikleştirildi: {raw_val} -> {norm_val}",
                manual_review_required=False,
            )
            findings.append(f)

    out_df["normalized_symbol"] = normalized_col
    return out_df, findings


def build_commodity_symbol_normalization_enforcement_report(
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records = []
    for raw, norm in COMMODITY_MAPPINGS.items():
        records.append({
            "raw_symbol": raw,
            "normalized_symbol": norm,
            "is_continuous_placeholder": "PLACEHOLDER" in norm,
            "current_phase": 113,
        })
    df = pd.DataFrame.from_records(records)
    summary = summarize_commodity_symbol_normalization_enforcement(df)
    return df, summary


def summarize_commodity_symbol_normalization_enforcement(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_mappings": len(df),
        "unique_normalized_symbols": df["normalized_symbol"].unique().tolist() if "normalized_symbol" in df.columns else [],
        "current_phase": 113,
        "target_final_phase": 160,
    }
