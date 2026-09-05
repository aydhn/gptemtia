"""Reproducibility dossier maps."""
import pandas as pd
from pathlib import Path
from .reproducibility_config import LocalReproducibilityGovernanceProfile
from .reproducibility_models import ReproducibilityDossierItem, build_reproducibility_dossier_item_id, reproducibility_dossier_item_to_dict

def build_reproducibility_dossier_source_map(project_root: Path, profile: LocalReproducibilityGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_reproducibility_dossier_items(profile)
    df = pd.DataFrame([reproducibility_dossier_item_to_dict(i) for i in items])
    return df, summarize_reproducibility_dossier_map(df)

def build_reproducibility_dossier_output_map(profile: LocalReproducibilityGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_reproducibility_dossier_items(profile)
    df = pd.DataFrame([reproducibility_dossier_item_to_dict(i) for i in items])
    return df, summarize_reproducibility_dossier_map(df)

def build_reproducibility_dossier_command_map(profile: LocalReproducibilityGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_reproducibility_dossier_items(profile)
    df = pd.DataFrame([reproducibility_dossier_item_to_dict(i) for i in items])
    return df, summarize_reproducibility_dossier_map(df)

def build_default_reproducibility_dossier_items(profile: LocalReproducibilityGovernanceProfile) -> list[ReproducibilityDossierItem]:
    return [
        ReproducibilityDossierItem(
            dossier_id=build_reproducibility_dossier_item_id("dos_1", "src_1"),
            item_name="dos_1",
            source_ref="src_1",
            output_ref="out_1",
            status_label="reproducibility_rehearsal_ready",
            manual_review_required=True,
            warnings=["Command map komut calistirmaz", "Source map icerik kopyalamaz", "Build/deploy safe-listed yapilmaz"]
        )
    ]

def summarize_reproducibility_dossier_map(df: pd.DataFrame) -> dict:
    return {"items": len(df)}
