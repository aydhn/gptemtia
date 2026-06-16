"""
Model Cards module.
"""

import pandas as pd
from pathlib import Path
from .metadata_models import ArtifactCard, build_artifact_card_id, artifact_card_to_dict
from .metadata_config import ArtifactMetadataProfile

def infer_model_inputs_outputs(artifact_row: pd.Series) -> dict:
    return {
        "inputs": ["ohlcv_data", "technical_indicators", "macro_data"],
        "outputs": ["offline_signal_candidate", "ml_context_supportive"]
    }

def infer_model_metrics_from_reports(artifact_row: pd.Series, project_root: Path | None = None) -> dict:
    return {
        "accuracy": "unknown/not available",
        "f1_score": "unknown/not available"
    }

def build_model_card_for_artifact(artifact_row: pd.Series, profile: ArtifactMetadataProfile) -> ArtifactCard:
    art_id = artifact_row["artifact_id"]
    in_out = infer_model_inputs_outputs(artifact_row)
    metrics = infer_model_metrics_from_reports(artifact_row)

    return ArtifactCard(
        card_id=build_artifact_card_id(art_id, "model_card"),
        artifact_id=art_id,
        card_type="model_card",
        title=f"Model Card for {artifact_row['title']}",
        summary="Local/offline research model artifact.",
        intended_use="offline research review",
        non_use_policy="canli emir icin kullanilamaz, broker talimati icin kullanilamaz, yatirim tavsiyesi icin kullanilamaz, model deployment onayi degildir.",
        limitations=["offline/local only", "no live trading validation", "no broker execution", "no investment advice"],
        inputs=in_out["inputs"],
        outputs=in_out["outputs"],
        metrics=metrics,
        lineage=[artifact_row["relative_path"]],
        reproducibility="reproducible_with_warnings",
        warnings=[]
    )

def build_model_card_registry(artifact_df: pd.DataFrame, profile: ArtifactMetadataProfile) -> tuple[pd.DataFrame, dict]:
    if artifact_df.empty or not profile.scan_models:
        return pd.DataFrame(), {"total_model_cards": 0}

    model_artifacts = artifact_df[artifact_df["artifact_type"] == "model_artifact"]
    cards = []

    for _, row in model_artifacts.iterrows():
        card = build_model_card_for_artifact(row, profile)
        cards.append(artifact_card_to_dict(card))

    df = pd.DataFrame(cards) if cards else pd.DataFrame()
    return df, {"total_model_cards": len(cards)}

def summarize_model_cards(model_cards_df: pd.DataFrame) -> dict:
    if model_cards_df.empty:
        return {"total_cards": 0}
    return {"total_cards": len(model_cards_df)}
