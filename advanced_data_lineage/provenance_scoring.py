from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_data_lineage.data_lineage_config import DataLineageProfile


PROVENANCE_SCORE_ENTITIES = [
    ("advanced_fx_providers_engine", "provider", "dataset_fx_quote", 0.95, "provenance_high_confidence", 0, 0, "Complete local fixture lineage, no credentials required"),
    ("advanced_commodity_providers_engine", "provider", "dataset_commodity_spot", 0.90, "provenance_high_confidence", 0, 1, "Complete local fixture lineage, futures roll review queued"),
    ("advanced_macro_providers_engine", "provider", "dataset_macro_timeseries", 0.92, "provenance_high_confidence", 0, 0, "Complete local fixture lineage, standard vocabulary"),
    ("advanced_economic_calendar_engine", "provider", "dataset_calendar_event", 0.94, "provenance_high_confidence", 0, 0, "Complete local fixture lineage, release times tracked"),
    ("advanced_news_metadata_engine", "provider", "dataset_news_metadata", 0.98, "provenance_high_confidence", 0, 0, "Strict metadata-only, zero full-text, copyright compliant"),
    ("advanced_data_providers_abstraction", "provider", "dataset_provider_metadata", 0.95, "provenance_high_confidence", 0, 0, "Multi-provider abstraction contracts verified"),
    ("manual_file_provider_adapter", "provider", "dataset_provider_metadata", 0.70, "provenance_medium_confidence", 1, 1, "User-provided dropzone file, manual review required"),
    ("local_cache_provider_adapter", "provider", "dataset_provider_metadata", 0.88, "provenance_high_confidence", 0, 0, "Local offline snapshot cache with valid manifest"),
    ("official_api_provider_placeholder", "provider", "dataset_provider_metadata", 0.65, "provenance_medium_confidence", 1, 1, "Contract placeholder, zero live keys"),
    ("licensed_vendor_provider_placeholder", "provider", "dataset_provider_metadata", 0.55, "provenance_low_confidence", 2, 1, "Commercial placeholder, vendor license verification required"),
]


def calculate_provenance_confidence_score(
    df: pd.DataFrame, entity_name: str, profile: DataLineageProfile
) -> float:
    if "entity_name" in df.columns and "score" in df.columns:
        match = df[df["entity_name"] == entity_name]
        if not match.empty:
            return float(match["score"].iloc[0])
    return 0.80


def build_provenance_confidence_score_report(
    profile: DataLineageProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records = []
    for ent, etype, ds_type, sc, stat, missing, revs, notes in PROVENANCE_SCORE_ENTITIES:
        records.append({
            "score_id": f"prov_conf_{ent}",
            "entity_name": ent,
            "entity_type": etype,
            "dataset_type": ds_type,
            "provider_name": ent,
            "score": sc,
            "status_label": stat,
            "missing_links": missing,
            "manual_review_count": revs,
            "notes": notes,
        })
    df = pd.DataFrame.from_records(records)
    summary = summarize_provenance_confidence_scores(df)
    return df, summary


def summarize_provenance_confidence_scores(df: pd.DataFrame) -> Dict[str, Any]:
    mean_score = float(df["score"].mean()) if "score" in df.columns and len(df) > 0 else 0.0
    min_score = float(df["score"].min()) if "score" in df.columns and len(df) > 0 else 0.0
    return {
        "total_scored_entities": len(df),
        "mean_provenance_score": round(mean_score, 4),
        "min_provenance_score": round(min_score, 4),
        "high_confidence_count": int((df["status_label"] == "provenance_high_confidence").sum()) if "status_label" in df.columns else 0,
        "current_phase": 114,
        "target_final_phase": 160,
    }
