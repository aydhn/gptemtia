"""
Scenario Cards module.
"""

import pandas as pd
from pathlib import Path
from .metadata_models import ArtifactCard, build_artifact_card_id, artifact_card_to_dict
from .metadata_config import ArtifactMetadataProfile

def infer_scenario_scope(artifact_row: pd.Series) -> dict:
    return {"scope": "offline synthetic scenario demo"}

def build_scenario_card_for_artifact(artifact_row: pd.Series, profile: ArtifactMetadataProfile) -> ArtifactCard:
    art_id = artifact_row["artifact_id"]

    return ArtifactCard(
        card_id=build_artifact_card_id(art_id, "scenario_card"),
        artifact_id=art_id,
        card_type="scenario_card",
        title=f"Scenario Card for {artifact_row['title']}",
        summary="Local offline scenario artifact.",
        intended_use="synthetic scenario demo",
        non_use_policy="canli emir icin kullanilamaz, broker talimati icin kullanilamaz, yatirim tavsiyesi icin kullanilamaz.",
        limitations=["offline/local only", "synthetic fixture limitations", "no live trading validation"],
        inputs=["synthetic_data", "scenario_config"],
        outputs=["scenario_results"],
        metrics={},
        lineage=[artifact_row["relative_path"]],
        reproducibility="reproducible_with_local_fixtures",
        warnings=["Scenario validated is not approval for live use."]
    )

def build_scenario_card_registry(artifact_df: pd.DataFrame, profile: ArtifactMetadataProfile) -> tuple[pd.DataFrame, dict]:
    if artifact_df.empty or not profile.scan_scenarios:
        return pd.DataFrame(), {"total_scenario_cards": 0}

    artifacts = artifact_df[artifact_df["artifact_type"] == "scenario_artifact"]
    cards = []

    for _, row in artifacts.iterrows():
        card = build_scenario_card_for_artifact(row, profile)
        cards.append(artifact_card_to_dict(card))

    df = pd.DataFrame(cards) if cards else pd.DataFrame()
    return df, {"total_scenario_cards": len(cards)}

def summarize_scenario_cards(scenario_cards_df: pd.DataFrame) -> dict:
    if scenario_cards_df.empty:
        return {"total_cards": 0}
    return {"total_cards": len(scenario_cards_df)}
