"""
Intended Use Cards module.
"""

import pandas as pd
from pathlib import Path
from .metadata_models import ArtifactCard, build_artifact_card_id, artifact_card_to_dict
from .metadata_config import ArtifactMetadataProfile

def infer_intended_use(artifact_row: pd.Series) -> str:
    art_type = artifact_row.get("artifact_type", "")
    if art_type == "scenario_artifact" or art_type == "synthetic_data_artifact":
        return "synthetic scenario demo"
    elif art_type == "research_report_artifact" or art_type == "documentation_artifact":
        return "documentation_use_only"
    return "offline research review"

def build_intended_use_card(artifact_row: pd.Series, profile: ArtifactMetadataProfile) -> ArtifactCard:
    art_id = artifact_row["artifact_id"]
    use = infer_intended_use(artifact_row)

    return ArtifactCard(
        card_id=build_artifact_card_id(art_id, "intended_use_card"),
        artifact_id=art_id,
        card_type="intended_use_card",
        title=f"Intended Use Card for {artifact_row['title']}",
        summary="Local offline artifact intended use.",
        intended_use=use,
        non_use_policy="canli emir icin kullanilamaz, broker talimati icin kullanilamaz, yatirim tavsiyesi icin kullanilamaz.",
        limitations=["offline/local only"],
        inputs=[],
        outputs=[],
        metrics={},
        lineage=[artifact_row["relative_path"]],
        reproducibility="reproducibility_unknown",
        warnings=[]
    )

def build_intended_use_cards(artifact_df: pd.DataFrame, profile: ArtifactMetadataProfile) -> tuple[pd.DataFrame, dict]:
    if artifact_df.empty or not profile.scan_evidence:
        return pd.DataFrame(), {"total_intended_use_cards": 0}

    cards = []

    for _, row in artifact_df.iterrows():
        card = build_intended_use_card(row, profile)
        cards.append(artifact_card_to_dict(card))

    df = pd.DataFrame(cards) if cards else pd.DataFrame()
    return df, {"total_intended_use_cards": len(cards)}

def summarize_intended_use_cards(intended_df: pd.DataFrame) -> dict:
    if intended_df.empty:
        return {"total_cards": 0}
    return {"total_cards": len(intended_df)}
