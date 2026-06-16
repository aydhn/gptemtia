"""
Lineage Cards module.
"""

import pandas as pd
from pathlib import Path
from .metadata_models import ArtifactCard, build_artifact_card_id, artifact_card_to_dict
from .metadata_config import ArtifactMetadataProfile

def infer_artifact_lineage(artifact_row: pd.Series, artifact_df: pd.DataFrame) -> list[str]:
    return ["unknown"]

def build_artifact_lineage_card(artifact_row: pd.Series, artifact_df: pd.DataFrame, profile: ArtifactMetadataProfile) -> ArtifactCard:
    art_id = artifact_row["artifact_id"]
    lineage = infer_artifact_lineage(artifact_row, artifact_df)

    return ArtifactCard(
        card_id=build_artifact_card_id(art_id, "lineage_card"),
        artifact_id=art_id,
        card_type="lineage_card",
        title=f"Lineage Card for {artifact_row['title']}",
        summary="Local offline artifact lineage.",
        intended_use="quality inspection",
        non_use_policy="canli emir icin kullanilamaz, broker talimati icin kullanilamaz, yatirim tavsiyesi icin kullanilamaz.",
        limitations=["offline/local only", "lineage may be approximate"],
        inputs=[],
        outputs=[],
        metrics={},
        lineage=lineage,
        reproducibility="reproducibility_unknown",
        warnings=["Unknown lineage warning. Lineage is not official audit trace."]
    )

def build_artifact_lineage_cards(artifact_df: pd.DataFrame, profile: ArtifactMetadataProfile) -> tuple[pd.DataFrame, dict]:
    if artifact_df.empty or not profile.scan_evidence:
        return pd.DataFrame(), {"total_lineage_cards": 0}

    cards = []

    for _, row in artifact_df.iterrows():
        card = build_artifact_lineage_card(row, artifact_df, profile)
        cards.append(artifact_card_to_dict(card))

    df = pd.DataFrame(cards) if cards else pd.DataFrame()
    return df, {"total_lineage_cards": len(cards)}

def summarize_lineage_cards(lineage_cards_df: pd.DataFrame) -> dict:
    if lineage_cards_df.empty:
        return {"total_cards": 0}
    return {"total_cards": len(lineage_cards_df)}
