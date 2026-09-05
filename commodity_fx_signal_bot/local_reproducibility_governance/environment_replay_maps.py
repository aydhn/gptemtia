"""Environment replay maps."""
import pandas as pd
from .reproducibility_config import LocalReproducibilityGovernanceProfile
from .reproducibility_models import EnvironmentReplayItem, build_environment_replay_item_id, environment_replay_item_to_dict

def build_environment_replay_variable_registry(profile: LocalReproducibilityGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_environment_replay_items(profile)
    df = pd.DataFrame([environment_replay_item_to_dict(i) for i in items])
    return df, summarize_environment_replay_map(df)

def build_environment_replay_path_registry(profile: LocalReproducibilityGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_environment_replay_items(profile)
    df = pd.DataFrame([environment_replay_item_to_dict(i) for i in items])
    return df, summarize_environment_replay_map(df)

def build_environment_replay_dependency_note_registry(profile: LocalReproducibilityGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_environment_replay_items(profile)
    df = pd.DataFrame([environment_replay_item_to_dict(i) for i in items])
    return df, summarize_environment_replay_map(df)

def build_environment_replay_non_install_boundary_registry(profile: LocalReproducibilityGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_environment_replay_items(profile)
    df = pd.DataFrame([environment_replay_item_to_dict(i) for i in items])
    return df, summarize_environment_replay_map(df)

def build_environment_replay_machine_assumption_registry(profile: LocalReproducibilityGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_environment_replay_items(profile)
    df = pd.DataFrame([environment_replay_item_to_dict(i) for i in items])
    return df, summarize_environment_replay_map(df)

def build_environment_replay_limitation_register(profile: LocalReproducibilityGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_environment_replay_items(profile)
    df = pd.DataFrame([environment_replay_item_to_dict(i) for i in items])
    return df, summarize_environment_replay_map(df)

def build_default_environment_replay_items(profile: LocalReproducibilityGovernanceProfile) -> list[EnvironmentReplayItem]:
    return [
        EnvironmentReplayItem(
            replay_id=build_environment_replay_item_id("area_1", "rep_1"),
            replay_area="area_1",
            replay_name="rep_1",
            replay_status="environment_replay_documented_only",
            boundary_note="No install",
            manual_review_required=True,
            warnings=["Dependency notes kurulum talimati degildir."]
        )
    ]

def summarize_environment_replay_map(df: pd.DataFrame) -> dict:
    return {"items": len(df)}
