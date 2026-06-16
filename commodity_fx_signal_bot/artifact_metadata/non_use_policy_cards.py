"""
Non-Use Policy Cards module.
"""

import pandas as pd
from pathlib import Path
from .metadata_models import ArtifactCard, build_artifact_card_id, artifact_card_to_dict
from .metadata_config import ArtifactMetadataProfile

def build_global_non_use_policy(profile: ArtifactMetadataProfile) -> str:
    return (
        "canli emir icin kullanilamaz. "
        "broker talimati icin kullanilamaz. "
        "gercek pozisyon yonetimi icin kullanilamaz. "
        "yatirim tavsiyesi icin kullanilamaz. "
        "model deployment onayi degildir. "
        "resmi compliance/hukuki onay degildir. "
        "guaranteed profit/risksiz getiri iddiasi degildir."
    )

def build_non_use_policy_card(artifact_row: pd.Series, profile: ArtifactMetadataProfile) -> ArtifactCard:
    art_id = artifact_row["artifact_id"]
    policy = build_global_non_use_policy(profile)

    return ArtifactCard(
        card_id=build_artifact_card_id(art_id, "non_use_policy_card"),
        artifact_id=art_id,
        card_type="non_use_policy_card",
        title=f"Non-Use Policy Card for {artifact_row['title']}",
        summary="Local offline artifact non-use policy.",
        intended_use="offline research review",
        non_use_policy=policy,
        limitations=["offline/local only"],
        inputs=[],
        outputs=[],
        metrics={},
        lineage=[artifact_row["relative_path"]],
        reproducibility="reproducibility_unknown",
        warnings=[]
    )

def build_non_use_policy_cards(artifact_df: pd.DataFrame, profile: ArtifactMetadataProfile) -> tuple[pd.DataFrame, dict]:
    if artifact_df.empty or not profile.scan_evidence:
        return pd.DataFrame(), {"total_non_use_policy_cards": 0}

    cards = []

    for _, row in artifact_df.iterrows():
        card = build_non_use_policy_card(row, profile)
        cards.append(artifact_card_to_dict(card))

    df = pd.DataFrame(cards) if cards else pd.DataFrame()
    return df, {"total_non_use_policy_cards": len(cards)}

def summarize_non_use_policy_cards(non_use_df: pd.DataFrame) -> dict:
    if non_use_df.empty:
        return {"total_cards": 0}
    return {"total_cards": len(non_use_df)}
