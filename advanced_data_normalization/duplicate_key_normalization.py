from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_normalization.data_normalization_config import DataNormalizationProfile
from advanced_data_normalization.data_normalization_models import (
    NormalizationFinding,
    build_normalization_finding_id,
)


def build_canonical_duplicate_key(row: Dict[str, Any], key_fields: List[str]) -> str:
    parts = []
    for f in key_fields:
        val = row.get(f, "")
        parts.append(str(val).strip().lower())
    return "::".join(parts)


def add_duplicate_key_column(
    df: pd.DataFrame,
    key_fields: List[str],
    key_field_name: str = "canonical_duplicate_key",
) -> Tuple[pd.DataFrame, List[NormalizationFinding]]:
    out_df = df.copy()
    findings: List[NormalizationFinding] = []
    if not key_fields:
        return out_df, findings

    canonical_keys = []
    for idx, row in out_df.iterrows():
        key = build_canonical_duplicate_key(row.to_dict(), key_fields)
        canonical_keys.append(key)

    out_df[key_field_name] = canonical_keys

    # Check for duplicates non-destructively
    duplicated_mask = out_df.duplicated(subset=[key_field_name], keep=False)
    dup_count = int(duplicated_mask.sum())
    if dup_count > 0:
        f = NormalizationFinding(
            finding_id=build_normalization_finding_id("dup_key", "dataset_all", key_field_name),
            rule_id="norm_rule_duplicate_key_duplicate_key_generation",
            dataset_type="dataset_all",
            source_field=key_field_name,
            original_value_repr=f"duplicates_found: {dup_count}",
            normalized_value_repr=f"key_column_added: {key_field_name}",
            status_label="normalization_manual_review_required",
            severity_label="normalization_medium",
            message=f"{dup_count} mükerrer kanonik anahtar tespit edildi. Silme yapılmadı, kayıtlar korundu.",
            manual_review_required=True,
        )
        findings.append(f)

    return out_df, findings


def build_duplicate_key_normalization_registry(
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records = [
        {
            "canonical_key_field": "canonical_duplicate_key",
            "separator": "::",
            "deduplication_mode": "non_destructive_tagging_only",
            "records_deleted": 0,
            "policy": "Kayıt silinmez; mükerrerlik Phase 115 benchmark veya ileri veri operasyonlarına devredilir.",
            "current_phase": 113,
        }
    ]
    df = pd.DataFrame.from_records(records)
    summary = summarize_duplicate_key_normalization(df)
    return df, summary


def summarize_duplicate_key_normalization(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "canonical_key_field": "canonical_duplicate_key",
        "records_deleted": 0,
        "destructive_action_allowed": False,
        "current_phase": 113,
        "target_final_phase": 160,
    }
