import re
from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_normalization.data_normalization_config import DataNormalizationProfile
from advanced_data_normalization.data_normalization_models import (
    NormalizationFinding,
    build_normalization_finding_id,
)


def normalize_slug_value(value: str) -> str:
    if not value or not isinstance(value, str):
        return ""
    clean = re.sub(r"[^\w\s-]", " ", value.strip().lower())
    return re.sub(r"[\s_-]+", "_", clean).strip("_")


def normalize_upper_token(value: str) -> str:
    if not value or not isinstance(value, str):
        return ""
    clean = re.sub(r"[^\w\s-]", " ", value.strip().upper())
    return re.sub(r"[\s_-]+", "_", clean).strip("_")



def normalize_string_dataframe(
    df: pd.DataFrame,
    fields: List[str],
) -> Tuple[pd.DataFrame, List[NormalizationFinding]]:
    out_df = df.copy()
    findings: List[NormalizationFinding] = []

    for fld in fields:
        if fld not in out_df.columns:
            continue
        normalized_col = []
        for idx, raw_val in enumerate(out_df[fld]):
            norm_val = normalize_slug_value(str(raw_val))
            normalized_col.append(norm_val)
            if str(raw_val) != norm_val:
                f = NormalizationFinding(
                    finding_id=build_normalization_finding_id("slug_std", "dataset_string", f"{fld}_{idx}"),
                    rule_id="norm_rule_string_case_slug_string_case_slug_standard",
                    dataset_type="dataset_string",
                    source_field=fld,
                    original_value_repr=str(raw_val),
                    normalized_value_repr=norm_val,
                    status_label="normalization_applied",
                    severity_label="normalization_info",
                    message=f"Metin slug standardına dönüştürüldü: {raw_val} -> {norm_val}",
                    manual_review_required=False,
                )
                findings.append(f)
        out_df[f"normalized_{fld}"] = normalized_col

    return out_df, findings


def build_string_case_slug_normalization_registry(
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records = [
        {
            "format": "snake_case_slug",
            "regex": r"[a-z0-9]+(?:_[a-z0-9]+)*",
            "description": "Küçük harf, alt tire ile ayrılmış kanonik kimlik biçimi.",
            "current_phase": 113,
        },
        {
            "format": "upper_token",
            "regex": r"[A-Z0-9]+(?:_[A-Z0-9]+)*",
            "description": "Büyük harf, alt tire ile ayrılmış taksonomi ve etiket biçimi.",
            "current_phase": 113,
        }
    ]
    df = pd.DataFrame.from_records(records)
    summary = summarize_string_case_slug_normalization(df)
    return df, summary


def summarize_string_case_slug_normalization(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "formats_count": len(df),
        "formats": df["format"].tolist() if "format" in df.columns else [],
        "current_phase": 113,
        "target_final_phase": 160,
    }
