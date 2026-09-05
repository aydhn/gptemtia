"""Universal navigation map module."""
import pandas as pd
from .atlas_config import LocalProjectAtlasProfile
from .atlas_models import NavigationItem, build_navigation_item_id, navigation_item_to_dict

def build_default_navigation_items(profile: LocalProjectAtlasProfile) -> list[NavigationItem]:
    items = []
    routes = ["route_operator", "route_analyst", "route_maintainer", "route_codex_agent", "route_future_reader", "route_quality", "route_safety"]
    for r in routes:
        items.append(NavigationItem(
            nav_id=build_navigation_item_id(r, f"Start for {r}"),
            route_label=r,
            nav_title=f"{r} entry point",
            nav_area="general",
            target_ref="README.md",
            reading_priority=1,
            manual_review_required=True,
            warnings=["Not official SOP."]
        ))
    return items

def build_universal_navigation_map(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_navigation_items(profile)
    df = pd.DataFrame([navigation_item_to_dict(i) for i in items])
    return df, summarize_universal_navigation(df)

def summarize_universal_navigation(df: pd.DataFrame) -> dict:
    return {
        "total_routes": len(df["route_label"].unique()) if not df.empty else 0,
        "total_items": len(df)
    }
