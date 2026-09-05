from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_normalization.data_normalization_config import DataNormalizationProfile

VERSION_MAPPING = {
    "1": "v1.0",
    "1.0": "v1.0",
    "v1": "v1.0",
    "v1.0": "v1.0",
    "version_1": "v1.0",
    "2": "v2.0",
    "2.0": "v2.0",
    "v2": "v2.0",
    "v2.0": "v2.0",
}


import re

def normalize_schema_version(schema_name: str, version: str | None = None) -> str:
    if not version or not isinstance(version, str) or not version.strip():
        return "unknown_version_manual_review"
    clean = version.strip().lower()
    if clean in VERSION_MAPPING:
        return VERSION_MAPPING[clean]
    if re.match(r"^v\d+(\.\d+)?$", clean):
        return clean if "." in clean else f"{clean}.0"
    return f"custom_{clean}_manual_review"



def build_schema_version_normalization_registry(
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    for raw_v, norm_v in VERSION_MAPPING.items():
        records.append({
            "raw_version_input": raw_v,
            "normalized_version": norm_v,
            "is_canonical": norm_v.startswith("v"),
            "manual_review_required": False,
            "non_destructive": True,
        })
    df = pd.DataFrame.from_records(records)
    summary = summarize_schema_version_normalization(df)
    return df, summary


def summarize_schema_version_normalization(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_mappings": len(df),
        "canonical_versions": df["normalized_version"].unique().tolist() if "normalized_version" in df.columns else [],
        "current_phase": 113,
        "target_final_phase": 160,
    }
