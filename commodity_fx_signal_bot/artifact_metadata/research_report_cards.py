"""
Research Report Cards module.
"""

import pandas as pd
from pathlib import Path
from .metadata_models import ArtifactCard, build_artifact_card_id, artifact_card_to_dict
from .metadata_config import ArtifactMetadataProfile

def infer_report_sections(artifact_row: pd.Series, project_root: Path | None = None) -> dict:
    return {"sections": "unknown"}

def build_research_report_card_for_artifact(artifact_row: pd.Series, profile: ArtifactMetadataProfile) -> ArtifactCard:
    art_id = artifact_row["artifact_id"]

    return ArtifactCard(
        card_id=build_artifact_card_id(art_id, "research_report_card"),
        artifact_id=art_id,
        card_type="research_report_card",
        title=f"Research Report Card for {artifact_row['title']}",
        summary="Local offline research report artifact.",
        intended_use="documentation_use_only",
        non_use_policy="canli emir icin kullanilamaz, broker talimati icin kullanilamaz, yatirim tavsiyesi icin kullanilamaz.",
        limitations=["offline/local only", "not independently audited"],
        inputs=[],
        outputs=[],
        metrics={},
        lineage=[artifact_row["relative_path"]],
        reproducibility="reproducibility_unknown",
        warnings=["Missing sections warning", "Report is not investment advice."]
    )

def build_research_report_card_registry(artifact_df: pd.DataFrame, profile: ArtifactMetadataProfile) -> tuple[pd.DataFrame, dict]:
    if artifact_df.empty or not profile.scan_reports:
        return pd.DataFrame(), {"total_report_cards": 0}

    artifacts = artifact_df[artifact_df["artifact_type"] == "research_report_artifact"]
    cards = []

    for _, row in artifacts.iterrows():
        card = build_research_report_card_for_artifact(row, profile)
        cards.append(artifact_card_to_dict(card))

    df = pd.DataFrame(cards) if cards else pd.DataFrame()
    return df, {"total_report_cards": len(cards)}

def summarize_research_report_cards(report_cards_df: pd.DataFrame) -> dict:
    if report_cards_df.empty:
        return {"total_cards": 0}
    return {"total_cards": len(report_cards_df)}
