import pandas as pd
from local_final_closing.final_closing_config import LocalFinalClosingProfile
from local_final_closing.final_closing_models import ProjectConstitutionItem, build_project_constitution_item_id, project_constitution_item_to_dict

def build_default_project_constitution_items(profile: LocalFinalClosingProfile) -> list[ProjectConstitutionItem]:
    return [
        ProjectConstitutionItem(
            constitution_id=build_project_constitution_item_id("core", "constitution"),
            constitution_area="core",
            constitution_title="constitution",
            constitution_status="project_constitution_documented_only",
            boundary_note="Not an official constitution",
            manual_review_required=True,
            warnings=["no official constitution", "no legal authority", "no compliance approval", "no production approval", "no broker readiness", "no live trading approval", "no investment advice", "no release approval", "no project lock", "no archive generation"]
        )
    ]

def build_project_constitution_principle_registry(profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_project_constitution_items(profile)
    df = pd.DataFrame([project_constitution_item_to_dict(i) for i in items])
    return df, summarize_project_constitution_map(df)

def build_project_constitution_boundary_registry(profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_project_constitution_items(profile)
    df = pd.DataFrame([project_constitution_item_to_dict(i) for i in items])
    return df, summarize_project_constitution_map(df)

def build_project_constitution_scope_registry(profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_project_constitution_items(profile)
    df = pd.DataFrame([project_constitution_item_to_dict(i) for i in items])
    return df, summarize_project_constitution_map(df)

def build_project_constitution_non_goals_registry(profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_project_constitution_items(profile)
    df = pd.DataFrame([project_constitution_item_to_dict(i) for i in items])
    return df, summarize_project_constitution_map(df)

def build_project_constitution_role_registry(profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_project_constitution_items(profile)
    df = pd.DataFrame([project_constitution_item_to_dict(i) for i in items])
    return df, summarize_project_constitution_map(df)

def build_project_constitution_reading_order(profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_project_constitution_items(profile)
    df = pd.DataFrame([project_constitution_item_to_dict(i) for i in items])
    return df, summarize_project_constitution_map(df)

def summarize_project_constitution_map(df: pd.DataFrame) -> dict:
    return {"total_items": len(df) if df is not None else 0}
