"""Atlas crosswalks module."""
import pandas as pd
from .atlas_config import LocalProjectAtlasProfile
from .atlas_models import AtlasCrosswalkItem, build_atlas_crosswalk_item_id

def build_default_crosswalk_items(area: str, profile: LocalProjectAtlasProfile) -> list[AtlasCrosswalkItem]:
    return [AtlasCrosswalkItem(
        crosswalk_id=build_atlas_crosswalk_item_id(area, "Offline Concept", "Project Mapping"),
        crosswalk_area=area,
        source_concept="Offline Concept",
        target_concept="Project Mapping",
        interpretation_note="Not legal or compliance evidence",
        warnings=["No investment advice"]
    )]

def _build_crosswalk(area: str, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_crosswalk_items(area, profile)
    df = pd.DataFrame([i.__dict__ for i in items])
    return df, summarize_atlas_crosswalk(df)

def build_atlas_concept_crosswalk(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]: return _build_crosswalk("concept", profile)
def build_atlas_no_go_safe_go_crosswalk(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]: return _build_crosswalk("no_go_safe_go", profile)
def build_atlas_safety_boundary_crosswalk(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]: return _build_crosswalk("safety_boundary", profile)
def build_atlas_maintenance_crosswalk(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]: return _build_crosswalk("maintenance", profile)
def build_atlas_continuity_crosswalk(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]: return _build_crosswalk("continuity", profile)
def build_atlas_preservation_crosswalk(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]: return _build_crosswalk("preservation", profile)
def build_atlas_project_completion_crosswalk(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]: return _build_crosswalk("project_completion", profile)
def build_atlas_longterm_operations_crosswalk(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]: return _build_crosswalk("longterm_operations", profile)
def build_atlas_release_candidate_crosswalk(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]: return _build_crosswalk("release_candidate", profile)
def build_atlas_incident_response_crosswalk(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]: return _build_crosswalk("incident_response", profile)
def build_atlas_redteam_governance_crosswalk(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]: return _build_crosswalk("redteam_governance", profile)

def summarize_atlas_crosswalk(df: pd.DataFrame) -> dict:
    return {"mappings": len(df)}
