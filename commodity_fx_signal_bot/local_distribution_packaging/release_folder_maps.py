import pandas as pd
from .packaging_config import LocalDistributionPackagingProfile
from .packaging_models import ReleaseFolderItem, build_release_folder_item_id

def build_default_release_folder_items(profile: LocalDistributionPackagingProfile) -> list[ReleaseFolderItem]:
    return [
        ReleaseFolderItem(
            folder_item_id=build_release_folder_item_id("docs", "docs/"),
            folder_area="docs",
            folder_path="docs/",
            intended_contents=["README.md"],
            artifact_label="artifact_documentation_only",
            manual_review_required=True,
            warnings=["Not real folder creation"]
        )
    ]

def build_offline_release_folder_tree(profile: LocalDistributionPackagingProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_release_folder_items(profile)
    df = pd.DataFrame([i.__dict__ for i in items])
    return df, summarize_release_folder_map(df)

def build_offline_release_folder_checklist(profile: LocalDistributionPackagingProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"check": "Folder checked"}])
    return df, summarize_release_folder_map(df)

def build_offline_release_folder_non_goals_registry(profile: LocalDistributionPackagingProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"non_goal": "no real release"}])
    return df, summarize_release_folder_map(df)

def build_offline_release_folder_integrity_rehearsal(profile: LocalDistributionPackagingProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"file": "README.md", "hash_rehearsal": "dummy"}])
    return df, summarize_release_folder_map(df)

def summarize_release_folder_map(df: pd.DataFrame) -> dict:
    return {"status": "generated", "rows": len(df)}
