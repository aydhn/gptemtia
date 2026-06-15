"""
Limitation Cards module.
"""

import pandas as pd
from pathlib import Path
from .metadata_models import ArtifactCard, build_artifact_card_id, artifact_card_to_dict
from .metadata_config import ArtifactMetadataProfile

def infer_artifact_limitations(artifact_row: pd.Series) -> list[str]:
    return [
        "offline/local only",
        "no live trading validation",
        "no broker execution",
        "no investment advice"
    ]

def build_artifact_limitation_card(artifact_row: pd.Series, profile: ArtifactMetadataProfile) -> ArtifactCard:
    art_id = artifact_row["artifact_id"]
    limits = infer_artifact_limitations(artifact_row)

    return ArtifactCard(
        card_id=build_artifact_card_id(art_id, "limitation_card"),
        artifact_id=art_id,
        card_type="limitation_card",
        title=f"Limitation Card for {artifact_row['title']}",
        summary="Local offline artifact limitations.",
        intended_use="offline research review",
        non_use_policy="canli emir icin kullanilamaz, broker talimati icin kullanilamaz, yatirim tavsiyesi icin kullanilamaz.",
        limitations=limits,
        inputs=[],
        outputs=[],
        metrics={},
        lineage=[artifact_row["relative_path"]],
        reproducibility="reproducibility_unknown",
        warnings=["Risk/limitation is not market forecast."]
    )

def build_artifact_limitation_cards(artifact_df: pd.DataFrame, profile: ArtifactMetadataProfile) -> tuple[pd.DataFrame, dict]:
    if artifact_df.empty or not profile.scan_evidence:
        return pd.DataFrame(), {"total_limitation_cards": 0}

    cards = []

    for _, row in artifact_df.iterrows():
        card = build_artifact_limitation_card(row, profile)
        cards.append(artifact_card_to_dict(card))

    df = pd.DataFrame(cards) if cards else pd.DataFrame()
    return df, {"total_limitation_cards": len(cards)}

def build_risk_limitation_summary_cards(card_tables: dict[str, pd.DataFrame], profile: ArtifactMetadataProfile) -> tuple[pd.DataFrame, dict]:
    # In a real impl, this aggregates from limit cards
    return pd.DataFrame(), {"total_summary_cards": 0}
