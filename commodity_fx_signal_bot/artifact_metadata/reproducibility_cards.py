"""
Reproducibility Cards module.
"""

import pandas as pd
from pathlib import Path
from .metadata_models import ArtifactCard, ReproducibilityChecklistItem, build_artifact_card_id, build_reproducibility_check_id, artifact_card_to_dict, reproducibility_checklist_item_to_dict
from .metadata_config import ArtifactMetadataProfile

def classify_artifact_reproducibility(artifact_row: pd.Series) -> str:
    return "reproducible_with_warnings"

def build_reproducibility_card_for_artifact(artifact_row: pd.Series, profile: ArtifactMetadataProfile) -> ArtifactCard:
    art_id = artifact_row["artifact_id"]
    rep_status = classify_artifact_reproducibility(artifact_row)

    return ArtifactCard(
        card_id=build_artifact_card_id(art_id, "reproducibility_card"),
        artifact_id=art_id,
        card_type="reproducibility_card",
        title=f"Reproducibility Card for {artifact_row['title']}",
        summary="Local reproducibility evidence summary.",
        intended_use="reproducibility analysis",
        non_use_policy="canli emir icin kullanilamaz, broker talimati icin kullanilamaz, yatirim tavsiyesi icin kullanilamaz.",
        limitations=["offline/local only", "missing reproducibility evidence"],
        inputs=[],
        outputs=[],
        metrics={},
        lineage=[artifact_row["relative_path"]],
        reproducibility=rep_status,
        warnings=["Reproducibility is approximate."]
    )

def build_reproducibility_card_registry(artifact_df: pd.DataFrame, profile: ArtifactMetadataProfile) -> tuple[pd.DataFrame, dict]:
    if artifact_df.empty or not profile.scan_evidence:
        return pd.DataFrame(), {"total_reproducibility_cards": 0}

    cards = []
    # Generate for models, experiments, and backtests
    artifacts = artifact_df[artifact_df["artifact_type"].isin(["model_artifact", "experiment_artifact", "backtest_artifact"])]

    for _, row in artifacts.iterrows():
        card = build_reproducibility_card_for_artifact(row, profile)
        cards.append(artifact_card_to_dict(card))

    df = pd.DataFrame(cards) if cards else pd.DataFrame()
    return df, {"total_reproducibility_cards": len(cards)}

def build_reproducibility_checklist(artifact_df: pd.DataFrame, profile: ArtifactMetadataProfile) -> tuple[pd.DataFrame, dict]:
    if artifact_df.empty or not profile.scan_evidence:
        return pd.DataFrame(), {"total_checks": 0}

    checks = []
    artifacts = artifact_df[artifact_df["artifact_type"].isin(["model_artifact", "experiment_artifact", "backtest_artifact"])]

    check_names = ["source_artifact_present", "config_present", "expected_output_present"]

    for _, row in artifacts.iterrows():
        for check in check_names:
            item = ReproducibilityChecklistItem(
                item_id=build_reproducibility_check_id(row["artifact_id"], check),
                artifact_id=row["artifact_id"],
                check_name=check,
                status="partial",
                evidence_path=None,
                recommendation="Verify evidence manually.",
                warnings=["Automated check incomplete"]
            )
            checks.append(reproducibility_checklist_item_to_dict(item))

    df = pd.DataFrame(checks) if checks else pd.DataFrame()
    return df, {"total_checks": len(checks)}

def summarize_reproducibility_cards(repro_cards_df: pd.DataFrame, checklist_df: pd.DataFrame) -> dict:
    return {
        "total_cards": len(repro_cards_df) if not repro_cards_df.empty else 0,
        "total_checks": len(checklist_df) if not checklist_df.empty else 0
    }
