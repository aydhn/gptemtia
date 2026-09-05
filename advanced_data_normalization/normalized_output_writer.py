import json
from pathlib import Path
from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_normalization.data_normalization_config import DataNormalizationProfile


def write_normalized_view_copy(
    df: pd.DataFrame,
    output_path: Path,
    allow_overwrite: bool = False,
) -> Path:
    target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)

    if target.exists() and not allow_overwrite:
        # Generate safe non-destructive unique suffix
        suffix_idx = 1
        new_target = target.parent / f"{target.stem}_v{suffix_idx}{target.suffix}"
        while new_target.exists():
            suffix_idx += 1
            new_target = target.parent / f"{target.stem}_v{suffix_idx}{target.suffix}"
        target = new_target

    df.to_csv(target, index=False)
    return target


def write_normalization_report_json(
    report: Dict[str, Any],
    output_path: Path,
    allow_overwrite: bool = False,
) -> Path:
    target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)

    if target.exists() and not allow_overwrite:
        suffix_idx = 1
        new_target = target.parent / f"{target.stem}_v{suffix_idx}{target.suffix}"
        while new_target.exists():
            suffix_idx += 1
            new_target = target.parent / f"{target.stem}_v{suffix_idx}{target.suffix}"
        target = new_target

    with open(target, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    return target


def build_normalized_output_manifest(
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    # Baseline manifest showing supported datasets and safe output targets
    records = [
        {
            "manifest_id": "man_fx_quote_dry_run",
            "dataset_name": "fx_quote_contract",
            "dataset_type": "dataset_fx_quote",
            "provider_name": "fx_dry_run_fixture_provider",
            "original_ref": "data/raw/fx/quotes_raw.csv",
            "normalized_ref": "data/lake/advanced_data_normalization/normalized_views/fx_quotes_normalized.csv",
            "schema_version": "v1.0",
            "row_count": 100,
            "normalized_field_count": 5,
            "source_preserved": True,
            "destructive_action_allowed": False,
            "manual_review_required": False,
        },
        {
            "manifest_id": "man_commodity_spot_dry_run",
            "dataset_name": "commodity_spot_contract",
            "dataset_type": "dataset_commodity_spot",
            "provider_name": "commodity_dry_run_fixture_provider",
            "original_ref": "data/raw/commodity/spot_raw.csv",
            "normalized_ref": "data/lake/advanced_data_normalization/normalized_views/commodity_spot_normalized.csv",
            "schema_version": "v1.0",
            "row_count": 100,
            "normalized_field_count": 6,
            "source_preserved": True,
            "destructive_action_allowed": False,
            "manual_review_required": False,
        },
        {
            "manifest_id": "man_macro_timeseries_dry_run",
            "dataset_name": "macro_timeseries_contract",
            "dataset_type": "dataset_macro_timeseries",
            "provider_name": "macro_official_api_provider_placeholder",
            "original_ref": "data/raw/macro/macro_raw.csv",
            "normalized_ref": "data/lake/advanced_data_normalization/normalized_views/macro_timeseries_normalized.csv",
            "schema_version": "v1.0",
            "row_count": 100,
            "normalized_field_count": 7,
            "source_preserved": True,
            "destructive_action_allowed": False,
            "manual_review_required": False,
        },
        {
            "manifest_id": "man_calendar_event_dry_run",
            "dataset_name": "calendar_event_contract",
            "dataset_type": "dataset_calendar_event",
            "provider_name": "calendar_licensed_provider_placeholder",
            "original_ref": "data/raw/calendar/events_raw.csv",
            "normalized_ref": "data/lake/advanced_data_normalization/normalized_views/calendar_events_normalized.csv",
            "schema_version": "v1.0",
            "row_count": 100,
            "normalized_field_count": 7,
            "source_preserved": True,
            "destructive_action_allowed": False,
            "manual_review_required": False,
        },
        {
            "manifest_id": "man_news_metadata_dry_run",
            "dataset_name": "news_metadata_contract",
            "dataset_type": "dataset_news_metadata",
            "provider_name": "news_public_dataset_provider_placeholder",
            "original_ref": "data/raw/news/metadata_raw.csv",
            "normalized_ref": "data/lake/advanced_data_normalization/normalized_views/news_metadata_normalized.csv",
            "schema_version": "v1.0",
            "row_count": 100,
            "normalized_field_count": 7,
            "source_preserved": True,
            "destructive_action_allowed": False,
            "manual_review_required": False,
        },
    ]
    df = pd.DataFrame.from_records(records)
    summary = summarize_normalized_output_manifest(df)
    return df, summary


def summarize_normalized_output_manifest(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_manifest_entries": len(df),
        "source_preserved_all": bool(df["source_preserved"].all()) if "source_preserved" in df.columns and len(df) > 0 else True,
        "destructive_action_allowed_zero": bool((~df["destructive_action_allowed"]).all()) if "destructive_action_allowed" in df.columns and len(df) > 0 else True,
        "current_phase": 113,
        "target_final_phase": 160,
    }
