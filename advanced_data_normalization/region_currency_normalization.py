from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_normalization.data_normalization_config import DataNormalizationProfile
from advanced_data_normalization.data_normalization_models import (
    NormalizationFinding,
    build_normalization_finding_id,
)

REGION_MAPPINGS = {
    "UNITED STATES": "US",
    "USA": "US",
    "U.S.": "US",
    "US": "US",
    "EUROZONE": "EU",
    "EUROPE": "EU",
    "TÜRKİYE": "TR",
    "TÜRKIYE": "TR",
    "TURKEY": "TR",
    "TURKIYE": "TR",
    "TR": "TR",

    "UNITED KINGDOM": "GB",
    "UK": "GB",
    "GREAT BRITAIN": "GB",
    "GB": "GB",
    "JAPAN": "JP",
    "JP": "JP",
    "GERMANY": "DE",
    "DE": "DE",
    "CHINA": "CN",
    "CN": "CN",
}

CURRENCY_MAPPINGS = {
    "USDOLLAR": "USD",
    "USD": "USD",
    "DOLLAR": "USD",
    "TURKISH LIRA": "TRY",
    "TURKISH LIRASI": "TRY",
    "TRY": "TRY",
    "TL": "TRY",
    "EURO": "EUR",
    "EUR": "EUR",
    "BRITISH POUND": "GBP",
    "POUND": "GBP",
    "STERLING": "GBP",
    "GBP": "GBP",
    "JAPANESE YEN": "JPY",
    "YEN": "JPY",
    "JPY": "JPY",
    "SWISS FRANC": "CHF",
    "CHF": "CHF",
    "CANADIAN DOLLAR": "CAD",
    "CAD": "CAD",
    "AUSTRALIAN DOLLAR": "AUD",
    "AUD": "AUD",
}


def normalize_region_code(value: str) -> str:
    if not value or not isinstance(value, str):
        return "UNKNOWN_REGION"
    clean = value.strip().upper()
    return REGION_MAPPINGS.get(clean, clean[:2] if len(clean) >= 2 else "UNKNOWN_REGION")


def normalize_currency_code(value: str) -> str:
    if not value or not isinstance(value, str):
        return "UNKNOWN_CURRENCY"
    clean = value.strip().upper()
    return CURRENCY_MAPPINGS.get(clean, clean[:3] if len(clean) >= 3 else "UNKNOWN_CURRENCY")


def normalize_region_currency_dataframe(
    df: pd.DataFrame,
    region_field: str = "region",
    currency_field: str = "currency",
) -> Tuple[pd.DataFrame, List[NormalizationFinding]]:
    out_df = df.copy()
    findings: List[NormalizationFinding] = []

    if region_field in out_df.columns:
        norm_regions = []
        for idx, val in enumerate(out_df[region_field]):
            norm = normalize_region_code(str(val))
            norm_regions.append(norm)
            if norm == "UNKNOWN_REGION":
                f = NormalizationFinding(
                    finding_id=build_normalization_finding_id("region_std", "dataset_macro_timeseries", f"{region_field}_{idx}"),
                    rule_id="norm_rule_region_currency_region_iso_standard",
                    dataset_type="dataset_macro_timeseries",
                    source_field=region_field,
                    original_value_repr=str(val),
                    normalized_value_repr=norm,
                    status_label="normalization_manual_review_required",
                    severity_label="normalization_medium",
                    message=f"Bilinmeyen bölge/ülke kodu: {val}",
                    manual_review_required=True,
                )
                findings.append(f)
        out_df["normalized_region"] = norm_regions

    if currency_field in out_df.columns:
        norm_currs = []
        for idx, val in enumerate(out_df[currency_field]):
            norm = normalize_currency_code(str(val))
            norm_currs.append(norm)
            if norm == "UNKNOWN_CURRENCY":
                f = NormalizationFinding(
                    finding_id=build_normalization_finding_id("curr_std", "dataset_macro_timeseries", f"{currency_field}_{idx}"),
                    rule_id="norm_rule_region_currency_currency_iso_standard",
                    dataset_type="dataset_macro_timeseries",
                    source_field=currency_field,
                    original_value_repr=str(val),
                    normalized_value_repr=norm,
                    status_label="normalization_manual_review_required",
                    severity_label="normalization_medium",
                    message=f"Bilinmeyen para birimi kodu: {val}",
                    manual_review_required=True,
                )
                findings.append(f)
        out_df["normalized_currency"] = norm_currs

    return out_df, findings


def build_region_country_currency_normalization_registry(
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records = []
    for raw, norm in REGION_MAPPINGS.items():
        records.append({
            "mapping_type": "region",
            "raw_value": raw,
            "normalized_code": norm,
            "current_phase": 113,
        })
    for raw, norm in CURRENCY_MAPPINGS.items():
        records.append({
            "mapping_type": "currency",
            "raw_value": raw,
            "normalized_code": norm,
            "current_phase": 113,
        })
    df = pd.DataFrame.from_records(records)
    summary = summarize_region_currency_normalization(df)
    return df, summary


def summarize_region_currency_normalization(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_mappings": len(df),
        "region_mappings_count": len(df[df["mapping_type"] == "region"]) if "mapping_type" in df.columns else 0,
        "currency_mappings_count": len(df[df["mapping_type"] == "currency"]) if "mapping_type" in df.columns else 0,
        "current_phase": 113,
        "target_final_phase": 160,
    }
