"""
Backtest Cards module.
"""

import pandas as pd
from pathlib import Path
from .metadata_models import ArtifactCard, build_artifact_card_id, artifact_card_to_dict
from .metadata_config import ArtifactMetadataProfile

def infer_backtest_scope(artifact_row: pd.Series) -> dict:
    return {"symbols": "unknown", "timeframe": "unknown"}

def infer_backtest_limitations(artifact_row: pd.Series) -> list[str]:
    return ["offline/local only", "backtest overfitting risk", "no live trading validation"]

def build_backtest_card_for_artifact(artifact_row: pd.Series, profile: ArtifactMetadataProfile) -> ArtifactCard:
    art_id = artifact_row["artifact_id"]
    scope = infer_backtest_scope(artifact_row)
    limitations = infer_backtest_limitations(artifact_row)

    return ArtifactCard(
        card_id=build_artifact_card_id(art_id, "backtest_card"),
        artifact_id=art_id,
        card_type="backtest_card",
        title=f"Backtest Card for {artifact_row['title']}",
        summary="Local offline backtest artifact.",
        intended_use="offline research review",
        non_use_policy="canli emir icin kullanilamaz, broker talimati icin kullanilamaz, yatirim tavsiyesi icin kullanilamaz, garanti getiri iddiasi degildir.",
        limitations=limitations,
        inputs=["historical_data", "strategy_logic"],
        outputs=["backtest_metrics", "equity_curve_data"],
        metrics={},
        lineage=[artifact_row["relative_path"]],
        reproducibility="partially_reproducible",
        warnings=[]
    )

def build_backtest_card_registry(artifact_df: pd.DataFrame, profile: ArtifactMetadataProfile) -> tuple[pd.DataFrame, dict]:
    if artifact_df.empty or not profile.scan_backtests:
        return pd.DataFrame(), {"total_backtest_cards": 0}

    artifacts = artifact_df[artifact_df["artifact_type"] == "backtest_artifact"]
    cards = []

    for _, row in artifacts.iterrows():
        card = build_backtest_card_for_artifact(row, profile)
        cards.append(artifact_card_to_dict(card))

    df = pd.DataFrame(cards) if cards else pd.DataFrame()
    return df, {"total_backtest_cards": len(cards)}

def summarize_backtest_cards(backtest_cards_df: pd.DataFrame) -> dict:
    if backtest_cards_df.empty:
        return {"total_cards": 0}
    return {"total_cards": len(backtest_cards_df)}
