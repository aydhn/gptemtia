"""
Synthetic Data Cards module.
"""

import pandas as pd
from pathlib import Path
from .metadata_models import ArtifactCard, build_artifact_card_id, artifact_card_to_dict
from .metadata_config import ArtifactMetadataProfile

def infer_synthetic_generation_notes(artifact_row: pd.Series) -> dict:
    return {"notes": "Generated offline for demo/testing."}

def build_synthetic_data_card_for_artifact(artifact_row: pd.Series, profile: ArtifactMetadataProfile) -> ArtifactCard:
    art_id = artifact_row["artifact_id"]

    return ArtifactCard(
        card_id=build_artifact_card_id(art_id, "synthetic_data_card"),
        artifact_id=art_id,
        card_type="synthetic_data_card",
        title=f"Synthetic Data Card for {artifact_row['title']}",
        summary="Local synthetic data artifact.",
        intended_use="synthetic scenario demo",
        non_use_policy="canli emir icin kullanilamaz, broker talimati icin kullanilamaz, yatirim tavsiyesi icin kullanilamaz.",
        limitations=["offline/local only", "not real market data", "no performance claims"],
        inputs=[],
        outputs=[],
        metrics={},
        lineage=[artifact_row["relative_path"]],
        reproducibility="reproducible_with_local_fixtures",
        warnings=["Synthetic data is not real market data."]
    )

def build_synthetic_data_card_registry(artifact_df: pd.DataFrame, profile: ArtifactMetadataProfile) -> tuple[pd.DataFrame, dict]:
    if artifact_df.empty or not profile.scan_datasets:
        return pd.DataFrame(), {"total_synthetic_data_cards": 0}

    artifacts = artifact_df[artifact_df["artifact_type"] == "synthetic_data_artifact"]
    cards = []

    for _, row in artifacts.iterrows():
        card = build_synthetic_data_card_for_artifact(row, profile)
        cards.append(artifact_card_to_dict(card))

    df = pd.DataFrame(cards) if cards else pd.DataFrame()
    return df, {"total_synthetic_data_cards": len(cards)}

def summarize_synthetic_data_cards(synthetic_cards_df: pd.DataFrame) -> dict:
    if synthetic_cards_df.empty:
        return {"total_cards": 0}
    return {"total_cards": len(synthetic_cards_df)}
