"""Build-free reproduction maps."""
import pandas as pd
from .reproducibility_config import LocalReproducibilityGovernanceProfile
from .reproducibility_models import BuildFreeReproductionItem, build_build_free_reproduction_item_id, build_free_reproduction_item_to_dict

def build_build_free_reproduction_reading_order(profile: LocalReproducibilityGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_build_free_reproduction_items(profile)
    df = pd.DataFrame([build_free_reproduction_item_to_dict(i) for i in items])
    return df, summarize_build_free_reproduction_map(df)

def build_build_free_reproduction_script_map(profile: LocalReproducibilityGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_build_free_reproduction_items(profile)
    df = pd.DataFrame([build_free_reproduction_item_to_dict(i) for i in items])
    return df, summarize_build_free_reproduction_map(df)

def build_build_free_reproduction_report_map(profile: LocalReproducibilityGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_build_free_reproduction_items(profile)
    df = pd.DataFrame([build_free_reproduction_item_to_dict(i) for i in items])
    return df, summarize_build_free_reproduction_map(df)

def build_build_free_reproduction_datalake_map(profile: LocalReproducibilityGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_build_free_reproduction_items(profile)
    df = pd.DataFrame([build_free_reproduction_item_to_dict(i) for i in items])
    return df, summarize_build_free_reproduction_map(df)

def build_default_build_free_reproduction_items(profile: LocalReproducibilityGovernanceProfile) -> list[BuildFreeReproductionItem]:
    return [
        BuildFreeReproductionItem(
            reproduction_id=build_build_free_reproduction_item_id("area", "src"),
            reproduction_area="area",
            source_ref="src",
            output_ref="out",
            build_free_boundary="No build",
            warnings=["Build artifact uretmez.", "Raw secret/private data yok."]
        )
    ]

def summarize_build_free_reproduction_map(df: pd.DataFrame) -> dict:
    return {"items": len(df)}
