from typing import Tuple, Dict, Any, List, Optional
import pandas as pd
from advanced_data_normalization.data_normalization_config import DataNormalizationProfile
from advanced_data_normalization.data_normalization_models import (
    NormalizationFinding,
    build_normalization_finding_id,
)


def normalize_numeric_value(value: Any) -> Optional[float]:
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    clean = str(value).strip().replace(",", "")
    if clean.endswith("%"):
        clean = clean[:-1].strip()
    try:
        return float(clean)
    except (ValueError, TypeError):
        return None


def normalize_numeric_dataframe(
    df: pd.DataFrame,
    fields: List[str],
) -> Tuple[pd.DataFrame, List[NormalizationFinding]]:
    out_df = df.copy()
    findings: List[NormalizationFinding] = []

    for fld in fields:
        if fld not in out_df.columns:
            continue
        norm_values = []
        for idx, raw_val in enumerate(out_df[fld]):
            cast_val = normalize_numeric_value(raw_val)
            norm_values.append(cast_val)
            if cast_val is None and raw_val is not None and not (isinstance(raw_val, float) and pd.isna(raw_val)):
                f = NormalizationFinding(
                    finding_id=build_normalization_finding_id("num_cast", "dataset_numeric", f"{fld}_{idx}"),
                    rule_id="norm_rule_numeric_type_numeric_type_safe_cast",
                    dataset_type="dataset_numeric",
                    source_field=fld,
                    original_value_repr=str(raw_val),
                    normalized_value_repr="null",
                    status_label="normalization_manual_review_required",
                    severity_label="normalization_high",
                    message=f"Sayısal tipe dönüştürülemeyen değer: {raw_val}",
                    manual_review_required=True,
                )
                findings.append(f)
        out_df[f"normalized_{fld}"] = norm_values

    return out_df, findings


def build_numeric_type_normalization_registry(
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records = [
        {
            "canonical_numeric_type": "float64",
            "null_representation": "None / np.nan",
            "source_preserved": True,
            "policy": "Orijinal sütun asla silinmez; normalized_<field> alanı eklenir.",
            "current_phase": 113,
        }
    ]
    df = pd.DataFrame.from_records(records)
    summary = summarize_numeric_type_normalization(df)
    return df, summary


def summarize_numeric_type_normalization(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "canonical_numeric_type": "float64",
        "source_preserved": True,
        "destructive_cleaning_allowed": False,
        "current_phase": 113,
        "target_final_phase": 160,
    }
