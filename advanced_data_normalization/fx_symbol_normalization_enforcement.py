import re
from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_normalization.data_normalization_config import DataNormalizationProfile
from advanced_data_normalization.data_normalization_models import (
    NormalizationFinding,
    build_normalization_finding_id,
)

FX_SPECIAL_MAPPINGS = {
    "EURUSD": "EUR/USD",
    "EUR_USD": "EUR/USD",
    "USDTRY": "USD/TRY",
    "USD_TRY": "USD/TRY",
    "GBPJPY": "GBP/JPY",
    "GBP_JPY": "GBP/JPY",
    "USDJPY": "USD/JPY",
    "USD_JPY": "USD/JPY",
    "GBPUSD": "GBP/USD",
    "GBP_USD": "GBP/USD",
    "USDCHF": "USD/CHF",
    "USD_CHF": "USD/CHF",
    "AUDUSD": "AUD/USD",
    "AUD_USD": "AUD/USD",
    "USDCAD": "USD/CAD",
    "USD_CAD": "USD/CAD",
    "EURTRY": "EUR/TRY",
    "EUR_TRY": "EUR/TRY",
}


def normalize_fx_symbol_value(value: str) -> str:
    if not value or not isinstance(value, str):
        return "UNKNOWN/PAIR"
    v = value.strip().upper()
    if "/" in v:
        parts = v.split("/")
        if len(parts) == 2 and len(parts[0]) == 3 and len(parts[1]) == 3:
            return f"{parts[0]}/{parts[1]}"
    if v in FX_SPECIAL_MAPPINGS:
        return FX_SPECIAL_MAPPINGS[v]
    # Remove separators like _ or -
    clean = re.sub(r"[^A-Z]", "", v)
    if len(clean) == 6:
        return f"{clean[:3]}/{clean[3:]}"
    return v


def normalize_fx_symbol_dataframe(
    df: pd.DataFrame,
    field: str = "pair",
) -> Tuple[pd.DataFrame, List[NormalizationFinding]]:
    out_df = df.copy()
    findings: List[NormalizationFinding] = []
    if field not in out_df.columns:
        return out_df, findings

    normalized_col = []
    for idx, raw_val in enumerate(out_df[field]):
        norm_val = normalize_fx_symbol_value(raw_val)
        normalized_col.append(norm_val)
        is_canonical = ("/" in norm_val and len(norm_val) == 7)
        if not is_canonical:
            f = NormalizationFinding(
                finding_id=build_normalization_finding_id("fx_symbol_std", "dataset_fx_quote", f"{field}_{idx}"),
                rule_id="norm_rule_fx_symbol_fx_symbol_slashed_standard",
                dataset_type="dataset_fx_quote",
                source_field=field,
                original_value_repr=str(raw_val),
                normalized_value_repr=norm_val,
                status_label="normalization_manual_review_required",
                severity_label="normalization_medium",
                message=f"Bilinmeyen FX parite sembolü: {raw_val}",
                manual_review_required=True,
            )
            findings.append(f)
        elif str(raw_val) != norm_val:

            f = NormalizationFinding(
                finding_id=build_normalization_finding_id("fx_symbol_std", "dataset_fx_quote", f"{field}_{idx}"),
                rule_id="norm_rule_fx_symbol_fx_symbol_slashed_standard",
                dataset_type="dataset_fx_quote",
                source_field=field,
                original_value_repr=str(raw_val),
                normalized_value_repr=norm_val,
                status_label="normalization_applied",
                severity_label="normalization_info",
                message=f"FX sembolü standart slash formatına dönüştürüldü: {raw_val} -> {norm_val}",
                manual_review_required=False,
            )
            findings.append(f)

    out_df["normalized_pair"] = normalized_col
    return out_df, findings


def build_fx_symbol_normalization_enforcement_report(
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records = []
    for raw, norm in FX_SPECIAL_MAPPINGS.items():
        records.append({
            "raw_symbol": raw,
            "normalized_pair": norm,
            "iso_compliant": True,
            "current_phase": 113,
        })
    df = pd.DataFrame.from_records(records)
    summary = summarize_fx_symbol_normalization_enforcement(df)
    return df, summary


def summarize_fx_symbol_normalization_enforcement(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_rules": len(df),
        "normalized_pairs": df["normalized_pair"].unique().tolist() if "normalized_pair" in df.columns else [],
        "current_phase": 113,
        "target_final_phase": 160,
    }
