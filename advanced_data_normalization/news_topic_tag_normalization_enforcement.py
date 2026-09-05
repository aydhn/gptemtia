import re
from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_normalization.data_normalization_config import DataNormalizationProfile
from advanced_data_normalization.data_normalization_models import (
    NormalizationFinding,
    build_normalization_finding_id,
)

NEWS_TOPIC_MAP = {
    "central bank": "CENTRAL_BANK",
    "central_bank": "CENTRAL_BANK",
    "monetary policy": "CENTRAL_BANK",
    "inflation": "INFLATION",
    "cpi": "INFLATION",
    "crude oil": "CRUDE_OIL",
    "oil": "CRUDE_OIL",
    "energy": "CRUDE_OIL",
    "gold": "PRECIOUS_METALS",
    "precious metals": "PRECIOUS_METALS",
    "interest rate": "INTEREST_RATE",
    "rates": "INTEREST_RATE",
    "risk sentiment": "RISK_SENTIMENT",
    "risk_on": "RISK_SENTIMENT",
    "risk_off": "RISK_SENTIMENT",
    "forex": "FX_CURRENCY",
    "currencies": "FX_CURRENCY",
}


def normalize_news_topic_value(value: str) -> str:
    if not value or not isinstance(value, str):
        return "GENERAL"
    clean = value.strip().lower()
    return NEWS_TOPIC_MAP.get(clean, clean.upper().replace(" ", "_"))


def normalize_news_tag_value(value: str) -> str:
    if not value or not isinstance(value, str):
        return ""
    tags = [t.strip() for t in value.split(",") if t.strip()]
    normalized = [normalize_news_topic_value(t) for t in tags]
    return ",".join(sorted(list(set(normalized))))


def normalize_news_tags_dataframe(
    df: pd.DataFrame,
    fields: List[str] = None,
) -> Tuple[pd.DataFrame, List[NormalizationFinding]]:
    if fields is None:
        fields = ["tags"]
    out_df = df.copy()
    findings: List[NormalizationFinding] = []

    for fld in fields:
        if fld not in out_df.columns:
            continue
        normalized_col = []
        for idx, raw_val in enumerate(out_df[fld]):
            norm_val = normalize_news_tag_value(str(raw_val))
            normalized_col.append(norm_val)
            if str(raw_val) != norm_val:
                f = NormalizationFinding(
                    finding_id=build_normalization_finding_id("news_tag_std", "dataset_news_metadata", f"{fld}_{idx}"),
                    rule_id="norm_rule_news_topic_tag_news_topic_tag_standard",
                    dataset_type="dataset_news_metadata",
                    source_field=fld,
                    original_value_repr=str(raw_val),
                    normalized_value_repr=norm_val,
                    status_label="normalization_applied",
                    severity_label="normalization_info",
                    message=f"Haber etiketleri kanonik taksonomiye dönüştürüldü: {raw_val} -> {norm_val}",
                    manual_review_required=False,
                )
                findings.append(f)
        out_df[f"normalized_{fld}"] = normalized_col

    return out_df, findings


def build_news_topic_tag_normalization_enforcement_report(
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records = []
    for raw, norm in NEWS_TOPIC_MAP.items():
        records.append({
            "raw_topic": raw,
            "normalized_topic": norm,
            "current_phase": 113,
        })
    df = pd.DataFrame.from_records(records)
    summary = summarize_news_topic_tag_normalization_enforcement(df)
    return df, summary


def summarize_news_topic_tag_normalization_enforcement(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_mappings": len(df),
        "unique_normalized_topics": df["normalized_topic"].unique().tolist() if "normalized_topic" in df.columns else [],
        "current_phase": 113,
        "target_final_phase": 160,
    }
