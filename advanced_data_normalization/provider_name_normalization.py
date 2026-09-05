import re
from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_normalization.data_normalization_config import DataNormalizationProfile

PROVIDER_CANONICAL_MAP = {
    "fx dry run fixture provider": "fx_dry_run_fixture_provider",
    "commodity dry run": "commodity_dry_run_fixture_provider",
    "commodity dry run fixture provider": "commodity_dry_run_fixture_provider",
    "macro official placeholder": "macro_official_api_provider_placeholder",
    "macro official api provider placeholder": "macro_official_api_provider_placeholder",
    "calendar licensed placeholder": "calendar_licensed_provider_placeholder",
    "calendar licensed provider placeholder": "calendar_licensed_provider_placeholder",
    "news public dataset": "news_public_dataset_provider_placeholder",
    "news public dataset provider placeholder": "news_public_dataset_provider_placeholder",
    "fx manual file provider": "fx_manual_file_provider",
    "fx local cache provider": "fx_local_cache_provider",
    "fx official api provider placeholder": "fx_official_api_provider_placeholder",
    "commodity manual file provider": "commodity_manual_file_provider",
    "commodity local cache provider": "commodity_local_cache_provider",
    "macro manual file provider": "macro_manual_file_provider",
    "macro local cache provider": "macro_local_cache_provider",
    "calendar manual file provider": "calendar_manual_file_provider",
    "calendar local cache provider": "calendar_local_cache_provider",
    "news manual file provider": "news_manual_file_provider",
    "news local cache provider": "news_local_cache_provider",
}


def normalize_provider_name(provider_name: str) -> str:
    if not provider_name or not isinstance(provider_name, str) or not provider_name.strip():
        return "unknown_provider"
    clean = provider_name.strip().lower()
    if clean in PROVIDER_CANONICAL_MAP:
        return PROVIDER_CANONICAL_MAP[clean]
    # Slugify arbitrary provider name safely
    slug = re.sub(r"[^\w\s-]", "", clean)
    slug = re.sub(r"[\s_-]+", "_", slug).strip("_")
    return slug or "unknown_provider"


def build_provider_name_normalization_registry(
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    for raw_name, norm_name in PROVIDER_CANONICAL_MAP.items():
        records.append({
            "raw_provider_name": raw_name,
            "normalized_provider_name": norm_name,
            "is_fixture_or_placeholder": "placeholder" in norm_name or "fixture" in norm_name or "dry_run" in norm_name,
            "no_credentials_contained": True,
            "current_phase": 113,
        })
    df = pd.DataFrame.from_records(records)
    summary = summarize_provider_name_normalization(df)
    return df, summary


def summarize_provider_name_normalization(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_providers": len(df),
        "total_mappings": len(df),
        "normalized_providers": df["normalized_provider_name"].tolist() if "normalized_provider_name" in df.columns else [],
        "current_phase": 113,
        "target_final_phase": 160,
    }

