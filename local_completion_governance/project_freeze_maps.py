import pandas as pd
from local_completion_governance.completion_config import LocalCompletionGovernanceProfile
from local_completion_governance.completion_models import ProjectFreezeItem, build_project_freeze_item_id, project_freeze_item_to_dict

def build_default_project_freeze_items(profile: LocalCompletionGovernanceProfile) -> list[ProjectFreezeItem]:
    return [
        ProjectFreezeItem(
            freeze_id=build_project_freeze_item_id("General", "Freeze"),
            freeze_area="General",
            freeze_title="Freeze",
            snapshot_ref="Snapshot",
            freeze_status="frozen",
            manual_review_required=True,
            warnings=["Not an official freeze."]
        )
    ]

def build_project_freeze_snapshot_registry(profile: LocalCompletionGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_project_freeze_items(profile)
    df = pd.DataFrame([project_freeze_item_to_dict(i) for i in items])
    return df, summarize_project_freeze_map(df)

def build_project_freeze_scope_registry(profile: LocalCompletionGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_project_freeze_items(profile)
    df = pd.DataFrame([project_freeze_item_to_dict(i) for i in items])
    return df, summarize_project_freeze_map(df)

def build_project_freeze_non_goals_registry(profile: LocalCompletionGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_project_freeze_items(profile)
    df = pd.DataFrame([project_freeze_item_to_dict(i) for i in items])
    return df, summarize_project_freeze_map(df)

def build_project_freeze_manual_review_ledger(profile: LocalCompletionGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_project_freeze_items(profile)
    df = pd.DataFrame([project_freeze_item_to_dict(i) for i in items])
    return df, summarize_project_freeze_map(df)

def summarize_project_freeze_map(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}\n