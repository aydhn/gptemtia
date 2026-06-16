"""
Dataset Cards module.
"""

import pandas as pd
from pathlib import Path
from .metadata_models import ArtifactCard, build_artifact_card_id, artifact_card_to_dict
from .metadata_config import ArtifactMetadataProfile

def infer_dataset_schema(artifact_row: pd.Series, project_root: Path | None = None) -> dict:
    return {"schema": "unknown"}

def infer_dataset_source_type(artifact_row: pd.Series) -> str:
    path = str(artifact_row.get("relative_path", "")).lower()
    if "synthetic" in path:
        return "synthetic"
    if "fixture" in path:
        return "fixture"
    if "reports" in path:
        return "report-derived"
    return "local"

def build_dataset_card_for_artifact(artifact_row: pd.Series, profile: ArtifactMetadataProfile) -> ArtifactCard:
    art_id = artifact_row["artifact_id"]
    source_type = infer_dataset_source_type(artifact_row)

    return ArtifactCard(
        card_id=build_artifact_card_id(art_id, "dataset_card"),
        artifact_id=art_id,
        card_type="dataset_card",
        title=f"Dataset Card for {artifact_row['title']}",
        summary=f"Local research dataset artifact (source: {source_type}).",
        intended_use="offline research review",
        non_use_policy="canli emir icin kullanilamaz, broker talimati icin kullanilamaz, yatirim tavsiyesi icin kullanilamaz.",
        limitations=["offline/local only", "data staleness risk", "synthetic flag" if source_type == "synthetic" else "no live trading validation"],
        inputs=[],
        outputs=[],
        metrics={},
        lineage=[artifact_row["relative_path"]],
        reproducibility="reproducibility_unknown",
        warnings=[]
    )

def build_dataset_card_registry(artifact_df: pd.DataFrame, profile: ArtifactMetadataProfile) -> tuple[pd.DataFrame, dict]:
    if artifact_df.empty or not profile.scan_datasets:
        return pd.DataFrame(), {"total_dataset_cards": 0}

    ds_artifacts = artifact_df[artifact_df["artifact_type"].isin(["dataset_artifact", "feature_set_artifact", "synthetic_data_artifact"])]
    cards = []

    for _, row in ds_artifacts.iterrows():
        card = build_dataset_card_for_artifact(row, profile)
        cards.append(artifact_card_to_dict(card))

    df = pd.DataFrame(cards) if cards else pd.DataFrame()
    return df, {"total_dataset_cards": len(cards)}

def summarize_dataset_cards(dataset_cards_df: pd.DataFrame) -> dict:
    if dataset_cards_df.empty:
        return {"total_cards": 0}
    return {"total_cards": len(dataset_cards_df)}
