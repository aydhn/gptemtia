"""
Metadata Scoring module.
"""

import pandas as pd
from datetime import datetime, timezone
from pathlib import Path
from .metadata_config import ArtifactMetadataProfile

def calculate_metadata_completeness_score(cards_df: pd.DataFrame) -> float:
    if cards_df.empty:
        return 0.0
    # Simple check: non_use_policy and intended_use must exist and not be empty
    required_cols = ["intended_use", "non_use_policy", "limitations"]
    for col in required_cols:
        if col not in cards_df.columns:
             return 0.0

    complete_rows = cards_df[
        (cards_df["intended_use"].str.len() > 0) &
        (cards_df["non_use_policy"].str.len() > 0)
    ]
    return len(complete_rows) / len(cards_df)

def calculate_metadata_freshness_score(artifact_df: pd.DataFrame, profile: ArtifactMetadataProfile) -> float:
    if artifact_df.empty or "created_or_modified_at_utc" not in artifact_df.columns:
        return 0.0

    now = datetime.now(timezone.utc)
    fresh_count = 0
    total = len(artifact_df)

    for _, row in artifact_df.iterrows():
        dt_str = row["created_or_modified_at_utc"]
        if pd.isna(dt_str) or not dt_str:
            continue
        try:
            dt = datetime.fromisoformat(dt_str)
            days_old = (now - dt).days
            if days_old <= profile.freshness_days_warning:
                fresh_count += 1
        except:
            pass

    return fresh_count / total if total > 0 else 0.0

def classify_metadata_status(card_row: pd.Series) -> str:
    if pd.isna(card_row.get("intended_use")) or pd.isna(card_row.get("non_use_policy")):
        return "metadata_missing"
    return "metadata_complete"

def build_metadata_completeness_report(card_tables: dict[str, pd.DataFrame], profile: ArtifactMetadataProfile) -> tuple[pd.DataFrame, dict]:
    results = []

    for table_name, df in card_tables.items():
        score = calculate_metadata_completeness_score(df)
        results.append({
            "table_name": table_name,
            "completeness_score": score,
            "total_cards": len(df) if not df.empty else 0
        })

    res_df = pd.DataFrame(results) if results else pd.DataFrame()
    overall_score = res_df["completeness_score"].mean() if not res_df.empty else 0.0

    return res_df, {"overall_completeness_score": overall_score}

def build_metadata_freshness_report(artifact_df: pd.DataFrame, profile: ArtifactMetadataProfile) -> tuple[pd.DataFrame, dict]:
    score = calculate_metadata_freshness_score(artifact_df, profile)

    df = pd.DataFrame([{
        "metric": "overall_freshness_score",
        "value": score,
        "warning_threshold_days": profile.freshness_days_warning
    }])

    return df, {"overall_freshness_score": score}

def summarize_metadata_scoring(completeness_df: pd.DataFrame, freshness_df: pd.DataFrame) -> dict:
    comp_score = completeness_df["completeness_score"].mean() if not completeness_df.empty and "completeness_score" in completeness_df.columns else 0.0
    fresh_score = freshness_df["value"].iloc[0] if not freshness_df.empty and "value" in freshness_df.columns else 0.0

    return {
        "completeness_score": comp_score,
        "freshness_score": fresh_score
    }
