import pandas as pd
from .packaging_config import LocalDistributionPackagingProfile
from .packaging_models import ZipMapItem, build_zip_map_item_id

def build_default_zip_map_items(profile: LocalDistributionPackagingProfile) -> list[ZipMapItem]:
    return [
        ZipMapItem(
            zip_map_id=build_zip_map_item_id("docs/", "README.md"),
            map_area="docs",
            folder_ref="docs/",
            file_ref="README.md",
            compression_status="rehearsal",
            boundary_note="Not a real ZIP",
            warnings=["No zipfile used"]
        )
    ]

def build_zip_map_folder_to_file_registry(profile: LocalDistributionPackagingProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_zip_map_items(profile)
    df = pd.DataFrame([i.__dict__ for i in items])
    return df, summarize_zip_map(df)

def build_zip_map_compression_non_goals_registry(profile: LocalDistributionPackagingProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"non_goal": "No compression"}])
    return df, summarize_zip_map(df)

def build_zip_map_handover_route_map(profile: LocalDistributionPackagingProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"route": "operator"}])
    return df, summarize_zip_map(df)

def build_zip_map_recipient_checklist(profile: LocalDistributionPackagingProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"check": "Recipient notified"}])
    return df, summarize_zip_map(df)

def summarize_zip_map(df: pd.DataFrame) -> dict:
    return {"status": "generated", "rows": len(df)}
