from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_data_lineage.data_lineage_config import DataLineageProfile


METADATA_ONLY_PROVENANCE_ITEMS = [
    {
        "provenance_id": "meta_prov_news",
        "dataset_type": "dataset_news_metadata",
        "metadata_only": True,
        "full_text_prohibited": True,
        "scraping_prohibited": True,
        "copyright_compliant": True,
        "retention_policy": "References and topic tags only",
        "status_label": "lineage_complete",
    },
    {
        "provenance_id": "meta_prov_calendar",
        "dataset_type": "dataset_calendar_event",
        "metadata_only": True,
        "full_text_prohibited": True,
        "scraping_prohibited": True,
        "copyright_compliant": True,
        "retention_policy": "Event schedules, categories, and impact flags only",
        "status_label": "lineage_complete",
    },
    {
        "provenance_id": "meta_prov_macro",
        "dataset_type": "dataset_macro_timeseries",
        "metadata_only": True,
        "full_text_prohibited": True,
        "scraping_prohibited": True,
        "copyright_compliant": True,
        "retention_policy": "Indicator definitions, frequencies, and numeric points only",
        "status_label": "lineage_complete",
    },
    {
        "provenance_id": "meta_prov_provider",
        "dataset_type": "dataset_provider_metadata",
        "metadata_only": True,
        "full_text_prohibited": True,
        "scraping_prohibited": True,
        "copyright_compliant": True,
        "retention_policy": "Provider schemas and capability matrices only",
        "status_label": "lineage_complete",
    },
]


def build_metadata_only_provenance_registry(
    profile: DataLineageProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    df = pd.DataFrame.from_records(METADATA_ONLY_PROVENANCE_ITEMS)
    summary = summarize_metadata_only_provenance(df)
    return df, summary


def summarize_metadata_only_provenance(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_metadata_only_records": len(df),
        "all_metadata_only": bool(df["metadata_only"].all()) if "metadata_only" in df.columns and len(df) > 0 else True,
        "all_scraping_prohibited": bool(df["scraping_prohibited"].all()) if "scraping_prohibited" in df.columns and len(df) > 0 else True,
        "current_phase": 114,
        "target_final_phase": 160,
    }
