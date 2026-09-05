from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_data_lineage.data_lineage_config import DataLineageProfile


OUTPUT_LINEAGE_ITEMS = [
    {
        "output_lineage_id": "out_lin_fx_quote",
        "dataset_type": "dataset_fx_quote",
        "original_ref": "data/raw/fx/quotes_sample.csv",
        "normalized_ref": "data/lake/advanced_data_normalization/normalized_views/fx_quotes_normalized.parquet",
        "transformation_provenance_id": "trans_prov_dataset_fx_quote_pair_to_normalized_pair",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "lineage_status": "lineage_complete",
    },
    {
        "output_lineage_id": "out_lin_fx_ohlcv",
        "dataset_type": "dataset_fx_ohlcv",
        "original_ref": "data/raw/fx/ohlcv_sample.csv",
        "normalized_ref": "data/lake/advanced_data_normalization/normalized_views/fx_ohlcv_normalized.parquet",
        "transformation_provenance_id": "trans_prov_dataset_fx_ohlcv_timestamp_to_normalized_timestamp",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "lineage_status": "lineage_complete",
    },
    {
        "output_lineage_id": "out_lin_commodity_spot",
        "dataset_type": "dataset_commodity_spot",
        "original_ref": "data/raw/commodity/spot_sample.csv",
        "normalized_ref": "data/lake/advanced_data_normalization/normalized_views/commodity_spot_normalized.parquet",
        "transformation_provenance_id": "trans_prov_dataset_commodity_spot_symbol_to_normalized_symbol",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "lineage_status": "lineage_complete",
    },
    {
        "output_lineage_id": "out_lin_macro_timeseries",
        "dataset_type": "dataset_macro_timeseries",
        "original_ref": "data/raw/macro/macro_sample.csv",
        "normalized_ref": "data/lake/advanced_data_normalization/normalized_views/macro_timeseries_normalized.parquet",
        "transformation_provenance_id": "trans_prov_dataset_macro_timeseries_indicator_to_normalized_indicator",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "lineage_status": "lineage_complete",
    },
    {
        "output_lineage_id": "out_lin_calendar_event",
        "dataset_type": "dataset_calendar_event",
        "original_ref": "data/raw/calendar/events_sample.csv",
        "normalized_ref": "data/lake/advanced_data_normalization/normalized_views/calendar_events_normalized.parquet",
        "transformation_provenance_id": "trans_prov_dataset_calendar_event_event_to_normalized_event",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "lineage_status": "lineage_complete",
    },
    {
        "output_lineage_id": "out_lin_news_metadata",
        "dataset_type": "dataset_news_metadata",
        "original_ref": "data/raw/news/metadata_sample.csv",
        "normalized_ref": "data/lake/advanced_data_normalization/normalized_views/news_metadata_normalized.parquet",
        "transformation_provenance_id": "trans_prov_dataset_news_metadata_tags_to_normalized_tags",
        "source_preserved": True,
        "destructive_action_allowed": False,
        "lineage_status": "lineage_complete",
    },
]


def build_normalized_output_lineage_registry(
    profile: DataLineageProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    df = pd.DataFrame.from_records(OUTPUT_LINEAGE_ITEMS)
    summary = summarize_normalized_output_lineage_registry(df)
    return df, summary


def summarize_normalized_output_lineage_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_output_lineage_records": len(df),
        "dataset_types": df["dataset_type"].tolist() if "dataset_type" in df.columns else [],
        "all_source_preserved": bool(df["source_preserved"].all()) if "source_preserved" in df.columns and len(df) > 0 else True,
        "zero_destructive_actions": bool((~df["destructive_action_allowed"]).all()) if "destructive_action_allowed" in df.columns and len(df) > 0 else True,
        "current_phase": 114,
        "target_final_phase": 160,
    }
