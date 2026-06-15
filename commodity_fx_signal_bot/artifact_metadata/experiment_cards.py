"""
Experiment Cards module.
"""

import pandas as pd
from pathlib import Path
from .metadata_models import ArtifactCard, build_artifact_card_id, artifact_card_to_dict
from .metadata_config import ArtifactMetadataProfile

def infer_experiment_parameters(artifact_row: pd.Series, project_root: Path | None = None) -> dict:
    return {"parameters": "unknown"}

def infer_experiment_outputs(artifact_row: pd.Series) -> list[str]:
    return ["experiment_metrics", "research_notes"]

def build_experiment_card_for_artifact(artifact_row: pd.Series, profile: ArtifactMetadataProfile) -> ArtifactCard:
    art_id = artifact_row["artifact_id"]

    return ArtifactCard(
        card_id=build_artifact_card_id(art_id, "experiment_card"),
        artifact_id=art_id,
        card_type="experiment_card",
        title=f"Experiment Card for {artifact_row['title']}",
        summary="Local/offline research experiment artifact.",
        intended_use="offline research review",
        non_use_policy="canli emir icin kullanilamaz, broker talimati icin kullanilamaz, yatirim tavsiyesi icin kullanilamaz.",
        limitations=["offline/local only", "backtest overfitting risk", "no live trading validation"],
        inputs=["historical_data"],
        outputs=infer_experiment_outputs(artifact_row),
        metrics={},
        lineage=[artifact_row["relative_path"]],
        reproducibility="partially_reproducible",
        warnings=[]
    )

def build_experiment_card_registry(artifact_df: pd.DataFrame, profile: ArtifactMetadataProfile) -> tuple[pd.DataFrame, dict]:
    if artifact_df.empty or not profile.scan_experiments:
        return pd.DataFrame(), {"total_experiment_cards": 0}

    artifacts = artifact_df[artifact_df["artifact_type"] == "experiment_artifact"]
    cards = []

    for _, row in artifacts.iterrows():
        card = build_experiment_card_for_artifact(row, profile)
        cards.append(artifact_card_to_dict(card))

    df = pd.DataFrame(cards) if cards else pd.DataFrame()
    return df, {"total_experiment_cards": len(cards)}

def summarize_experiment_cards(experiment_cards_df: pd.DataFrame) -> dict:
    if experiment_cards_df.empty:
        return {"total_cards": 0}
    return {"total_cards": len(experiment_cards_df)}
