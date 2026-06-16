"""
Regression Cards module.
"""

import pandas as pd
from pathlib import Path
from .metadata_models import ArtifactCard, build_artifact_card_id, artifact_card_to_dict
from .metadata_config import ArtifactMetadataProfile

def infer_regression_scope(artifact_row: pd.Series) -> dict:
    return {"scope": "deterministic replay/snapshot"}

def build_regression_card_for_artifact(artifact_row: pd.Series, profile: ArtifactMetadataProfile) -> ArtifactCard:
    art_id = artifact_row["artifact_id"]

    return ArtifactCard(
        card_id=build_artifact_card_id(art_id, "regression_card"),
        artifact_id=art_id,
        card_type="regression_card",
        title=f"Regression Card for {artifact_row['title']}",
        summary="Local offline regression artifact.",
        intended_use="quality inspection",
        non_use_policy="canli emir icin kullanilamaz, broker talimati icin kullanilamaz, yatirim tavsiyesi icin kullanilamaz.",
        limitations=["offline/local only", "snapshot diff is not investment signal"],
        inputs=["previous_snapshot", "current_run_output"],
        outputs=["diff_report"],
        metrics={},
        lineage=[artifact_row["relative_path"]],
        reproducibility="reproducible_with_local_fixtures",
        warnings=["Regression passed is not production readiness."]
    )

def build_regression_card_registry(artifact_df: pd.DataFrame, profile: ArtifactMetadataProfile) -> tuple[pd.DataFrame, dict]:
    if artifact_df.empty or not profile.scan_scenarios:
        return pd.DataFrame(), {"total_regression_cards": 0}

    artifacts = artifact_df[artifact_df["artifact_type"] == "regression_artifact"]
    cards = []

    for _, row in artifacts.iterrows():
        card = build_regression_card_for_artifact(row, profile)
        cards.append(artifact_card_to_dict(card))

    df = pd.DataFrame(cards) if cards else pd.DataFrame()
    return df, {"total_regression_cards": len(cards)}

def summarize_regression_cards(regression_cards_df: pd.DataFrame) -> dict:
    if regression_cards_df.empty:
        return {"total_cards": 0}
    return {"total_cards": len(regression_cards_df)}
