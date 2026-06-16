"""
Feature Set Cards module.
"""

import pandas as pd
from pathlib import Path
from .metadata_models import ArtifactCard, build_artifact_card_id, artifact_card_to_dict
from .metadata_config import ArtifactMetadataProfile

def infer_feature_set_schema(artifact_row: pd.Series, project_root: Path | None = None) -> dict:
    return {"schema": "unknown"}

def infer_feature_set_limitations(artifact_row: pd.Series) -> list[str]:
    return ["offline/local only", "feature leakage risk", "indicator incompatibilities possible"]

def build_feature_set_card_for_artifact(artifact_row: pd.Series, profile: ArtifactMetadataProfile) -> ArtifactCard:
    art_id = artifact_row["artifact_id"]

    return ArtifactCard(
        card_id=build_artifact_card_id(art_id, "feature_set_card"),
        artifact_id=art_id,
        card_type="feature_set_card",
        title=f"Feature Set Card for {artifact_row['title']}",
        summary="Local offline feature set artifact.",
        intended_use="offline research review",
        non_use_policy="canli emir icin kullanilamaz, broker talimati icin kullanilamaz, yatirim tavsiyesi icin kullanilamaz.",
        limitations=infer_feature_set_limitations(artifact_row),
        inputs=["raw_data"],
        outputs=["features"],
        metrics={},
        lineage=[artifact_row["relative_path"]],
        reproducibility="partially_reproducible",
        warnings=["Feature set card is not a signal guarantee."]
    )

def build_feature_set_card_registry(artifact_df: pd.DataFrame, profile: ArtifactMetadataProfile) -> tuple[pd.DataFrame, dict]:
    if artifact_df.empty or not profile.scan_datasets:
        return pd.DataFrame(), {"total_feature_set_cards": 0}

    artifacts = artifact_df[artifact_df["artifact_type"] == "feature_set_artifact"]
    cards = []

    for _, row in artifacts.iterrows():
        card = build_feature_set_card_for_artifact(row, profile)
        cards.append(artifact_card_to_dict(card))

    df = pd.DataFrame(cards) if cards else pd.DataFrame()
    return df, {"total_feature_set_cards": len(cards)}

def summarize_feature_set_cards(feature_cards_df: pd.DataFrame) -> dict:
    if feature_cards_df.empty:
        return {"total_cards": 0}
    return {"total_cards": len(feature_cards_df)}
