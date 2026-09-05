"""Atlas route maps module."""
import pandas as pd
from .atlas_config import LocalProjectAtlasProfile
from .atlas_models import NavigationItem, build_navigation_item_id

def build_default_route_items(route_label: str, profile: LocalProjectAtlasProfile) -> list[NavigationItem]:
    return [NavigationItem(
        nav_id=build_navigation_item_id(route_label, "start"),
        route_label=route_label,
        nav_title="start",
        nav_area="root",
        target_ref="README.md",
        reading_priority=1,
        manual_review_required=True,
        warnings=["Not SOP"]
    )]

def _build_route_map(route_label: str, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_route_items(route_label, profile)
    df = pd.DataFrame([i.__dict__ for i in items])
    return df, summarize_atlas_route_map(df)

def build_atlas_reading_route_map(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_route_map("route_reading", profile)

def build_atlas_operator_route_map(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_route_map("route_operator", profile)

def build_atlas_analyst_route_map(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_route_map("route_analyst", profile)

def build_atlas_maintainer_route_map(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_route_map("route_maintainer", profile)

def build_atlas_codex_agent_route_map(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_route_map("route_codex_agent", profile)

def summarize_atlas_route_map(df: pd.DataFrame) -> dict:
    return {"steps": len(df)}
